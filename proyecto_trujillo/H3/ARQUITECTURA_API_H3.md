# Arquitectura API H3 - Proyecto Trujillo

**Fecha:** 4 de febrero 2026
**Resolución H3:** 9 (~360m de borde)
**Autor:** Leonardo Gutiérrez

---

## 1. Resumen

Sistema para indexar peticiones de viaje usando celdas hexagonales H3, permitiendo análisis de demanda por zonas en Trujillo.

---

## 2. Flujo General

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              FLUJO DE PETICIÓN                               │
└─────────────────────────────────────────────────────────────────────────────┘

     ┌──────────┐         ┌──────────┐         ┌──────────────────────────────┐
     │          │         │          │         │                              │
     │   APP    │────────▶│   API    │────────▶│         BACKEND              │
     │  MÓVIL   │         │  SERVER  │         │                              │
     │          │         │          │         │  1. Recibe origen/destino    │
     └──────────┘         └──────────┘         │  2. Calcula H3 index         │
          │                                     │  3. Guarda petición          │
          │                                     │  4. Actualiza contadores     │
          │                                     │  5. Retorna respuesta        │
          │                                     │                              │
          │                                     └──────────────┬───────────────┘
          │                                                    │
          │                                                    ▼
          │                                     ┌──────────────────────────────┐
          │                                     │        BASE DE DATOS         │
          │                                     │                              │
          │                                     │  ┌────────────────────────┐  │
          │                                     │  │      PETICIONES        │  │
          │                                     │  │  (registro completo)   │  │
          │                                     │  └────────────────────────┘  │
          │                                     │                              │
          │                                     │  ┌────────────────────────┐  │
          │                                     │  │    CONTADORES_H3       │  │
          │                                     │  │  (agregación rápida)   │  │
          │                                     │  └────────────────────────┘  │
          │                                     │                              │
          └─────────────────────────────────────┴──────────────────────────────┘
```

---

## 3. Cálculo H3

Cuando llega una petición con coordenadas, se calcula el índice H3:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            CÁLCULO H3 INDEX                                  │
└─────────────────────────────────────────────────────────────────────────────┘

                    ENTRADA                              SALIDA
              ┌─────────────────┐                  ┌─────────────────┐
              │                 │                  │                 │
              │  lat: -8.1116   │                  │  h3_index:      │
              │  lng: -79.0288  │ ───────────────▶ │                 │
              │  resolution: 9  │    h3.latlng    │ "89283082837fff"│
              │                 │    _to_cell()    │                 │
              └─────────────────┘                  └─────────────────┘

         Coordenada geográfica              ID único de celda hexagonal
              (cualquiera)                    (global, determinístico)
```

**Importante:** El cálculo es instantáneo y determinístico. La misma coordenada SIEMPRE retorna el mismo H3 index.

---

## 4. Modelo de Datos

### 4.1 Tabla PETICIONES (registro completo)

Guarda TODAS las peticiones con su información completa.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              PETICIONES                                      │
├─────────────────┬──────────────┬────────────────────────────────────────────┤
│ Campo           │ Tipo         │ Descripción                                │
├─────────────────┼──────────────┼────────────────────────────────────────────┤
│ id              │ UUID         │ Identificador único de la petición         │
│ timestamp       │ DATETIME     │ Fecha y hora de la petición                │
│ origen_lat      │ FLOAT        │ Latitud del origen                         │
│ origen_lng      │ FLOAT        │ Longitud del origen                        │
│ origen_h3       │ VARCHAR(15)  │ H3 index del origen (resolución 9)         │
│ destino_lat     │ FLOAT        │ Latitud del destino                        │
│ destino_lng     │ FLOAT        │ Longitud del destino                       │
│ destino_h3      │ VARCHAR(15)  │ H3 index del destino (resolución 9)        │
│ usuario_id      │ VARCHAR      │ ID del usuario (opcional)                  │
│ metadata        │ JSON         │ Datos adicionales                          │
└─────────────────┴──────────────┴────────────────────────────────────────────┘
```

**Uso:** Análisis detallados, filtros complejos, histórico completo.

---

### 4.2 Tabla CONTADORES_H3 (agregación rápida)

Mantiene contadores actualizados en tiempo real.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            CONTADORES_H3                                     │
├─────────────────┬──────────────┬────────────────────────────────────────────┤
│ Campo           │ Tipo         │ Descripción                                │
├─────────────────┼──────────────┼────────────────────────────────────────────┤
│ h3_index        │ VARCHAR(15)  │ ID de la celda H3 (PRIMARY KEY)            │
│ count_origen    │ INTEGER      │ Veces que esta celda fue ORIGEN            │
│ count_destino   │ INTEGER      │ Veces que esta celda fue DESTINO           │
│ count_total     │ INTEGER      │ count_origen + count_destino               │
│ last_updated    │ DATETIME     │ Última actualización                       │
└─────────────────┴──────────────┴────────────────────────────────────────────┘
```

