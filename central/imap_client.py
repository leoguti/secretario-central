"""
Cliente IMAP para cuentas externas (GoDaddy, etc.)
Permite leer correos de servidores que no usan OAuth de Google.
"""

import imaplib
import email
from email.header import decode_header
from typing import List, Dict, Optional
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class IMAPClient:
    """Cliente IMAP para cuentas de correo externas."""
    
    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None
    
    def connect(self) -> bool:
        """Conecta al servidor IMAP."""
        try:
            self.connection = imaplib.IMAP4_SSL(self.host, self.port)
            self.connection.login(self.username, self.password)
            print(f"✅ Conectado a {self.username}")
            return True
        except Exception as e:
            print(f"❌ Error al conectar: {e}")
            return False
    
    def disconnect(self):
        """Desconecta del servidor."""
        if self.connection:
            try:
                self.connection.logout()
            except:
                pass
    
    def get_messages(self, folder: str = 'INBOX', max_results: int = 10) -> List[Dict]:
        """Obtiene mensajes de una carpeta."""
        if not self.connection:
            if not self.connect():
                return []
        
        try:
            self.connection.select(folder)
            status, messages = self.connection.search(None, 'ALL')
            
            if status != 'OK':
                return []
            
            message_ids = messages[0].split()
            message_ids = message_ids[-max_results:]
            
            result = []
            
            for msg_id in reversed(message_ids):
                status, msg_data = self.connection.fetch(msg_id, '(RFC822)')
                
                if status != 'OK':
                    continue
                
                raw_email = msg_data[0][1]
                msg = email.message_from_bytes(raw_email)
                
                subject = self._decode_header(msg.get('Subject', ''))
                from_addr = self._decode_header(msg.get('From', ''))
                date = msg.get('Date', '')
                body = self._get_body(msg)
                
                result.append({
                    'id': msg_id.decode(),
                    'subject': subject,
                    'from': from_addr,
                    'date': date,
                    'snippet': body[:200] if body else ''
                })
            
            return result
            
        except Exception as e:
            print(f"Error al obtener mensajes: {e}")
            return []
    
    def _decode_header(self, header: str) -> str:
        """Decodifica header de email."""
        if not header:
            return ''
        
        decoded = decode_header(header)
        result = []
        
        for part, encoding in decoded:
            if isinstance(part, bytes):
                try:
                    result.append(part.decode(encoding or 'utf-8'))
                except:
                    result.append(part.decode('utf-8', errors='ignore'))
            else:
                result.append(str(part))
        
        return ''.join(result)
    
    def _get_body(self, msg) -> str:
        """Extrae el cuerpo del mensaje."""
        body = ''
        
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain':
                    try:
                        body = part.get_payload(decode=True).decode()
                        break
                    except:
                        pass
        else:
            try:
                body = msg.get_payload(decode=True).decode()
            except:
                pass
        
        return body


def get_rumbo_client() -> Optional[IMAPClient]:
    """Cliente IMAP para info@rumbo.digital"""
    password = os.getenv('RUMBO_PASSWORD')
    
    if not password:
        print("❌ Falta RUMBO_PASSWORD en archivo .env")
        return None
    
    client = IMAPClient(
        host='imap.secureserver.net',
        port=993,
        username='info@rumbo.digital',
        password=password
    )
    
    return client
