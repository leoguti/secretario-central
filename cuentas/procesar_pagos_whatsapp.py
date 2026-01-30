#!/usr/bin/env python3
"""
Script para procesar automáticamente pagos de WhatsApp:
1. Extrae info del chat
2. Sube imágenes a Drive (/recibos/2026-01/)
3. Usa OCR para extraer montos
4. Registra en Google Sheet con enlaces a imágenes
"""
import re
import os
from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from PIL import Image
import pytesseract
from datetime import datetime

# Configuración
BASE_DIR = Path(__file__).resolve().parent.parent
TOKEN_PATH = BASE_DIR / 'token_personal_drive.json'
DATA_DIR = BASE_DIR / 'data'
CHAT_FILE = DATA_DIR / 'Chat de WhatsApp con Pagos GP.txt'

SCOPES = [
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets'
]

# IDs de Drive
FOLDER_2026_01_ID = '1fINRdEET487vpYHIjSZMuBIfOY-sSUgr'  # /recibos/2026-01/
SPREADSHEET_ID = '1ypFoP9DuhyM_9CkLL5TLZHJy-cwstzA8w_x75uVEayw'  # BALANCE FINANCIERO 2026

def extract_transactions_from_chat():
    """Extrae transacciones del archivo de chat"""
    print('📖 Leyendo chat de WhatsApp...')
    
    with open(CHAT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    transactions = []
    current_date = None
    
    for i, line in enumerate(lines):
        # Detectar fecha (formato: dd/mm/yyyy)
        date_match = re.match(r'(\d+/\d+/\d+)', line)
        if date_match:
            current_date = date_match.group(1)
        
        # Detectar imagen
        img_match = re.search(r'(IMG-\d+-WA\d+\.jpg)', line)
        if img_match:
            img_name = img_match.group(1)
            
            # Buscar descripción en líneas siguientes
            desc = ""
            for j in range(i+1, min(i+3, len(lines))):
                next_line = lines[j].strip()
                if next_line and not next_line.startswith('‎') and 'archivo adjunto' not in next_line:
                    # Limpiar descripción
                    desc = re.sub(r'^\d+/\d+/\d+.*?- Mami: ', '', next_line)
                    desc = re.sub(r'^\d+/\d+/\d+.*?- Leonardo.*?: ', '', desc)
                    break
            
            # Solo imágenes de enero 2026
            if '202601' in img_name or '202512' in img_name:
                transactions.append({
                    'fecha': current_date,
                    'imagen': img_name,
                    'descripcion': desc,
                    'imagen_path': DATA_DIR / img_name
                })
    
    print(f'✅ {len(transactions)} transacciones encontradas\n')
    return transactions

def extract_amount_from_image(image_path):
    """Extrae monto de la imagen usando OCR mejorado"""
    try:
        img = Image.open(image_path)
        
        # Mejorar imagen para OCR
        img = img.convert('L')  # Convertir a escala de grises
        
        text = pytesseract.image_to_string(img, lang='spa')
        
        # Buscar patrones específicos de comprobantes colombianos
        amounts_found = []
        
        # Patrón 1: $123.456 o $ 123.456 (con punto como separador de miles)
        pattern1 = r'\$\s*(\d{1,3}(?:\.\d{3})+)(?:\D|$)'
        matches1 = re.findall(pattern1, text)
        for m in matches1:
            # Eliminar puntos (son separadores de miles)
            amount = m.replace('.', '')
            if 1000 <= int(amount) <= 100000000:  # Rango razonable
                amounts_found.append(int(amount))
        
        # Patrón 2: Total, Valor, Monto seguido de número
        pattern2 = r'(?:Total|Valor|Monto|Pago)[\s:]+\$?\s*(\d{1,3}(?:[.,]\d{3})+)'
        matches2 = re.findall(pattern2, text, re.IGNORECASE)
        for m in matches2:
            amount = m.replace('.', '').replace(',', '')
            if 1000 <= int(amount) <= 100000000:
                amounts_found.append(int(amount))
        
        # Patrón 3: Números grandes con puntos (formato colombiano)
        pattern3 = r'(?<!\d)(\d{1,3}(?:\.\d{3}){1,3})(?!\d)'
        matches3 = re.findall(pattern3, text)
        for m in matches3:
            amount = m.replace('.', '')
            # Filtrar números que probablemente son montos (no fechas, IDs, etc)
            if 10000 <= int(amount) <= 100000000:  # Entre 10k y 100M
                amounts_found.append(int(amount))
        
        # Retornar el monto más común o el más razonable
        if amounts_found:
            # Si hay múltiples montos, tomar el más frecuente
            from collections import Counter
            if len(amounts_found) > 1:
                # Filtrar montos muy similares (diferencia < 1%)
                unique_amounts = []
                for amt in amounts_found:
                    if not any(abs(amt - u) / max(amt, u) < 0.01 for u in unique_amounts):
                        unique_amounts.append(amt)
                
                if unique_amounts:
                    # Tomar el monto más pequeño razonable (usualmente el monto real)
                    return min(unique_amounts)
            
            return amounts_found[0]
        
        return None
    except Exception as e:
        print(f'  ⚠️ Error OCR: {e}')
        return None

def upload_image_to_drive(image_path, drive_service):
    """Sube imagen a Google Drive y retorna el enlace"""
    try:
        file_metadata = {
            'name': image_path.name,
            'parents': [FOLDER_2026_01_ID]
        }
        
        media = MediaFileUpload(str(image_path), mimetype='image/jpeg')
        
        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, webViewLink'
        ).execute()
        
        return file.get('webViewLink')
    except Exception as e:
        print(f'  ❌ Error subiendo imagen: {e}')
        return None

