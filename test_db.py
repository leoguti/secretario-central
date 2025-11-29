"""
Script de prueba para verificar la funcionalidad de la base de datos de eventos.

Este script:
1. Inicializa la base de datos
2. Inserta varios eventos de prueba
3. Consulta y muestra los eventos
4. Muestra estadísticas
"""

from central.db import init_db, insert_evento, get_eventos_recientes, get_estadisticas
from datetime import datetime, timedelta
import json


def main():
	print("=" * 60)
	print("PRUEBA DE BASE DE DATOS - SECRETARIO CENTRAL")
	print("=" * 60)
	print()
	
	# 1. Inicializar base de datos
	print("1. Inicializando base de datos...")
	init_db()
	print()
	
	# 2. Insertar eventos de prueba
	print("2. Insertando eventos de prueba...")
	
	# Evento 1: Email de GIZ sobre GTFS en México
	evento1_id = insert_evento(
		fuente='gmail',
		fuente_id='19abc123def456',
		tipo='email',
		fecha_evento_utc=(datetime.utcnow() - timedelta(hours=2)).isoformat() + 'Z',
		actor_email='contacto@giz.de',
		actor_nombre='GIZ México',
		proyecto='Mexico-GTFS',
		ciudad='Toluca',
		pais='MX',
		etiquetas='gtfs,giz,licitacion,transporte',
		resumen_corto='GIZ solicita propuesta para implementación de GTFS en Toluca',
		asunto='Propuesta GTFS - Ciudad de Toluca',
		extracto='Estimados, nos ponemos en contacto para solicitar una propuesta técnica para la implementación de GTFS en el sistema de transporte público de Toluca...',
		url_origen='https://mail.google.com/mail/u/0/#inbox/19abc123def456',
		importancia=2,
		estado='nuevo'
	)
	print(f"   ✓ Evento 1 insertado (ID: {evento1_id})")
	
	# Evento 2: Reunión sobre OMUS en Perú
	evento2_id = insert_evento(
		fuente='calendar',
		fuente_id='cal_567890',
		tipo='reunion',
		fecha_evento_utc=(datetime.utcnow() - timedelta(hours=24)).isoformat() + 'Z',
		actor_email='municipalidad@arequipa.gob.pe',
		actor_nombre='Municipalidad de Arequipa',
		proyecto='Peru-OMUS',
		ciudad='Arequipa',
		pais='PE',
		etiquetas='omus,municipalidad,reunion,movilidad',
		resumen_corto='Reunión de seguimiento del proyecto OMUS en Arequipa',
		asunto='Seguimiento OMUS Arequipa - Q4 2025',
		extracto='Reunión mensual para revisar avances del Observatorio de Movilidad Urbana Sostenible',
		importancia=1,
		estado='nuevo'
	)
	print(f"   ✓ Evento 2 insertado (ID: {evento2_id})")
	
	# Evento 3: Email sobre mapeo OSM en Colombia
	evento3_id = insert_evento(
		fuente='gmail',
		fuente_id='19abc789xyz012',
		tipo='email',
		fecha_evento_utc=(datetime.utcnow() - timedelta(days=1)).isoformat() + 'Z',
		actor_email='voluntarios@osm.org.co',
		actor_nombre='OSM Colombia',
		proyecto='Boyaca-OSM',
		ciudad='Tunja',
		pais='CO',
		etiquetas='osm,mapeo,voluntarios,boyaca',
		resumen_corto='Convocatoria para jornada de mapeo en Boyacá',
		asunto='Jornada de Mapeo OSM - Boyacá Diciembre 2025',
		extracto='Invitamos a la comunidad a participar en la jornada de mapeo colaborativo del transporte público en Boyacá...',
		url_origen='https://mail.google.com/mail/u/0/#inbox/19abc789xyz012',
		importancia=0,
		estado='nuevo'
	)
	print(f"   ✓ Evento 3 insertado (ID: {evento3_id})")
	
	# Evento 4: Mensaje de Slack sobre documentación
	evento4_id = insert_evento(
		fuente='slack',
		fuente_id='slack_msg_12345',
		tipo='mensaje',
		fecha_evento_utc=(datetime.utcnow() - timedelta(hours=5)).isoformat() + 'Z',
		actor_email='maria@trufi.org',
		actor_nombre='María González',
		proyecto='Mexico-GTFS',
		etiquetas='documentacion,slack,gtfs',
		resumen_corto='María compartió documentación actualizada de GTFS',
		asunto='Documentación GTFS actualizada',
		extracto='He actualizado la documentación con los últimos cambios del estándar GTFS. Por favor revisen...',
		importancia=0,
		estado='nuevo'
	)
	print(f"   ✓ Evento 4 insertado (ID: {evento4_id})")
	
	print()
	
	# 3. Consultar eventos recientes
	print("3. Consultando eventos recientes...")
	eventos = get_eventos_recientes(limit=5)
	print(f"   Total de eventos encontrados: {len(eventos)}")
	print()
	
	for evento in eventos:
		print(f"   • [{evento['fuente']}] {evento['asunto']}")
		print(f"     Proyecto: {evento['proyecto'] or 'N/A'} | Importancia: {evento['importancia']}")
		print(f"     Fecha: {evento['fecha_evento_utc']}")
		print()
	
	# 4. Mostrar estadísticas
	print("4. Estadísticas de la base de datos:")
	stats = get_estadisticas()
	print(f"   Total de eventos: {stats['total_eventos']}")
	print()
	
	print("   Por fuente:")
	for item in stats['por_fuente']:
		print(f"     - {item['fuente']}: {item['count']}")
	print()
	
	print("   Por proyecto:")
	for item in stats['por_proyecto']:
		print(f"     - {item['proyecto']}: {item['count']}")
	print()
	
	print("   Por importancia:")
	for item in stats['por_importancia']:
		nivel = {0: 'Normal', 1: 'Media', 2: 'Alta'}.get(item['importancia'], 'Desconocida')
		print(f"     - {nivel}: {item['count']}")
	print()
	
	print("=" * 60)
	print("✓ PRUEBA COMPLETADA EXITOSAMENTE")
	print("=" * 60)


if __name__ == '__main__':
	main()
