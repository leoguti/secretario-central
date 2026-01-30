# 💡 SISTEMA DE ANÁLISIS FINANCIERO PERMANENTE

## 🎯 Visión General

Este no es solo un sistema de "pago de deudas". Es una **plataforma de inteligencia financiera permanente** que evoluciona con las necesidades de la familia Gutiérrez-Pineda.

### **Propósito Multi-fase:**

#### **FASE ACTUAL (2026): Liquidación de Deuda**
- 🔥 Objetivo: Eliminar deuda cara ($20M TC + $50M libre inversión)
- 📊 Herramienta: Optimización de gastos + tracking de progreso
- ⏱️ Duración estimada: 12-24 meses (dependiendo de excedentes)

#### **FASE MEDIA (2027-2028): Construcción de Estabilidad**
- 💰 Objetivo: Fondo de emergencia $20M + gestión hipotecario
- 📊 Herramienta: Balance estructurado + proyecciones
- 🎯 Meta: Independencia financiera básica

#### **FASE FUTURA (2028+): Crecimiento Patrimonial**
- 📈 Objetivo: Inversiones + optimización fiscal + patrimonio
- 📊 Herramienta: Análisis de oportunidades + ROI
- 🏆 Meta: Libertad financiera

---

## 📊 ESTRUCTURA DEL SISTEMA

### **Sheet: "BALANCE FINANCIERO 2026"**

Diseñado para ser la **única fuente de verdad** sobre finanzas del hogar.

---

## 📋 TAB 1: "TRANSACCIONES"

### **Propósito:**
Registro detallado de TODOS los movimientos de dinero (excepto cuentas fijas ya en sheet de Lucía).

### **Columnas:**

| Col | Nombre | Tipo | Descripción | Ejemplo |
|-----|--------|------|-------------|---------|
| A | Fecha | Date | Fecha de la transacción | 2026-01-04 |
| B | Tipo | Dropdown | Ingreso / Gasto / Transferencia | Gasto |
| C | Categoría | Dropdown | Ver tabla de categorías | Comida |
| D | Subcategoría | Text | Detalle opcional | Supermercado |
| E | Concepto | Text | Descripción breve | "Mercado Carulla - Semana" |
| F | Monto | Currency | Valor en pesos | $150.000 |
| G | Método Pago | Dropdown | Efectivo/TC/Débito/Transferencia | TC Davivienda |
| H | Recibo | Link | Link al archivo en Drive | [Ver recibo] |
| I | Fuente | Text | Quién registró | Leonardo / Lucía / IA |
| J | Procesado Por | Email | Email de quien ingresó | leogiga+secretario-ia@gmail.com |
| K | Notas | Text | Observaciones | "Compra del mes" |
| L | Estado | Dropdown | Pendiente/Procesado/Revisado | Procesado |

### **Datos que necesitamos definir:**

#### ❓ **CATEGORÍAS principales (a definir con Lucía):**
- [ ] Lista completa de categorías de gastos
- [ ] Prioridad de cada categoría (Esencial/Optimizable/Discrecional)
- [ ] Meta mensual por categoría (si aplica)

Propuesta inicial:
```
🍽️ COMIDA
  - Supermercado
  - Restaurantes
  - Domicilios
  - Otros alimentos

🚗 TRANSPORTE
  - Gasolina
  - Taxi/Uber
  - Mantenimiento vehículo
  - Parqueadero
  - Otros

🏥 SALUD
  - Medicamentos
  - Consultas médicas
  - Seguros salud
  - Laboratorios

👨‍👩‍👧‍👦 FAMILIA
  - Educación
  - Ropa
  - Actividades
  - Regalos

🎉 ENTRETENIMIENTO
  - Cine/Teatro
  - Suscripciones (Netflix, etc.)
  - Salidas
  - Hobbies

🏠 HOGAR
  - Aseo/Limpieza
  - Reparaciones
  - Mejoras
  - Artículos hogar

💳 DEUDA (Tracking especial)
  - Pago TC Davivienda
  - Abono Libre Inversión Banco 1
  - Abono Libre Inversión Banco 2
  - (Hipotecario ya está en sheet Lucía)

💰 AHORRO/INVERSIÓN
  - Fondo Emergencia
  - Inversiones
  - Ahorros metas específicas

📦 OTROS
  - Sin categorizar
  - Misceláneos
```

