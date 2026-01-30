#!/usr/bin/env python3
"""
Script para leer documento en Shared Drive
"""

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import json

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

    # Obtener metadata del archivo CON soporte para Shared Drives
    try:
        file_metadata = service.files().get(
            fileId=DOC_ID,
            fields='id, name, mimeType, driveId',
            supportsAllDrives=True
        ).execute()

        print(f"Archivo: {file_metadata.get('name')}")
        print(f"Tipo: {file_metadata.get('mimeType')}")
        print(f"Drive ID: {file_metadata.get('driveId', 'Personal')}")
        print('=' * 60)

        mime_type = file_metadata.get('mimeType', '')

        # Si es un documento de Google o Word, exportar como texto
        if 'document' in mime_type or 'word' in mime_type:
            content = service.files().export(
                fileId=DOC_ID,
                mimeType='text/plain'
            ).execute()

            if isinstance(content, bytes):
                content = content.decode('utf-8')

            print(content)

        else:
            print(f"Tipo de archivo no soportado para exportación de texto: {mime_type}")

    except Exception as e:
        print(f"Error: {e}")

        # Listar archivos en shared drives para debug
        print("\nBuscando en Shared Drives...")
        results = service.files().list(
            q=f"name contains 'arquitectura' or name contains 'Trujillo'",
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
            fields='files(id, name, mimeType, driveId)'
        ).execute()

        files = results.get('files', [])
        if files:
            print(f"Encontrados {len(files)} archivos:")
            for f in files[:10]:
                print(f"  - {f['name']} ({f['mimeType']}) ID: {f['id']}")
        else:
            print("No se encontraron archivos")

if __name__ == '__main__':
    main()