**Uso:** Consultas rápidas de estadísticas por zona.

---

## 5. Proceso de Guardado

Cuando llega una petición, se ejecutan estos pasos:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PROCESO DE GUARDADO                                  │
└─────────────────────────────────────────────────────────────────────────────┘

  PETICIÓN ENTRANTE
         │
         ▼
┌─────────────────────┐
│ 1. CALCULAR H3      │
│                     │
│ origen_h3 = h3(     │
│   origen.lat,       │
│   origen.lng, 9)    │
│                     │
│ destino_h3 = h3(    │
│   destino.lat,      │
│   destino.lng, 9)   │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ 2. GUARDAR EN       │
│    PETICIONES       │
│                     │
│ INSERT INTO         │
│ peticiones (...)    │
│ VALUES (...)        │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ 3. ACTUALIZAR       │
│    CONTADORES       │
│                     │
│ UPSERT origen_h3:   │
│   count_origen += 1 │
│                     │
│ UPSERT destino_h3:  │
│   count_destino += 1│
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ 4. RETORNAR         │
│    RESPUESTA        │
│                     │
│ { id, origen_h3,    │
│   destino_h3, ... } │
└─────────────────────┘
```

---

## 6. Endpoints API

### 6.1 Crear Petición

```
POST /api/peticiones

REQUEST:
{
  "origen": {
    "lat": -8.1116,
    "lng": -79.0288
  },
  "destino": {
    "lat": -8.1050,
    "lng": -79.0350
  }
}

RESPONSE:
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "timestamp": "2026-02-04T15:30:00Z",
  "origen": {
    "lat": -8.1116,
    "lng": -79.0288,
    "h3_index": "89283082837ffff"
  },
  "destino": {
    "lat": -8.1050,
    "lng": -79.0350,
    "h3_index": "89283082833ffff"
  }
}
```

---

### 6.2 Estadísticas por Celda

```
GET /api/stats/celda/{h3_index}

EJEMPLO:
GET /api/stats/celda/89283082837ffff

RESPONSE:
{
  "h3_index": "89283082837ffff",
  "count_origen": 145,
  "count_destino": 89,
  "count_total": 234,
  "last_updated": "2026-02-04T15:30:00Z"
}
```

---

### 6.3 Top Celdas

```
GET /api/stats/top?tipo=origen&limit=10

RESPONSE:
{
  "tipo": "origen",
  "celdas": [
    { "h3_index": "89283082837ffff", "count": 145 },
    { "h3_index": "89283082833ffff", "count": 132 },
    { "h3_index": "89283082831ffff", "count": 98 },
    ...
  ]
}
```

---

### 6.4 Estadísticas con Filtros (desde tabla PETICIONES)

```
GET /api/stats/agregado?fecha=2026-02-04&hora_inicio=08:00&hora_fin=09:00

RESPONSE:
{
  "filtros": {
    "fecha": "2026-02-04",
    "hora_inicio": "08:00",
    "hora_fin": "09:00"
  },
  "origenes": [
    { "h3_index": "89283082837ffff", "count": 45 },
    { "h3_index": "89283082833ffff", "count": 32 },
    ...
  ],
  "destinos": [
    { "h3_index": "89283082831ffff", "count": 38 },
    ...
  ]
}
```

---

### 6.5 Matriz Origen-Destino

```
GET /api/stats/matriz-od?fecha=2026-02-04

RESPONSE:
{
  "fecha": "2026-02-04",
  "pares": [
    {
      "origen_h3": "89283082837ffff",
      "destino_h3": "89283082833ffff",
      "count": 23
    },
    {
      "origen_h3": "89283082837ffff",
      "destino_h3": "89283082831ffff",
      "count": 18
    },
    ...
  ]
}
```

---

## 7. Código de Ejemplo

### 7.1 Python - Función de cálculo H3

```python
import h3

RESOLUTION = 9

def calcular_h3(lat: float, lng: float) -> str:
    """
    Calcula el índice H3 para una coordenada.

    Args:
        lat: Latitud (-90 a 90)
        lng: Longitud (-180 a 180)

    Returns:
        String con el índice H3 (ej: "89283082837ffff")
    """
    return h3.latlng_to_cell(lat, lng, RESOLUTION)
```

---

### 7.2 Python - Procesar petición

```python
from datetime import datetime
import uuid

def procesar_peticion(origen: dict, destino: dict) -> dict:
    """
    Procesa una petición de viaje, calculando H3 indexes.

    Args:
        origen: {"lat": float, "lng": float}
        destino: {"lat": float, "lng": float}

    Returns:
        Petición procesada con H3 indexes
    """
    return {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "origen": {
            **origen,
            "h3_index": calcular_h3(origen["lat"], origen["lng"])
        },
        "destino": {
            **destino,
            "h3_index": calcular_h3(destino["lat"], destino["lng"])
        }
    }
