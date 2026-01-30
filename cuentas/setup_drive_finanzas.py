#!/usr/bin/env python3
"""
Script para crear estructura de carpetas en Google Drive para finanzas personales
"""
import os
import sys
from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Cargar credenciales
SCOPES = ['https://www.googleapis.com/auth/drive']
BASE_DIR = Path(__file__).resolve().parent.parent
TOKEN_PATH = BASE_DIR / 'token_personal_drive.json'

def get_drive_service():
    """Obtiene el servicio de Google Drive"""
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    return build('drive', 'v3', credentials=creds)

def create_folder(service, folder_name, parent_id=None):
    """Crea una carpeta en Google Drive"""
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    
    if parent_id:
        file_metadata['parents'] = [parent_id]
    
    try:
        folder = service.files().create(
            body=file_metadata,
            fields='id, name, webViewLink'
        ).execute()
        
        print(f"✅ Carpeta creada: {folder['name']}")
        print(f"   ID: {folder['id']}")
        print(f"   Link: {folder['webViewLink']}")
        return folder['id']
    except HttpError as error:
        print(f"❌ Error creando carpeta {folder_name}: {error}")
        return None

def check_folder_exists(service, folder_name, parent_id=None):
    """Verifica si una carpeta ya existe"""
    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    if parent_id:
        query += f" and '{parent_id}' in parents"
    
    try:
        results = service.files().list(
            q=query,
            spaces='drive',
            fields='files(id, name, webViewLink)'
        ).execute()
        
        files = results.get('files', [])
        if files:
            return files[0]
        return None
    except HttpError as error:
        print(f"❌ Error buscando carpeta: {error}")
        return None

def setup_finanzas_structure():
    """Crea la estructura completa de carpetas para finanzas"""
    service = get_drive_service()
    
    print("\n🚀 Creando estructura de carpetas para Finanzas en Google Drive...\n")
    
    # Carpeta principal: Finanzas
    finanzas = check_folder_exists(service, 'Finanzas')
    if finanzas:
        print(f"📁 Carpeta 'Finanzas' ya existe")
        print(f"   Link: {finanzas['webViewLink']}")
        finanzas_id = finanzas['id']
    else:
        finanzas_id = create_folder(service, 'Finanzas')
    
    if not finanzas_id:
        print("❌ No se pudo crear/encontrar la carpeta principal")
        return
    
    print()
    
    # Subcarpetas
    subcarpetas = {
        'recibos': 'Aquí suben recibos/facturas (PDF, imágenes)',
        'procesados': 'Recibos ya procesados se mueven aquí automáticamente'
    }
    
    folder_ids = {'Finanzas': finanzas_id}
    
    for nombre, descripcion in subcarpetas.items():
        existing = check_folder_exists(service, nombre, finanzas_id)
        if existing:
            print(f"📁 Subcarpeta '{nombre}' ya existe")
            folder_ids[nombre] = existing['id']
        else:
            folder_id = create_folder(service, nombre, finanzas_id)
            if folder_id:
                folder_ids[nombre] = folder_id
        print(f"   └─ {descripcion}")
        print()
    
    # Crear subcarpetas por mes en recibos
    if 'recibos' in folder_ids:
        print("📅 Creando carpeta para el mes actual...")
        from datetime import datetime
        mes_actual = datetime.now().strftime('%Y-%m')
        
        existing_mes = check_folder_exists(service, mes_actual, folder_ids['recibos'])
        if existing_mes:
            print(f"📁 Carpeta '{mes_actual}' ya existe en recibos")
        else:
            create_folder(service, mes_actual, folder_ids['recibos'])
        print()
    
    print("=" * 60)
    print("✅ ESTRUCTURA CREADA EXITOSAMENTE")
    print("=" * 60)
    print("\n📂 Estructura final:")
    print("   Finanzas/")
    print("   ├── recibos/")
    print("   │   └── 2026-01/")
    print("   └── procesados/")
    print("\n💡 Puedes compartir la carpeta 'Finanzas' con tu esposa")
    print("   para que ambos suban recibos.\n")
    
    return folder_ids

if __name__ == '__main__':
    setup_finanzas_structure()
