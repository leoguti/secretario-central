#!/usr/bin/env python3
"""
Script para actualizar el cronograma en la sección 6 del documento AEMUS
"""

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import json

DOC_ID = '1HHglOnbnjZkdycsT-Kih0pgGwTJ4GQpoy3jlYsLAhjE'
TOKEN_PATH = 'token_trufi.json'

def get_docs_service():
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

    return build('docs', 'v1', credentials=creds)

def find_text_position(service, doc_id, search_text):
    """Encuentra la posición de un texto en el documento"""
    document = service.documents().get(documentId=doc_id).execute()
    body = document.get('body', {})
    content = body.get('content', [])

    for element in content:
        if 'paragraph' in element:
            para = element['paragraph']
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    text = elem['textRun'].get('content', '')
                    if search_text in text:
                        return elem.get('startIndex'), elem.get('endIndex')
    return None, None

def replace_text(service, doc_id, old_text, new_text):
    """Reemplaza texto en el documento"""
    requests = [
        {
            'replaceAllText': {
                'containsText': {
                    'text': old_text,
                    'matchCase': True
                },
                'replaceText': new_text
            }
        }
    ]

    result = service.documents().batchUpdate(
        documentId=doc_id,
        body={'requests': requests}
    ).execute()

    replies = result.get('replies', [])
    if replies and 'replaceAllText' in replies[0]:
        count = replies[0]['replaceAllText'].get('occurrencesChanged', 0)
        return count
    return 0

def main():
    print('🔧 ACTUALIZANDO CRONOGRAMA - SECCIÓN 6')
    print('=' * 60)

    service = get_docs_service()
    print('✅ Conectado a Google Docs\n')

    # Texto antiguo de la tabla (buscar el encabezado para identificar)
    old_table_header = "Desarrollo de la aplicación personalizada\t3 meses"

    # El texto viejo completo de la celda de condiciones
    old_condition_text = "⚠️ Importante:El desarrollo requiere que se proporcione  elbranding institucional completo(logos, colores, lineamientos gráficos).Este servicio de diseño de branding NO está incluido en esta ofertay debe ser proporcionado por el cliente."

    new_condition_text = "⚠️ Importante: El desarrollo requiere branding institucional completo (logos, colores, lineamientos gráficos). Este servicio NO está incluido y debe ser proporcionado por el cliente."

    # Primero corregimos el texto de condiciones si existe
    count = replace_text(service, DOC_ID, old_condition_text, new_condition_text)
    if count > 0:
        print(f'✅ Corregido texto de condiciones')

    # Ahora vamos a reemplazar las filas de la tabla una por una
    # Fila 1: Desarrollo de aplicación
    replacements = [
        # Actualizar tiempo de desarrollo app
        ("3 meses\tInicia con entrega de branding", "3 meses\tMeses 2-4 (paralelo a GTFS desde mes 2)"),

        # Agregar más contenido si es necesario mediante texto
    ]

    for old, new in replacements:
        count = replace_text(service, DOC_ID, old, new)
        if count > 0:
            print(f'✅ Actualizado: "{old[:40]}..."')
        else:
            print(f'⚠️  No encontrado: "{old[:40]}..."')

    print('\n' + '=' * 60)
    print('ℹ️  La tabla actual tiene formato complejo.')
    print('   Te recomiendo que copies el nuevo cronograma manualmente.')
    print('=' * 60)

if __name__ == '__main__':
    main()
