## Endpoint de prueba de Gmail

Con la app corriendo:

   python app.py

Visita:

   http://localhost:5001/gmail/test

y verás un JSON con los últimos correos (id, subject, snippet) de la cuenta configurada.
# Secretario Central

Este proyecto es una aplicación en Python que actúa como un "secretario central" para registrar, organizar y analizar eventos de múltiples fuentes (Gmail, Calendar, Slack, etc.).

## Características principales

### Base de datos de eventos
El sistema incluye una base de datos SQLite que registra eventos de diferentes fuentes en una tabla unificada llamada `eventos`.

**¿Qué información almacena?**
- **Metadatos básicos**: fuente (gmail, calendar, slack), tipo (email, reunión, mensaje), fecha del evento
- **Actores**: email y nombre de la persona involucrada
- **Contexto de proyecto**: proyecto, ciudad, país
- **Contenido**: asunto, resumen corto, extracto, URL original
- **Clasificación**: etiquetas, nivel de importancia, estado

**¿Para qué se usará?**
En fases posteriores, esta base de datos permitirá:
- Generar resúmenes diarios automáticos
- Detectar oportunidades de negocio
- Identificar patrones en proyectos
- Hacer seguimiento de conversaciones importantes
- Analizar actividad por proyecto/país/ciudad

### Integración con Gmail
- Lectura de correos a través de la API de Gmail
- Autenticación OAuth2 configurada

## Tecnologías usadas
- Python 3.12
- Flask (framework web)
- SQLite (base de datos)
- Google API Client (Gmail)
- Git y GitHub para control de versiones

## ¿Cómo ejecutar la app?

### Instalación inicial
1. Clona el repositorio:
   ```bash
   git clone https://github.com/leoguti/secretario-central.git
   cd secretario-central
   ```

2. Crea y activa el entorno virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # En Linux/Mac
   # .venv\Scripts\activate   # En Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Inicializar la base de datos
Antes de usar la aplicación por primera vez, inicializa la base de datos de eventos:

```bash
python -m central.db
```

Esto creará el archivo `data/secretario.db` con la tabla `eventos` y sus índices.

### Ejecutar la aplicación
```bash
python app.py
```

La aplicación estará disponible en http://localhost:5001

### Probar la base de datos
Ejecuta el script de prueba para insertar eventos de ejemplo y ver estadísticas:

```bash
python test_db.py
```

Este script:
- Inicializa la base de datos si no existe
- Inserta 4 eventos de prueba (emails, reuniones, mensajes)
- Muestra los eventos más recientes
- Muestra estadísticas por fuente, proyecto e importancia

### Ingesta de correos de Gmail

Para importar correos de Gmail a la base de datos de eventos, ejecuta:

```bash
python -m central.gmail_ingest
```

**¿Qué hace este comando?**
- Obtiene correos recibidos en los **últimos 3 días**
- **Excluye** automáticamente:
  - Promociones (CATEGORY_PROMOTIONS)
  - Mensajes sociales (CATEGORY_SOCIAL)
- Inserta cada correo como un evento en la tabla `eventos`
- **Evita duplicados**: verifica si el correo ya fue procesado usando `fuente_id`
- Mapea información del correo a campos de eventos:
  - `fuente` → 'gmail'
  - `tipo` → 'email'
  - `actor_email` → remitente del correo
  - `asunto` → subject del correo
  - `extracto` → snippet de Gmail
  - `url_origen` → enlace web al correo en Gmail
  - `fecha_evento_utc` → timestamp del correo en UTC

**Resultado esperado:**
```
============================================================
INGESTA DE CORREOS DE GMAIL
============================================================
→ Buscando correos de los últimos 3 días...
→ Excluyendo: promociones y sociales

✓ Se encontraron 15 mensajes

  ✓ Insertado: Reunión proyecto GTFS México...
  ○ Ya existe: Propuesta OSM Colombia...
  ✓ Insertado: Actualización Arequipa OMUS...
  
============================================================
RESUMEN DE INGESTA
============================================================
  Mensajes analizados:  15
  Nuevos insertados:    12
  Ya existían:          3
============================================================
```

**Nota:** La primera vez que ejecutes este comando puede pedirte autorización en el navegador para acceder a Gmail.

### Resúmenes automáticos con OpenAI

El sistema puede generar resúmenes inteligentes de los eventos usando la API de OpenAI.

**Requisito previo:**
```bash
export OPENAI_API_KEY='tu-api-key-aqui'
```

**Ejecutar generación de resumen:**
```bash
python -m central.resumen
```

**¿Qué hace este comando?**
- Lee los eventos **nuevos desde el último resumen** generado
- Si es la primera vez, toma las **últimas 12 horas** de eventos
- Envía los eventos a OpenAI (modelo `gpt-4o-mini` económico)
- Recibe un JSON estructurado con:
  - Resumen general del periodo
  - Eventos clave identificados
  - Oportunidades de negocio detectadas
  - Riesgos o problemas encontrados
  - Pendientes sugeridos para Leonardo
