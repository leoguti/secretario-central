# 📊 PROCESO DE GESTIÓN DE FINANZAS PERSONALES

## 🎯 Filosofía del Sistema

**"Todo va a una carpeta en bruto, luego organizamos"**

No perdemos tiempo organizando en el momento. Subimos todo rápido y dejamos que el sistema procese y organice después.

## 💰 Contexto Financiero y Estrategia

### **Panorama de Deuda Actual:**
- **Tarjeta de crédito**: $20 millones (~25-30% EA) - PRIORIDAD MÁXIMA
- **Créditos libre inversión**: $50 millones (1,4% mensual ≈18% EA) - PRIORIDAD ALTA
- **Crédito hipotecario**: $200 millones (12% EA) - LARGO PLAZO
- **Total deuda**: $270 millones

### **Plan Estratégico (Lucía):**

**FASE 1: Liquidez mínima**
- ✅ Fondo de emergencia: 1-1.5 meses de gastos
- 🎯 Evitar quedar expuestos sin colchón

**FASE 2: Pago agresivo de deuda cara**
- 🔥 Prioridad 1: Eliminar tarjeta crédito ($20M)
- 🔥 Prioridad 2: Eliminar libre inversión ($50M)
- 💡 "Retorno" implícito > cualquier inversión conservadora

**FASE 3: Fondo de emergencia completo**
- 💰 Meta: $20 millones en instrumentos líquidos
- ⏳ Solo cuando quede únicamente hipotecario

**FASE 4: Optimización**
- 🏠 Evaluar abonos a hipotecario vs inversiones largo plazo
- 📈 Con estabilidad financiera establecida

### **Principio clave:**
> "Invertir mientras existan deudas caras NO optimiza el costo total"

---

## 📂 Estructura de Carpetas

```
Google Drive/Finanzas/
├── recibos/                           ← 📥 AQUÍ SUBEN TODO (carpeta en bruto)
│   └── 2026-01/          
├── procesados/                        ← ✅ Script mueve aquí después de procesar
│   └── 2026-01/
│       ├── comida/
│       ├── transporte/
│       ├── servicios/
│       └── otros/
├── 2025 CUENTAS GUTIERREZ PINEDA      ← 🔒 INTOCABLE (shortcut - Lucía gestiona)
└── BALANCE FINANCIERO 2026            ← 📊 Nuevo sheet con reportes y análisis
    ├── Tab "Transacciones"            → Registro detallado de gastos variables
    ├── Tab "Cuentas Fijas"            → Importa/sync con sheet de Lucía
    ├── Tab "Resumen Mensual"          → Balance: Ingresos - Gastos totales
    ├── Tab "Estrategia Deuda"         → Tracking del plan de pago agresivo
    ├── Tab "Fondo Emergencia"         → Progreso hacia meta $20M
    └── Tab "Dashboard"                → Gráficos y KPIs
```

---

## 🔄 FLUJO DE TRABAJO

### **FASE 1: SUBIR (Tú y tu esposa)**

**Regla simple: Todo a `/recibos/YYYY-MM/`**

- 📷 Foto de recibo desde celular → Drive móvil → `/recibos/2026-01/`
- 📄 PDF de factura → Subir a `/recibos/2026-01/`
- 💬 Gasto sin recibo → *(Fase 2: Bot Telegram)*

**No importa:**
- ❌ Nombres de archivos desordenados
- ❌ Duplicados
- ❌ Fotos borrosas (intentaremos procesar)
- ❌ Mezcla de tipos de gastos

**Solo importa:** ✅ Que esté en `/recibos/`

---

### **FASE 2: PROCESAR (Sistema automático)**

**El script revisa `/recibos/` y hace:**

1. **🔍 Leer archivo** (PDF/imagen)
2. **🧠 Extraer datos:**
   - Fecha
   - Monto
   - Establecimiento/concepto
   - Categoría (inteligente)
3. **📝 Escribir en Google Sheet "BALANCE FINANCIERO 2026"** 
   - Tab "Transacciones"
   - Identificado como: `leogiga+secretario-ia@gmail.com`
4. **📦 Mover a `/procesados/YYYY-MM/categoria/`**
5. **✅ Renombrar:** `2026-01-04_150.00_Oxxo.pdf`
6. **📊 Actualizar reportes automáticos:**
   - Balance mensual
   - Excedente disponible para pago de deuda
   - Progreso hacia metas

**Ejecución:**
- Opción A: Corre cada noche automático (cron)
- Opción B: Ejecutar manualmente cuando quieras
- Opción C: *(Fase 3: Bot responde cuando subes)*

---

### **FASE 3: REVISAR Y TOMAR DECISIONES**

**Dashboard muestra:**
- 💰 **Balance del mes**: Ingresos - Gastos totales
- 🔥 **Excedente disponible**: Para pago agresivo de deuda
- 📊 **Tracking de deudas**: Progreso en eliminar TC y libre inversión
- 🏦 **Fondo de emergencia**: Progreso hacia $20M
- 📈 **Tendencias de gasto**: Por categoría

**Decisiones informadas:**
- ¿Cuánto destinar este mes a TC?
- ¿Estamos cumpliendo plan de pago?
- ¿Hay gastos a optimizar?

---

## 📋 CATEGORÍAS AUTOMÁTICAS

El sistema aprenderá y categorizará con enfoque en **control de gastos**:

