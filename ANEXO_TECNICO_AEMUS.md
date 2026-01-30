# ANEXO TÉCNICO - PROYECTO AEMUS LIMA

## Arquitectura del Sistema de Movilidad

---

### 1. Visión General

El sistema propuesto para AEMUS consiste en una plataforma de movilidad compuesta por:

- **Aplicación móvil** (iOS/Android) para usuarios finales
- **Backend de planificación** basado en OpenTripPlanner
- **Módulo de tiempo real** para integración con GPS de flota
- **API de integración** con sistema de pagos MOVILIZATE (opcional)

---

### 2. Diagrama de Arquitectura (C4 - Nivel Contexto)

```
┌─────────────────────────────────────────────────────────────────┐
│                         USUARIOS                                 │
│                    (Pasajeros AEMUS)                            │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                   APP MÓVIL AEMUS                               │
│              (iOS / Android - Flutter)                          │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
│  │ Planificador │ │ Tiempo Real  │ │   Pagos      │            │
│  │  de Viajes   │ │  GPS Buses   │ │ (MOVILIZATE) │            │
│  └──────────────┘ └──────────────┘ └──────────────┘            │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                   BACKEND TRUFI                                  │
│                 (Cloud - Administrado)                          │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
│  │ OpenTrip     │ │  GTFS-RT     │ │   API        │            │
│  │ Planner      │ │  Server      │ │  Gateway     │            │
│  └──────────────┘ └──────────────┘ └──────────────┘            │
└─────────────────────┬───────────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  DATOS GTFS  │ │  GPS AEMUS   │ │  MOVILIZATE  │
│  (4 rutas)   │ │ (430 buses)  │ │    API       │
└──────────────┘ └──────────────┘ └──────────────┘
```

---

### 3. Componentes del Sistema

#### 3.1 Aplicación Móvil

| Aspecto | Especificación |
|---------|----------------|
| **Framework** | Flutter (código único iOS/Android) |
| **Lenguaje** | Dart |
| **Licencia** | Open Source (BSD) |
| **Compatibilidad** | Android 6.0+ / iOS 12+ |

**Funcionalidades principales:**
- Búsqueda de origen y destino
- Cálculo de rutas óptimas (hasta 3 opciones)
- Visualización de mapa interactivo
- Ubicación de buses en tiempo real
- Estimación de tiempo de llegada
- Consulta de saldo MOVILIZATE (opcional)

#### 3.2 Backend de Planificación

| Componente | Tecnología | Función |
|------------|------------|---------|
| **Motor de rutas** | OpenTripPlanner 2.x | Cálculo de itinerarios multimodales |
| **Base de datos** | PostgreSQL + PostGIS | Almacenamiento geoespacial |
| **Cache** | Redis | Optimización de consultas frecuentes |
| **API** | REST / GraphQL | Comunicación con app móvil |

#### 3.3 Módulo de Tiempo Real

| Componente | Tecnología | Función |
|------------|------------|---------|
| **Protocolo** | GTFS-Realtime | Estándar para datos en tiempo real |
| **Ingesta** | Conector API GPS AEMUS | Captura posiciones vehiculares |
| **Procesamiento** | Python/Node.js | Transformación a GTFS-RT |
| **Distribución** | WebSocket / Polling | Actualización en app |

---

### 4. Flujo de Datos

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   GPS BUS   │────▶│  API AEMUS  │────▶│  GTFS-RT    │
│  (430 buses)│     │  (existente)│     │  Processor  │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                               ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    GTFS     │────▶│ OpenTrip    │◀────│  GTFS-RT    │
│  (estático) │     │  Planner    │     │   Feed      │
└─────────────┘     └──────┬──────┘     └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  APP MÓVIL  │
                    │   AEMUS     │
                    └─────────────┘
```

---

### 5. Stack Tecnológico

| Capa | Tecnología | Licencia |
|------|------------|----------|
| **App Móvil** | Flutter + Dart | BSD |
| **Mapas** | OpenStreetMap + Mapbox/MapLibre | ODbL / BSD |
| **Motor de Rutas** | OpenTripPlanner | LGPL |
| **Base de Datos** | PostgreSQL + PostGIS | PostgreSQL License |
| **Servidor** | Linux (Ubuntu/Debian) | GPL |
| **Contenedores** | Docker | Apache 2.0 |
| **Cloud** | AWS / DigitalOcean | - |

**Nota:** Todo el stack base es **Open Source**, cumpliendo con estándares internacionales y mejores prácticas de la industria.

---

### 6. Integración con Sistemas AEMUS

#### 6.1 Sistema GPS (430 buses)

**Requisitos de AEMUS:**
- Acceso a API o base de datos del sistema GPS actual
- Frecuencia de actualización: mínimo cada 30 segundos
- Datos requeridos: ID vehículo, latitud, longitud, timestamp, ID ruta

**Formato de intercambio:**
```json
{
  "vehicle_id": "BUS-001",
  "route_id": "RUTA-A",
  "latitude": -12.0464,
  "longitude": -77.0428,
  "timestamp": "2026-01-22T10:30:00Z",
  "speed": 25.5
}
```

#### 6.2 Sistema MOVILIZATE (Opcional)

**Funcionalidades a integrar (sujeto a análisis técnico):**
- Consulta de saldo de tarjeta
- Historial de transacciones
- Recarga desde la app (requiere pasarela de pagos)

**Requisitos:**
- Documentación de API MOVILIZATE
- Credenciales de acceso (ambiente de pruebas y producción)
- Definición de protocolos de seguridad

---

### 7. Seguridad

| Aspecto | Implementación |
|---------|----------------|
| **Comunicaciones** | HTTPS/TLS 1.3 |
| **Autenticación API** | JWT / API Keys |
| **Datos personales** | No se almacenan datos personales de usuarios |
| **Backups** | Automáticos diarios, retención 30 días |
| **Monitoreo** | Alertas 24/7 ante caídas del servicio |

---

### 8. Entregables Técnicos

| Entregable | Formato | Momento |
|------------|---------|---------|
| Archivo GTFS validado | ZIP (TXT estructurados) | Mes 2 |
| APK Android | .apk / .aab | Mes 4 |
| Build iOS | TestFlight / App Store | Mes 4 |
| Documentación API | OpenAPI/Swagger | Mes 4 |
| Manual técnico | PDF | Mes 6 |
| Código fuente | Repositorio Git | Mes 6 |

---

### 9. Propiedad de Datos

| Tipo de Dato | Propiedad | Acceso |
|--------------|-----------|--------|
| GTFS (rutas, paradas) | AEMUS | Público (open data) |
| Datos de uso app | AEMUS | Privado |
| Posiciones GPS | AEMUS | Privado |
| Código fuente app | AEMUS + Trufi | Licencia acordada |

---

*Documento técnico complementario a la propuesta comercial AEMUS Lima - Trufi Association*
