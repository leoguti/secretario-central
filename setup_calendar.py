"""
Script para habilitar acceso a Google Calendar.
Ejecutar este script una sola vez para autorizar Calendar.
"""

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import os

# SCOPES: Gmail (readonly) + Calendar (read/write)
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/calendar"
]

def setup_calendar_access():
    """
    Re-autentica con los nuevos scopes incluyendo Calendar.
    """
    print("=" * 80)
    print("🔐 CONFIGURACIÓN DE ACCESO A GOOGLE CALENDAR")
    print("=" * 80)
    print()
    print("Este script va a:")
    print("1. Abrir tu navegador")
    print("2. Pedirte que autorices acceso a Gmail Y Calendar")
    print("3. Guardar el nuevo token con ambos permisos")
    print()
    
    # Verificar que existe credentials.json
    if not os.path.exists("credentials.json"):
        print("❌ ERROR: No se encuentra credentials.json")
        print("   Necesitas el archivo credentials.json de Google Cloud Console")
        return
    
    # Si existe token.json viejo, hacer backup
    if os.path.exists("token.json"):
        print("📦 Haciendo backup del token anterior...")
        os.rename("token.json", "token.json.backup")
        print("   Guardado como token.json.backup")
        print()
    
    print("🌐 Abriendo navegador para autorización...")
    print()
    
    # Iniciar flujo de autenticación
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", 
        SCOPES
    )
    
    # Esto abrirá el navegador
    creds = flow.run_local_server(port=0)
    
    # Guardar nuevo token
    with open("token.json", "w") as token:
        token.write(creds.to_json())
    
    print()
    print("=" * 80)
    print("✅ CONFIGURACIÓN COMPLETADA")
    print("=" * 80)
    print()
    print("Ahora tienes acceso a:")
    print("  ✓ Gmail (lectura)")
    print("  ✓ Google Calendar (lectura y escritura)")
    print()
    print("El token se guardó en: token.json")
    print()

if __name__ == "__main__":
    setup_calendar_access()
