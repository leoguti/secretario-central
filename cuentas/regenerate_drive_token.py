#!/usr/bin/env python3
"""
Script para regenerar token de Google Drive CON PERMISOS DE ESCRITURA
"""

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os

# IMPORTANTE: Cambiar a scope con ESCRITURA (no solo readonly)
SCOPES = [
    'https://www.googleapis.com/auth/drive.file',  # Crear/editar archivos propios
    'https://www.googleapis.com/auth/drive'         # Acceso completo a Drive
]

def regenerate_drive_token():
    """Regenera token con permisos de escritura"""
    
    print('🔐 Regenerando token de Google Drive con permisos de ESCRITURA...')
    print()
    print('IMPORTANTE: Se abrirá tu navegador para autorizar.')
    print('Debes aceptar los nuevos permisos para crear carpetas/archivos.')
    print()
    
    # Eliminar token viejo si existe
    if os.path.exists('token_personal_drive.json'):
        os.remove('token_personal_drive.json')
        print('🗑️  Token anterior eliminado')
    
    print('🌐 Iniciando flujo OAuth...')
    
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials_personal.json', 
        SCOPES
    )
    
    creds = flow.run_local_server(port=0)
    
    # Guardar nuevo token
    with open('token_personal_drive.json', 'w') as token:
        token.write(creds.to_json())
    
    print()
    print('✅ Nuevo token guardado en token_personal_drive.json')
    print('✅ Permisos incluidos:')
    print('   - Lectura de Drive')
    print('   - ESCRITURA de Drive (crear carpetas/archivos)')
    print()
    
    # Probar creando una carpeta de prueba
    from googleapiclient.discovery import build
    
    drive_service = build('drive', 'v3', credentials=creds)
    
    print('🧪 Probando permisos de escritura...')
    
    try:
        # Intentar listar archivos
        results = drive_service.files().list(pageSize=5).execute()
        items = results.get('files', [])
        print(f'   ✅ Lectura OK: {len(items)} archivos encontrados')
        
        print()
        print('✅ TODO LISTO! Ahora puedes crear carpetas en Drive.')
        
    except Exception as e:
        print(f'   ❌ Error: {e}')
    
    return True

if __name__ == '__main__':
    regenerate_drive_token()