#### ❓ **MÉTODOS DE PAGO (a validar):**
- [ ] ¿Qué tarjetas de crédito usan activamente?
- [ ] ¿Qué cuentas bancarias?
- [ ] ¿Usan billeteras digitales (Nequi, Daviplata)?

Propuesta inicial:
```
- TC Davivienda (principal - $20M deuda)
- TC Bancolombia Leo
- TC Pricesmart Leo
- Débito Bancolombia
- Débito Davivienda
- Efectivo
- Nequi
- Daviplata
- Transferencia bancaria
```

#### ❓ **INGRESOS (a definir):**
- [ ] Fuentes de ingreso fijas (salarios)
- [ ] Fuentes variables (freelance, bonos, etc.)
- [ ] Frecuencia de cada ingreso

Necesitamos:
```
- Salario Leonardo: $X mensual (fecha de pago: día X)
- Salario Lucía: $X mensual (fecha de pago: día X)
- Otros ingresos: (describir)
```

---

## 📊 TAB 2: "CUENTAS FIJAS"

### **Propósito:**
Vista consolidada de las cuentas que Lucía gestiona en su sheet. NO duplicar datos, sino IMPORTAR/REFERENCIAR.

### **Columnas:**

| Col | Nombre | Descripción |
|-----|--------|-------------|
| A | Cuenta | Nombre de la cuenta fija |
| B | Valor Mensual | Monto aproximado mensual |
| C | Tipo | Crédito/Servicio/Suscripción/Empleada |
| D | Link | Link a fila específica en sheet de Lucía |
| E | Observaciones | Notas importantes |

### **Fórmula de importación (ejemplo):**
```
=IMPORTRANGE("1PASCuQ7znKod-HHlCQUDz8SYYbAZD3icre9Jv8a9n74","Enero 2026!A:E")
```

#### ❓ **Datos que necesitamos:**
- [ ] ¿Cuál es el total aproximado mensual de cuentas fijas? (gastos recurrentes)
- [ ] ¿Este monto es relativamente estable o varía mucho mes a mes?
- [ ] ¿Hay cuentas que puedan optimizarse o negociarse?

---

## 📈 TAB 3: "RESUMEN MENSUAL"

### **Propósito:**
Dashboard ejecutivo mensual. Vista rápida de la salud financiera.

### **Secciones:**

#### **A) INGRESOS DEL MES**
```
Salario Leonardo:           $ ___________
Salario Lucía:              $ ___________
Otros ingresos:             $ ___________
─────────────────────────────────────────
TOTAL INGRESOS:             $ ___________
```

#### ❓ **Dato necesario:**
- [ ] Monto total de ingresos mensuales promedio

---

#### **B) GASTOS FIJOS (del sheet de Lucía)**
```
Créditos (casa, libre inv):  $ ___________
Tarjetas de crédito:         $ ___________
Servicios (luz, agua, etc.): $ ___________
Celulares:                   $ ___________
Empleadas:                   $ ___________
Otros fijos:                 $ ___________
─────────────────────────────────────────
TOTAL GASTOS FIJOS:          $ ___________
```

#### ❓ **Dato necesario:**
- [ ] Total de gastos fijos mensuales (de sheet Lucía)

---

#### **C) GASTOS VARIABLES (de tab Transacciones)**
```
Comida:                      $ ___________
Transporte:                  $ ___________
Salud:                       $ ___________
Familia:                     $ ___________
Entretenimiento:             $ ___________
Hogar:                       $ ___________
Otros:                       $ ___________
─────────────────────────────────────────
TOTAL GASTOS VARIABLES:      $ ___________
```

---

#### **D) BALANCE Y EXCEDENTE**
```
TOTAL INGRESOS:              $ ___________
- TOTAL GASTOS FIJOS:        $ ___________
- TOTAL GASTOS VARIABLES:    $ ___________
═════════════════════════════════════════
EXCEDENTE/DÉFICIT:           $ ___________
```

#### **E) ASIGNACIÓN DE EXCEDENTE (según fase)**

**Si EXCEDENTE > 0:**

**FASE 1 (Actual): Pago Agresivo Deuda**
```
Destino del excedente:
├─ 10% Fondo Emergencia Mínimo:  $ ___________
└─ 90% Pago Deuda Cara:          $ ___________
   ├─ Prioridad 1: TC Davivienda $ ___________
   └─ Prioridad 2: Libre Inv.    $ ___________
```

