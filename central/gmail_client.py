from __future__ import print_function
import os.path
from typing import List, Dict

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Solo lectura de Gmail
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def get_gmail_service():
    """
    Usa credentials.json la primera vez, guarda token.json
    y luego reutiliza ese token para acceder al Gmail de Leonardo.
    """
    creds = None

    # Si ya tenemos token guardado, lo usamos
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # Si no hay credenciales válidas o son inválidas, lanzamos flujo OAuth
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refrescar token si está vencido
            creds.refresh(Request())
        else:
            # Primera vez: usar credentials.json y abrir navegador
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Guardar token para próximas veces
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("gmail", "v1", credentials=creds)
    return service

def get_sample_messages(max_results: int = 5) -> List[Dict]:
    """
    Devuelve una lista de mensajes sencillos: id, asunto y snippet.
    """
    service = get_gmail_service()

    results = service.users().messages().list(
        userId="me", maxResults=max_results
    ).execute()

    messages = results.get("messages", [])
    output = []

    for m in messages:
        msg = service.users().messages().get(
            userId="me",
            id=m["id"],
            format="metadata",
            metadataHeaders=["Subject"]
        ).execute()

        headers = msg.get("payload", {}).get("headers", [])
        subject = next(
            (h["value"] for h in headers if h["name"] == "Subject"), "(no subject)"
        )

        output.append({
            "id": m["id"],
            "subject": subject,
            "snippet": msg.get("snippet", "")
        })

    return output


def get_messages_last_n_days(days: int = 3, exclude_categories: List[str] = None) -> List[Dict]:
	"""
	Obtiene mensajes de Gmail de los últimos N días, excluyendo categorías específicas.
	
	Args:
		days: Número de días hacia atrás para buscar mensajes (default: 3)
		exclude_categories: Lista de categorías a excluir (ej: ['CATEGORY_PROMOTIONS', 'CATEGORY_SOCIAL'])
	
	Returns:
		List[Dict]: Lista de mensajes con información completa
	"""
	from datetime import datetime, timedelta
	
	if exclude_categories is None:
		exclude_categories = []
	
	service = get_gmail_service()
	
	# Calcular fecha límite (N días atrás)
	fecha_limite = datetime.utcnow() - timedelta(days=days)
	fecha_limite_str = fecha_limite.strftime('%Y/%m/%d')
	
	# Construir query de búsqueda
	query = f'after:{fecha_limite_str}'
	
	# Obtener lista de mensajes
	try:
		results = service.users().messages().list(
			userId='me',
			q=query,
			maxResults=500  # Límite razonable
		).execute()
		
		messages = results.get('messages', [])
		
		# Obtener detalles completos de cada mensaje
		detailed_messages = []
		
		for msg_ref in messages:
			msg = service.users().messages().get(
				userId='me',
				id=msg_ref['id'],
				format='full'
			).execute()
			
			# Verificar si el mensaje tiene categorías a excluir
			labels = msg.get('labelIds', [])
			
			# Si tiene alguna categoría excluida, saltar este mensaje
			if any(cat in labels for cat in exclude_categories):
				continue
			
			# Extraer información del mensaje
			headers = msg.get('payload', {}).get('headers', [])
			
			# Obtener headers importantes
			subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '(sin asunto)')
			from_header = next((h['value'] for h in headers if h['name'].lower() == 'from'), '')
			date_header = next((h['value'] for h in headers if h['name'].lower() == 'date'), '')
			
			# Parsear el remitente (formato: "Nombre <email@example.com>" o solo "email@example.com")
			actor_email = ''
			actor_nombre = ''
			
			if from_header:
				# Extraer email
				if '<' in from_header and '>' in from_header:
					actor_email = from_header.split('<')[1].split('>')[0].strip()
					actor_nombre = from_header.split('<')[0].strip().strip('"')
				else:
					actor_email = from_header.strip()
					actor_nombre = from_header.strip()
			
			# Obtener timestamp interno de Gmail (más confiable que el header Date)
			internal_date_ms = int(msg.get('internalDate', 0))
			fecha_evento_utc = datetime.utcfromtimestamp(internal_date_ms / 1000).isoformat() + 'Z'
			
			detailed_messages.append({
				'id': msg['id'],
				'thread_id': msg.get('threadId', ''),
				'subject': subject,
				'from': from_header,
				'actor_email': actor_email,
				'actor_nombre': actor_nombre,
				'date': date_header,
				'fecha_evento_utc': fecha_evento_utc,
				'snippet': msg.get('snippet', ''),
				'labels': labels
			})
		
		return detailed_messages
		
	except Exception as e:
		print(f"Error al obtener mensajes: {e}")
		return []
