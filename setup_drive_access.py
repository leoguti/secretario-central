#!/usr/bin/env python3
"""
Script para configurar acceso a Google Drive (leogiga@gmail.com)
Incluye permisos para Gmail Y Drive
"""

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os

# Scopes necesarios: Gmail readonly + Drive readonly
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/drive.readonly'
]

def setup_drive_access():
    """Configura acceso a Drive para cuenta personal"""
    
    creds = None
    
    # Intentar cargar token existente
    if os.path.exists('token_personal_drive.json'):
        print('📋 Cargando token existente...')
        creds = Credentials.from_authorized_user_file('token_personal_drive.json', SCOPES)
    
    # Si no hay credenciales válidas, hacer OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print('🔄 Refrescando token...')
            creds.refresh(Request())
        else:
            print('🔐 Iniciando flujo de autenticación OAuth...')
            print('Se abrirá tu navegador para autorizar acceso a Gmail + Drive')
            print()
            
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials_personal.json', SCOPES
            )
            creds = flow.run_local_server(port=0)
        
        # Guardar credenciales
        with open('token_personal_drive.json', 'w') as token:
            token.write(creds.to_json())
        
        print('✅ Token guardado en token_personal_drive.json')
    
    # Probar acceso a Drive
    from googleapiclient.discovery import build
    
    drive_service = build('drive', 'v3', credentials=creds)
    
    print()
    print('🔍 Probando acceso a Drive...')
    
    # Listar archivos recientes
    results = drive_service.files().list(
        pageSize=10,
        fields='files(id, name, mimeType)'
    ).execute()
    
    items = results.get('files', [])
    
    if not items:
        print('   No se encontraron archivos')
    else:
        print(f'   ✅ Acceso correcto! Encontrados {len(items)} archivos recientes:')
        for item in items[:5]:
            print(f'      - {item["name"]}')
    
    print()
    print('✅ Configuración completada!')
    
    return True

if __name__ == '__main__':
    setup_drive_access()
