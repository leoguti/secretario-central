#!/usr/bin/env python3
"""
Script para insertar disclaimer de licencias en el documento de AEMUS
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
    print('📝 INSERTANDO DISCLAIMER DE LICENCIAS')
    print('=' * 60)

    service = get_docs_service()
    print('✅ Conectado a Google Docs\n')

    # Texto actual de la sección A.7
    texto_actual = """A.7. ¿De quién son los datos?

• Rutas y paraderos (GTFS): Propiedad de AEMUS. Se publican para aparecer en Google Maps.
• Estadísticas de uso de la app: Propiedad de AEMUS. Información privada para planificación.
• Ubicación de buses: Propiedad de AEMUS. Solo se muestra en la app.

Importante: Trufi administra la tecnología, pero todos los datos generados son propiedad exclusiva de AEMUS."""

    # Nuevo texto con disclaimer completo
    texto_nuevo = """A.7. Propiedad de Datos y Licencias de Software

Es importante distinguir entre la propiedad de los datos y las licencias del software:

PROPIEDAD DE LOS DATOS
Todos los datos generados por el proyecto son propiedad exclusiva de AEMUS:

• Rutas y paraderos (GTFS): Propiedad de AEMUS. Se publican en formato abierto para aparecer en Google Maps y otras plataformas de movilidad.
• Estadísticas de uso de la app: Propiedad de AEMUS. Información privada y confidencial para uso interno en planificación del servicio.
• Ubicación de buses: Propiedad de AEMUS. Solo se muestra a usuarios de la app, no se comparte con terceros.

Trufi Association administra la infraestructura tecnológica, pero no tiene ningún derecho sobre los datos de AEMUS.

LICENCIAS DEL SOFTWARE
El software utilizado en este proyecto se desarrolla bajo licencias de código abierto (open source):

• El código fuente de la aplicación móvil y componentes desarrollados se entrega bajo licencia abierta, lo que permite a AEMUS:
  - Usar el software sin restricciones
  - Modificarlo o adaptarlo según sus necesidades futuras
  - Contratar a cualquier desarrollador para darle mantenimiento
  - No depender exclusivamente de Trufi para cambios futuros

• El código abierto NO significa que los datos sean públicos. Son conceptos separados:
  - Código = las instrucciones que hacen funcionar la app (abierto)
  - Datos = la información de rutas, usuarios y buses (propiedad de AEMUS)

• Trufi Association es una organización sin fines de lucro que promueve el transporte público mediante tecnologías abiertas. El uso de licencias open source es parte de nuestra filosofía institucional y beneficia a AEMUS al evitar dependencia tecnológica.

Nota: Los componentes de terceros (OpenTripPlanner, Flutter, OpenStreetMap) mantienen sus licencias originales, todas compatibles con uso comercial y sin costo de licenciamiento."""

    count = replace_text(service, DOC_ID, texto_actual, texto_nuevo)

    if count > 0:
        print('✅ Disclaimer insertado correctamente')
        print(f'   Secciones actualizadas: {count}')
    else:
        print('⚠️  No se encontró el texto a reemplazar')
        print('   Intentando insertar al final del anexo...')

        # Buscar donde insertar después de A.7
        get_document_end_index_and_insert(service, DOC_ID)

def get_document_end_index_and_insert(service, doc_id):
    """Inserta el disclaimer al final si no se pudo reemplazar"""
    document = service.documents().get(documentId=doc_id).execute()
    body = document.get('body', {})
    content = body.get('content', [])

    end_index = 1
    for element in content:
        if 'endIndex' in element:
            end_index = element['endIndex']

    disclaimer_adicional = """


NOTA IMPORTANTE SOBRE LICENCIAS Y PROPIEDAD

Propiedad de los Datos:
Todos los datos generados (rutas GTFS, estadísticas de uso, ubicaciones GPS) son propiedad exclusiva de AEMUS. Trufi solo administra la tecnología.

Licencias del Software:
El código se entrega bajo licencia abierta (open source). Esto significa que AEMUS puede usar, modificar y mantener el software sin restricciones ni dependencia de Trufi. El código abierto NO afecta la propiedad de los datos - son conceptos independientes.

"""

    requests = [
        {
            'insertText': {
                'location': {
                    'index': end_index - 1
                },
                'text': disclaimer_adicional
            }
        }
    ]

    service.documents().batchUpdate(
        documentId=doc_id,
        body={'requests': requests}
    ).execute()

    print('✅ Disclaimer adicional insertado al final')

if __name__ == '__main__':
    main()
