# 🎙️ Sistema de Captura de Transcripts de Google Meet

**Fecha creación:** 21 enero 2026  
**Propósito:** Capturar en tiempo real los captions de reuniones en Google Meet (especialmente útil para reuniones en inglés)

---

## 📋 PROBLEMA ORIGINAL

Necesitaba capturar los captions/subtítulos de Google Meet para:
- Seguir reuniones en inglés en tiempo real
- Tener transcript completo de las conversaciones
- Poder revisar lo que se dijo después

**Problema:** Google Meet muestra captions pero NO permite copiar el texto (no se puede seleccionar).

---

## 🔍 INVESTIGACIÓN DE SOLUCIONES

### Extensiones evaluadas:

1. **Meet-Script** (RutvijDv/Meet-Script)
   - ⭐ 52 stars
   - ❌ Desactualizada (2021)
   - ✅ Descarga PDF
   - ❌ Sin tracking de speakers ni timestamps

2. **GMeet Transcription Extension** (Tgcohce/gmeet-transcription-extension) ✅ **ELEGIDA**
   - 🆕 Actualizada (Nov 2024)
   - ✅ Tracking de speakers
   - ✅ Timestamps
   - ✅ Estado persistente
   - ✅ Descarga .txt
   - 📍 **Repo:** https://github.com/Tgcohce/gmeet-transcription-extension

---

## 🛠️ INSTALACIÓN

### 1. Descargar extensión:

```bash
cd /tmp
git clone https://github.com/Tgcohce/gmeet-transcription-extension.git
```

### 2. Instalar en Chrome:

1. Ir a: `chrome://extensions/`
2. Activar **"Modo de desarrollador"** (arriba derecha)
3. Click **"Cargar extensión sin empaquetar"**
4. Seleccionar carpeta: `/tmp/gmeet-transcription-extension`
5. **Pin** la extensión (icono de puzzle en toolbar)

---

## ⚙️ MODIFICACIONES REALIZADAS

### Problema 1: Selectores DOM desactualizados

**Error:** Extensión no capturaba texto (Google Meet cambió su HTML)

**Solución:** Actualizar selectores en `content.js`:

```javascript
// ANTES (no funcionaba):
const subtitleDiv = parentContainer.querySelector('div[jsname="tgaKEf"]');

// DESPUÉS (funciona):
const subtitleDiv = parentContainer.querySelector('div.ygicle');
```

### Problema 2: Auto-save no funcionaba

**Error:** Content scripts no pueden hacer downloads automáticos sin interacción del usuario.

**Solución:** Implementar auto-download desde el popup cada 15 segundos.

**Archivo modificado:** `popup.js`

```javascript
// Auto-download cada 15 segundos mientras graba
autoDownloadInterval = setInterval(() => {
  autoDownloadTranscript();
}, 15000);
```

### Problema 3: Script se inyectaba múltiples veces

**Error:** Cada "Start" inyectaba el script de nuevo → variables duplicadas

**Solución:** Agregar protección contra múltiples inyecciones:

```javascript
// Prevent multiple injections
if (window.gmeetTranscriptRunning) {
  console.log("Transcript capture already running!");
} else {
  window.gmeetTranscriptRunning = true;
  // ... resto del código
}
```

### Problema 4: Auto-refresh en popup

**Agregado:** Popup se actualiza cada 10 segundos mostrando transcript en tiempo real

```javascript
// Auto-refresh every 10 seconds
refreshInterval = setInterval(() => {
  chrome.storage.local.get(["recording"], (data) => {
    if (data.recording) {
      updateTranscriptDisplay();
    }
  });
}, 10000);
```

---

## 📁 UBICACIÓN DE ARCHIVOS

### Extensión modificada:
```
/tmp/gmeet-transcription-extension/
├── content.js          (modificado - selectores + protección)
├── popup.js            (modificado - auto-download + refresh)
├── popup.html          (sin cambios)
├── background.js       (sin cambios)
└── manifest.json       (sin cambios)
```

### Transcripts descargados:
```
~/Descargas/gmeet_transcript_live*.txt
```