**FASE 2 (Futura): Construcción Estabilidad**
```
Destino del excedente:
├─ 50% Fondo Emergencia:         $ ___________
├─ 30% Abono Hipotecario:        $ ___________
└─ 20% Optimización/Extras:      $ ___________
```

#### ❓ **Datos necesarios:**
- [ ] ¿Cuál es el excedente mensual promedio actual?
- [ ] ¿Qué porcentaje prefieren destinar a fondo emergencia vs pago deuda?
- [ ] ¿Meta mensual de pago a TC Davivienda?

---

## 💳 TAB 4: "ESTRATEGIA DEUDA"

### **Propósito:**
Tracking detallado del plan de eliminación de deuda. Motivación visual del progreso.

### **Sección A: Estado Actual de Deudas**

| Deuda | Saldo Inicial | Tasa Interés | Saldo Actual | Pagado | % Progreso | Meta Pago Mensual |
|-------|--------------|--------------|--------------|--------|------------|-------------------|
| TC Davivienda | $20.000.000 | 27% EA | $_______ | $_______ | __% | $_______ |
| Libre Inv. 1 | $25.000.000 | 18% EA | $_______ | $_______ | __% | $_______ |
| Libre Inv. 2 | $25.000.000 | 18% EA | $_______ | $_______ | __% | $_______ |
| **TOTAL DEUDA CARA** | **$70.000.000** | | **$_______** | **$_______** | **__%** | **$_______** |

### **Sección B: Historial de Pagos**

| Mes | TC Davivienda | Libre Inv 1 | Libre Inv 2 | Total Pagado | Saldo Restante | Interés Ahorrado |
|-----|---------------|-------------|-------------|--------------|----------------|------------------|
| Ene 2026 | $_______ | $_______ | $_______ | $_______ | $_______ | $_______ |
| Feb 2026 | $_______ | $_______ | $_______ | $_______ | $_______ | $_______ |
| ... | | | | | | |

### **Sección C: Proyecciones**

**Escenario Actual:**
```
Con pago promedio de $X por mes:
├─ TC Davivienda libre en: __ meses (___/2026)
├─ Libre Inversión libre en: __ meses (___/2027)
└─ Interés total a pagar: $___________
```

**Escenario Optimista (+20% pago):**
```
Con pago promedio de $X por mes:
├─ TC Davivienda libre en: __ meses (___/2026)
├─ Libre Inversión libre en: __ meses (___/2027)
└─ Interés AHORRADO: $___________
```

#### ❓ **Datos necesarios:**
- [ ] Saldo exacto actual de cada deuda
- [ ] Tasa de interés exacta de cada una
- [ ] Pago mínimo requerido de cada una
- [ ] ¿Hay penalidades por pago anticipado?

---

## 💰 TAB 5: "FONDO EMERGENCIA"

### **Propósito:**
Tracking del colchón financiero. Meta: $20 millones.

### **Sección A: Estado Actual**

```
META FINAL:              $20.000.000

FASE 1 (Mínimo):         $ 5.000.000 (1.5 meses gastos)
FASE 2 (Completo):       $20.000.000

──────────────────────────────────────
ACTUAL:                  $ ___________
PROGRESO:                ____%
FALTA:                   $ ___________
```

### **Sección B: Composición del Fondo**

| Instrumento | Monto | % del Total | Liquidez | Rendimiento |
|-------------|-------|-------------|----------|-------------|
| Cuenta Ahorros | $_______ | __% | Inmediata | ~3% EA |
| CDT Corto Plazo | $_______ | __% | 30-90 días | ~7% EA |
| Fondo Liquidez | $_______ | __% | 1-2 días | ~5% EA |
| **TOTAL** | **$_______** | **100%** | | |

### **Sección C: Historial de Aportes**

| Mes | Aporte | Saldo Acumulado | Rendimientos | Meta FASE |
|-----|--------|-----------------|--------------|-----------|
| Ene 2026 | $_______ | $_______ | $_______ | FASE 1 |
| Feb 2026 | $_______ | $_______ | $_______ | FASE 1 |

#### ❓ **Datos necesarios:**
- [ ] ¿Cuánto tienen actualmente en fondo de emergencia?
- [ ] ¿En qué instrumentos está? (cuenta ahorros, CDT, etc.)
- [ ] ¿Cuál es el gasto mensual promedio? (para calcular 1.5 meses)

---

## 📉 TAB 6: "ANÁLISIS POR CATEGORÍA"