```

---

### 7.3 SQL - Crear tablas

```sql
-- Tabla de peticiones (registro completo)
CREATE TABLE peticiones (
    id UUID PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    origen_lat FLOAT NOT NULL,
    origen_lng FLOAT NOT NULL,
    origen_h3 VARCHAR(15) NOT NULL,
    destino_lat FLOAT NOT NULL,
    destino_lng FLOAT NOT NULL,
    destino_h3 VARCHAR(15) NOT NULL,
    usuario_id VARCHAR(100),
    metadata JSONB
);

-- Índices para búsquedas rápidas
CREATE INDEX idx_peticiones_origen_h3 ON peticiones(origen_h3);
CREATE INDEX idx_peticiones_destino_h3 ON peticiones(destino_h3);
CREATE INDEX idx_peticiones_timestamp ON peticiones(timestamp);

-- Tabla de contadores (agregación rápida)
CREATE TABLE contadores_h3 (
    h3_index VARCHAR(15) PRIMARY KEY,
    count_origen INTEGER DEFAULT 0,
    count_destino INTEGER DEFAULT 0,
    count_total INTEGER DEFAULT 0,
    last_updated TIMESTAMP
);
```

---

### 7.4 SQL - Actualizar contadores

```sql
-- Función para actualizar contador cuando llega petición
-- (ejecutar después de INSERT en peticiones)

-- Actualizar contador de ORIGEN
INSERT INTO contadores_h3 (h3_index, count_origen, count_total, last_updated)
VALUES ('89283082837ffff', 1, 1, NOW())
ON CONFLICT (h3_index) DO UPDATE SET
    count_origen = contadores_h3.count_origen + 1,
    count_total = contadores_h3.count_total + 1,
    last_updated = NOW();

-- Actualizar contador de DESTINO
INSERT INTO contadores_h3 (h3_index, count_destino, count_total, last_updated)
VALUES ('89283082833ffff', 1, 1, NOW())
ON CONFLICT (h3_index) DO UPDATE SET
    count_destino = contadores_h3.count_destino + 1,
    count_total = contadores_h3.count_total + 1,
    last_updated = NOW();
```

---

## 8. Diagrama de Arquitectura Completa

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ARQUITECTURA COMPLETA                                 │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌─────────┐      ┌─────────┐      ┌─────────┐
    │  App    │      │  App    │      │  App    │
    │ Usuario │      │ Usuario │      │ Usuario │
    │    1    │      │    2    │      │    N    │
    └────┬────┘      └────┬────┘      └────┬────┘
         │                │                │
         └────────────────┼────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │                       │
              │      API SERVER       │
              │                       │
              │  ┌─────────────────┐  │
              │  │ POST /peticiones│  │
              │  │ GET /stats/*    │  │
              │  └─────────────────┘  │
              │                       │
              │  ┌─────────────────┐  │
              │  │   H3 LIBRARY    │  │
              │  │  (cálculo)      │  │
              │  └─────────────────┘  │
              │                       │
              └───────────┬───────────┘
                          │
            ┌─────────────┴─────────────┐
            │                           │
            ▼                           ▼
┌───────────────────────┐   ┌───────────────────────┐
│                       │   │                       │
│      PETICIONES       │   │    CONTADORES_H3      │
│    (PostgreSQL)       │   │    (PostgreSQL)       │
│                       │   │                       │
│ • Registro completo   │   │ • Agregación rápida   │
│ • Filtros flexibles   │   │ • Consultas O(1)      │
│ • Histórico           │   │ • Tiempo real         │
│                       │   │                       │
└───────────────────────┘   └───────────────────────┘
            │                           │
            └─────────────┬─────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │                       │
              │      DASHBOARD        │
              │   (Power BI / Web)    │
              │                       │
              │ • Mapa de calor       │
              │ • Top zonas           │
              │ • Matriz O-D          │
              │ • Tendencias          │
              │                       │
              └───────────────────────┘
```

---

## 9. Ventajas de esta Arquitectura

| Aspecto | Beneficio |
|---------|-----------|
| **Velocidad** | Contadores dan respuestas instantáneas |
| **Flexibilidad** | Tabla peticiones permite cualquier filtro |
| **Escalabilidad** | H3 index permite sharding por zona |
| **Análisis** | Matriz O-D lista para Power BI |
| **Histórico** | Todo queda registrado para auditoría |

---

## 10. Próximos Pasos

- [ ] Definir tecnología del backend (Python/FastAPI, Node/Express, etc.)
- [ ] Configurar base de datos PostgreSQL
- [ ] Implementar endpoints básicos
- [ ] Crear triggers para actualización de contadores
- [ ] Conectar con dashboard de visualización

---

## 11. Referencias

- [H3 Documentation](https://h3geo.org/)
- [H3 Python Library](https://uber.github.io/h3-py/)
- [H3 Resolution Table](https://h3geo.org/docs/core-library/restable/)
