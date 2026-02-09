# Plan: Agente Local de Investigacion de Mercado

**Fecha**: 2026-02-01
**Estado**: BORRADOR - Pendiente de aprobacion
**Hardware**: Ryzen 5 4500U, 14GB RAM, Radeon Vega 6 (integrada), 468GB NVMe

---

## 1. Objetivo

Construir un agente de IA local (corriendo en esta maquina) capaz de:

- **Investigar mercados** en Latinoamerica mediante scraping de multiples fuentes
- **Generar reportes** estructurados en Markdown y PDF
- Funcionar de forma **semi-autonoma** con reglas predefinidas y limites claros
- Servir como **ejercicio generico** que luego se adapte a cualquier nicho

El agente debe poder recibir un objetivo como:
> "Investiga el mercado de [X] en [pais/region]: competidores, precios, reviews, presencia online"

Y devolver un reporte completo con datos, tablas, y analisis.

---

## 2. Arquitectura: Estrategia Moderada

```
                    +------------------+
                    |   TU (humano)    |
                    |  defines reglas  |
                    |  apruebas plan   |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    |   ORQUESTADOR    |  <-- Script Python principal
                    |  (Plan-then-     |
                    |   Execute)       |
                    +--------+---------+
                             |
              +--------------+--------------+
              |              |              |
              v              v              v
     +--------+----+ +------+------+ +-----+-------+
     |  OLLAMA     | | SCRAPER     | | GENERADOR   |
     |  (cerebro)  | | (manos)     | | (output)    |
     |  qwen3:8b   | | requests +  | | Markdown +  |
     |  o similar  | | BeautifulSoup| | PDF         |
     +---------+---+ +------+------+ +-----+-------+
               |             |              |
               v             v              v
        Razonamiento   Datos crudos    Reportes
        + decisiones   de la web       finales
```

### Por que "Plan-then-Execute"?

Es la arquitectura **mas segura contra prompt injection**:

1. El modelo genera un **plan completo** (que URLs visitar, que datos extraer)
2. **Tu apruebas** el plan (o lo ajustas)
3. El scraper ejecuta el plan **sin volver a consultar al modelo** hasta tener datos
4. El modelo analiza los datos y genera el reporte

Esto significa que si una pagina web tiene instrucciones maliciosas ocultas,
el modelo NO las procesa durante la fase de ejecucion -- solo las ve despues,
cuando ya no controla las acciones de scraping.

---

## 3. Modelo de Seguridad

### 3.1 Triada Letal -- Como la rompemos

```
  Pata 1: DATOS PRIVADOS      -->  NEGADA
  Pata 2: INPUT NO CONFIABLE  -->  SI (scraping de webs)
  Pata 3: SALIDA AL EXTERIOR  -->  LIMITADA (solo dominios aprobados)
```

**Pata 1 NEGADA**: El agente corre en un directorio aislado (`~/agente-mercado/`).
No tiene acceso a tu repo `secretario/`, a tus credenciales, SSH keys, ni .env.

**Pata 2 PRESENTE pero controlada**: El agente procesara contenido web (no confiable),
pero solo DESPUES de que el plan esta aprobado, y el contenido pasa por limpieza
(strip de scripts, solo texto plano).

**Pata 3 LIMITADA**: El agente solo puede hacer requests a:
- Dominios que esten en una whitelist predefinida
- Opcionalmente, una API de IA externa (Anthropic/OpenAI) para tareas que superen
  la capacidad del modelo local

### 3.2 Reglas del agente (guardrails)

| Regla | Valor | Justificacion |
|-------|-------|---------------|
| Max requests por ejecucion | 50 | Evitar ban de IPs y abuso |
| Delay entre requests | 2-5 seg | Respetar servidores, evitar deteccion |
| Dominios permitidos | Whitelist explicita | Solo fuentes aprobadas |
| Timeout por request | 30 seg | No colgarse en servidores lentos |
| Tamano max de pagina | 1 MB | No descargar archivos pesados |
| Ejecucion de codigo | NO | El agente NO puede ejecutar codigo arbitrario |
| Acceso a filesystem | Solo su directorio | ~/agente-mercado/ y subdirectorios |
| Escritura de archivos | Solo reportes | Solo en ~/agente-mercado/output/ |

### 3.3 Aislamiento

**Opcion A (simple, para empezar)**:
- El agente corre como script Python normal
- Restricciones implementadas en codigo (whitelist, limites)
- Tu lo lanzas manualmente y revisas el output

**Opcion B (mas seguro, fase 2)**:
- El agente corre dentro de un contenedor Docker/Podman
- Filesystem aislado, red restringida por reglas
- Ollama corre en el host, el agente se conecta via API

**Recomendacion**: Empezar con Opcion A, migrar a B cuando el agente funcione.

---

## 4. Componentes Tecnicos

### 4.1 Motor de IA -- Ollama

