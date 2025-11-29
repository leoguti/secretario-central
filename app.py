from flask import Flask, jsonify
from central.gmail_client import get_sample_messages
from central.db import get_eventos_recientes, get_estadisticas, init_db

app = Flask(__name__)

# Inicializar base de datos al arrancar la aplicación
init_db()

@app.route('/')
def home():
	return jsonify({"status": "ok", "message": "Secretario Central API"})

@app.route('/gmail/test')
def gmail_test():
	mensajes = get_sample_messages()
	return jsonify(mensajes)

@app.route('/eventos/recientes')
def eventos_recientes():
	"""Endpoint para obtener eventos recientes de la base de datos."""
	limit = 20
	eventos = get_eventos_recientes(limit=limit)
	return jsonify({
		"total": len(eventos),
		"eventos": eventos
	})

@app.route('/eventos/estadisticas')
def eventos_estadisticas():
	"""Endpoint para obtener estadísticas de los eventos."""
	stats = get_estadisticas()
	return jsonify(stats)

if __name__ == '__main__':
	print("🚀 Iniciando Secretario Central en puerto 5001...")
	app.run(host='0.0.0.0', port=5001)