| Concepto detectado | → Categoría | Impacto en estrategia |
|-------------------|-------------|----------------------|
| Oxxo, Supermercado, Mercado | 🍽️ Comida | Gasto esencial - optimizable |
| Uber, Taxi, Gasolina, DiDi | 🚗 Transporte | Variable - revisar alternativas |
| CFE, Telmex, Agua, Gas | 💡 Servicios | Fijo - ya en sheet de Lucía |
| Farmacia, Doctor, Hospital | 🏥 Salud | Esencial - parte de emergencias |
| Renta, Mantenimiento | 🏠 Hogar | Fijo - ya en sheet de Lucía |
| Regalo, Mamá, Papá | 🎁 Regalos | Discrecional - optimizable |
| Cine, Restaurante, Salida | 🎉 Entretenimiento | Discrecional - reducir en Fase 2 |
| Pago TC, Abono deuda | 💳 Pago Deuda | PRIORIDAD - tracking especial |
| Ahorro, Inversión | 💰 Fondo Emergencia | Meta $20M |
| (resto) | 📦 Otros | Revisar mensualmente |

**El sistema mejora con el tiempo:** Si corriges una categoría en el Sheet, aprende para la próxima.

### **KPIs Clave a Monitorear:**

1. **Gastos discrecionales** (Entretenimiento + Regalos + Otros)
   - Meta: Minimizar en Fase 2 (pago agresivo)
   
2. **Gastos optimizables** (Comida + Transporte)
   - Buscar reducción sin afectar calidad de vida
   
3. **Excedente mensual**
   - Ingresos - Gastos Fijos - Gastos Variables = Disponible para deuda

4. **Velocidad de pago de deuda**
   - ¿Cuándo eliminamos TC?
   - ¿Cuándo eliminamos libre inversión?

---

## 🎯 VENTAJAS DE ESTE PROCESO

✅ **Cero fricción:** Subes y olvidas  
✅ **Ambos participan:** Sin coordinación complicada  
✅ **Organización automática:** El sistema ordena  
✅ **Histórico completo:** Todo en un lugar  
✅ **Consultas rápidas:** Sheet siempre actualizado  

---

## 🔒 POLÍTICA CRÍTICA: SHEETS EXISTENTES

### **Sheet "2025 CUENTAS GUTIERREZ PINEDA"**

**🚫 PROHIBIDO MODIFICAR**

**Razones:**
- ✅ Usado por esposa desde 2019 (7 años de historial)
- ✅ Contiene cuentas FIJAS/RECURRENTES (créditos, servicios, etc.)
- ✅ Ella hace los PAGOS desde ahí
- ✅ Contiene info sensible (contraseñas, referencias)
- ✅ Flujo de trabajo establecido

**Regla estricta:**
- ✅ **Lectura**: PERMITIDA (para análisis, reportes, consultas)
- ❌ **Escritura**: PROHIBIDA (nunca modificar sin autorización explícita)
- ❌ **NO agregar filas/columnas**
- ❌ **NO cambiar fórmulas**
- ❌ **NO modificar formato**

**División clara de responsabilidades:**

| Sheet Existente (INTOCABLE) | Nuevo Sheet (IA escribe aquí) |
|------------------------------|--------------------------------|
| 🔒 Cuentas fijas/recurrentes | 📝 Gastos variables |
| 🔒 Créditos y préstamos | 📝 Supermercado |
| 🔒 Tarjetas de crédito | 📝 Gasolina/Transporte |
| 🔒 Servicios (luz, agua, internet) | 📝 Restaurantes |
| 🔒 Celulares | 📝 Farmacia/Salud |
| 🔒 Empleadas domésticas | 📝 Regalos |
| 🔒 Tu esposa gestiona | 📝 Sistema IA gestiona |

**En caso de duda:** Preguntar primero, no modificar.

---

## 🚀 COMANDOS ÚTILES (cuando estén listos)

```bash
# Procesar recibos manualmente
python3 procesar_recibos.py

# Ver resumen del mes
python3 resumen_mes.py

# Generar reporte
python3 generar_reporte.py --mes 2026-01
```

---

## 📌 NOTAS IMPORTANTES

- 📱 **Drive móvil:** Instalar app en ambos celulares
- 🔔 **Notificaciones:** Opcional activar para saber cuando el otro sube
- 🔒 **Privacidad:** Carpeta compartida solo entre ustedes
- 💾 **Backup:** Google Drive ya tiene respaldo automático

---

## 🛠️ ROADMAP

### ✅ Fase 1 (Actual)
- [x] Estructura de carpetas en Drive
- [x] Shortcut a sheet existente (sin modificar)
- [ ] Crear "BALANCE FINANCIERO 2026" con tabs:
  - [ ] Transacciones (IA escribe)
  - [ ] Resumen Mensual (cálculos)
  - [ ] Estrategia Deuda (tracking plan Lucía)
  - [ ] Fondo Emergencia (progreso a $20M)
  - [ ] Dashboard (visualización)
- [ ] Script de procesamiento básico

### 🔄 Fase 2 (Próxima)
- [ ] Bot Telegram para comandos texto
- [ ] OCR mejorado con IA
- [ ] Categorización inteligente
- [ ] Alertas de gastos discrecionales excesivos

### 🎯 Fase 3 (Futuro)
- [ ] Sincronización automática con sheet de Lucía (importación)
- [ ] Proyecciones: "A este ritmo, TC libre en X meses"
- [ ] Recomendaciones automáticas de optimización
- [ ] Reportes mensuales automáticos por email

---

---

## 📚 DOCUMENTOS RELACIONADOS

- **ANALISIS_SHEET_EXISTENTE.md**: Análisis detallado del sheet actual
- **POLITICAS_TRABAJO.md**: Políticas generales del sistema (incluye política de emails)

---

**Última actualización:** 2026-01-04  
**Carpeta Drive:** https://drive.google.com/drive/folders/1yKx1kfJsJAO_iC_6K0_2DTubWaGXM8Q2  
**Sheet existente (NO tocar):** https://docs.google.com/spreadsheets/d/1PASCuQ7znKod-HHlCQUDz8SYYbAZD3icre9Jv8a9n74/
