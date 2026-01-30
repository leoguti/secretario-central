# REVISIÓN DOCUMENTO AEMUS - INCONSISTENCIAS DETECTADAS

**Fecha:** 22 de enero de 2026
**Documento:** 2026-01 Propuesta AEMUS Lima - Trufi Association

---

## 🔴 ERRORES CRÍTICOS - MENCIONES DE MÉXICO

### 1. Sección 9.1 - Moneda y facturación
**Ubicación:** Sección 9.1
**Texto actual:**
> "Los valores indicados no incluyen impuestos aplicables en **México** (IVA u otros)."

**Debe decir:**
> "Los valores indicados no incluyen impuestos aplicables en **Perú** (IGV u otros)."

**Nota:** En Perú el impuesto es IGV (Impuesto General a las Ventas), no IVA.

---

### 2. Sección 9.1 - Moneda incompleta
**Ubicación:** Sección 9.1
**Texto actual:**
> "Si el pago se realiza en , se liquidará al tipo de cambio vigente..."

**Problema:** Falta especificar la moneda local (PEN - Soles peruanos)

**Debe decir:**
> "Si el pago se realiza en **PEN (Soles peruanos)**, se liquidará al tipo de cambio vigente..."

---

## 🟠 INCONSISTENCIAS DE PRECIOS

### 3. Precio de renovación anual - DISCREPANCIA
**Ubicación 1:** Sección 4.1.5 - Alojamiento
> "Renovación anual: **€1,500/año**"

**Ubicación 2:** Sección 9.6 - Soporte post-entrega
> "a partir del segundo año, la renovación es **2,500 €/año**"

**Problema:** Hay una diferencia de €1,000 entre las dos secciones.

**Acción:** Unificar el precio. Según las notas (tabla_costos_aemus.md), el precio correcto es **€1,500/año**.

---

## 🟡 REFERENCIAS GENÉRICAS QUE DEBEN AJUSTARSE

### 4. Referencias a "Estado" en lugar de "AEMUS"
**Ubicación:** Sección 7 - Beneficios Estratégicos
> "Se recomienda que el **Estado** involucre a universidades locales..."

**Ubicación:** Glosario - "Aplicación propia"
> "App móvil exclusiva para un cliente (en este caso el **AEMUS**), con identidad visual y control de datos."

**Recomendación:** Mantener consistencia usando "AEMUS" en todo el documento, no "Estado".

---

### 5. Sección 6 - Referencia a "ATU" inconsistente
**Texto actual:**
> "La propuesta considera la posibilidad de recolección de datos en campo, en caso de que las **ATU** (Autoridad de Transporte Urbano) no cuenten con geometrías suficientes."

**Nota:** ATU es correcto para Lima (Autoridad de Transporte Urbano para Lima y Callao). Verificar que esta mención tenga sentido en el contexto de AEMUS que es una asociación de empresas, no una autoridad gubernamental.

---

## 🟢 SECCIÓN 5 - PLAN DE PAGOS (SIN ERRORES)

La sección 5 está correcta:
- 50% - Inicio del proyecto
- 30% - Avance intermedio
- 20% - Entrega final
- Total: 100% ✓

Los hitos están bien definidos y coinciden con el alcance del proyecto.

---

## 📝 ERRORES MENORES DE ORTOGRAFÍA

### 6. Glosario - Error tipográfico
**Texto actual:**
> "Coordinación con **zona de operacións**, operadores y dependencias..."

**Debe decir:**
> "Coordinación con **zonas de operaciones**, operadores y dependencias..."

---

## ✅ RESUMEN DE ACCIONES REQUERIDAS

| # | Prioridad | Sección | Acción |
|---|-----------|---------|--------|
| 1 | 🔴 ALTA | 9.1 | Cambiar "México" por "Perú" e "IVA" por "IGV" |
| 2 | 🔴 ALTA | 9.1 | Agregar "PEN (Soles peruanos)" donde falta la moneda |
| 3 | 🟠 MEDIA | 4.1.5 / 9.6 | Unificar precio renovación: €1,500/año |
| 4 | 🟡 BAJA | 7 | Cambiar "Estado" por "AEMUS" |
| 5 | 🟢 MENOR | Glosario | Corregir "operacións" → "operaciones" |

---

## 🔍 VERIFICACIÓN CONTRA NOTAS

Comparando con `TAREA_19_ENERO_AEMUS.md` y `tabla_costos_aemus.md`:

- ✅ Costos del paquete base coinciden (€17,344)
- ✅ Desglose de componentes coincide
- ✅ Integración MOVILIZATE como opcional (€5,000 - €9,000)
- ✅ Contacto correcto (Ing. Luis Edgardo Ramírez García)
- ⚠️ Precio renovación: notas dicen €1,500/año, documento tiene discrepancia

---

*Generado automáticamente para revisión en reunión con Edgardo*
