#!/usr/bin/env python3
"""
Regenerar token personal CON permisos de envío de Gmail
"""

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import os

# Scopes necesarios: Gmail envío + Drive
SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',       # Enviar emails
    'https://www.googleapis.com/auth/gmail.readonly',   # Leer emails
    'https://www.googleapis.com/auth/drive',            # Drive completo
    'https://www.googleapis.com/auth/drive.file'        # Crear archivos
]

def regenerate_token_with_gmail_send():
    """Regenera token con permisos de Gmail send"""
    
    print('🔐 Regenerando token con permisos de Gmail SEND + Drive...')
    print()
    print('Scopes incluidos:')
    print('  ✅ Gmail: Enviar correos')
    print('  ✅ Gmail: Leer correos')
    print('  ✅ Drive: Lectura/Escritura completa')
    print()
    
    # Eliminar token viejo
    if os.path.exists('token_personal.json'):
        os.remove('token_personal.json')
        print('🗑️  Token anterior eliminado')
    
    print('🌐 Abriendo navegador para autorización...')
    
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials_personal.json', 
        SCOPES
    )
    
    creds = flow.run_local_server(port=0)
    
    # Guardar nuevo token
    with open('token_personal.json', 'w') as token:
        token.write(creds.to_json())
    
    print()
    print('✅ Nuevo token guardado!')
    print('✅ Ahora puedes enviar emails desde leogiga+secretario-ia@gmail.com')
    print()
    
    return True

if __name__ == '__main__':
    regenerate_token_with_gmail_send()
