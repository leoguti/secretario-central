#!/usr/bin/env python3
"""
Script para corregir errores en el documento de AEMUS
"""

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
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
    print('🔧 CORRIGIENDO DOCUMENTO AEMUS')
    print('=' * 60)

    service = get_docs_service()
    print('✅ Conectado a Google Docs\n')

    # Lista de correcciones
    correcciones = [
        # Error 1: México por Perú en contexto de impuestos
        ('impuestos aplicables en México', 'impuestos aplicables en Perú'),

        # Error 2: IVA por IGV (impuesto peruano)
        ('(IVA u otros)', '(IGV u otros)'),

        # Error 3: Agregar moneda local donde falta
        ('Si el pago se realiza en , se liquidará', 'Si el pago se realiza en PEN (Soles peruanos), se liquidará'),

        # Error 4: Precio de renovación incorrecto
        ('la renovación es 2,500 €/año', 'la renovación es 1,500 €/año'),

        # Error 5: Typo en glosario
        ('zona de operacións', 'zonas de operaciones'),

        # Eliminar el texto de prueba que inserté antes
        ('[Prueba de escritura automática - 2026-01-22 09:31:24]', ''),
    ]

    total_cambios = 0

    for old_text, new_text in correcciones:
        try:
            count = replace_text(service, DOC_ID, old_text, new_text)
            if count > 0:
                print(f'✅ Corregido ({count}x): "{old_text[:50]}..."')
                print(f'   → "{new_text[:50]}..."' if new_text else '   → [eliminado]')
                total_cambios += count
            else:
                print(f'⚠️  No encontrado: "{old_text[:50]}..."')
        except HttpError as e:
            print(f'❌ Error: {e._get_reason()}')

    print()
    print('=' * 60)
    print(f'✅ CORRECCIONES COMPLETADAS: {total_cambios} cambios realizados')
    print('=' * 60)

if __name__ == '__main__':
    main()