### **Propósito:**
Detalle de cada categoría de gasto. Identificar oportunidades de optimización.

### **Estructura por Categoría:**

**Ejemplo: COMIDA**

```
MES ACTUAL: Enero 2026
─────────────────────────────────────────────
Supermercado:           $ _______ (___%)
Restaurantes:           $ _______ (___%)
Domicilios:             $ _______ (___%)
Otros:                  $ _______ (___%)
─────────────────────────────────────────────
TOTAL COMIDA:           $ _______

Promedio últimos 3 meses:   $ _______
Tendencia:                  ↗ ↘ → 
Clasificación:              Esencial

OPORTUNIDADES:
• ¿Reducir restaurantes en 20%? Ahorro: $_______
• ¿Comprar por mayoreo? Ahorro estimado: $_______
```

### **Vista Comparativa Multi-categoría:**

| Categoría | Ene | Feb | Mar | Promedio | vs Promedio | Tipo |
|-----------|-----|-----|-----|----------|-------------|------|
| Comida | $_ | $_ | $_ | $_ | +5% | Esencial |
| Transporte | $_ | $_ | $_ | $_ | -10% | Variable |
| Entretenimiento | $_ | $_ | $_ | $_ | +25% | Discrecional |

#### ❓ **Datos necesarios:**
- [ ] ¿Hay presupuestos deseados por categoría?
- [ ] ¿Qué categorías consideran más importantes de controlar?
- [ ] ¿Hay metas específicas? (ej: "reducir restaurantes 30%")

---

## 📊 TAB 7: "DASHBOARD"

### **Propósito:**
Visualización ejecutiva. Gráficos y KPIs principales.

### **Sección A: KPIs Principales** (Cards visuales)

