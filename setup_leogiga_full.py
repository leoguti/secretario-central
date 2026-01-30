#!/usr/bin/env python3
"""
Script para configurar acceso COMPLETO a cuenta personal leogiga@gmail.com
Incluye: Gmail, Calendar y Drive (lectura/escritura)
"""

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os

# Scopes completos para Gmail, Calendar y Drive
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
]

def setup_leogiga_access():
    """Configura acceso completo a cuenta personal leogiga@gmail.com"""
    
    print('='*80)
    print('🔐 CONFIGURACIÓN COMPLETA - CUENTA PERSONAL')
    print('='*80)
    print()
    print('   Cuenta: leogiga@gmail.com')
    print('   Permisos: Gmail + Calendar + Drive (completo)')
    print()
    print('⚠️  IMPORTANTE: Selecciona leogiga@gmail.com cuando se abra el navegador')
    print()
    
    creds = None
    token_file = 'token_leogiga.json'
    
    # Hacer backup si existe
    if os.path.exists(token_file):
        print(f'📦 Token existente encontrado.')
        respuesta = input('   ¿Deseas re-autorizar? (s/n): ')
        if respuesta.lower() != 's':
            print('❌ Cancelado')
            return False
        
        # Backup
        import shutil
        shutil.copy(token_file, f'{token_file}.backup')
        print(f'   Backup guardado como {token_file}.backup')
    
    print()
    print('🌐 Abriendo navegador para autorización...')
    print()
    print('👉 SELECCIONA LA CUENTA: leogiga@gmail.com')
    print()
    
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials_personal.json', SCOPES
    )
    creds = flow.run_local_server(port=0)
    
    # Guardar credenciales
    with open(token_file, 'w') as token:
        token.write(creds.to_json())
    
    print()
    print('✅ Token guardado en', token_file)
    print()
    
    # Probar accesos
    from googleapiclient.discovery import build
    
    print('='*80)
    print('🧪 PROBANDO ACCESOS')
    print('='*80)
    print()
    
    # Test Gmail
    try:
        gmail = build('gmail', 'v1', credentials=creds)
        profile = gmail.users().getProfile(userId='me').execute()
        print(f'✅ Gmail: {profile["emailAddress"]}')
    except Exception as e:
        print(f'❌ Gmail: Error - {e}')
    
    # Test Calendar
    try:
        calendar = build('calendar', 'v3', credentials=creds)
        calendars = calendar.calendarList().list().execute()
        print(f'✅ Calendar: {len(calendars.get("items", []))} calendarios')
    except Exception as e:
        print(f'❌ Calendar: Error - {e}')
    
    # Test Drive
    try:
        drive = build('drive', 'v3', credentials=creds)
        results = drive.files().list(pageSize=5, fields='files(id, name)').execute()
        items = results.get('files', [])
        print(f'✅ Drive: {len(items)} archivos encontrados')
        for item in items[:3]:
            print(f'      - {item["name"]}')
    except Exception as e:
        print(f'❌ Drive: Error - {e}')
    
    print()
    print('='*80)
    print('✅ CONFIGURACIÓN COMPLETADA!')
    print('='*80)
    print()
    print(f'💾 Token guardado en: {token_file}')
    print('📋 Este token tiene acceso completo a Gmail, Calendar y Drive')
    print()
    
    return True

if __name__ == '__main__':
    try:
        setup_leogiga_access()
    except KeyboardInterrupt:
        print()
        print('❌ Cancelado por el usuario')
    except Exception as e:
        print(f'❌ Error: {e}')
        import traceback
        traceback.print_exc()
