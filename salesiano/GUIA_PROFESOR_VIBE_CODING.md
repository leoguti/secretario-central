# Guía del Profesor - Taller OpenStreetMap + Vibe Coding 2026

**Instructor:** Leonardo Gutiérrez
**Fecha de creación:** 21 de febrero de 2026
**Grupo:** 2 estudiantes mayores (6to+ grado) + 1 niña de 8 años

---

## Estudiantes y niveles

| Estudiante | Edad | Nivel | Herramientas |
|---|---|---|---|
| Mayor 1 | 13+ | GitHub + VS Code + Copilot + OSM avanzado | Cuenta propia |
| Mayor 2 | 13+ | GitHub + VS Code + Copilot + OSM avanzado | Cuenta propia |
| Niña | 8 años | Scratch + OSM exploración + verificación de campo | Cuenta supervisada |

**Nota:** GitHub y Claude.ai requieren 13+ años. La niña participa con supervisión.

---

## Infraestructura disponible

- Sala de cómputo con PCs Windows
- Conexión a internet
- El instructor tiene Claude Code (cuenta paga)
- Los estudiantes usarán herramientas gratuitas

---

## Herramientas gratuitas para los estudiantes mayores

### GitHub Copilot Pro (gratis para estudiantes)

- **Qué incluye:** 300 solicitudes premium/mes, acceso a Claude Sonnet, agent mode en VS Code
- **Requisitos:** 13+ años, estar matriculados
- **Verificación:** Subir foto del carné estudiantil o certificado de matrícula
- **Tiempo de aprobación:** ~72 horas
- **Enlace:** https://education.github.com/pack

### Pasos para activar

1. Crear cuenta en github.com
2. Aplicar al Student Developer Pack con carné del colegio
3. Esperar aprobación (~72h)
4. Instalar VS Code (gratis, Windows)
5. Instalar extensión GitHub Copilot en VS Code
6. Seleccionar modelo Claude Sonnet en Copilot

### Copilot gratuito sin verificación (mientras esperan aprobación)

- 50 chats/mes + 2000 autocompletados de código
- Acceso a GPT-4o y Claude 3.5 Sonnet
- Agent mode disponible con solicitudes limitadas

---

## Herramientas y plan para Milagros (8 años)

### Fase 1: Habilidades básicas del computador (VALIDADO)

**Enfoque pedagógico: Scaffolding (andamiaje)**
Se enseña una habilidad a la vez, se practica hasta dominarla, y luego se agrega la siguiente.

**Principios:**
- Retroalimentación inmediata (sonido, color, animación en cada acción)
- Interfaz visual, poco o nada de texto
- Error sin castigo (no hay "game over", solo reintentar)
- Contexto significativo (ojalá con temas de Duitama/colegio)
- Sesiones cortas (10-15 min por habilidad)
- Progresión visible (estrellas, niveles, barra de progreso)

**Progresión de habilidades:**
1. Mover el mouse (solo mover, sin clic)
2. Clic izquierdo (mover + clic en un objetivo)
3. Arrastrar (clic sostenido + mover)
4. Scroll (navegar contenido largo)
5. Doble clic
6. Teclado (encontrar letras, escribir palabras)
7. Combinación (teclado + mouse juntos)

**Herramienta principal: GCompris 26.0** (requiere versión 26.0, NO la 4.0 de apt)
- Open source (KDE/GNU), gratuito
- +150 actividades para niños de 2-10 años
- Incluye entrenamiento de mouse, teclado, clic, doble clic, arrastrar
- Disponible en Windows (Microsoft Store) y en español
- Enlace: https://gcompris.net
- Se instala en el PC de Milagros (Windows) y en el portátil del instructor (Linux)

**GCompris-Teachers 26.0 (dashboard del profesor)**
- App complementaria para el instructor, lanzada en febrero 2026
- Funciona como servidor/cliente en red local
- Disponible para Linux y Windows
- Descarga: https://www.gcompris.net/downloads-en.html
- Debe ser la misma versión que GCompris del alumno

