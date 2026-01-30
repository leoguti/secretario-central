#!/usr/bin/env python3
"""
Script para leer el contenido completo del documento de AEMUS
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

def extract_text(document):
    """Extrae todo el texto del documento"""
    body = document.get('body', {})
    content = body.get('content', [])

    full_text = []

    for element in content:
        if 'paragraph' in element:
            para = element['paragraph']
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')
            full_text.append(para_text)
        elif 'table' in element:
            table = element['table']
            full_text.append('\n[TABLA]')
            for row in table.get('tableRows', []):
                row_text = []
                for cell in row.get('tableCells', []):
                    cell_text = ''
                    for cell_content in cell.get('content', []):
                        if 'paragraph' in cell_content:
                            for elem in cell_content['paragraph'].get('elements', []):
                                if 'textRun' in elem:
                                    cell_text += elem['textRun'].get('content', '').strip()
                    row_text.append(cell_text)
                full_text.append(' | '.join(row_text))
            full_text.append('[/TABLA]\n')

    return '\n'.join(full_text)

def main():
    service = get_docs_service()
    document = service.documents().get(documentId=DOC_ID).execute()

    title = document.get('title', 'Sin título')
    print(f'# {title}\n')
    print('=' * 60)

    text = extract_text(document)
    print(text)

if __name__ == '__main__':
    main()
