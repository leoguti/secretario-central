#!/usr/bin/env python3
"""
Script para insertar el anexo técnico en el documento de AEMUS
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

def get_document_end_index(service, doc_id):
    """Obtiene el índice final del documento"""
    document = service.documents().get(documentId=doc_id).execute()
    body = document.get('body', {})
    content = body.get('content', [])

    end_index = 1
    for element in content:
        if 'endIndex' in element:
            end_index = element['endIndex']

    return end_index - 1

def main():
    print('📝 INSERTANDO ANEXO TÉCNICO EN DOCUMENTO AEMUS')
    print('=' * 60)

    service = get_docs_service()
    print('✅ Conectado a Google Docs\n')

    # Obtener posición final
    end_index = get_document_end_index(service, DOC_ID)
    print(f'   Insertando en posición: {end_index}')

    # Texto del anexo técnico (simplificado para Google Docs)
    anexo_texto = """


ANEXO A: Arquitectura Técnica del Sistema

Este anexo describe de forma general cómo funcionará el sistema de la aplicación móvil para AEMUS.


A.1. ¿Cómo funciona el sistema?

El sistema tiene tres partes principales que trabajan juntas:

1. APLICACIÓN MÓVIL (lo que usan los pasajeros)
   • Buscar cómo llegar de un punto a otro
   • Ver dónde están los buses en el mapa
   • Saber cuánto falta para que llegue el bus
   • Consultar saldo de tarjeta (opcional)

2. SERVIDORES EN LA NUBE (administrados por Trufi)
   • Calculan las mejores rutas para el usuario
   • Reciben la ubicación de los 430 buses
   • Envían información actualizada a la app

3. SISTEMAS DE AEMUS (ya existentes)
   • Sistema GPS de los 430 buses
   • Sistema de pagos MOVILIZATE (opcional)


A.2. La Aplicación Móvil

Es lo que los pasajeros descargan en su teléfono.

• Disponible en: Android (Google Play) e iOS (App Store)
• Funciona en: Teléfonos con Android 6.0+ o iPhone con iOS 12+
• Requiere: Conexión a internet y GPS activado
• Idioma: Español


A.3. Los Servidores en la Nube

Son computadoras en internet que hacen todo el trabajo pesado:

• Calculan rutas: Cuando un usuario pregunta "¿cómo llego de A a B?", el servidor calcula las mejores opciones usando las 4 rutas de AEMUS y otras rutas de Lima.

• Procesan ubicaciones: Reciben constantemente la posición de los 430 buses y la muestran en el mapa de la app.

• Están siempre disponibles: Funcionan 24 horas, 7 días a la semana, con copias de seguridad automáticas.


A.4. ¿Qué datos se utilizan?

Datos de las Rutas (GTFS)
GTFS es un formato estándar mundial para describir rutas de transporte público. Incluye:
• El recorrido exacto de cada ruta (por qué calles pasa)
• La ubicación de los paraderos
• Los horarios y frecuencias de servicio
• Información de los operadores

Estos datos permiten que la app calcule rutas y que AEMUS aparezca en Google Maps.

Datos del GPS (Tiempo Real)
La app muestra dónde está cada bus en tiempo real gracias a:
• El sistema GPS que ya tiene AEMUS instalado en sus 430 buses
• Una conexión entre ese sistema y nuestros servidores
• Actualización cada pocos segundos en el mapa de la app


A.5. Tecnologías Utilizadas

Todo el sistema usa tecnologías de código abierto (open source), lo que significa:
• No hay costos de licencias de software
• Son tecnologías probadas y usadas en todo el mundo
• AEMUS no queda "atado" a un solo proveedor

Tecnologías principales:
• Aplicación móvil: Flutter (usado por Google, Alibaba, BMW)
• Mapas: OpenStreetMap (la Wikipedia de los mapas)
• Cálculo de rutas: OpenTripPlanner (usado por ciudades en todo el mundo)
• Servidores: Linux (usado por el 90% de internet)


A.6. Seguridad

• Comunicaciones: Toda la información viaja encriptada (HTTPS)
• Datos de usuarios: La app NO requiere registro ni guarda datos personales
• Servidores: Protegidos con firewalls y monitoreo continuo
• Respaldos: Copias de seguridad automáticas diarias


A.7. ¿De quién son los datos?

• Rutas y paraderos (GTFS): Propiedad de AEMUS. Se publican para aparecer en Google Maps.
• Estadísticas de uso de la app: Propiedad de AEMUS. Información privada para planificación.
• Ubicación de buses: Propiedad de AEMUS. Solo se muestra en la app.

Importante: Trufi administra la tecnología, pero todos los datos generados son propiedad exclusiva de AEMUS.


A.8. Qué necesitamos de AEMUS

Para que el sistema funcione correctamente, necesitamos:

• Acceso al GPS: Conexión al sistema que muestra la ubicación de los buses (Mes 3)
• Branding: Logo, colores y elementos gráficos para personalizar la app (Mes 1)
• Documentación MOVILIZATE: Si se desea integrar consulta de saldo - opcional (Mes 4)

"""

    # Insertar texto
    requests = [
        {
            'insertText': {
                'location': {
                    'index': end_index
                },
                'text': anexo_texto
            }
        }
    ]

    result = service.documents().batchUpdate(
        documentId=DOC_ID,
        body={'requests': requests}
    ).execute()

    print('✅ Anexo técnico insertado correctamente')
    print(f'   Caracteres insertados: {len(anexo_texto)}')

if __name__ == '__main__':
    main()