**Nota:** Chrome crea archivos numerados si ya existe uno:
- `gmeet_transcript_live.txt`
- `gmeet_transcript_live (1).txt`
- `gmeet_transcript_live (2).txt`
- etc.

### Scripts de monitoreo:
```
~/secretario/monitor_meet_live.sh       (monitor con reporte de cambios)
~/secretario/watch_transcript.sh        (watch simple)
```

---

## 🚀 CÓMO USAR EL SISTEMA

### Paso 1: Entrar a Google Meet

1. Unirse a reunión
2. **Activar captions/subtítulos:** Click en **CC** (abajo en controles)
3. Verificar que se vean los captions en pantalla

### Paso 2: Iniciar captura

1. **Click en icono** de la extensión (arriba en Chrome)
2. **Click "Start"** en el popup
3. **IMPORTANTE:** Dejar el **popup abierto** (puede minimizarlo pero NO cerrarlo)
   - El auto-download solo funciona mientras el popup está abierto

### Paso 3: Monitorear en tiempo real (opcional)

**Opción A - Watch simple (recomendado):**
```bash
watch -n 2 -d 'tail -50 "$(ls -t ~/Descargas/gmeet_transcript_live*.txt | head -1)"'
```

**Opción B - Monitor con reportes:**
```bash
~/secretario/monitor_meet_live.sh
```

**Opción C - Ver en consola Chrome:**
- Presionar **F12** en pestaña del Meet
- Ver pestaña **Console**
- Verás líneas como: `[Speaker Name]: texto capturado`

### Paso 4: Finalizar

1. **Click "Stop"** en popup
2. **Click "Download"** (opcional - ya hay auto-saves)
3. Los archivos quedan en `~/Descargas/`

---

## 💡 COMANDOS ÚTILES

### Ver transcript más reciente:
```bash
cat "$(ls -t ~/Descargas/gmeet_transcript_live*.txt | head -1)"
```

### Monitorear cambios en tiempo real:
```bash
watch -n 2 -d 'tail -50 "$(ls -t ~/Descargas/gmeet_transcript_live*.txt | head -1)"'
```

### Ver todos los transcripts del día:
```bash
ls -lth ~/Descargas/gmeet_transcript_live*.txt
```

### Limpiar transcripts viejos:
```bash
rm ~/Descargas/gmeet_transcript_live*.txt
```

### Ver última modificación de archivo:
```bash
stat -c "Última mod: %y" ~/Descargas/gmeet_transcript_live.txt
```

---

## ⚠️ PROBLEMAS COMUNES Y SOLUCIONES

### ❌ No captura nada

**Causas:**
1. Captions no activados en Meet
2. Popup cerrado (auto-download no funciona)
3. Nadie está hablando

**Solución:**
- Verificar **CC** activo en Meet
- Abrir popup de extensión
- Verificar que hay audio/personas hablando

### ❌ Error "Identifier already declared"

**Causa:** Script inyectado múltiples veces sin refrescar página

**Solución:**
1. Recargar extensión: `chrome://extensions/` → 🔄
2. **Refrescar página del Meet (F5)** ← IMPORTANTE
3. Reactivar captions
4. Click "Start"

### ❌ Archivo no se actualiza

**Causa:** Popup cerrado

**Solución:**
- Abrir popup de extensión
- Dejar abierto (puede minimizar)

### ❌ No encuentra archivo en watch

**Causa:** Espacios en nombre de archivo generan error

**Solución:**
Usar comando con comillas:
```bash
watch -n 2 -d 'tail -50 "$(ls -t ~/Descargas/gmeet_transcript_live*.txt | head -1)"'
```

---

## 🎯 MEJORAS IMPLEMENTADAS

1. ✅ **Auto-download cada 15 segundos** (mientras popup abierto)
2. ✅ **Auto-refresh popup cada 10 segundos** (ver progreso en tiempo real)
3. ✅ **Protección contra inyección múltiple** del script
4. ✅ **Selectores DOM actualizados** para Google Meet 2026
5. ✅ **Timestamps en cada línea** capturada
6. ✅ **Identificación de speakers** automática

