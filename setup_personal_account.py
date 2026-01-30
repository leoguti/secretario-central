"""
Script para configurar acceso a cuenta personal de Gmail/Calendar.
Este script crea un token separado para leogiga@gmail.com
"""

from google_auth_oauthlib.flow import InstalledAppFlow
import os

# SCOPES: Gmail (readonly) + Calendar (read/write)
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/calendar"
]

def setup_personal_account():
    """
    Configura acceso a cuenta personal (leogiga@gmail.com).
    Guarda el token en token_personal.json
    """
    print("=" * 80)
    print("🔐 CONFIGURACIÓN DE CUENTA PERSONAL")
    print("=" * 80)
    print()
    print("Este script configurará acceso a: leogiga@gmail.com")
    print()
    print("⚠️  IMPORTANTE:")
    print("   Cuando se abra el navegador, asegúrate de:")
    print("   1. Seleccionar la cuenta: leogiga@gmail.com")
    print("   2. NO seleccionar: leonardo.gutierrez@trufi-association.org")
    print()
    
    # Usar credentials_personal.json
    if not os.path.exists("credentials_personal.json"):
        print("❌ ERROR: No se encuentra credentials_personal.json")
        return
    
    # Si existe token_personal.json viejo, hacer backup
    if os.path.exists("token_personal.json"):
        print("📦 Token personal existente encontrado.")
        respuesta = input("   ¿Deseas re-autorizar? (s/n): ")
        if respuesta.lower() != 's':
            print("   Operación cancelada.")
            return
        os.rename("token_personal.json", "token_personal.json.backup")
        print("   Backup guardado como token_personal.json.backup")
        print()
    
    print("🌐 Abriendo navegador para autorización...")
    print()
    print("👉 SELECCIONA LA CUENTA: leogiga@gmail.com")
    print()
    
    # Iniciar flujo de autenticación con credentials_personal.json
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials_personal.json", 
        SCOPES
    )
    
    # Esto abrirá el navegador
    creds = flow.run_local_server(port=0)
    
    # Guardar token en archivo separado
    with open("token_personal.json", "w") as token:
        token.write(creds.to_json())
    
    print()
    print("=" * 80)
    print("✅ CUENTA PERSONAL CONFIGURADA")
    print("=" * 80)
    print()
    print("Token guardado en: token_personal.json")
    print()
    print("Ahora el Secretario puede acceder a:")
    print("  📧 Gmail: leogiga@gmail.com")
    print("  📅 Calendar: leogiga@gmail.com")
    print()

if __name__ == "__main__":
    setup_personal_account()
