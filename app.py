from flask import Flask, jsonify
from central.gmail_client import get_sample_messages

app = Flask(__name__)

@app.route('/')
def home():
	return jsonify({"status": "ok", "message": "Secretario Central API"})

@app.route('/gmail/test')
def gmail_test():
	mensajes = get_sample_messages()
	return jsonify(mensajes)

if __name__ == '__main__':
	print("🚀 Iniciando Secretario Central en puerto 5001...")
	app.run(host='0.0.0.0', port=5001)
