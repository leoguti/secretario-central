"""
Cliente multi-cuenta para Gmail y Calendar.
Soporta múltiples cuentas de Google simultáneamente.
"""

from __future__ import print_function
import os.path
from typing import Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes necesarios
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/calendar"
]

# Mapeo de cuentas a archivos de token
CUENTAS = {
    'trufi': 'token_trufi.json',      # leonardo.gutierrez@trufi-association.org
    'personal': 'token_personal.json'  # leogiga@gmail.com
}


def get_service(service_name: str, version: str, cuenta: str = 'trufi'):
    """
    Obtiene un servicio de Google API (Gmail o Calendar) para una cuenta específica.
    
    Args:
        service_name: 'gmail' o 'calendar'
        version: 'v1' para gmail, 'v3' para calendar
        cuenta: 'trufi' o 'personal'
    
    Returns:
        Google API service object
    """
    token_file = CUENTAS.get(cuenta)
    
    if not token_file:
        print(f"❌ Cuenta '{cuenta}' no reconocida. Usa 'trufi' o 'personal'")
        return None
    
    if not os.path.exists(token_file):
        print(f"❌ Token no encontrado: {token_file}")
        print(f"   Ejecuta: python setup_{'calendar' if cuenta == 'trufi' else 'personal_account'}.py")
        return None
    
    creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open(token_file, "w") as token:
                token.write(creds.to_json())
        else:
            print(f"❌ Token inválido para cuenta '{cuenta}'")
            return None
    
    service = build(service_name, version, credentials=creds)
    return service


def get_gmail_service(cuenta: str = 'trufi'):
    """
    Obtiene servicio de Gmail para la cuenta especificada.
    
    Args:
        cuenta: 'trufi' (leonardo.gutierrez@trufi-association.org) 
                o 'personal' (leogiga@gmail.com)
    """
    return get_service('gmail', 'v1', cuenta)


def get_calendar_service(cuenta: str = 'trufi'):
    """
    Obtiene servicio de Calendar para la cuenta especificada.
    
    Args:
        cuenta: 'trufi' (leonardo.gutierrez@trufi-association.org) 
                o 'personal' (leogiga@gmail.com)
    """
    return get_service('calendar', 'v3', cuenta)


def listar_cuentas_disponibles():
    """
    Lista las cuentas que están configuradas y listas para usar.
    """
    print("📧 CUENTAS CONFIGURADAS:")
    print()
    
    for nombre, archivo in CUENTAS.items():
        existe = os.path.exists(archivo)
        emoji = "✅" if existe else "❌"
        estado = "Configurada" if existe else "No configurada"
        
        if nombre == 'trufi':
            email = "leonardo.gutierrez@trufi-association.org"
        else:
            email = "leogiga@gmail.com"
        
        print(f"{emoji} {nombre.upper()}: {email} - {estado}")
        
        if not existe:
            if nombre == 'trufi':
                print(f"   → Ejecuta: python setup_calendar.py")
            else:
                print(f"   → Ejecuta: python setup_personal_account.py")
    
    print()


if __name__ == "__main__":
    listar_cuentas_disponibles()