| Componente | Detalle |
|------------|---------|
| Ollama | Motor de inferencia local |
| Modelo principal | `qwen3:8b` (bueno para tool-calling) |
| Modelo ligero (backup) | `llama3.2:3b` (mas rapido, menos capaz) |
| Modelo grande (opcional) | `qwen2.5:14b` (lento pero mas inteligente) |

El modelo principal (`qwen3:8b`) se usara para:
- Analizar la tarea del usuario y generar el plan de scraping
- Decidir que datos extraer de cada pagina
- Analizar los datos recopilados
- Redactar el reporte final

### 4.2 Scraping

| Herramienta | Uso |
|-------------|-----|
| `requests` | HTTP client para descargar paginas |
| `BeautifulSoup4` | Parseo de HTML, extraccion de texto/datos |
| `trafilatura` | Extraccion inteligente de contenido principal (ignora menus, ads) |
| `fake_useragent` | Rotacion de User-Agent para evitar bloqueos basicos |

NO se usara Selenium/Playwright (navegador headless) en la primera fase.
Solo HTTP puro. Esto limita el scraping a paginas que no requieren JavaScript,
pero es mucho mas simple y seguro.

### 4.3 Generacion de reportes

| Herramienta | Uso |
|-------------|-----|
| Markdown | Formato nativo de los reportes |
| `weasyprint` o `md-to-pdf` | Conversion a PDF |
| Tablas en Markdown | Datos comparativos |

### 4.4 API externa (opcional)

Si decides usar una API externa como respaldo:

```python
# El orquestador decide cuando usar el modelo local vs externo
if tarea_compleja and api_key_disponible:
    usar_api_externa()  # Claude API o OpenAI
else:
    usar_ollama_local()  # qwen3:8b
```

Criterios para escalar a API externa:
- El reporte requiere analisis comparativo muy detallado
- El modelo local no genera output de calidad suficiente
- Se necesita procesar mucho texto (contexto largo)

---

## 5. Flujo de Ejecucion

### Paso 1: Definir la investigacion

```
Tu: "Investiga glampings en Colombia: competidores, precios, capacidad, reviews"
```

### Paso 2: El agente genera un plan

El modelo local analiza tu peticion y genera:

```yaml
plan:
  objetivo: "Investigacion de mercado de glampings en Colombia"
  fuentes:
    - dominio: booking.com
      busqueda: "glamping Colombia"
      extraer: [nombre, precio, rating, ubicacion, capacidad]
    - dominio: airbnb.com
      busqueda: "glamping Colombia"
      extraer: [nombre, precio, rating, ubicacion, amenidades]
    - dominio: tripadvisor.com
      busqueda: "glamping Colombia"
      extraer: [nombre, rating, num_reviews, rango_precios]
    - dominio: google.com
      busqueda: "glamping Colombia mejores"
      extraer: [urls_competidores]
  max_resultados_por_fuente: 20
  idioma: es
```

### Paso 3: Tu apruebas (o ajustas) el plan

```
[PLAN GENERADO] ¿Aprobar? (s/n/editar)
> s
```

### Paso 4: Scraping automatico

El agente ejecuta el plan:
- Visita cada fuente en la whitelist
- Extrae los datos definidos
- Guarda datos crudos en ~/agente-mercado/data/
- Respeta limites (delay, max requests, timeout)

### Paso 5: Analisis y generacion del reporte

El modelo local recibe los datos extraidos y genera:

```
~/agente-mercado/output/
  reporte_glamping_colombia_2026-02-01.md
  reporte_glamping_colombia_2026-02-01.pdf
  datos_crudos_glamping_colombia.json
```

### Paso 6: Tu revisas el reporte

---

## 6. Fases de Implementacion

### Fase 1: Fundamentos (lo minimo funcional)

- [ ] Instalar Ollama
- [ ] Descargar modelo `qwen3:8b` (o `llama3.2:3b` si queremos empezar rapido)
- [ ] Crear estructura de directorios `~/agente-mercado/`
- [ ] Script basico de scraping con requests + BeautifulSoup
- [ ] Script de conexion a Ollama API (localhost:11434)
- [ ] Orquestador minimo: prompt -> plan -> scraping -> reporte
- [ ] Test con una busqueda simple en un solo sitio

### Fase 2: Agente funcional

- [ ] Implementar flujo Plan-then-Execute completo
- [ ] Whitelist de dominios configurable
- [ ] Limites de requests y delays
- [ ] Generacion de reportes en Markdown
- [ ] Conversion a PDF
- [ ] Guardar datos crudos en JSON para re-analisis
- [ ] Logging de todas las acciones del agente

### Fase 3: Mejoras

- [ ] Soporte para multiples modelos (cambiar entre 3B/8B/14B)
- [ ] Integracion opcional con API externa (Anthropic/OpenAI)
- [ ] Extraccion mas inteligente con trafilatura
- [ ] Templates de investigacion reutilizables
- [ ] Historial de investigaciones previas