def categorize_transaction(description):
    """Categoriza transacción basado en descripción"""
    desc_lower = description.lower()
    
    categorias = {
        'Servicios': ['energía', 'agua', 'gas', 'internet', 'celular'],
        'Hogar': ['arriendo', 'administración', 'yaneth', 'aseo'],
        'Salud': ['medicina', 'odontología', 'sicología', 'sanitas', 'eps'],
        'Pago Deuda': ['crédito', 'tc', 'tarjeta', 'leasing', 'cuota'],
        'Comida': ['mercado', 'supermercado'],
        'Transporte': ['gasolina', 'uber', 'taxi'],
        'Entretenimiento': ['entrenamiento', 'gym'],
        'Otros': []
    }
    
    for categoria, keywords in categorias.items():
        for keyword in keywords:
            if keyword in desc_lower:
                return categoria
    
    return 'Otros'

def convert_date_format(date_str):
    """Convierte fecha de dd/mm/yyyy a yyyy-mm-dd"""
    try:
        parts = date_str.split('/')
        if len(parts) == 3:
            day, month, year = parts
            return f'{year}-{month.zfill(2)}-{day.zfill(2)}'
    except:
        pass
    return date_str

def register_in_sheet(transactions, sheets_service):
    """Registra transacciones en Google Sheet"""
    print('📊 Registrando en Google Sheet...\n')
    
    # Preparar datos para el sheet
    values = []
    
    for t in transactions:
        fecha = convert_date_format(t['fecha'])
        categoria = categorize_transaction(t['descripcion'])
        monto = t.get('monto', '')
        link = t.get('drive_link', '')
        
        # Formato: Fecha, Tipo, Categoría, Subcategoría, Concepto, Monto, Método Pago, Recibo, Fuente, Procesado Por, Notas, Estado
        row = [
            fecha,                           # A: Fecha
            'Gasto',                         # B: Tipo
            categoria,                       # C: Categoría
            '',                              # D: Subcategoría
            t['descripcion'],                # E: Concepto
            monto if monto else '',          # F: Monto
            '',                              # G: Método Pago
            link,                            # H: Recibo (link a imagen)
            'Lucía',                         # I: Fuente
            'leogiga+secretario-ia@gmail.com',  # J: Procesado Por
            f"Imagen: {t['imagen']}",       # K: Notas
            'Procesado' if monto else 'Pendiente OCR'  # L: Estado
        ]
        values.append(row)
    
    # Escribir en el sheet (tab "Transacciones")
    body = {'values': values}
    
    result = sheets_service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range='Transacciones!A2',  # Empezar en A2 (después de encabezados)
        valueInputOption='USER_ENTERED',
        insertDataOption='INSERT_ROWS',
        body=body
    ).execute()
    
    print(f"✅ {result.get('updates').get('updatedRows')} transacciones registradas")
    print(f"📊 Sheet: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}")

def main():
    print('🚀 PROCESADOR AUTOMÁTICO DE PAGOS\n')
    print('=' * 60)
    
    # 1. Extraer transacciones del chat
    transactions = extract_transactions_from_chat()
    
    if not transactions:
        print('❌ No se encontraron transacciones')
        return
    
    # 2. Inicializar servicios de Google
    print('🔐 Conectando a Google Drive y Sheets...')
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    drive_service = build('drive', 'v3', credentials=creds)
    sheets_service = build('sheets', 'v4', credentials=creds)
    print('✅ Conectado\n')
    
    # 3. Procesar cada transacción
    print('🔄 Procesando transacciones...\n')
    
    for i, t in enumerate(transactions, 1):
        print(f"[{i}/{len(transactions)}] {t['descripcion'][:50]}...")
        
        # 3a. Subir imagen a Drive
        if t['imagen_path'].exists():
            print(f"  📤 Subiendo {t['imagen']}...")
            drive_link = upload_image_to_drive(t['imagen_path'], drive_service)
            t['drive_link'] = drive_link
            if drive_link:
                print(f"  ✅ Subida: {drive_link[:50]}...")
        else:
            print(f"  ⚠️  Imagen no encontrada: {t['imagen_path']}")
            t['drive_link'] = None
        
        # 3b. Extraer monto con OCR
        if t['imagen_path'].exists():
            print(f"  🔍 Extrayendo monto con OCR...")
            monto = extract_amount_from_image(t['imagen_path'])
            t['monto'] = monto
            if monto:
                print(f"  💰 Monto detectado: ${monto:,}")
            else:
                print(f"  ⚠️  Monto no detectado (revisar manualmente)")
        
        print()
    
    # 4. Registrar en Google Sheet
    register_in_sheet(transactions, sheets_service)
    
    print('\n' + '=' * 60)
    print('✅ PROCESO COMPLETADO')
    print('\nResumen:')
    print(f"  • {len(transactions)} transacciones procesadas")
    print(f"  • Imágenes subidas a: /recibos/2026-01/")
    print(f"  • Registros en sheet: BALANCE FINANCIERO 2026")
    print(f"\n👁️  Revisa el sheet para completar montos faltantes")

if __name__ == '__main__':
    main()