Arquitectura en clase:
```
Portátil instructor (Linux)         PC Milagros (Windows)
┌───────────────────────┐           ┌───────────────────────┐
│ GCompris-Teachers 26.0│◄──red────►│ GCompris 26.0         │
│ (dashboard profesor)  │   local   │ (actividades alumna)  │
└───────────────────────┘           └───────────────────────┘
```

Funcionalidades del dashboard:
- Crear grupos de alumnos (importar por CSV)
- Crear planes de trabajo específicos por alumno
- Enviar plan de trabajo al PC del alumno por red local
- Ver resultados por grupo y por alumno (gráficos)
- Analizar respuestas en detalle (patrones de error, qué reforzar)
- Actividad "Multiple Choice Questions" configurable por el profesor

**IMPORTANTE - Instalación:**
- En Ubuntu, `apt install gcompris-qt` instala la versión 4.0 (vieja, sin teachers tool)
- Se necesita la versión 26.0: instalar via snap (`sudo snap install gcompris`) o descargar el .sh desde gcompris.net
- Desinstalar la 4.0 antes: `sudo apt remove gcompris-qt`

**Proyecto futuro: Juego web "Explora Duitama"**
- Los estudiantes mayores lo construyen como proyecto de vibe coding
- Temática de Duitama/OSM, personalizado para Milagros
- Servido desde el portátil del instructor (python -m http.server)
- Milagros accede desde su PC en la red local

### Fase 2: OSM y exploración (después de dominar lo básico)

| Herramienta | Para qué | Enlace |
|---|---|---|
| **OpenStreetMap** (explorar) | Buscar lugares, identificar qué falta | https://www.openstreetmap.org |
| **StreetComplete** (Android) | Misiones gamificadas de mapeo | Play Store |
| **Scratch** | Programación visual con bloques | https://scratch.mit.edu |
| **Dibujo en papel** | Mapear su barrio a mano, comparar con OSM | - |

### Tareas apropiadas para Milagros

**Básicas (Fase 1):**
1. Practicar mouse, teclado, scroll con GCompris
2. Jugar "Explora Duitama" cuando esté listo

**Intermedias (Fase 2):**
3. Explorar openstreetmap.org: buscar el colegio, su casa, el parque
4. Hacer lista en papel de 5 cosas que faltan en el mapa cerca del colegio
5. Ser "verificadora de campo": confirmar si lo que dice el mapa es correcto
6. Tomar fotos de calles y lugares para que los mayores las suban

**Avanzadas (Fase 3):**
7. Aprender Scratch: hacer que un personaje se mueva por un mapa
8. Los estudiantes mayores son sus "mentores"

---

## Clase 1 - Introducción (ya realizada)

- Se hizo introducción al vibe coding y Claude Code
- Se explicaron las capacidades vs ChatGPT web

## Clase 2 - Demo y cuentas GitHub (21 de febrero 2026)

### Parte 1 - Demo con Claude Code (20 min)

**Guión para el profesor:**

> "Lo que ven aquí es una terminal. Es la forma en que los programadores profesionales trabajan. No es una página web, no es un chat. Es una herramienta que se llama Claude Code y es una inteligencia artificial que puede crear archivos, programas, páginas web, leer documentos, buscar información - todo desde aquí."

> "Yo le hablo en español, le digo qué quiero, y Claude lo hace. Vamos a probarlo."

**Demo preparada:** Mapa interactivo de Duitama
- Archivo: `salesiano/demo/mapa_duitama.html`
- Muestra: Colegio Salesiano, Plaza de los Libertadores, Terminal, Parque de la Milagrosa
- Usa tiles de OpenStreetMap (conexión directa con lo que aprenden)

**Después de la demo:**

> "Eso que acaban de ver es vibe coding: yo le dije a la IA qué quería y ella lo construyó. Ustedes van a aprender a hacer esto."

### Parte 2 - Crear cuentas GitHub (30 min) - Solo mayores

