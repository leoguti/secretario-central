"""
Módulo de generación de resúmenes automáticos usando OpenAI.

Este módulo lee eventos nuevos desde la base de datos, llama a la API de OpenAI
para generar un resumen estructurado, y lo guarda en la tabla resumenes.
"""

import os
import json
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List, Tuple

from central.db import (
	init_db,
	obtener_ultimo_resumen,
	obtener_eventos_en_rango,
	insertar_resumen
)


# Prompt del sistema para OpenAI
SYSTEM_PROMPT = """Eres el "Secretario Central" de Leonardo Gutiérrez.
Tu trabajo es ayudarle a priorizar información importante relacionada con:

- Desarrollo de negocios (BD) y nuevas oportunidades de proyectos
- Gestión de proyectos en curso (entregables, plazos, coordinación con aliados)
- Su rol en la directiva de la asociación Trufi
- Riesgos y problemas que puedan afectar proyectos u oportunidades

Recibirás una lista de eventos recientes (correos, mensajes, etc.) con fecha, fuente, asunto y un resumen corto.

Debes:

1. Identificar qué ha sido realmente importante en este periodo
2. Detectar oportunidades de proyectos y crecimiento:
   - Proyectos GTFS, digitalización de transporte público
   - Aplicaciones de planificación de viajes
   - Observatorios de movilidad
   - Colaboración con ciudades, GIZ, universidades u otros aliados
   - Licitaciones, convocatorias, RFP, propuestas, talleres financiados
3. Detectar riesgos o problemas:
   - Retrasos, bloqueos, malentendidos, plazos cercanos
   - Posibles conflictos con aliados o equipos
4. Proponer pendientes concretos para Leonardo:
   - Respuestas a correos importantes
   - Coordinación de reuniones
   - Revisión de documentos
   - Decisiones que debería tomar

Tu respuesta debe ser SIEMPRE un JSON válido con esta estructura:

{
  "resumen_general": "Texto breve explicando qué ha pasado en este periodo.",
  "eventos_clave": [
    "..."
  ],
  "oportunidades": [
    "..."
  ],
  "riesgos": [
    "..."
  ],
  "pendientes": [
    "..."
  ]
}

Si alguna lista está vacía, devuélvela como [].
No incluyas comentarios ni texto fuera del JSON.
Usa un lenguaje claro, profesional y directo."""


def verificar_api_key() -> bool:
	"""
	Verifica que la API key de OpenAI esté configurada.
	
	Returns:
		bool: True si la key está configurada, False en caso contrario
	"""
	api_key = os.getenv('OPENAI_API_KEY')
	if not api_key:
		print("✗ ERROR: Variable de entorno OPENAI_API_KEY no está definida")
		print()
		print("Para usar este módulo necesitas:")
		print("  export OPENAI_API_KEY='tu-api-key-aqui'")
		print()
		return False
	return True


def calcular_rango_resumen() -> Tuple[str, str]:
	"""
	Calcula el rango de tiempo para el nuevo resumen.
	
	Returns:
		tuple: (desde_utc, hasta_utc) como strings ISO8601
	"""
	ahora_utc = datetime.utcnow()
	hasta_utc = ahora_utc.isoformat() + 'Z'
	
	# Obtener último resumen
	ultimo_resumen = obtener_ultimo_resumen()
	
	if ultimo_resumen:
		# Continuar desde donde terminó el último resumen
		desde_utc = ultimo_resumen['hasta_utc']
	else:
		# Primera vez: tomar últimas 12 horas
		desde_utc = (ahora_utc - timedelta(hours=12)).isoformat() + 'Z'
	
	return desde_utc, hasta_utc


