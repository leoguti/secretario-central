#!/usr/bin/env python3
"""
Script para probar acceso de lectura/escritura a Google Docs
usando las credenciales de la cuenta Trufi
"""

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime
import json

# ID del documento de AEMUS
DOC_ID = '1HHglOnbnjZkdycsT-Kih0pgGwTJ4GQpoy3jlYsLAhjE'
TOKEN_PATH = 'token_trufi.json'

def get_docs_service():
    """Obtiene el servicio de Google Docs con token de Trufi"""

    # Cargar y refrescar token si es necesario
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

    # Refrescar si expiró
    if creds.expired and creds.refresh_token:
        print('🔄 Refrescando token...')
        creds.refresh(Request())

        # Guardar token actualizado
        token_data['token'] = creds.token
        token_data['expiry'] = creds.expiry.isoformat() if creds.expiry else None
        with open(TOKEN_PATH, 'w') as f:
            json.dump(token_data, f, indent=2)
        print('✅ Token actualizado')

    return build('docs', 'v1', credentials=creds)

def test_read_document(service):
    """Prueba lectura del documento"""
    print('\n📖 PRUEBA DE LECTURA')
    print('=' * 50)

    try:
        document = service.documents().get(documentId=DOC_ID).execute()

        title = document.get('title', 'Sin título')
        print(f'✅ Acceso correcto!')
        print(f'   Título: {title}')

        # Mostrar primeros contenidos
        body = document.get('body', {})
        content = body.get('content', [])

        print(f'   Elementos en el documento: {len(content)}')

        # Extraer texto de los primeros elementos
        text_preview = []
        for element in content[:10]:
            if 'paragraph' in element:
                para = element['paragraph']
                for elem in para.get('elements', []):
                    if 'textRun' in elem:
                        text = elem['textRun'].get('content', '').strip()
                        if text:
                            text_preview.append(text[:100])

        if text_preview:
            print('\n   📝 Vista previa del contenido:')
            for i, text in enumerate(text_preview[:5], 1):
                preview = text[:80] + '...' if len(text) > 80 else text
                print(f'      {i}. {preview}')

        return True

    except HttpError as e:
        print(f'❌ Error de acceso: {e.resp.status}')
        print(f'   {e._get_reason()}')
        return False

def test_write_document(service):
    """Prueba escritura al documento (añade texto al final)"""
    print('\n✏️  PRUEBA DE ESCRITURA')
    print('=' * 50)

    # Primero obtenemos el documento para saber dónde insertar
    try:
        document = service.documents().get(documentId=DOC_ID).execute()

        # Encontrar el índice final del documento
        body = document.get('body', {})
        content = body.get('content', [])

        # El último elemento tiene el endIndex
        end_index = 1
        for element in content:
            if 'endIndex' in element:
                end_index = element['endIndex']

        # Texto de prueba con timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        test_text = f'\n\n[Prueba de escritura automática - {timestamp}]'

        print(f'   Insertando texto de prueba al final (índice {end_index - 1})...')

        # Crear request de inserción
        requests = [
            {
                'insertText': {
                    'location': {
                        'index': end_index - 1  # Justo antes del final
                    },
                    'text': test_text
                }
            }
        ]

        result = service.documents().batchUpdate(
            documentId=DOC_ID,
            body={'requests': requests}
        ).execute()

        print(f'✅ Escritura exitosa!')
        print(f'   Texto insertado: "{test_text.strip()}"')
        print(f'   Documento actualizado correctamente')

        return True

    except HttpError as e:
        print(f'❌ Error de escritura: {e.resp.status}')
        error_details = e._get_reason()
        print(f'   {error_details}')

        if e.resp.status == 403:
            print('\n   💡 Posibles causas:')
            print('      - El documento no está compartido con la cuenta Trufi')
            print('      - La cuenta solo tiene permiso de lectura')
            print('      - Necesitas compartir el documento con permisos de edición')

        return False

def main():
    print('🔗 PRUEBA DE ACCESO A GOOGLE DOCS - DOCUMENTO AEMUS')
    print('=' * 60)
    print(f'   Document ID: {DOC_ID}')
    print(f'   Token: {TOKEN_PATH}')

    try:
        service = get_docs_service()
        print('✅ Servicio de Google Docs conectado')

        # Prueba de lectura
        read_ok = test_read_document(service)

        if read_ok:
            # Preguntar si quiere probar escritura
            print('\n' + '=' * 60)
            response = input('¿Quieres probar la escritura? Esto añadirá texto al documento. (s/n): ')

            if response.lower() in ['s', 'si', 'y', 'yes']:
                test_write_document(service)
            else:
                print('   Escritura omitida.')

    except Exception as e:
        print(f'❌ Error general: {e}')
        raise

if __name__ == '__main__':
    main()
