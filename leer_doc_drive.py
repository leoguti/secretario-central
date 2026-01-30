#!/usr/bin/env python3
"""
Script para leer documento via Drive API (para archivos Word/importados)
"""

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import json
import io

DOC_ID = '1z0HYH29b_JHrEPIMQuZD73Kt5cO7n4WX'
TOKEN_PATH = 'token_trufi.json'

def get_drive_service():
    with open(TOKEN_PATH, 'r') as f:
        token_data = json.load(f)

    creds = Credentials(
        token=token_data['token'],
        refresh_token=token_data['refresh_token'],
        token_uri=token_data['token_uri'],
        client_id=token_data['client_id'],
        client_secret=token_data['client_secret'],
        scopes=token_data['scopes']
    )

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        token_data['token'] = creds.token
        with open(TOKEN_PATH, 'w') as f:
            json.dump(token_data, f, indent=2)

    return build('drive', 'v3', credentials=creds)

def main():
    service = get_drive_service()

    # Obtener metadata del archivo
    file_metadata = service.files().get(
        fileId=DOC_ID,
        fields='id, name, mimeType'
    ).execute()

    print(f"Archivo: {file_metadata.get('name')}")
    print(f"Tipo: {file_metadata.get('mimeType')}")
    print('=' * 60)

    # Exportar como texto plano
    try:
        content = service.files().export(
            fileId=DOC_ID,
            mimeType='text/plain'
        ).execute()

        if isinstance(content, bytes):
            content = content.decode('utf-8')

        print(content)

    except Exception as e:
        print(f"Error exportando: {e}")

        # Intentar descargar directamente
        try:
            content = service.files().get_media(fileId=DOC_ID).execute()
            print(f"Contenido binario: {len(content)} bytes")
        except Exception as e2:
            print(f"Error descargando: {e2}")

if __name__ == '__main__':
    main()
