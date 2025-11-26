# Secretario Central

Este proyecto es una aplicación mínima en Python usando Flask.

## ¿Qué hemos hecho?
- Creamos un entorno virtual de Python para aislar dependencias.
- Instalamos Flask como framework principal para la aplicación web.
- Desarrollamos una app mínima (`app.py`) que responde en http://localhost:5001 con un mensaje simple.
- Inicializamos un repositorio Git y lo subimos a GitHub en: https://github.com/leoguti/secretario-central
- Instalamos las librerías de Google API para Python.
- Configuramos credenciales OAuth2 para Gmail y autenticamos la aplicación.
- Creamos un script (`gmail_hola_mundo.py`) que envía un correo de prueba usando la API de Gmail.
- Probamos el envío de correos y confirmamos que, tras la primera autorización, ya no es necesario abrir el navegador para enviar más correos.

## Tecnologías usadas
- Python 3.12
- Flask
- Git y GitHub para control de versiones

## ¿Cómo ejecutar la app?
1. Clona el repositorio:
   ```bash
   git clone https://github.com/leoguti/secretario-central.git
   cd secretario-central
   ```
2. Activa el entorno virtual (si existe) o créalo:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install Flask
   ```
3. Ejecuta la aplicación:
   ```bash
   python app.py
   ```
4. Abre tu navegador en http://localhost:5001

## Próximos pasos
- Agregar nuevas rutas y funcionalidades.
- Mejorar la documentación.
- Crear archivos de configuración como `.gitignore` y `requirements.txt`.

---
Este README se irá actualizando a medida que avance el proyecto.
