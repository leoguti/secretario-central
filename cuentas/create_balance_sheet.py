#!/usr/bin/env python3
"""
Script para crear el Google Sheet "BALANCE FINANCIERO 2026"
"""
from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file'
]

BASE_DIR = Path(__file__).resolve().parent.parent
TOKEN_PATH = BASE_DIR / 'token_personal_drive.json'
FINANZAS_FOLDER_ID = '1yKx1kfJsJAO_iC_6K0_2DTubWaGXM8Q2'

def create_balance_sheet():
    """Crea el sheet BALANCE FINANCIERO 2026 con tabs básicos"""
    
    print('📊 Creando Google Sheet "BALANCE FINANCIERO 2026"...')
    
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    sheets_service = build('sheets', 'v4', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)
    
    # Crear spreadsheet
    spreadsheet = {
        'properties': {
            'title': 'BALANCE FINANCIERO 2026',
            'locale': 'es_CO',
            'timeZone': 'America/Bogota'
        },
        'sheets': [
            {
                'properties': {
                    'title': 'Transacciones',
                    'gridProperties': {'rowCount': 1000, 'columnCount': 12}
                }
            },
            {
                'properties': {
                    'title': 'Resumen Mensual',
                    'gridProperties': {'rowCount': 100, 'columnCount': 10}
                }
            },
            {
                'properties': {
                    'title': 'Estrategia Deuda',
                    'gridProperties': {'rowCount': 100, 'columnCount': 10}
                }
            },
            {
                'properties': {
                    'title': 'Fondo Emergencia',
                    'gridProperties': {'rowCount': 100, 'columnCount': 8}
                }
            }
        ]
    }
    
    result = sheets_service.spreadsheets().create(body=spreadsheet).execute()
    spreadsheet_id = result['spreadsheetId']
    
    print(f'✅ Sheet creado con ID: {spreadsheet_id}')
    
    # Mover a carpeta Finanzas
    file = drive_service.files().get(fileId=spreadsheet_id, fields='parents').execute()
    previous_parents = ','.join(file.get('parents', []))
    
    drive_service.files().update(
        fileId=spreadsheet_id,
        addParents=FINANZAS_FOLDER_ID,
        removeParents=previous_parents,
        fields='id, parents'
    ).execute()
    
    print(f'✅ Sheet movido a carpeta Finanzas')
    
    # Configurar encabezados del tab Transacciones
    headers = [
        'Fecha', 'Tipo', 'Categoría', 'Subcategoría', 'Concepto',
        'Monto', 'Método Pago', 'Recibo', 'Fuente', 'Procesado Por',
        'Notas', 'Estado'
    ]
    
    requests = [
        {
            'updateCells': {
                'range': {
                    'sheetId': 0,
                    'startRowIndex': 0,
                    'endRowIndex': 1,
                    'startColumnIndex': 0,
                    'endColumnIndex': len(headers)
                },
                'rows': [{
                    'values': [
                        {
                            'userEnteredValue': {'stringValue': header},
                            'userEnteredFormat': {
                                'backgroundColor': {'red': 0.2, 'green': 0.6, 'blue': 0.9},
                                'textFormat': {'bold': True, 'foregroundColor': {'red': 1, 'green': 1, 'blue': 1}}
                            }
                        } for header in headers
                    ]
                }],
                'fields': 'userEnteredValue,userEnteredFormat'
            }
        },
        {
            'autoResizeDimensions': {
                'dimensions': {
                    'sheetId': 0,
                    'dimension': 'COLUMNS',
                    'startIndex': 0,
                    'endIndex': len(headers)
                }
            }
        }
    ]
    
    sheets_service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={'requests': requests}
    ).execute()
    
    print(f'✅ Encabezados configurados')
    print(f'\n🎉 SHEET LISTO!')
    print(f'📊 Link: https://docs.google.com/spreadsheets/d/{spreadsheet_id}')
    print(f'\n💾 Guarda este ID: {spreadsheet_id}')
    
    return spreadsheet_id

if __name__ == '__main__':
    create_balance_sheet()
