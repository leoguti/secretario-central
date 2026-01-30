#!/usr/bin/env python3
"""
Script para re-autorizar cuenta Trufi con permisos de escritura en Gmail.
Diseñado para funcionar desde terminal en celular (no abre navegador automáticamente).

Cuenta: leonardo.gutierrez@trufi-association.org
Token: token_trufi.json
"""

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os
import shutil

# Scopes: lectura Gmail + crear borradores/enviar + Calendar
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.compose",
    "https://www.googleapis.com/auth/calendar"
]

TOKEN_FILE = "token_trufi.json"
CREDENTIALS_FILE = "credentials.json"


def setup():
    print("=" * 60)
    print("  RE-AUTORIZACION CUENTA TRUFI")
    print("  leonardo.gutierrez@trufi-association.org")
    print("=" * 60)
    print()
    print("Permisos solicitados:")
    print("  - Gmail lectura")
    print("  - Gmail crear borradores y enviar")
    print("  - Google Calendar")
    print()

    if not os.path.exists(CREDENTIALS_FILE):
        print(f"ERROR: No se encuentra {CREDENTIALS_FILE}")
        return

    # Backup del token actual
    if os.path.exists(TOKEN_FILE):
        backup = f"{TOKEN_FILE}.backup"
        shutil.copy(TOKEN_FILE, backup)
        print(f"Backup guardado en: {backup}")
        print()

    print("INSTRUCCIONES:")
    print("1. Copia la URL que aparece abajo")
    print("2. Abrela en el navegador del celular")
    print("3. Selecciona la cuenta: leonardo.gutierrez@trufi-association.org")
    print("4. Acepta los permisos")
    print("5. Se redirige automaticamente y el script captura el codigo")
    print()

    flow = InstalledAppFlow.from_client_secrets_file(
        CREDENTIALS_FILE, SCOPES
    )

    # open_browser=False: solo imprime la URL, no intenta abrir navegador
    # port=8080: puerto fijo para que sea predecible
    creds = flow.run_local_server(port=8095, open_browser=False)

    # Guardar nuevo token
    with open(TOKEN_FILE, "w") as token:
        token.write(creds.to_json())

    print()
    print("=" * 60)
    print("  VERIFICANDO ACCESOS")
    print("=" * 60)
    print()

    # Test Gmail
    try:
        gmail = build("gmail", "v1", credentials=creds)
        profile = gmail.users().getProfile(userId="me").execute()
        print(f"Gmail OK: {profile['emailAddress']}")
    except Exception as e:
        print(f"Gmail ERROR: {e}")

    # Test crear borrador (vacio, luego se borra)
    try:
        draft = gmail.users().drafts().create(
            userId="me",
            body={"message": {"raw": ""}}
        ).execute()
        # Borrar el draft de prueba
        gmail.users().drafts().delete(userId="me", id=draft["id"]).execute()
        print("Borradores OK: puede crear y eliminar")
    except Exception as e:
        print(f"Borradores ERROR: {e}")

    # Test Calendar
    try:
        cal = build("calendar", "v3", credentials=creds)
        cals = cal.calendarList().list().execute()
        print(f"Calendar OK: {len(cals.get('items', []))} calendarios")
    except Exception as e:
        print(f"Calendar ERROR: {e}")

    print()
    print("=" * 60)
    print(f"Token guardado en: {TOKEN_FILE}")
    print("Ya puedes crear borradores desde el secretario.")
    print("=" * 60)


if __name__ == "__main__":
    try:
        setup()
    except KeyboardInterrupt:
        print("\nCancelado.")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
