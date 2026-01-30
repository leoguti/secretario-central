#!/usr/bin/env python3
"""
Crear hoja de cálculo en Google Sheets para oportunidades DEVEX
"""

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime

# Autenticación con cuenta Trufi
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

def create_devex_opportunities_sheet():
    """Crear hoja de cálculo con oportunidades DEVEX"""
    
    # Cargar credenciales
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Conectar a Google Sheets
    sheets_service = build('sheets', 'v4', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)
    
    # Crear nueva hoja de cálculo
    spreadsheet = {
        'properties': {
            'title': f'Oportunidades DEVEX - {datetime.now().strftime("%Y-%m")}'
        },
        'sheets': [{
            'properties': {
                'title': 'Oportunidades',
                'gridProperties': {
                    'frozenRowCount': 1
                }
            }
        }]
    }
    
    spreadsheet = sheets_service.spreadsheets().create(
        body=spreadsheet,
        fields='spreadsheetId,spreadsheetUrl'
    ).execute()
    
    spreadsheet_id = spreadsheet.get('spreadsheetId')
    spreadsheet_url = spreadsheet.get('spreadsheetUrl')
    
    print(f"✅ Hoja creada: {spreadsheet_url}")
    
    # Datos iniciales - Oportunidades conocidas
    values = [
        # Encabezados
        ['ID', 'Tipo', 'Título', 'Organización', 'País/Región', 'Deadline', 'URL', 'Estado', 'Prioridad', 'Notas'],
        
        # Oportunidades con datos parciales
        ['843233', 'Tender', 'Kiribati Urban Policy - Consultancy Services', 'World Bank Group', 'Kiribati', '2026-01-15', 
         'https://www.devex.com/funding/tenders/843233', 'VENCIDO', 'BAJA', 'Deadline pasado'],
        
        ['843260', 'Tender', '(Revisar en plataforma)', '?', '?', '?', 
         'https://www.devex.com/funding/tenders/843260', 'PENDIENTE REVISAR', '', ''],
        
        ['843329', 'Tender', '(Revisar en plataforma)', '?', '?', '?', 
         'https://www.devex.com/funding/tenders/843329', 'PENDIENTE REVISAR', '', ''],
        
        ['843302', 'Tender', '(Revisar en plataforma)', '?', '?', '?', 
         'https://www.devex.com/funding/tenders/843302', 'PENDIENTE REVISAR', '', ''],
        
        ['843364', 'Tender', '(Revisar en plataforma)', '?', '?', '?', 
         'https://www.devex.com/funding/tenders/843364', 'PENDIENTE REVISAR', '', ''],
        
        ['843255', 'Tender', '(Revisar en plataforma)', '?', '?', '?', 
         'https://www.devex.com/funding/tenders/843255', 'PENDIENTE REVISAR', '', ''],
        
        ['843259', 'Tender', '(Revisar en plataforma)', '?', '?', '?', 
         'https://www.devex.com/funding/tenders/843259', 'PENDIENTE REVISAR', '', ''],
        
        ['52059', 'Grant', '(Revisar en plataforma)', '?', '?', '?', 
         'https://www.devex.com/funding/grants/52059', 'PENDIENTE REVISAR', '', ''],
        
        ['52064', 'Grant', '(Revisar en plataforma)', '?', '?', '?', 
         'https://www.devex.com/funding/grants/52064', 'PENDIENTE REVISAR', '', ''],
        
        ['52058', 'Grant', '(Revisar en plataforma)', '?', '?', '?', 
         'https://www.devex.com/funding/grants/52058', 'PENDIENTE REVISAR', '', ''],
    ]
    
    # Escribir datos
    body = {'values': values}
    sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range='Oportunidades!A1:J',
        valueInputOption='RAW',
        body=body
    ).execute()
    
    # Formatear encabezados
    requests = [
        # Encabezados en negrita y con fondo
        {
            'repeatCell': {
                'range': {
                    'sheetId': 0,
                    'startRowIndex': 0,
                    'endRowIndex': 1
                },
                'cell': {
                    'userEnteredFormat': {
                        'backgroundColor': {'red': 0.2, 'green': 0.6, 'blue': 0.9},
                        'textFormat': {'bold': True, 'foregroundColor': {'red': 1, 'green': 1, 'blue': 1}},
                        'horizontalAlignment': 'CENTER'
                    }
                },
                'fields': 'userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)'
            }
        },
        # Auto-resize columnas
        {
            'autoResizeDimensions': {
                'dimensions': {
                    'sheetId': 0,
                    'dimension': 'COLUMNS',
                    'startIndex': 0,
                    'endIndex': 10
                }
            }
        },
        # Columna URL como hipervínculo (color azul)
        {
            'repeatCell': {
                'range': {
                    'sheetId': 0,
                    'startRowIndex': 1,
                    'startColumnIndex': 6,
                    'endColumnIndex': 7
                },
                'cell': {
                    'userEnteredFormat': {
                        'textFormat': {'foregroundColor': {'red': 0.06, 'green': 0.42, 'blue': 0.82}, 'underline': True}
                    }
                },
                'fields': 'userEnteredFormat.textFormat'
            }
        }
    ]
    
    sheets_service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={'requests': requests}
    ).execute()
    
    print(f"✅ Formato aplicado")
    print(f"\n📊 Total oportunidades listadas: {len(values)-1}")
    print(f"\n🔗 URL: {spreadsheet_url}")
    
    # Guardar URL en archivo
    with open('/home/leonardo-gutierrez/secretario/devex_sheet_url.txt', 'w') as f:
        f.write(spreadsheet_url)
    
    return spreadsheet_url

if __name__ == '__main__':
    create_devex_opportunities_sheet()
