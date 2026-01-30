# 🤖 Secretario Personal y Familiar

Asistente inteligente para gestionar **trabajo profesional** y **operaciones del hogar**.

## 🎯 Objetivo

Sistema automatizado que centraliza y procesa:
- 📧 **Correos importantes** (Gmail)
- 💰 **Finanzas familiares** (recibos, gastos, control de deudas)
- 📅 **Calendario** y eventos
- 🔔 **Notificaciones** y alertas

## 🏗️ Componentes Principales

### 1. **Gestión de Finanzas Familiares** 📊
- Procesamiento automático de recibos (fotos/PDFs)
- Transcripción de mensajes de voz con gastos (WhatsApp)
- Categorización inteligente con IA
- Registro en Google Sheets
- Ver: [`cuentas/PROCESO_FINANZAS.md`](cuentas/PROCESO_FINANZAS.md)

### 2. **Monitoreo de Gmail** 📧
- Lectura automática de correos importantes
- Filtrado de promociones y spam
- Resúmenes diarios con OpenAI
- Ver: [`POLITICAS_TRABAJO.md`](POLITICAS_TRABAJO.md)

### 3. **Integración WhatsApp** 💬
- Recepción de mensajes de familia (gastos, tareas)
- Notificaciones de eventos importantes
- Bot conversacional (en desarrollo)

## 💻 Tecnologías

- **Python 3.12**
- **Google APIs**: Gmail, Drive, Calendar, Sheets
- **OpenAI**: Resúmenes y categorización
- **Whisper API**: Transcripción de voz
- **Textit/WhatsApp**: Mensajería familiar

## 🚀 Instalación

### 1. Configurar entorno
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configurar credenciales de Google
- Coloca `credentials.json` (OAuth) en la raíz del proyecto
- Primera ejecución pedirá autorización en navegador
- Se generará `token.json` automáticamente

### 3. Configurar OpenAI (opcional)
```bash
export OPENAI_API_KEY='tu-api-key-aqui'
```

## 📁 Estructura del Proyecto

```
secretario/
├── cuentas/              # Documentación y scripts de finanzas
│   ├── PROCESO_FINANZAS.md
│   ├── SISTEMA_ANALISIS_FINANCIERO.md
│   └── setup_drive_finanzas.py
├── central/              # Módulos de backend (Gmail, Calendar, etc.)
│   ├── gmail_client.py
│   ├── calendar_client.py
│   └── db.py            # SQLite para trabajo profesional
├── data/                 # Base de datos (no se sube a Git)
├── credentials.json      # OAuth Google (no se sube)
├── token.json           # Token generado (no se sube)
└── app.py               # Servidor Flask
```

## 🔧 Uso del Sistema

### Trabajo Profesional (Gmail + Resúmenes)

**1. Ejecutar servidor Flask:**
```bash
python app.py
```
Endpoints disponibles:
- `http://localhost:5001/` - Estado de la API
- `http://localhost:5001/gmail/test` - Últimos correos

**2. Ingestar correos importantes:**
```bash
python -m central.gmail_ingest
```
- Busca correos de últimos 3 días
- Excluye promociones y redes sociales
- Guarda en SQLite (`data/secretario.db`)

**3. Generar resúmenes con IA:**
```bash
export OPENAI_API_KEY='tu-key'
python -m central.resumen
```
- Analiza eventos nuevos
- Genera resumen estructurado
- Identifica oportunidades y riesgos

### Finanzas Familiares

Ver documentación completa en:
- [`cuentas/PROCESO_FINANZAS.md`](cuentas/PROCESO_FINANZAS.md) - Flujo de trabajo
- [`cuentas/SISTEMA_ANALISIS_FINANCIERO.md`](cuentas/SISTEMA_ANALISIS_FINANCIERO.md) - Estructura del sistema
- [`cuentas/ANALISIS_SHEET_EXISTENTE.md`](cuentas/ANALISIS_SHEET_EXISTENTE.md) - Sheet de Lucía

**Carpeta Drive:** [/Finanzas](https://drive.google.com/drive/folders/1yKx1kfJsJAO_iC_6K0_2DTubWaGXM8Q2)

## 📋 Roadmap

### ✅ Implementado
- [x] Lectura de Gmail vía API
- [x] Base de datos SQLite para trabajo profesional
- [x] Resúmenes automáticos con OpenAI
- [x] Documentación sistema de finanzas
- [x] Estructura de carpetas en Google Drive

### 🔄 En Desarrollo
- [ ] Procesamiento automático de recibos (OCR + IA)
- [ ] Transcripción de mensajes de voz (Whisper)
- [ ] Integración WhatsApp/Textit
- [ ] Escritura automática en Google Sheets

### 🎯 Futuro
- [ ] Dashboard web de finanzas
- [ ] Notificaciones inteligentes
- [ ] Alertas de gastos
- [ ] Proyecciones de deuda

## 📚 Documentos Relacionados

- [`POLITICAS_TRABAJO.md`](POLITICAS_TRABAJO.md) - Políticas del sistema
- [`TRANSACCIONES_FINANCIERAS.md`](TRANSACCIONES_FINANCIERAS.md) - Transacciones financieras
- [`cuentas/`](cuentas/) - Todo sobre finanzas familiares

## 🧹 Archivos de Prueba (No usar)

Los siguientes archivos son **experimentos/pruebas** y no forman parte del sistema principal:
- `whatsapp_*.sh` - Pruebas de automatización con ADB (no se usan)
- `phone_automation.sh` - Experimento de control de teléfono (no se usa)
- `test_voces*.sh` - Pruebas de text-to-speech (no se usan)
- `edge_tts_audiobook.py` - Experimento TTS (no se usa)
- `elevenlabs_tts.py` - Experimento TTS (no se usa)
- `dryrun_*.png` - Screenshots de pruebas (no se usan)

---

**Última actualización:** 2026-01-05
