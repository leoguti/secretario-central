#!/usr/bin/env python3
"""
Script para actualizar SOLO los montos de las transacciones existentes
usando OCR mejorado
"""
import re
from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from PIL import Image
import pytesseract

# Configuración
BASE_DIR = Path(__file__).resolve().parent.parent
TOKEN_PATH = BASE_DIR / 'token_personal_drive.json'
DATA_DIR = BASE_DIR / 'data'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1ypFoP9DuhyM_9CkLL5TLZHJy-cwstzA8w_x75uVEayw'

def extract_amount_from_image(image_path):
    """Extrae monto de la imagen usando OCR mejorado"""
    try:
        img = Image.open(image_path)
        img = img.convert('L')  # Escala de grises
        
        text = pytesseract.image_to_string(img, lang='spa')
        
        amounts_found = []
        
        # Patrón: $123.456 o $ 123.456
        pattern1 = r'\$\s*(\d{1,3}(?:\.\d{3})+)(?:\D|$)'
        matches1 = re.findall(pattern1, text)
        for m in matches1:
            amount = m.replace('.', '')
            if 1000 <= int(amount) <= 100000000:
                amounts_found.append(int(amount))
        
        # Patrón: Total, Valor, Monto
        pattern2 = r'(?:Total|Valor|Monto|Pago)[\s:]+\$?\s*(\d{1,3}(?:[.,]\d{3})+)'
        matches2 = re.findall(pattern2, text, re.IGNORECASE)
        for m in matches2:
            amount = m.replace('.', '').replace(',', '')
            if 1000 <= int(amount) <= 100000000:
                amounts_found.append(int(amount))
        
        # Patrón: Números con formato colombiano
        pattern3 = r'(?<!\d)(\d{1,3}(?:\.\d{3}){1,3})(?!\d)'
        matches3 = re.findall(pattern3, text)
        for m in matches3:
            amount = m.replace('.', '')
            if 10000 <= int(amount) <= 100000000:
                amounts_found.append(int(amount))
        
        if amounts_found:
            # Filtrar duplicados similares
            unique_amounts = []
            for amt in amounts_found:
                if not any(abs(amt - u) / max(amt, u) < 0.01 for u in unique_amounts):
                    unique_amounts.append(amt)
            
            if unique_amounts:
                return min(unique_amounts)  # Tomar el menor (más probable)
        
        return None
    except Exception as e:
        print(f'  ⚠️ Error OCR: {e}')
        return None

def main():
    print('🔄 ACTUALIZANDO MONTOS CON OCR MEJORADO\n')
    print('=' * 60)
    
    # Conectar a Sheets
    print('🔐 Conectando a Google Sheets...')
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    sheets_service = build('sheets', 'v4', credentials=creds)
    
    # Leer transacciones actuales
    print('📖 Leyendo transacciones...')
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range='Transacciones!A2:L100'
    ).execute()
    
    values = result.get('values', [])
    print(f'✅ {len(values)} transacciones encontradas\n')
    
    # Procesar cada transacción
    print('🔍 Extrayendo montos con OCR mejorado...\n')
    
    updates = []
    for i, row in enumerate(values, start=2):  # Empezar en fila 2
        if len(row) < 11:  # Verificar que tenga la columna de Notas
            continue
        
        # Extraer nombre de imagen de la columna Notas (K)
        notas = row[10] if len(row) > 10 else ''
        img_match = re.search(r'IMG-\d+-WA\d+\.jpg', notas)
        
        if not img_match:
            continue
        
        img_name = img_match.group(0)
        img_path = DATA_DIR / img_name
        
        if not img_path.exists():
            print(f'[{i-1}] ⚠️  Imagen no encontrada: {img_name}')
            continue
        
        concepto = row[4] if len(row) > 4 else ''
        print(f'[{i-1}] {concepto[:50]}...')
        print(f'     📷 {img_name}')
        
        # Extraer monto
        monto = extract_amount_from_image(img_path)
        
        if monto:
            print(f'     💰 Monto detectado: ${monto:,}')
            # Agregar actualización
            updates.append({
                'range': f'Transacciones!F{i}',  # Columna F (Monto)
                'values': [[monto]]
            })
            updates.append({
                'range': f'Transacciones!L{i}',  # Columna L (Estado)
                'values': [['Procesado']]
            })
        else:
            print(f'     ⚠️  Monto no detectado')
            updates.append({
                'range': f'Transacciones!L{i}',
                'values': [['Pendiente OCR - revisar manualmente']]
            })
        
        print()
    
    # Aplicar todas las actualizaciones
    if updates:
        print(f'💾 Actualizando {len(updates)} celdas en el sheet...')
        body = {'data': updates, 'valueInputOption': 'USER_ENTERED'}
        sheets_service.spreadsheets().values().batchUpdate(
            spreadsheetId=SPREADSHEET_ID,
            body=body
        ).execute()
        print('✅ Montos actualizados')
    
    print('\n' + '=' * 60)
    print('✅ PROCESO COMPLETADO')
    print(f'📊 Sheet: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}')
    print('\n👁️  Revisa las transacciones con estado "Pendiente OCR"')

if __name__ == '__main__':
    main()
