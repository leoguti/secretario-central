# ESTADO DEL PROYECTO TRUJILLO - Actualización 22 de Enero 2026

**Proyecto**: CIMO 3 – Aplicación Móvil de Planificación de Viajes (Trujillo)  
**Cliente**: Trufi Association e.V. / GIZ  
**Contrato a nombre de**: Leonardo Gutiérrez (persona natural)  
**Fecha de análisis**: 22 de enero de 2026  
**Analizado con**: Oscar Frank (oscar.frank.rb@gmail.com)

---

## 📊 RESUMEN EJECUTIVO

| Métrica | Valor |
|---------|-------|
| **Fecha inicio real** | 28 octubre 2025 |
| **Tareas completadas** | 10 de 37 |
| **Tareas en progreso** | 1 (API-AN 80%) |
| **Tareas pendientes** | 26 |
| **Progreso general** | ~30% |
| **Fecha lanzamiento acordada** | Marzo 2026 (en nube) |
| **Fecha migración municipal** | Abril 2026 |

---

## ✅ TAREAS COMPLETADAS

### FASE 0 - Arranque (COMPLETADA)
- ✅ **A001** Kick-off y canales → **28 oct 2025**
- ✅ **A002** Plan de trabajo validado → **28 oct 2025**

### FASE 1 - Preparación técnica (COMPLETADA)
- ✅ **A101** Definición API-AN → **12 nov 2025**
- ✅ **A102** Definición requisitos SITR → **12 nov 2025**

### FASE 2 - Datos GTFS (MAYORMENTE COMPLETADA)
- ✅ **A201** Revisión de fuentes → **1 dic 2025**
  - 29 oct: Enviadas fuentes iniciales
  - 24 nov: Recibidas fuentes oficiales
  - 1 dic: Enviado reporte
  
- ✅ **A203** Definición codificación con autoridad → **2 dic 2025**
  - **Decisión clave**: Usar plan de optimización/regulador, NO rutas Trufi previas

- ✅ **A204** Elaboración AAR v1 → **2 dic 2025**

- ✅ **A205** AAR validado [HITO] → **24 nov 2025**
  - **CAMBIO**: NO se hizo AAR formal, se recibió **acta** definiendo cambio de alcance
  
- ✅ **A206** Revisión de paraderos → **26 dic 2025**
  - 24 nov: Centro
  - 26 dic: Otras zonas
  - ⚠️ Aún faltan paraderos por recibir

- ✅ **A207** Evaluación toma de campo → **28 nov 2025**
  - **Decisión**: NO realizar toma de campo (por cambio a plan regulador)

- ❌ **A208** Toma de datos en campo → **NO REALIZADA** (cancelada)

- ✅ **A209** Subida a OSM + revisión topológica → **22 dic 2025**

- ✅ **A210** Consolidación feed GTFS → **19 ene 2026**
  - Primera versión: 22 dic 2025
  - **Rehacer completo**: Por problema de paraderos recibidos tarde
  - Versión final: 19 ene 2026

- ✅ **A212** Validación MobilityData [HITO] → **22 dic 2025**
  - Validado inicialmente 22 dic 2025
  - Revalidado con cada actualización (última: 19 ene 2026)

### FASE 3 - Backend (PARCIALMENTE COMPLETADA)
- ✅ **A305** Montaje en nube → **6 ene 2026**
  - Entregado: APK + OTP web para pruebas
  - Correo a Oscar: 6 enero 2026

### FASE 4 - App Móvil (PARCIALMENTE COMPLETADA)
- ✅ **A401** Construcción aplicación → **6 ene 2026**
  - **Nota**: Se hizo con GTFS nuevo (desde cero), no con GTFS previo como planeado

---

## 🔄 TAREAS EN PROGRESO

- 🔄 **A302** Desarrollo API-AN → **80% completado**
  - **Extendido** por requerimiento extra
  - Primera versión funcional disponible

---

## ❌ TAREAS PENDIENTES

### FASE 2 - Datos GTFS
- ❌ **A202** Compatibilidad GTFS-gestor (preliminar) → **PENDIENTE**
- ❌ **A211** Compatibilidad GTFS-gestor (final) → **PENDIENTE**

