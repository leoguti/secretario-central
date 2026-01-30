#!/usr/bin/env python3
"""
Script para habilitar Google Sheets API en el proyecto
"""
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import webbrowser

# Leer el project ID de las credenciales
import json

with open('credentials_personal.json', 'r') as f:
    creds_data = json.load(f)
    if 'installed' in creds_data:
        project_id = creds_data['installed'].get('project_id', 'No encontrado')
    elif 'web' in creds_data:
        project_id = creds_data['web'].get('project_id', 'No encontrado')
    else:
        project_id = 'No encontrado'

print('🔧 Para habilitar Google Sheets API:')
print('=' * 60)
print(f'Project ID: {project_id}')
print()
print('Abre este link en tu navegador:')
print(f'https://console.developers.google.com/apis/api/sheets.googleapis.com/overview?project={project_id}')
print()
print('Luego:')
print('  1. Click en "HABILITAR" o "ENABLE"')
print('  2. Espera 1-2 minutos')
print('  3. Vuelve aquí y confirma')
print()

input('Presiona ENTER cuando hayas habilitado la API...')

print()
print('✅ Ahora prueba acceder al spreadsheet.')
