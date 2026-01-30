"""
Cliente de Slack para el Secretario.
Permite leer mensajes, enviar notificaciones y gestionar canales.
"""

import os
from typing import List, Dict, Optional
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Cargar variables de entorno
load_dotenv()


class SlackClient:
    """Cliente de Slack para gestión de mensajes y canales."""
    
    def __init__(self, token: str):
        """
        Inicializa cliente de Slack.
        
        Args:
            token: Bot User OAuth Token
        """
        self.client = WebClient(token=token)
        self.bot_user_id = None
    
    def test_connection(self) -> bool:
        """Prueba la conexión y obtiene info del bot."""
        try:
            response = self.client.auth_test()
            self.bot_user_id = response['user_id']
            print(f"✅ Conectado a Slack como: {response['user']}")
            print(f"   Workspace: {response['team']}")
            return True
        except SlackApiError as e:
            print(f"❌ Error al conectar: {e.response['error']}")
            return False
    
    def list_channels(self, types: str = "public_channel,private_channel") -> List[Dict]:
        """
        Lista canales disponibles.
        
        Args:
            types: Tipos de canales (public_channel, private_channel, im, mpim)
        
        Returns:
            Lista de canales
        """
        try:
            result = self.client.conversations_list(
                types=types,
                exclude_archived=True
            )
            channels = result.get('channels', [])
            return channels
        except SlackApiError as e:
            print(f"Error al listar canales: {e.response['error']}")
            # Intentar solo con canales públicos
            try:
                result = self.client.conversations_list(
                    types="public_channel",
                    exclude_archived=True
                )
                channels = result.get('channels', [])
                return channels
            except SlackApiError as e2:
                print(f"Error (retry): {e2.response['error']}")
                return []
    
    def get_channel_messages(self, channel_id: str, limit: int = 10) -> List[Dict]:
        """
        Obtiene mensajes de un canal.
        
        Args:
            channel_id: ID del canal
            limit: Número máximo de mensajes
        
        Returns:
            Lista de mensajes
        """
        try:
            result = self.client.conversations_history(
                channel=channel_id,
                limit=limit
            )
            messages = result['messages']
            return messages
        except SlackApiError as e:
            print(f"Error al obtener mensajes: {e.response['error']}")
            return []
    
    def send_message(self, channel_id: str, text: str) -> bool:
        """
        Envía un mensaje a un canal.
        
        Args:
            channel_id: ID del canal
            text: Texto del mensaje
        
        Returns:
            True si se envió correctamente
        """
        try:
            self.client.chat_postMessage(
                channel=channel_id,
                text=text
            )
            print(f"✅ Mensaje enviado a canal {channel_id}")
            return True
        except SlackApiError as e:
            print(f"❌ Error al enviar mensaje: {e.response['error']}")
            return False
    
    def get_user_info(self, user_id: str) -> Optional[Dict]:
        """Obtiene información de un usuario."""
        try:
            result = self.client.users_info(user=user_id)
            return result['user']
        except SlackApiError as e:
            print(f"Error al obtener usuario: {e.response['error']}")
            return None
    
    def get_direct_messages(self, limit: int = 10) -> List[Dict]:
        """
        Obtiene mensajes directos recientes.
        
        Args:
            limit: Número máximo de conversaciones
        
        Returns:
            Lista de conversaciones DM
        """
        try:
            # Listar conversaciones de tipo IM (direct messages)
            result = self.client.conversations_list(types="im", limit=limit)
            dms = []
            
            for channel in result['channels']:
                # Obtener mensajes de cada DM
                messages = self.get_channel_messages(channel['id'], limit=5)
                if messages:
                    dms.append({
                        'channel_id': channel['id'],
                        'user': channel.get('user'),
                        'messages': messages
                    })
            
            return dms
        except SlackApiError as e:
            print(f"Error al obtener DMs: {e.response['error']}")
            return []
    
    def search_messages(self, query: str, count: int = 20) -> List[Dict]:
        """
        Busca mensajes en el workspace.
        
        Args:
            query: Término de búsqueda
            count: Número de resultados
        
        Returns:
            Lista de mensajes encontrados
        """
        try:
            result = self.client.search_messages(query=query, count=count)
            return result['messages']['matches']
        except SlackApiError as e:
            print(f"Error en búsqueda: {e.response['error']}")
            return []


def get_slack_client(use_user_token: bool = True) -> Optional[SlackClient]:
    """
    Obtiene cliente de Slack configurado.
    
    Args:
        use_user_token: Si True, usa user token (actúa como usuario).
                       Si False, usa bot token (aparece como bot).
    
    Returns:
        Cliente de Slack o None si falta token
    """
    if use_user_token:
        token = os.getenv('SLACK_USER_TOKEN')
        if not token:
            print("❌ Falta SLACK_USER_TOKEN en archivo .env")
            return None
    else:
        token = os.getenv('SLACK_BOT_TOKEN')
        if not token:
            print("❌ Falta SLACK_BOT_TOKEN en archivo .env")
            return None
    
    client = SlackClient(token)
    return client


if __name__ == "__main__":
    # Test de conexión
    print('=' * 80)
    print('PROBANDO CONEXIÓN A SLACK')
    print('=' * 80)
    print()
    
    client = get_slack_client()
    
    if client and client.test_connection():
        print()
        print('📋 Canales disponibles:')
        channels = client.list_channels()
        
        for ch in channels[:10]:  # Primeros 10
            name = ch.get('name', ch.get('id'))
            is_member = '✓' if ch.get('is_member') else ' '
            print(f'   [{is_member}] #{name}')
        
        print()
        print(f'Total: {len(channels)} canales')