def preparar_eventos_para_openai(eventos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
	"""
	Prepara la lista de eventos en formato ligero para enviar a OpenAI.
	
	Args:
		eventos: Lista de eventos de la base de datos
	
	Returns:
		List[Dict]: Eventos en formato simplificado
	"""
	eventos_simplificados = []
	
	for evento in eventos:
		evento_simple = {
			'fecha_evento_utc': evento.get('fecha_evento_utc'),
			'fuente': evento.get('fuente'),
			'tipo': evento.get('tipo'),
			'actor_email': evento.get('actor_email'),
			'actor_nombre': evento.get('actor_nombre'),
			'asunto': evento.get('asunto'),
			'resumen_corto': evento.get('resumen_corto') or evento.get('extracto', ''),
			'proyecto': evento.get('proyecto'),
			'ciudad': evento.get('ciudad'),
			'pais': evento.get('pais'),
			'url_origen': evento.get('url_origen')
		}
		eventos_simplificados.append(evento_simple)
	
	return eventos_simplificados


def llamar_openai(desde_utc: str, hasta_utc: str, eventos: List[Dict[str, Any]]) -> Dict[str, Any]:
	"""
	Llama a la API de OpenAI para generar el resumen.
	
	Args:
		desde_utc: Inicio del rango de tiempo
		hasta_utc: Fin del rango de tiempo
		eventos: Lista de eventos a resumir
	
	Returns:
		Dict: JSON del resumen o dict con error
	"""
	try:
		from openai import OpenAI
		client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
		
		# Preparar mensaje de usuario
		mensaje_usuario = {
			"periodo": {
				"desde_utc": desde_utc,
				"hasta_utc": hasta_utc
			},
			"eventos": eventos
		}
		
		# Llamar a OpenAI
		response = client.chat.completions.create(
			model="gpt-4o-mini",  # Modelo económico
			messages=[
				{"role": "system", "content": SYSTEM_PROMPT},
				{"role": "user", "content": json.dumps(mensaje_usuario, ensure_ascii=False, indent=2)}
			],
			temperature=0.7,
			response_format={"type": "json_object"}  # Forzar respuesta JSON
		)
		
		# Extraer y parsear respuesta
		contenido = response.choices[0].message.content
		resumen_json = json.loads(contenido)
		
		return resumen_json
		
	except json.JSONDecodeError as e:
		return {
			"error": "json_parse_error",
			"mensaje": f"No se pudo parsear la respuesta de OpenAI: {str(e)}",
			"respuesta_cruda": contenido if 'contenido' in locals() else ""
		}
	except Exception as e:
		return {
			"error": "api_error",
			"mensaje": f"Error al llamar a OpenAI: {str(e)}"
		}


def generar_resumen(verbose: bool = True) -> Optional[Dict[str, Any]]:
	"""
	Función principal que genera un resumen automático de eventos.
	
	Args:
		verbose: Si True, imprime información detallada del proceso
	
	Returns:
		Dict con información del resumen generado, o None si falla
	"""
	# Verificar API key
	if not verificar_api_key():
		return None
	
	# Inicializar BD
	init_db()
	
	if verbose:
		print("=" * 70)
		print("GENERACIÓN DE RESUMEN AUTOMÁTICO")
		print("=" * 70)
		print()
	
	# Calcular rango de tiempo
	desde_utc, hasta_utc = calcular_rango_resumen()
	
	if verbose:
		print(f"→ Rango de tiempo:")
		print(f"  Desde: {desde_utc}")
		print(f"  Hasta: {hasta_utc}")
		print()
	
	# Obtener eventos en el rango
	eventos = obtener_eventos_en_rango(desde_utc, hasta_utc)
	
	if verbose:
		print(f"→ Eventos encontrados: {len(eventos)}")
		print()
	
	# Preparar eventos para OpenAI
	eventos_para_openai = preparar_eventos_para_openai(eventos)
	
	# Caso especial: sin eventos
	if len(eventos) == 0:
		if verbose:
			print("→ No hay eventos en este periodo")
			print("→ Generando resumen vacío...")
			print()
		
		resumen_json_obj = {
			"resumen_general": "No hubo eventos relevantes en este periodo.",
			"eventos_clave": [],
			"oportunidades": [],
			"riesgos": [],
			"pendientes": []
		}
	else:
		# Llamar a OpenAI
		if verbose:
			print("→ Llamando a OpenAI para generar resumen...")
			print()
		
		resumen_json_obj = llamar_openai(desde_utc, hasta_utc, eventos_para_openai)
	
	# Verificar si hubo error
	estado_envio = 'pendiente'
	if 'error' in resumen_json_obj:
		if verbose:
			print(f"✗ ERROR: {resumen_json_obj.get('mensaje', 'Error desconocido')}")
			print()
		estado_envio = 'error'
	
	# Convertir a string JSON para guardar
	resumen_json_str = json.dumps(resumen_json_obj, ensure_ascii=False, indent=2)
	
	# Determinar tipo de resumen (simplificado por ahora)
	hora_local = datetime.now().hour
	if 5 <= hora_local < 12:
		tipo = 'manana'
	elif 12 <= hora_local < 18:
		tipo = 'tarde'
	else:
		tipo = 'automatico'
	
	# Guardar en la base de datos
	resumen_id = insertar_resumen(
		desde_utc=desde_utc,
		hasta_utc=hasta_utc,
		resumen_json=resumen_json_str,
		tipo=tipo,
		fuente_eventos='eventos_sqlite',
		estado_envio=estado_envio,
		canales_enviados=None
	)
	
	if verbose:
		print("=" * 70)
		print("RESUMEN GENERADO")
		print("=" * 70)
		print()
		
		if 'error' not in resumen_json_obj:
			print(f"📋 Resumen General:")
			print(f"   {resumen_json_obj.get('resumen_general', 'N/A')}")
			print()
			
			if resumen_json_obj.get('eventos_clave'):
				print(f"🔑 Eventos Clave ({len(resumen_json_obj['eventos_clave'])}):")
				for evento in resumen_json_obj['eventos_clave']:
					print(f"   • {evento}")
				print()
			
			if resumen_json_obj.get('oportunidades'):
				print(f"💡 Oportunidades ({len(resumen_json_obj['oportunidades'])}):")
				for oportunidad in resumen_json_obj['oportunidades']:
					print(f"   • {oportunidad}")
				print()
			
			if resumen_json_obj.get('riesgos'):
				print(f"⚠️  Riesgos ({len(resumen_json_obj['riesgos'])}):")
				for riesgo in resumen_json_obj['riesgos']:
					print(f"   • {riesgo}")
				print()
			
			if resumen_json_obj.get('pendientes'):
				print(f"✅ Pendientes ({len(resumen_json_obj['pendientes'])}):")
				for pendiente in resumen_json_obj['pendientes']:
					print(f"   • {pendiente}")
				print()
		
		print("=" * 70)
		print(f"✓ Resumen guardado con ID: {resumen_id}")
		print(f"✓ Tipo: {tipo}")
		print(f"✓ Estado: {estado_envio}")
		print("=" * 70)
	
	return {
		'id': resumen_id,
		'desde_utc': desde_utc,
		'hasta_utc': hasta_utc,
		'num_eventos': len(eventos),
		'tipo': tipo,
		'estado': estado_envio,
		'resumen': resumen_json_obj
	}


if __name__ == '__main__':
	"""
	Ejecutar este módulo directamente para generar un resumen:
	python -m central.resumen
	"""
	generar_resumen(verbose=True)
