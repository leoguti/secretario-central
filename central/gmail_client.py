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
