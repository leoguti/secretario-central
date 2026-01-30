#!/usr/bin/env python3
"""
Script para revisar contenido de carpeta de Google Drive (Cuenta Trufi)
Folder ID: 1AECFAWSsDu4rhixQm8JILQQpbZZpf5Y5
"""

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os
import sys

FOLDER_ID = '1AECFAWSsDu4rhixQm8JILQQpbZZpf5Y5'

def revisar_carpeta():
    """Revisa el contenido de la carpeta de Drive"""
    
    # Cargar credenciales de Trufi
    token_file = 'token_trufi.json'
    
    if not os.path.exists(token_file):
        print(f'❌ No se encontró {token_file}')
        print('   Ejecuta: python setup_drive_access.py')
        return False
    
    creds = Credentials.from_authorized_user_file(token_file)
    drive_service = build('drive', 'v3', credentials=creds)
    
    # Obtener info de la carpeta (soporte para Shared Drives)
    try:
        folder = drive_service.files().get(
            fileId=FOLDER_ID,
            fields='id, name, mimeType, owners, permissions',
            supportsAllDrives=True
        ).execute()
        
        print('📁 Carpeta de Drive')
        print(f'   Nombre: {folder.get("name")}')
        print(f'   ID: {folder.get("id")}')
        print()
        
    except Exception as e:
        print(f'❌ Error accediendo a la carpeta: {e}')
        return False
    
    # Listar archivos en la carpeta
    print('📄 Contenido de la carpeta:')
    print()
    
    query = f"'{FOLDER_ID}' in parents and trashed=false"
    
    try:
        results = drive_service.files().list(
            q=query,
            pageSize=100,
            fields='files(id, name, mimeType, size, modifiedTime, webViewLink)',
            orderBy='name',
            supportsAllDrives=True,
            includeItemsFromAllDrives=True
        ).execute()
        
        items = results.get('files', [])
        
        if not items:
            print('   (La carpeta está vacía)')
        else:
            for idx, item in enumerate(items, 1):
                mime_type = item.get('mimeType', '')
                size = item.get('size', 'N/A')
                
                # Identificar tipo
                if 'folder' in mime_type:
                    tipo = '📁 Carpeta'
                elif 'spreadsheet' in mime_type:
                    tipo = '📊 Hoja de cálculo'
                elif 'document' in mime_type:
                    tipo = '📝 Documento'
                elif 'presentation' in mime_type:
                    tipo = '📽️ Presentación'
                elif 'pdf' in mime_type:
                    tipo = '📄 PDF'
                else:
                    tipo = '📄 Archivo'
                
                print(f'{idx}. {tipo}')
                print(f'   Nombre: {item["name"]}')
                print(f'   ID: {item["id"]}')
                if size != 'N/A':
                    size_mb = int(size) / (1024*1024)
                    print(f'   Tamaño: {size_mb:.2f} MB')
                print(f'   Link: {item.get("webViewLink", "N/A")}')
                print()
        
        print(f'Total: {len(items)} elementos')
        
    except Exception as e:
        print(f'❌ Error listando archivos: {e}')
        return False
    
    return True

if __name__ == '__main__':
    revisar_carpeta()
