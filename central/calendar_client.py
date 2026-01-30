"""
Cliente de Google Calendar para el Secretario.
Permite leer y manipular eventos de calendario.
"""

from __future__ import print_function
import os.path
from typing import List, Dict, Optional
from datetime import datetime, timedelta

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes necesarios: Gmail + Calendar
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/calendar"
]

def get_calendar_service():
    """
    Obtiene el servicio de Google Calendar usando token.json.
    """
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print("❌ Token no válido. Ejecuta: python setup_calendar.py")
            return None

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
    return service


def listar_calendarios() -> List[Dict]:
    """
    Lista todos los calendarios disponibles.
    """
    service = get_calendar_service()
    if not service:
        return []
    
    try:
        calendarios = service.calendarList().list().execute()
        return calendarios.get('items', [])
    except Exception as e:
        print(f"Error al listar calendarios: {e}")
        return []


def obtener_eventos(
    calendar_id: str = 'primary',
    fecha_inicio: Optional[datetime] = None,
    fecha_fin: Optional[datetime] = None,
    max_resultados: int = 50
) -> List[Dict]:
    """
    Obtiene eventos del calendario en un rango de fechas.
    
    Args:
        calendar_id: ID del calendario (default: 'primary' = calendario principal)
        fecha_inicio: Fecha inicial (default: ahora)
        fecha_fin: Fecha final (default: +30 días)
        max_resultados: Máximo de eventos a retornar
    
    Returns:
        Lista de eventos
    """
    service = get_calendar_service()
    if not service:
        return []
    
    # Valores por defecto
    if not fecha_inicio:
        fecha_inicio = datetime.utcnow()
    if not fecha_fin:
        fecha_fin = fecha_inicio + timedelta(days=30)
    
    # Convertir a formato ISO
    time_min = fecha_inicio.isoformat() + 'Z'
    time_max = fecha_fin.isoformat() + 'Z'
    
    try:
        events_result = service.events().list(
            calendarId=calendar_id,
            timeMin=time_min,
            timeMax=time_max,
            maxResults=max_resultados,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        
        events = events_result.get('items', [])
        return events
        
    except Exception as e:
        print(f"Error al obtener eventos: {e}")
        return []


def crear_evento(
    titulo: str,
    fecha_inicio: datetime,
    fecha_fin: datetime,
    descripcion: str = "",
    ubicacion: str = "",
    asistentes: List[str] = None,
    calendar_id: str = 'primary'
) -> Optional[Dict]:
    """
    Crea un nuevo evento en el calendario.
    
    Args:
        titulo: Título del evento
        fecha_inicio: Fecha y hora de inicio
        fecha_fin: Fecha y hora de finalización
        descripcion: Descripción del evento
        ubicacion: Ubicación del evento
        asistentes: Lista de emails de asistentes
        calendar_id: ID del calendario
    
    Returns:
        Evento creado o None si hubo error
    """
    service = get_calendar_service()
    if not service:
        return None
    
    evento = {
        'summary': titulo,
        'description': descripcion,
        'start': {
            'dateTime': fecha_inicio.isoformat(),
            'timeZone': 'America/Bogota',
        },
        'end': {
            'dateTime': fecha_fin.isoformat(),
            'timeZone': 'America/Bogota',
        },
    }
    
    if ubicacion:
        evento['location'] = ubicacion
    
    if asistentes:
        evento['attendees'] = [{'email': email} for email in asistentes]
    
    try:
        evento_creado = service.events().insert(
            calendarId=calendar_id,
            body=evento,
            sendUpdates='all'  # Enviar notificaciones a asistentes
        ).execute()
        
        return evento_creado
        
    except Exception as e:
        print(f"Error al crear evento: {e}")
        return None


def actualizar_evento(
    evento_id: str,
    titulo: Optional[str] = None,
    fecha_inicio: Optional[datetime] = None,
    fecha_fin: Optional[datetime] = None,
    descripcion: Optional[str] = None,
    calendar_id: str = 'primary'
) -> Optional[Dict]:
    """
    Actualiza un evento existente.
    """
    service = get_calendar_service()
    if not service:
        return None
    
    try:
        # Obtener evento actual
        evento = service.events().get(
            calendarId=calendar_id,
            eventId=evento_id
        ).execute()
        
        # Actualizar campos proporcionados
        if titulo:
            evento['summary'] = titulo
        if descripcion:
            evento['description'] = descripcion
        if fecha_inicio:
            evento['start']['dateTime'] = fecha_inicio.isoformat()
        if fecha_fin:
            evento['end']['dateTime'] = fecha_fin.isoformat()
        
        # Guardar cambios
        evento_actualizado = service.events().update(
            calendarId=calendar_id,
            eventId=evento_id,
            body=evento,
            sendUpdates='all'
        ).execute()
        
        return evento_actualizado
        
    except Exception as e:
        print(f"Error al actualizar evento: {e}")
        return None


def eliminar_evento(evento_id: str, calendar_id: str = 'primary') -> bool:
    """
    Elimina un evento del calendario.
    """
    service = get_calendar_service()
    if not service:
        return False
    
    try:
        service.events().delete(
            calendarId=calendar_id,
            eventId=evento_id,
            sendUpdates='all'
        ).execute()
        return True
        
    except Exception as e:
        print(f"Error al eliminar evento: {e}")
        return False


def responder_invitacion(
    evento_id: str,
    respuesta: str,  # 'accepted', 'declined', 'tentative'
    calendar_id: str = 'primary'
) -> Optional[Dict]:
    """
    Responde a una invitación de calendario.
    """
    service = get_calendar_service()
    if not service:
        return None
    
    try:
        # Obtener evento
        evento = service.events().get(
            calendarId=calendar_id,
            eventId=evento_id
        ).execute()
        
        # Actualizar respuesta del usuario
        # Esto requiere identificar al usuario actual en la lista de asistentes
        # y actualizar su responseStatus
        
        evento_actualizado = service.events().patch(
            calendarId=calendar_id,
            eventId=evento_id,
            body={
                'attendees': [
                    {
                        'email': 'me',
                        'responseStatus': respuesta
                    }
                ]
            },
            sendUpdates='all'
        ).execute()
        
        return evento_actualizado
        
    except Exception as e:
        print(f"Error al responder invitación: {e}")
        return None


def buscar_eventos_conflicto(
    fecha_inicio: datetime,
    fecha_fin: datetime,
    calendar_id: str = 'primary'
) -> List[Dict]:
    """
    Busca eventos que tengan conflicto con un rango de fechas.
    """
    eventos = obtener_eventos(
        calendar_id=calendar_id,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin
    )
    
    conflictos = []
    for evento in eventos:
        # Verificar si hay solapamiento
        start = evento.get('start', {})
        end = evento.get('end', {})
        
        # Obtener datetime del evento
        start_dt = start.get('dateTime') or start.get('date')
        end_dt = end.get('dateTime') or end.get('date')
        
        if start_dt and end_dt:
            conflictos.append(evento)
    
    return conflictos