```
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ BALANCE MES     │  │ DEUDA RESTANTE  │  │ FONDO EMERGENCIA│
│                 │  │                 │  │                 │
│  $ __________   │  │  $ __________   │  │  $ __________   │
│  +/- vs ant.   │  │  -X% vs mes ant.│  │  +X% vs mes ant.│
└─────────────────┘  └─────────────────┘  └─────────────────┘

┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ MESES PARA      │  │ GASTOS DISCR.   │  │ TASA AHORRO     │
│ ELIMINAR DEUDA  │  │ DEL MES         │  │ DEL MES         │
│                 │  │                 │  │                 │
│  __ meses       │  │  $ __________   │  │  ___%           │
│  Meta: 18 meses │  │  -20% vs ant.  │  │  Meta: 15%      │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

### **Sección B: Gráficos**

1. **Línea temporal: Evolución deuda**
   - Eje X: Meses
   - Eje Y: Saldo deuda total
   - Líneas: TC, Libre Inv 1, Libre Inv 2

2. **Barras: Gastos por categoría (mes actual)**
   - Barras ordenadas de mayor a menor
   - Colores: Verde (esencial), Amarillo (variable), Rojo (discrecional)

3. **Pie: Distribución del gasto mensual**
   - Gastos Fijos vs Variables
   - Con % de cada uno

4. **Línea: Balance mensual (últimos 12 meses)**
   - Verde si positivo, Rojo si negativo
   - Línea de tendencia

5. **Barras apiladas: Ingresos vs Gastos (últimos 6 meses)**
   - Barra Ingresos (verde)
   - Barra Gastos Fijos (azul)
   - Barra Gastos Variables (amarillo)
   - Diferencia = Excedente

#### ❓ **Preferencias de visualización:**
- [ ] ¿Qué gráficos son más útiles para ustedes?
- [ ] ¿Qué KPIs quieren ver diariamente?
- [ ] ¿Frecuencia de revisión? (diario/semanal/mensual)

---

## 🎯 TAB 8: "METAS Y OBJETIVOS"

### **Propósito:**
Tracking de metas financieras a corto, mediano y largo plazo.

### **Metas Activas:**

| Meta | Tipo | Monto | Plazo | Progreso | Estado |
|------|------|-------|-------|----------|--------|
| Eliminar TC Davivienda | Deuda | $20M | 12 meses | __% | En curso |
| Fondo Emergencia Mínimo | Ahorro | $5M | 6 meses | __% | En curso |
| Viaje Familiar | Ahorro | $____M | ___/2026 | __% | Planeado |
| Mejora Casa | Proyecto | $____M | ___/2026 | __% | Pendiente |

#### ❓ **Metas a definir:**
- [ ] ¿Hay metas específicas adicionales? (viajes, compras grandes, etc.)
- [ ] ¿Prioridad de cada meta?
- [ ] ¿Cómo se financian? (ahorro mensual, excedentes, etc.)

---

## 🔔 TAB 9: "ALERTAS Y NOTIFICACIONES"

### **Propósito:**
Sistema de alertas proactivo. Notificaciones automáticas.

### **Tipos de Alertas:**

#### **Alertas de Gastos:**
- ⚠️ Categoría excede presupuesto en +20%
- 🔥 Gastos discrecionales > $X en el mes
- 📊 Gasto inusual detectado (>$X en transacción)

#### **Alertas de Deuda:**
- 💳 Saldo TC cerca del límite
- 📅 Fecha de pago próxima (5 días antes)
- 🎯 Oportunidad: Excedente disponible para abono extra

#### **Alertas de Progreso:**
- 🎉 Hito alcanzado (ej: TC reducida en 25%)
- 📈 Fondo emergencia alcanzó nueva fase
- 🏆 Meta mensual de ahorro cumplida

#### ❓ **Configuración de alertas:**
- [ ] ¿Qué alertas son prioritarias?
- [ ] ¿Cómo notificar? (email, Telegram, dashboard)
- [ ] ¿Umbrales específicos? (ej: alerta si gasto >$500k)

---

## 📝 TAB 10: "NOTAS Y DECISIONES"

### **Propósito:**
Bitácora financiera. Registro de decisiones importantes.

### **Formato:**

| Fecha | Categoría | Decisión/Nota | Impacto Estimado | Resultado |
|-------|-----------|---------------|------------------|-----------|
| 2026-01-04 | Estrategia | Inicio plan pago agresivo TC | -$20M en 12 meses | En curso |
| | | | | |

### **Notas de reuniones financieras:**
- Espacio para documentar conversaciones importantes
- Decisiones tomadas en conjunto
- Cambios de estrategia

---

## 🔄 PROCESOS AUTOMATIZADOS

### **Diario:**
- [ ] Procesar recibos nuevos de carpeta Drive
- [ ] Actualizar tab "Transacciones"
- [ ] Recalcular todos los totales
- [ ] Verificar alertas

### **Semanal:**
- [ ] Reporte semanal de gastos por email
- [ ] Resumen de transacciones pendientes de revisión
- [ ] Check de excedente disponible

### **Mensual:**
- [ ] Cerrar mes anterior
- [ ] Generar reporte mensual completo
- [ ] Actualizar proyecciones de deuda
- [ ] Crear nueva pestaña de resumen mensual
- [ ] Email con análisis completo a ambos

### **Trimestral:**
- [ ] Análisis de tendencias
- [ ] Revisión de categorías y metas
- [ ] Ajuste de estrategia si es necesario

---

## ❓ INFORMACIÓN FALTANTE - CHECKLIST

### **URGENTE (para crear el sheet):**
- [ ] Total ingresos mensuales
- [ ] Total gastos fijos mensuales (del sheet de Lucía)
- [ ] Saldo actual de cada deuda
- [ ] Tasa de interés de cada deuda
- [ ] Monto actual de fondo de emergencia

### **IMPORTANTE (para configurar bien):**
- [ ] Categorías definitivas de gastos
- [ ] Presupuestos por categoría (si los hay)
- [ ] Métodos de pago que usan
- [ ] Metas financieras específicas
- [ ] Preferencias de visualización

### **ÚTIL (para optimizar):**
- [ ] Gastos promedio últimos 3 meses por categoría
- [ ] Historial de pagos a deudas (últimos meses)
- [ ] Gastos estacionales conocidos (ej: matrícula escolar)
- [ ] Ingresos extras esperados
- [ ] Proyectos grandes planeados

---

## 🚀 PRÓXIMOS PASOS

1. **Recopilar información faltante** (checklist arriba)
2. **Crear sheet base** con estructura definida
3. **Configurar fórmulas** y cálculos automáticos
4. **Importar datos** del sheet de Lucía (cuentas fijas)
5. **Cargar historial** (si hay datos de meses anteriores)
6. **Script de procesamiento** de recibos
7. **Configurar alertas** y notificaciones
8. **Prueba piloto** 1 mes
9. **Ajustes** según feedback
10. **Operación continua**

---

**Documento creado:** 2026-01-04  
**Estado:** Borrador - Información pendiente  
**Próxima acción:** Completar checklist de información faltante