### FASE 3 - Backend
- ❌ **A301** Formato gestor confirmado [HITO] → **PENDIENTE**
  - Se hará después de pruebas con gestor
- ❌ **A303** Pruebas internas API-AN → **PENDIENTE**
  - Depende de completar A302
- ❌ **A304** Desarrollo SITR (RT) → **NO INICIADA**
- ❌ **A306** Preparación migración servidor municipal → **PENDIENTE**
  - Programada para abril

### FASE 4 - App Móvil
- ⚠️ **A402** Branding oficial recibido [HITO] → **PENDIENTE** 🔴 **BLOQUEANTE**
- ⚠️ **A403** Integración GTFS + Branding → **BLOQUEADA** (esperando branding)
- ❌ **A404** Integración tiempo real (SITR) → **NO INICIADA**
- ❌ **A405** Builds internas QA → **PENDIENTE**

### FASE 5 - QA
- ❌ **A501** Pruebas SITR con gestor → **PENDIENTE**
- ❌ **A502** QA end-to-end → **PENDIENTE**
- ❌ **A503** Validación API-AN (Power BI) [HITO] → **PENDIENTE**
- ❌ **A504** Piloto controlado → **PENDIENTE**

### FASE 6 - Producción
- ❌ **A601** Infraestructura municipal operativa [HITO] → **PENDIENTE** (abril)
- ❌ **A602** Migración a servidores municipales → **PENDIENTE** (abril)
- ❌ **A603** Publicación en tiendas → **PENDIENTE** (marzo)
- ❌ **A604** Go-Live → **PENDIENTE** (marzo)

### FASE 7 - Cierre
- ❌ **A701** Documentación final → **PENDIENTE** (abril)
- ❌ **A702** Transferencia técnica → **PENDIENTE** (abril)
- ❌ **A703** Entrega código y migración cuentas → **PENDIENTE** (abril)

---

## 🚨 CAMBIOS CRÍTICOS DE ALCANCE

### 1. **GTFS desde Cero (no previsto)**

**Original**:
- Usar rutas existentes de Trufi → ajustar y generar GTFS

**Real**:
- Crear GTFS **completamente desde cero** basado en plan de optimización/regulador
- NO usar GTFS previo de Trufi
- Mayor complejidad y tiempo requerido

**Impacto**: +3 semanas aproximadamente

**Documento**: Acta recibida 24 nov 2025

---

### 2. **Retraso en Entrega de Paraderos**

**Problema**:
- Información de paraderos recibida en múltiples entregas tardías
- Centro: 24 nov 2025
- Otras zonas: 26 dic 2025
- Aún faltan paraderos

**Consecuencia**:
- GTFS tuvo que rehacerse completamente
- Primera versión: 22 dic 2025
- Versión rehecha: 19 ene 2026

**Impacto**: +4 semanas de retraso

---

### 3. **Cambio en Estrategia de Despliegue**

**Original**:
- Lanzamiento directo en servidores municipales (abril)

**Nuevo (acordado 20 ene 2026)**:
- **Marzo 2026**: Lanzamiento con infraestructura en la nube
- **Abril 2026**: Migración a servidores municipales

**Razón**: Permitir lanzamiento más temprano sin esperar infraestructura municipal

**Impacto**: Acelera go-live en ~1 mes

---

### 4. **No Toma de Datos en Campo**

**Decisión**: 28 nov 2025

**Razón**: Por usar plan de optimización/regulador en lugar de levantamiento de campo

**Implicación crítica**:
- App se lanzará con datos teóricos del plan regulador
- NO validados en campo operativo real
- Ajustes posteriores requerirán fase adicional

**Riesgo**:
- Rutas pueden no funcionar correctamente en práctica
- Expectativas deben gestionarse con municipalidad

---

## 🔴 BLOQUEADORES ACTUALES

### 1. **Branding Oficial** (CRÍTICO)
- **Estado**: No recibido
- **Planificado**: 12 ene 2026
- **Días de retraso**: 10 días
- **Bloquea**: A403 (Integración app con branding)
- **Impacto en lanzamiento marzo**: ALTO

