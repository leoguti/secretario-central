"""
Módulo de gestión de base de datos SQLite para el Secretario Central.

Este módulo maneja la base de datos de eventos, que registra información
de diferentes fuentes (Gmail, Calendar, Slack, etc.) para posterior análisis.
"""

import sqlite3
import os
from datetime import datetime
from typing import Optional, List, Dict, Any


# Ruta a la base de datos
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'secretario.db')


def get_connection():
	"""
	Obtiene una conexión a la base de datos SQLite.
	
	Returns:
		sqlite3.Connection: Conexión a la base de datos
	"""
	# Asegurar que el directorio data/ existe
	os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
	
	conn = sqlite3.connect(DB_PATH)
	conn.row_factory = sqlite3.Row  # Permite acceder a columnas por nombre
	return conn


def init_db():
	"""
	Inicializa la base de datos creando la tabla eventos y sus índices.
	
	Esta función es idempotente - puede ejecutarse múltiples veces sin problemas.
	"""
	conn = get_connection()
	cursor = conn.cursor()
	
	# Crear tabla eventos
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS eventos (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			fuente TEXT NOT NULL,
			fuente_id TEXT,
			tipo TEXT NOT NULL,
			fecha_evento_utc TEXT NOT NULL,
			actor_email TEXT,
			actor_nombre TEXT,
			proyecto TEXT,
			ciudad TEXT,
			pais TEXT,
			etiquetas TEXT,
			resumen_corto TEXT,
			asunto TEXT,
			extracto TEXT,
			url_origen TEXT,
			importancia INTEGER DEFAULT 0,
			estado TEXT DEFAULT 'nuevo',
			creado_en_utc TEXT NOT NULL,
			actualizado_en_utc TEXT NOT NULL
		)
	''')
	
	# Crear índices para búsquedas eficientes
	cursor.execute('CREATE INDEX IF NOT EXISTS idx_eventos_fecha ON eventos(fecha_evento_utc)')
	cursor.execute('CREATE INDEX IF NOT EXISTS idx_eventos_fuente_id ON eventos(fuente, fuente_id)')
	cursor.execute('CREATE INDEX IF NOT EXISTS idx_eventos_proyecto_fecha ON eventos(proyecto, fecha_evento_utc)')
	cursor.execute('CREATE INDEX IF NOT EXISTS idx_eventos_importancia_fecha ON eventos(importancia, fecha_evento_utc)')
	
	# Crear tabla resumenes
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS resumenes (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			desde_utc TEXT NOT NULL,
			hasta_utc TEXT NOT NULL,
			generado_en_utc TEXT NOT NULL,
			resumen_json TEXT NOT NULL,
			tipo TEXT,
			fuente_eventos TEXT,
			estado_envio TEXT DEFAULT 'pendiente',
			canales_enviados TEXT
		)
	''')
	
	# Crear índices para resumenes
	cursor.execute('CREATE INDEX IF NOT EXISTS idx_resumenes_rango ON resumenes(desde_utc, hasta_utc)')
	cursor.execute('CREATE INDEX IF NOT EXISTS idx_resumenes_generado ON resumenes(generado_en_utc)')
	
	conn.commit()
	conn.close()
	
	print(f"✓ Base de datos inicializada en: {DB_PATH}")