### Fase 4: Seguridad avanzada (opcional)

- [ ] Containerizacion con Docker/Podman
- [ ] Restriccion de red a nivel de contenedor
- [ ] Filesystem aislado montado como volumen
- [ ] Monitoreo de acciones del agente

---

## 7. Estructura de Directorios Propuesta

```
~/agente-mercado/
  config/
    whitelist_dominios.yaml    # Dominios permitidos
    config.yaml                # Configuracion general (limites, delays, modelo)
  src/
    orquestador.py             # Script principal
    scraper.py                 # Funciones de scraping
    analizador.py              # Conexion a Ollama + analisis
    generador_reporte.py       # Generacion de MD/PDF
    utils.py                   # Limpieza de HTML, validaciones
  templates/
    investigacion_mercado.yaml # Template de plan para mercados
  data/                        # Datos crudos (temporal)
  output/                      # Reportes generados
  logs/                        # Registro de acciones
```

---

## 8. Ejemplo de Whitelist de Dominios

```yaml
# whitelist_dominios.yaml
dominios_permitidos:
  portales_reservas:
    - booking.com
    - airbnb.com
    - tripadvisor.com
    - despegar.com
    - trivago.com
  buscadores:
    - google.com
    - bing.com
    - duckduckgo.com
  reviews:
    - trustpilot.com
    - yelp.com
  redes_sociales:
    - instagram.com    # Solo perfiles publicos via web
    - facebook.com     # Solo paginas publicas
  apis_ia:             # Solo si se configura API key
    - api.anthropic.com
    - api.openai.com

# Cualquier dominio NO listado aqui sera BLOQUEADO
```

---

## 9. Riesgos Identificados y Mitigaciones

| # | Riesgo | Probabilidad | Impacto | Mitigacion |
|---|--------|-------------|---------|------------|
| 1 | Prompt injection via contenido web | Media | Alto | Plan-then-Execute: el modelo no controla acciones durante scraping |
| 2 | Scraping detectado y bloqueado (IP ban) | Alta | Bajo | Delays, User-Agent rotation, respetar robots.txt |
| 3 | Modelo local genera analisis de baja calidad | Media | Medio | Escalar a API externa para analisis final si es necesario |
| 4 | Datos personales en paginas scrapeadas | Baja | Medio | Solo extraer datos publicos de negocios, no de personas |
| 5 | El agente consume toda la RAM | Baja | Medio | Monitor de recursos, matar proceso si RAM > 12GB |
| 6 | Contenido malicioso en paginas web | Baja | Bajo | Solo texto plano, no ejecutar JS ni descargar binarios |
| 7 | Violacion de terminos de servicio | Media | Medio | Respetar robots.txt, limitar frecuencia, no autenticarse |
| 8 | API externa costosa por uso excesivo | Baja | Bajo | Limitar calls a API externa, usar local primero siempre |

---

## 10. Dependencias / Requisitos Previos

- [ ] Python 3.10+ (verificar version actual)
- [ ] Ollama instalado y corriendo
- [ ] Modelo descargado (qwen3:8b o alternativa)
- [ ] Paquetes pip: requests, beautifulsoup4, trafilatura, pyyaml, weasyprint
- [ ] Espacio en disco: ~10GB (modelo + datos + reportes)
- [ ] Conexion a internet (para scraping y opcionalmente API externa)

---

## 11. Decision Pendiente: API Externa

| Opcion | Costo aprox. | Ventaja | Desventaja |
|--------|-------------|---------|------------|
| Solo local (Ollama) | $0 | Privacidad total, sin dependencias | Calidad limitada en analisis complejo |
| Anthropic Claude API | ~$0.003/1K tokens (Haiku) | Alta calidad, rapido | Requiere API key, costo por uso |
| OpenAI API | ~$0.002/1K tokens (GPT-4o-mini) | Alta calidad, ecosistema grande | Requiere API key, costo por uso |
| Ambos (local + fallback) | Variable | Lo mejor de ambos mundos | Mas complejidad en codigo |

**No es necesario decidir ahora.** El sistema se disenara para funcionar 100% local,
con la API externa como modulo opcional que se activa solo si configuras una API key.

---

## 12. Metricas de Exito

Para considerar el experimento exitoso, el agente debe poder:

1. Recibir un objetivo de investigacion en lenguaje natural
2. Generar un plan de scraping coherente
3. Ejecutar el scraping respetando todos los limites
4. Producir un reporte legible con datos reales
5. Completar todo el ciclo en una ejecucion sin intervencion manual (post-aprobacion)
6. No acceder a ningun recurso fuera de su directorio y whitelist

---

## Siguiente Paso

Cuando apruebes este plan, procedemos con la **Fase 1**:
1. Instalar Ollama
2. Descargar el modelo
3. Crear la estructura de directorios
4. Construir el orquestador minimo

**No se ejecutara nada hasta tu aprobacion.**