### 2. **Formato Gestor de Flotas** (MEDIO)
- **Estado**: No confirmado
- **Bloquea**: Todo el desarrollo SITR/RT
- **Impacto**: Si RT es requerido para marzo, proyecto en riesgo

### 3. **Paraderos Faltantes** (BAJO)
- **Estado**: Información incompleta
- **Impacto**: Posibles ajustes posteriores al GTFS

---

## 📅 CRONOGRAMA ACORDADO (Actualizado 20 ene 2026)

### Marzo 2026
- ✅ Recibir branding oficial (URGENTE)
- ✅ Integrar branding en app
- ✅ Builds finales
- ✅ Publicación en Play Store / App Store
- ✅ **Presentaciones/demos del proyecto**
- ✅ **Go-Live con infraestructura en nube**

### Abril 2026
- ✅ Preparación migración
- ✅ Migración a servidores municipales
- ✅ Documentación final
- ✅ Transferencia técnica
- ✅ Entrega de código

---

## 📋 TAREAS PRIORITARIAS (Próximas 2 Semanas)

### URGENTE (Esta semana - 22-26 ene)
1. **Obtener branding oficial** → Sin esto no hay lanzamiento en marzo
2. **Finalizar API-AN** (del 80% al 100%)
3. **Enviar cronograma actualizado a Oscar** (comprometido para viernes 24 ene)

### IMPORTANTE (Próxima semana - 29 ene - 2 feb)
4. **Integrar branding en app** (apenas lo reciban)
5. **Builds de prueba con branding**
6. **Coordinar con Oscar presentaciones marzo**

---

## �� ANÁLISIS DE RIESGO

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| **Branding no llega a tiempo** | ALTA | CRÍTICO | Escalar con Oscar/GIZ inmediatamente |
| **RT/SITR no listo para marzo** | MEDIA | MEDIO | Confirmar si es requerido o condicional |
| **Paraderos incompletos** | MEDIA | BAJO | Lanzar con lo disponible, actualizar después |
| **Infraestructura municipal no lista abril** | BAJA | BAJO | Ya acordado lanzar en nube primero |
| **Validaciones campo post-lanzamiento** | ALTA | MEDIO | Gestionar expectativas con municipalidad |

---

## 💡 RECOMENDACIONES

### Inmediatas
1. **Escalar tema branding** con Oscar/GIZ como prioridad #1
2. **Confirmar alcance RT** para marzo (¿condicional o mandatorio?)
3. **Preparar presentaciones** para demos marzo
4. **Actualizar GanttProject** con toda esta información

### Corto Plazo
5. **Plan B de branding**: ¿Trufi puede crear branding temporal?
6. **Coordinar accesos Play Store/App Store** para publicación
7. **Definir fechas exactas presentaciones marzo**

### Mediano Plazo
8. **Documentar limitaciones datos** para presentaciones
9. **Plan de actualización post-campo** (si se hace validación después)
10. **Coordinar con IT municipal** para migración abril

---

## 📌 CONTACTOS CLAVE

- **Oscar Frank** (CIMO - Líder Componente 03): oscar.frank.rb@gmail.com
- **Williams Ventura** (GIZ)
- **Débora Gonçalves** (LOGIT): debora.goncalves@logiteng.com
- **Janaina Lima** (LOGIT): janaina.lima@logiteng.com

---

## 📎 DOCUMENTOS RELACIONADOS

- Plan de Trabajo original: https://docs.google.com/document/d/1s1qUFAEnjGWgzyEcA8VIBuEuek-mnNeH5jic_hAkhj0/
- Cronograma GanttProject: `plan_trufi_proyecto_2025_2026.gan`
- Notas JourFix 20 ene: `notas_jourfix_trujillo_2026-01-20.md`
- Correo entrega APK: 6 enero 2026 a oscar.frank.rb@gmail.com

---

**Documento preparado por**: Leonardo Gutiérrez  
**Última actualización**: 22 de enero de 2026, 21:20  
**Próxima revisión**: Después de recibir branding oficial

---

## 🔄 HISTÓRICO DE ACTUALIZACIONES

- **22 ene 2026**: Documento inicial basado en revisión completa con Claude
