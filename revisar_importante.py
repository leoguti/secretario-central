#!/usr/bin/env python3
"""Script para revisar correos y Slack importantes"""

from central.gmail_client import get_messages_last_n_days
from central.slack_client import get_slack_client

def revisar_correos():
    """Revisa correos importantes de las últimas 24 horas"""
    print('📧 CORREOS RECIENTES (últimas 24 horas)')
    print('=' * 80)
    
    try:
        messages = get_messages_last_n_days(days=1, exclude_categories=['CATEGORY_PROMOTIONS', 'CATEGORY_SOCIAL'])
        
        for msg in messages[:10]:
            print(f"\nDe: {msg['actor_nombre']} <{msg['actor_email']}>")
            print(f"Asunto: {msg['subject']}")
            print(f"Fecha: {msg['date']}")
            print(f"Vista previa: {msg['snippet'][:100]}...")
            print('=' * 80)
        
        print(f'\nTotal de correos en últimas 24h: {len(messages)}')
        return messages
    except Exception as e:
        print(f"❌ Error al revisar correos: {e}")
        return []

def revisar_slack():
    """Revisa mensajes importantes de Slack"""
    print('\n\n💬 MENSAJES DE SLACK RECIENTES')
    print('=' * 80)
    
    try:
        client = get_slack_client(use_user_token=True)
        if client and client.test_connection():
            channels = client.list_channels()
            
            print(f'\n📋 Revisando {len(channels)} canales...\n')
            
            for ch in channels[:5]:
                if ch.get('is_member'):
                    name = ch.get('name', ch.get('id'))
                    print(f'\n#{name}:')
                    messages = client.get_channel_messages(ch['id'], limit=3)
                    for msg in messages[:3]:
                        user = msg.get('user', 'unknown')
                        text = msg.get('text', '')[:100]
                        print(f'  - {user}: {text}')
    except Exception as e:
        print(f"❌ Error al revisar Slack: {e}")

if __name__ == '__main__':
    revisar_correos()
    revisar_slack()
