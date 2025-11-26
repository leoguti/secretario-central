from flask import Flask, jsonify
from central.gmail_client import get_sample_messages

app = Flask(__name__)

@app.route('/gmail/test')
def gmail_test():
	mensajes = get_sample_messages()
	return jsonify(mensajes)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)
