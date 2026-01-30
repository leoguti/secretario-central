# 📋 Estado Actual del Proyecto

**Fecha:** 2026-01-05

## 🎯 Objetivo del Sistema

**Secretario Personal y Familiar** - Asistente inteligente que centraliza:
1. 💼 **Trabajo profesional** (correos, proyectos, resúmenes)
2. 💰 **Finanzas familiares** (gastos, control de deudas, presupuesto)
3. 📅 **Eventos y notificaciones**

---

## 👥 Usuarios

- **Leonardo**: Usuario principal (trabajo + finanzas)
- **Lucía** (esposa): Finanzas + gestión del hogar
- **2 hijos**: Reportar gastos familiares

---

## ✅ Lo que ESTÁ Funcionando

### Trabajo Profesional
- ✅ Flask app básica (`app.py`)
- ✅ Lectura de Gmail vía API (`central/gmail_client.py`)
- ✅ Base de datos SQLite para eventos (`data/secretario.db`)
- ✅ Ingesta de correos a BD (`central/gmail_ingest.py`)
- ✅ Resúmenes con OpenAI (`central/resumen.py`)
- ✅ Integración con Calendar (`central/calendar_client.py`)

### Finanzas Familiares
- ✅ Documentación completa del proceso (`cuentas/PROCESO_FINANZAS.md`)
- ✅ Análisis del sheet existente de Lucía (`cuentas/ANALISIS_SHEET_EXISTENTE.md`)
- ✅ Estructura de Google Drive definida
- ✅ Carpeta `/Finanzas/recibos/` para subir archivos
- ✅ Cuenta de Textit + número WhatsApp activos

---

## 🔄 En Desarrollo (Priorizar)

### DECISIONES PENDIENTES

**1. ¿Usar SQLite para finanzas o solo Google Sheets?**
- ❓ Respuesta: **Solo Google Sheets** (más familiar para familia)

**2. ¿Crear sheet nuevo o agregar al de Lucía?**
- ❓ Pendiente de decidir con Lucía
- Opción A: Sheet separado "BALANCE FINANCIERO 2026"
- Opción B: Nueva pestaña en sheet existente

**3. ¿Qué implementar primero?**
- ❓ Opciones:
  - A) WhatsApp → Transcripción → Google Sheets
  - B) Fotos de recibos → OCR → Google Sheets
  - C) Notificaciones de Gmail → WhatsApp

---

## 📊 Información Faltante (para finanzas)

### Urgente
- [ ] Total ingresos mensuales de la familia
- [ ] Total gastos fijos mensuales (del sheet de Lucía)
- [ ] Saldo actual de cada deuda (TC, libre inversión)
- [ ] Tasa de interés de cada deuda
- [ ] Monto actual fondo de emergencia

### Importante
- [ ] Categorías definitivas de gastos
- [ ] Presupuestos por categoría (si los hay)
- [ ] Métodos de pago que usan (tarjetas, cuentas)
- [ ] Metas financieras específicas

---

## 🚀 Próximos Pasos Sugeridos

### FASE 1: Definir Arquitectura Finanzas (Esta semana)
1. [ ] Decidir: Sheet nuevo vs pestaña en sheet de Lucía
2. [ ] Recopilar información faltante (checklist arriba)
3. [ ] Definir flujo: WhatsApp → Textit → Drive → Script → Sheet
4. [ ] Decidir si usar servidor 24/7 o batch local (1-2 veces/día)

### FASE 2: Implementar Procesamiento Básico
1. [ ] Script que lee audios de Drive
2. [ ] Integración con Whisper API (transcripción)
3. [ ] Parser de formato: "500 mil gasolina carro Leonardo"
4. [ ] Escritura en Google Sheets
5. [ ] Mover archivo procesado a `/procesados/`

### FASE 3: Integración WhatsApp
1. [ ] Configurar webhook de Textit → Google Drive
2. [ ] Familia envía mensaje → guarda en Drive automático
3. [ ] Probar flujo completo end-to-end

### FASE 4: OCR y Optimización
1. [ ] Procesamiento de fotos de recibos
2. [ ] OCR con Google Vision API o similar
3. [ ] Categorización inteligente con OpenAI
4. [ ] Dashboard de visualización

---

## 🧹 Limpieza Realizada

### Archivos Movidos a `experimentos/`
- ✅ Scripts de WhatsApp con ADB (no se usan)
- ✅ Scripts de text-to-speech (pruebas)
- ✅ Screenshots de pruebas
- ✅ Otros scripts de experimentos

### Documentación Actualizada
- ✅ README.md simplificado y enfocado
- ✅ .gitignore actualizado
- ✅ Estructura de carpetas organizada

---

## 🔗 Links Importantes

- **Drive Finanzas**: https://drive.google.com/drive/folders/1yKx1kfJsJAO_iC_6K0_2DTubWaGXM8Q2
- **Sheet de Lucía**: https://docs.google.com/spreadsheets/d/1PASCuQ7znKod-HHlCQUDz8SYYbAZD3icre9Jv8a9n74/

---

## 💬 Preguntas para Leonardo

**Para poder continuar necesito que me respondas:**

1. **Sheet de finanzas:**
   - ¿Creo uno nuevo o agregamos pestaña al de Lucía?
   - ¿Ya hablaste con ella sobre el sistema?

2. **WhatsApp/Textit:**
   - ¿Prefieres usar Textit (que ya tienes) o buscar alternativa?
   - ¿Recuerdas el número asociado a Textit?

3. **Prioridad:**
   - ¿Qué es más urgente implementar primero?
     - A) Procesamiento de mensajes de voz
     - B) Procesamiento de fotos de recibos
     - C) Notificaciones de correos importantes

4. **Servidor:**
   - ¿Tienes presupuesto para droplet DigitalOcean (~$6-12/mes)?
   - ¿O prefieres ejecutar batch local (cuando tu PC esté prendida)?

---

**Última actualización:** 2026-01-05 13:30