- Guarda el resumen en la tabla `resumenes` de SQLite
- Muestra el resumen en consola

**Ejemplo de salida:**
```
======================================================================
GENERACIÓN DE RESUMEN AUTOMÁTICO
======================================================================

→ Rango de tiempo:
  Desde: 2025-11-29T08:00:00Z
  Hasta: 2025-11-29T14:30:00Z

→ Eventos encontrados: 23

→ Llamando a OpenAI para generar resumen...

======================================================================
RESUMEN GENERADO
======================================================================

📋 Resumen General:
   En este periodo se recibieron múltiples comunicaciones relacionadas con
   proyectos GTFS en México y Perú, actualizaciones de la asociación Trufi,
   y oportunidades de colaboración con GIZ.

🔑 Eventos Clave (3):
   • Propuesta de GIZ para proyecto GTFS en Toluca con financiamiento confirmado
   • Reunión de la junta directiva de Trufi programada para el 5 de diciembre
   • Solicitud urgente de revisión de entregables del proyecto OMUS Arequipa

💡 Oportunidades (2):
   • Posible expansión del proyecto GTFS México a otras ciudades
   • Colaboración con universidad local para capacitación en OpenStreetMap

⚠️  Riesgos (1):
   • Plazo ajustado para entregables de Arequipa (vence 30 nov)

✅ Pendientes (4):
   • Responder propuesta de GIZ antes del 2 de diciembre
   • Preparar agenda para reunión Trufi del 5 de diciembre
   • Revisar documentos del proyecto Arequipa antes del 30 de noviembre
   • Coordinar con equipo OSM para taller en Boyacá

======================================================================
✓ Resumen guardado con ID: 1
✓ Tipo: tarde
✓ Estado: pendiente
======================================================================
```

**Uso programático:**
Puedes usar este comando en un cron para ejecutarlo automáticamente:
```bash
# Generar resumen a las 7:00 AM y 2:00 PM todos los días
0 7,14 * * * cd /path/to/secretario && source .venv/bin/activate && python -m central.resumen
```

## Endpoints disponibles

### API Principal
- `GET /` - Estado de la API
- `GET /gmail/test` - Obtiene los últimos correos de Gmail

### API de Eventos (Base de datos)
- `GET /eventos/recientes` - Obtiene los últimos 20 eventos registrados
- `GET /eventos/estadisticas` - Estadísticas de eventos (por fuente, proyecto, importancia)

## Estructura del proyecto
```
secretario-central/
├── app.py                    # Aplicación Flask principal
├── central/
│   ├── __init__.py
│   ├── db.py                 # Módulo de base de datos SQLite
│   └── gmail_client.py       # Cliente de Gmail API
├── data/
│   └── secretario.db         # Base de datos SQLite (no se sube a Git)
├── test_db.py                # Script de prueba de la base de datos
├── requirements.txt          # Dependencias del proyecto
├── .gitignore               # Archivos ignorados por Git
└── README.md                # Este archivo
```

## Esquema de la base de datos

### Tabla `eventos`
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER | ID único autoincremental |
| fuente | TEXT | Fuente del evento (gmail, calendar, slack, etc.) |
| fuente_id | TEXT | ID original en la fuente |
| tipo | TEXT | Tipo de evento (email, reunion, mensaje, etc.) |
| fecha_evento_utc | TEXT | Fecha/hora del evento en ISO8601 UTC |
| actor_email | TEXT | Email de la persona principal |
| actor_nombre | TEXT | Nombre de la persona |
| proyecto | TEXT | Nombre del proyecto relacionado |
| ciudad | TEXT | Ciudad relacionada |
| pais | TEXT | Código de país (MX, PE, CO, etc.) |
| etiquetas | TEXT | Tags separadas por comas |
| resumen_corto | TEXT | Resumen breve del evento |
| asunto | TEXT | Subject o título |
| extracto | TEXT | Snippet o extracto del contenido |
| url_origen | TEXT | URL al contenido original |
| importancia | INTEGER | 0=normal, 1=media, 2=alta |
| estado | TEXT | nuevo, en_proceso, ignorado, hecho |
| creado_en_utc | TEXT | Timestamp de creación en la BD |
| actualizado_en_utc | TEXT | Timestamp de última actualización |

**Índices creados:**
- `idx_eventos_fecha` - Por fecha de evento
- `idx_eventos_fuente_id` - Por fuente e ID de fuente
- `idx_eventos_proyecto_fecha` - Por proyecto y fecha
- `idx_eventos_importancia_fecha` - Por importancia y fecha

## Próximos pasos (Roadmap)
- [ ] Sincronización automática de Gmail a la base de datos
- [ ] Integración con Google Calendar
- [ ] Parser de información de proyectos desde emails
- [ ] Resúmenes diarios automáticos
- [ ] Detección de oportunidades de negocio
- [ ] Dashboard web para visualización de eventos

---
**Repositorio:** https://github.com/leoguti/secretario-central