def insert_evento(
	fuente: str,
	tipo: str,
	fecha_evento_utc: str,
	fuente_id: Optional[str] = None,
	actor_email: Optional[str] = None,
	actor_nombre: Optional[str] = None,
	proyecto: Optional[str] = None,
	ciudad: Optional[str] = None,
	pais: Optional[str] = None,
	etiquetas: Optional[str] = None,
	resumen_corto: Optional[str] = None,
	asunto: Optional[str] = None,
	extracto: Optional[str] = None,
	url_origen: Optional[str] = None,
	importancia: int = 0,
	estado: str = 'nuevo'
) -> int:
	"""
	Inserta un nuevo evento en la base de datos.
	
	Args:
		fuente: Fuente del evento ('gmail', 'calendar', 'slack', etc.)
		tipo: Tipo de evento ('email', 'reunion', 'mensaje', etc.)
		fecha_evento_utc: Fecha del evento en formato ISO8601 UTC
		fuente_id: ID original en la fuente
		actor_email: Email de la persona principal involucrada
		actor_nombre: Nombre de la persona
		proyecto: Nombre del proyecto
		ciudad: Ciudad relacionada
		pais: País (código ISO)
		etiquetas: Tags separadas por comas
		resumen_corto: Resumen breve del evento
		asunto: Subject o título
		extracto: Snippet o extracto del contenido
		url_origen: URL al contenido original
		importancia: Nivel de importancia (0=normal, 1=media, 2=alta)
		estado: Estado del evento ('nuevo', 'en_proceso', 'ignorado', 'hecho')
	
	Returns:
		int: ID del evento insertado
	"""
	conn = get_connection()
	cursor = conn.cursor()
	
	ahora = datetime.utcnow().isoformat() + 'Z'
	
	cursor.execute('''
		INSERT INTO eventos (
			fuente, fuente_id, tipo, fecha_evento_utc,
			actor_email, actor_nombre, proyecto, ciudad, pais,
			etiquetas, resumen_corto, asunto, extracto, url_origen,
			importancia, estado, creado_en_utc, actualizado_en_utc
		) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
	''', (
		fuente, fuente_id, tipo, fecha_evento_utc,
		actor_email, actor_nombre, proyecto, ciudad, pais,
		etiquetas, resumen_corto, asunto, extracto, url_origen,
		importancia, estado, ahora, ahora
	))
	
	evento_id = cursor.lastrowid
	conn.commit()
	conn.close()
	
	return evento_id


def get_eventos_recientes(limit: int = 10) -> List[Dict[str, Any]]:
	"""
	Obtiene los eventos más recientes de la base de datos.
	
	Args:
		limit: Número máximo de eventos a retornar
	
	Returns:
		List[Dict]: Lista de eventos como diccionarios
	"""
	conn = get_connection()
	cursor = conn.cursor()
	
	cursor.execute('''
		SELECT * FROM eventos 
		ORDER BY fecha_evento_utc DESC 
		LIMIT ?
	''', (limit,))
	
	rows = cursor.fetchall()
	conn.close()
	
	# Convertir Row objects a diccionarios
	eventos = []
	for row in rows:
		eventos.append(dict(row))
	
	return eventos


def existe_evento(fuente: str, fuente_id: str) -> bool:
	"""
	Verifica si ya existe un evento con la combinación fuente + fuente_id.
	
	Args:
		fuente: Fuente del evento ('gmail', 'calendar', etc.)
		fuente_id: ID original en la fuente
	
	Returns:
		bool: True si el evento ya existe, False en caso contrario
	"""
	conn = get_connection()
	cursor = conn.cursor()
	
	cursor.execute('''
		SELECT COUNT(*) as count FROM eventos 
		WHERE fuente = ? AND fuente_id = ?
	''', (fuente, fuente_id))
	
	result = cursor.fetchone()
	conn.close()
	
	return result['count'] > 0


def actualizar_timestamp_evento(fuente: str, fuente_id: str):
	"""
	Actualiza el campo actualizado_en_utc de un evento existente.
	
	Args:
		fuente: Fuente del evento
		fuente_id: ID original en la fuente
	"""
	conn = get_connection()
	cursor = conn.cursor()
	
	ahora = datetime.utcnow().isoformat() + 'Z'
	
	cursor.execute('''
		UPDATE eventos 
		SET actualizado_en_utc = ? 
		WHERE fuente = ? AND fuente_id = ?
	''', (ahora, fuente, fuente_id))
	
	conn.commit()
	conn.close()


def get_eventos_por_proyecto(proyecto: str, limit: int = 20) -> List[Dict[str, Any]]:
	"""
	Obtiene eventos filtrados por proyecto.
	
	Args:
		proyecto: Nombre del proyecto
		limit: Número máximo de eventos a retornar
	
	Returns:
		List[Dict]: Lista de eventos del proyecto
	"""
	conn = get_connection()
	cursor = conn.cursor()
	
	cursor.execute('''
		SELECT * FROM eventos 
		WHERE proyecto = ?
		ORDER BY fecha_evento_utc DESC 
		LIMIT ?
	''', (proyecto, limit))
	
	rows = cursor.fetchall()
	conn.close()
	
	eventos = []
	for row in rows:
		eventos.append(dict(row))
	
	return eventos