---

## 📊 FORMATO DEL TRANSCRIPT

**Ejemplo:**
```
[2026-01-21T21:34:54.749Z] Your Presentation:
Left after an X-ray has ejected. An electron will be taken...

[2026-01-21T21:34:58.079Z] Your Presentation:
independent particles, they talk to each other, right?

[2026-01-21T21:35:02.483Z] Speaker Name:
Another person speaking here...
```

Cada entrada incluye:
- `[Timestamp ISO 8601]` - Momento exacto de captura
- `Speaker Name:` - Quién está hablando
- `Texto capturado` - Lo que dijo

---

## 🔄 WORKFLOW COMPLETO TÍPICO

```
1. Entrar a Google Meet
2. Activar captions (CC)
3. Click extensión → "Start"
4. Dejar popup abierto (minimizado OK)
5. [Opcional] En terminal: watch -n 2 -d 'tail -50 "$(ls -t ~/Descargas/gmeet_transcript_live*.txt | head -1)"'
6. Al terminar: "Stop" → transcript final en ~/Descargas/
```

---

## 📝 NOTAS IMPORTANTES

- ✅ **Funciona con:** Google Meet (Chrome)
- ✅ **Requiere:** Captions activados en Meet
- ✅ **Formato salida:** Plain text (.txt)
- ✅ **Frecuencia auto-save:** 15 segundos
- ✅ **Popup:** Debe estar abierto para auto-download
- ⚠️ **Múltiples archivos:** Chrome crea copias numeradas si archivo existe
- 🔒 **Privacidad:** Todo local, nada se sube a internet

---

## 🎓 CASOS DE USO

### Para reuniones en inglés:
1. Entender mejor lo que se dice en tiempo real
2. No perderse detalles técnicos
3. Tener registro para revisar después

### Para documentación:
1. Capturar decisiones técnicas
2. Extraer action items
3. Crear minutas de reunión

### Para aprendizaje:
1. Ver videos educativos con transcript
2. Poder buscar conceptos específicos
3. Copiar definiciones importantes

---

## 🔗 RECURSOS

- **Extensión base:** https://github.com/Tgcohce/gmeet-transcription-extension
- **Extensión modificada:** `/tmp/gmeet-transcription-extension/`
- **Documentación:** Este archivo
- **Scripts:** `~/secretario/monitor_meet_live.sh`

---

## ✨ VENTAJAS DEL SISTEMA

1. 🚀 **Tiempo real:** Ve el texto mientras hablan
2. 📝 **Completo:** No se pierde nada de lo que se dice
3. 🔍 **Buscable:** Texto plano = fácil de buscar después
4. 💾 **Persistente:** Archivos guardados localmente
5. 🔒 **Privado:** Nada sale de tu computadora
6. ⚡ **Automático:** Auto-download cada 15 seg
7. 🎯 **Preciso:** Usa captions nativos de Google Meet

---

## 📅 HISTORIAL DE CAMBIOS

**21 Enero 2026:**
- ✅ Instalación inicial de extensión
- ✅ Fix selectores DOM (div.ygicle)
- ✅ Implementación auto-download cada 15 seg
- ✅ Auto-refresh popup cada 10 seg
- ✅ Protección contra inyección múltiple
- ✅ Comandos watch para monitoreo
- ✅ Scripts de monitoreo automatizado
- ✅ Documentación completa

---

## 🚀 PRÓXIMOS PASOS POTENCIALES

Ideas para mejorar (no implementadas aún):

- [ ] Integración con AI para resúmenes automáticos
- [ ] Detección automática de action items
- [ ] Traducción automática del transcript
- [ ] Indexación para búsqueda rápida
- [ ] Integración con sistema de notas (Obsidian/Notion)
- [ ] Notificaciones cuando se mencionen palabras clave
- [ ] Export a diferentes formatos (PDF, MD, JSON)

---

**Creado por:** Leonardo Gutiérrez (con asistencia de AI)  
**Última actualización:** 21 enero 2026, 21:39  
**Archivo:** `~/secretario/CAPTURA_TRANSCRIPTS_MEET.md`