"""
Módulo de ingesta de correos de Gmail hacia la base de datos de eventos.

Este script obtiene correos de Gmail de los últimos 3 días (excluyendo
promociones y sociales) y los inserta en la tabla eventos de SQLite.
"""

from central.gmail_client import get_messages_last_n_days
from central.db import init_db, insert_evento, existe_evento, actualizar_timestamp_evento


def construir_url_gmail(message_id: str) -> str:
	"""
	Construye la URL web para abrir un correo en Gmail.
	
	Args:
		message_id: ID del mensaje de Gmail
	
	Returns:
		str: URL para abrir el mensaje en el navegador
	"""
	return f"https://mail.google.com/mail/u/0/#inbox/{message_id}"


def ingerir_correos_gmail(dias: int = 3, verbose: bool = True):
	"""
	Ingiere correos de Gmail hacia la base de datos de eventos.
	
	Args:
		dias: Número de días hacia atrás para buscar correos (default: 3)
		verbose: Si True, imprime información detallada del proceso
	
	Returns:
		dict: Estadísticas de la ingesta (analizados, insertados, existentes)
	"""
	# Asegurar que la base de datos existe
	init_db()
	
	if verbose:
		print("=" * 60)
		print("INGESTA DE CORREOS DE GMAIL")
		print("=" * 60)
		print(f"→ Buscando correos de los últimos {dias} días...")
		print("→ Excluyendo: promociones y sociales")
		print()
	
	# Obtener mensajes de Gmail
	categorias_excluidas = ['CATEGORY_PROMOTIONS', 'CATEGORY_SOCIAL']
	mensajes = get_messages_last_n_days(days=dias, exclude_categories=categorias_excluidas)
	
	if verbose:
		print(f"✓ Se encontraron {len(mensajes)} mensajes")
		print()
	
	# Contadores
	analizados = 0
	insertados = 0
	existentes = 0
	
	# Procesar cada mensaje
	for msg in mensajes:
		analizados += 1
		
		# Verificar si ya existe
		if existe_evento('gmail', msg['id']):
			existentes += 1
			# Actualizar timestamp
			actualizar_timestamp_evento('gmail', msg['id'])
			if verbose:
				print(f"  ○ Ya existe: {msg['subject'][:60]}...")
			continue
		
		# Insertar nuevo evento
		try:
			evento_id = insert_evento(
				fuente='gmail',
				fuente_id=msg['id'],
				tipo='email',
				fecha_evento_utc=msg['fecha_evento_utc'],
				actor_email=msg['actor_email'],
				actor_nombre=msg['actor_nombre'],
				proyecto=None,  # Por ahora NULL
				ciudad=None,    # Por ahora NULL
				pais=None,      # Por ahora NULL
				etiquetas=None, # Por ahora NULL
				resumen_corto=msg['snippet'][:200] if msg['snippet'] else None,  # Limitar a 200 chars
				asunto=msg['subject'],
				extracto=msg['snippet'],
				url_origen=construir_url_gmail(msg['id']),
				importancia=0,
				estado='nuevo'
			)
			
			insertados += 1
			if verbose:
				print(f"  ✓ Insertado: {msg['subject'][:60]}...")
		
		except Exception as e:
			if verbose:
				print(f"  ✗ Error al insertar mensaje {msg['id']}: {e}")
	
	# Resumen final
	if verbose:
		print()
		print("=" * 60)
		print("RESUMEN DE INGESTA")
		print("=" * 60)
		print(f"  Mensajes analizados:  {analizados}")
		print(f"  Nuevos insertados:    {insertados}")
		print(f"  Ya existían:          {existentes}")
		print("=" * 60)
	
	return {
		'analizados': analizados,
		'insertados': insertados,
		'existentes': existentes
	}


if __name__ == '__main__':
	"""
	Ejecutar este módulo directamente para ingerir correos:
	python -m central.gmail_ingest
	"""
	ingerir_correos_gmail(dias=3, verbose=True)