def get_estadisticas() -> Dict[str, Any]:
	"""
	Obtiene estadísticas generales de la base de datos de eventos.
	
	Returns:
		Dict: Diccionario con estadísticas
	"""
	conn = get_connection()
	cursor = conn.cursor()
	
	stats = {}
	
	# Total de eventos
	cursor.execute('SELECT COUNT(*) as total FROM eventos')
	stats['total_eventos'] = cursor.fetchone()['total']
	
	# Eventos por fuente
	cursor.execute('''
		SELECT fuente, COUNT(*) as count 
		FROM eventos 
		GROUP BY fuente 
		ORDER BY count DESC
	''')
	stats['por_fuente'] = [dict(row) for row in cursor.fetchall()]
	
	# Eventos por proyecto
	cursor.execute('''
		SELECT proyecto, COUNT(*) as count 
		FROM eventos 
		WHERE proyecto IS NOT NULL
		GROUP BY proyecto 
		ORDER BY count DESC
		LIMIT 10
	''')
	stats['por_proyecto'] = [dict(row) for row in cursor.fetchall()]
	
	# Eventos por importancia
	cursor.execute('''
		SELECT importancia, COUNT(*) as count 
		FROM eventos 
		GROUP BY importancia 
		ORDER BY importancia DESC
	''')
	stats['por_importancia'] = [dict(row) for row in cursor.fetchall()]
	
	conn.close()
	
	return stats


# ============================================================================
# FUNCIONES PARA RESUMENES
# ============================================================================

def obtener_ultimo_resumen() -> Optional[Dict[str, Any]]:
	"""
	Obtiene el resumen más reciente de la base de datos.
	
	Returns:
		Dict con los datos del último resumen, o None si no hay resumenes
	"""
	conn = get_connection()
	cursor = conn.cursor()
	
	cursor.execute('''
		SELECT * FROM resumenes 
		ORDER BY hasta_utc DESC 
		LIMIT 1
	''')
	
	row = cursor.fetchone()
	conn.close()
	
	if row:
		return dict(row)
	return None


def obtener_eventos_en_rango(desde_utc: str, hasta_utc: str) -> List[Dict[str, Any]]:
	"""
	Obtiene eventos en un rango de tiempo específico.
	
	Args:
		desde_utc: Fecha inicial del rango en formato ISO8601 UTC
		hasta_utc: Fecha final del rango en formato ISO8601 UTC
	
	Returns:
		List[Dict]: Lista de eventos en el rango
	"""
	conn = get_connection()
	cursor = conn.cursor()
	
	cursor.execute('''
		SELECT * FROM eventos 
		WHERE fecha_evento_utc >= ? AND fecha_evento_utc < ?
		ORDER BY fecha_evento_utc ASC
	''', (desde_utc, hasta_utc))
	
	rows = cursor.fetchall()
	conn.close()
	
	eventos = []
	for row in rows:
		eventos.append(dict(row))
	
	return eventos


def insertar_resumen(
	desde_utc: str,
	hasta_utc: str,
	resumen_json: str,
	tipo: Optional[str] = None,
	fuente_eventos: str = 'eventos_sqlite',
	estado_envio: str = 'pendiente',
	canales_enviados: Optional[str] = None
) -> int:
	"""
	Inserta un nuevo resumen en la base de datos.
	
	Args:
		desde_utc: Inicio del rango de tiempo del resumen
		hasta_utc: Fin del rango de tiempo del resumen
		resumen_json: JSON del resumen como string
		tipo: Tipo de resumen ('manana', 'tarde', 'automatico', etc.)
		fuente_eventos: Fuente de los eventos resumidos
		estado_envio: Estado del envío ('pendiente', 'enviado', 'error')
		canales_enviados: Canales donde se envió (separados por coma)
	
	Returns:
		int: ID del resumen insertado
	"""
	conn = get_connection()
	cursor = conn.cursor()
	
	generado_en_utc = datetime.utcnow().isoformat() + 'Z'
	
	cursor.execute('''
		INSERT INTO resumenes (
			desde_utc, hasta_utc, generado_en_utc, resumen_json,
			tipo, fuente_eventos, estado_envio, canales_enviados
		) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
	''', (
		desde_utc, hasta_utc, generado_en_utc, resumen_json,
		tipo, fuente_eventos, estado_envio, canales_enviados
	))
	
	resumen_id = cursor.lastrowid
	conn.commit()
	conn.close()
	
	return resumen_id


if __name__ == '__main__':
	# Script de inicialización cuando se ejecuta directamente
	print("Inicializando base de datos del Secretario Central...")
	init_db()
	print("✓ Base de datos lista para usar")
