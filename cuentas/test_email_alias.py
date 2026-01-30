#!/usr/bin/env python3
"""
Script para probar envío de correo desde alias leogiga+secretario-ia@gmail.com
"""
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from pathlib import Path

# Configuración
BASE_DIR = Path(__file__).resolve().parent.parent
TOKEN_PATH = BASE_DIR / 'token_personal.json'
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def send_test_email():
    """Envía correo de prueba desde el alias"""
    
    print("📧 Preparando correo de prueba...")
    print(f"   From: leogiga+secretario-ia@gmail.com")
    print(f"   To: info@rumbo.digital")
    print()
    
    # Cargar credenciales
    creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)
    service = build('gmail', 'v1', credentials=creds)
    
    # Crear mensaje
    message = MIMEText('¡Hola!\n\nEste es un correo de prueba del sistema de Secretario-IA.\n\nEstamos probando el envío desde el alias leogiga+secretario-ia@gmail.com\n\nSaludos,\nSecretario-IA 🤖')
    message['To'] = 'info@rumbo.digital'
    message['From'] = 'leogiga+secretario-ia@gmail.com'
    message['Subject'] = 'Prueba de Secretario-IA'
    
    # Codificar
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    
    try:
        # Enviar
        print("📤 Enviando correo...")
        result = service.users().messages().send(
            userId='me',
            body={'raw': raw_message}
        ).execute()
        
        print()
        print("✅ ¡Correo enviado exitosamente!")
        print(f"   Message ID: {result['id']}")
        print()
        print("📬 Revisa info@rumbo.digital en unos segundos.")
        print("   El remitente debe aparecer como: leogiga+secretario-ia@gmail.com")
        
    except Exception as e:
        print(f"❌ Error enviando correo: {e}")
        print()
        print("💡 Posible causa: El token no tiene permisos de envío.")
        print("   Necesitas regenerar el token con scope 'gmail.send'")

if __name__ == '__main__':
    send_test_email()