1. Ir a github.com y crear cuenta
2. Explicar: "Esto es su portafolio profesional"
3. Aplicar al Student Developer Pack con carné
4. Crear primer repositorio con un README.md

**Mientras tanto, la niña:** Explora openstreetmap.org y hace su lista en papel.

### Parte 3 - Primer contacto (30 min)

- Usar Copilot gratuito básico o Claude.ai para un primer ejercicio
- La niña explora Scratch
- Tarea: cada uno tiene su primer repositorio creado

## Clase 3 - Primer proyecto real (cuando Copilot Pro esté aprobado)

- Instalar VS Code en los PCs
- Activar Copilot con Claude Sonnet
- Primer ejercicio de vibe coding con agent mode
- La niña: primer proyecto en Scratch

---

## Estructura de proyectos del año

### Los 3 pilares

1. **OpenStreetMap** - Mejorar el mapa digital de Duitama (todos)
2. **Vibe Coding** - Crear aplicaciones usando IA (mayores con Copilot, niña con Scratch)
3. **GitHub** - Portafolio profesional (mayores)

### Proyectos compartidos posibles

- Mapa interactivo del colegio hecho por todos
- Inventario de lugares del barrio (niña verifica, mayores mapean y programan)
- App que muestre los lugares mapeados por el grupo
- Participar en eventos de la comunidad OSM

### Proyecto con la Alcaldía de Duitama

- Mejorar el mapa digital de la ciudad en OpenStreetMap
- Mapear calles, parques, edificios públicos, puntos de interés
- Posibilidad de mapas de transporte público

---

## Dinámica del grupo (VALIDADO)

**Estructura típica de cada sesión:**

```
┌──────────────────────────────────────────────────┐
│  Mayores: Vibe Coding (VS Code + Copilot)        │
│  Milagros: GCompris / Explora Duitama            │
│                                                    │
│  Momento conjunto: proyecto OSM de Duitama        │
│  (cada uno aporta a su nivel)                     │
└──────────────────────────────────────────────────┘
```

- Mientras los mayores se entrenan en vibe coding, Milagros entrena habilidades básicas
- Los mayores son mentores de Milagros
- Proyectos compartidos donde cada uno aporta a su nivel
- El instructor demuestra con Claude Code, ellos replican con Copilot
- Aprendemos haciendo, no con teoría

---

## Recursos y enlaces

- GitHub Education: https://education.github.com/pack
- OpenStreetMap: https://www.openstreetmap.org
- Scratch: https://scratch.mit.edu
- VS Code: https://code.visualstudio.com
- Copilot en VS Code: https://code.visualstudio.com/blogs/2024/12/18/free-github-copilot
- Agent Mode: https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode
- GCompris descargas: https://www.gcompris.net/downloads-en.html
- GCompris Teachers Handbook: https://docs.kde.org/stable_kf6/en/gcompris-teachers-handbook/gcompris-teachers-handbook/index.html
- GCompris 26.0 release notes: https://ubuntuhandbook.org/index.php/2026/02/gcompris-26-0-released-with-2-new-activities-teachers-tool/

---

## Notas pendientes

- [ ] Definir horario definitivo de las clases
- [ ] Confirmar inscripción oficial de los 3 estudiantes
- [ ] Desarrollar programa clase por clase para el resto del año
- [ ] Explorar alianza con Alcaldía para mapeo
- [ ] Planificar participación en eventos OSM Bogotá (mayo 2026)
- [ ] Desinstalar GCompris 4.0 del portátil instructor (`sudo apt remove gcompris-qt`)
- [ ] Instalar GCompris 26.0 en portátil instructor (snap o .sh)
- [ ] Instalar GCompris-Teachers 26.0 en portátil instructor
- [ ] Instalar GCompris 26.0 en PC de Milagros (Windows, desde Microsoft Store o gcompris.net)
- [ ] Probar conexión servidor/cliente en red local antes del miércoles
- [ ] Configurar grupo de alumnos y plan de trabajo inicial para Milagros
