# Estrategia H3 - Proyecto Trujillo

**Fecha:** 4 de febrero 2026
**Resolución elegida:** 9 (~360m de borde)

---

## Resumen

Implementar indexación geoespacial H3 para identificar la zona de origen y destino de cada petición de viaje en la app móvil de Trujillo.

---

## ¿Qué es H3?

H3 es un sistema de indexación geoespacial hexagonal desarrollado por Uber. Divide el mundo en celdas hexagonales con IDs únicos globales.

### Características clave

- **IDs globales únicos**: Cada celda tiene un ID único en todo el planeta
- **Cálculo instantáneo**: No requiere base de datos, es un cálculo matemático
- **Sin pre-generación**: No necesitas crear las celdas previamente

---

## Resolución 9 (elegida)

| Métrica | Valor |
|---------|-------|
| Área promedio | 0.10 km² |
| Borde aproximado | ~360 m |
| Celdas por km² | ~10 |

**Justificación:** Balance entre granularidad (identificar zonas específicas) y cantidad manejable de celdas para análisis.

### Comparación de resoluciones

| Resolución | Borde aprox | Uso típico |
|------------|-------------|------------|
| 7 | ~2.6 km | Zonas/distritos |
| 8 | ~960 m | Vecindarios |
| **9** | **~360 m** | **Bloques (elegida)** |
| 10 | ~135 m | Manzanas |
| 11 | ~50 m | Edificios |

---

## Arquitectura

### Flujo de petición

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   App Móvil │────▶│   API       │────▶│   Backend   │
│  (origen,   │     │  /peticion  │     │  + H3 calc  │
│   destino)  │     │             │     │             │
└─────────────┘     └─────────────┘     └─────────────┘
                                               │
                                               ▼
                                        ┌─────────────┐
                                        │  Respuesta  │
                                        │  + h3_origen│
                                        │  + h3_destino│
                                        └─────────────┘
```

### Endpoint API

```
POST /api/peticion
Content-Type: application/json

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
```

### Respuesta

```json
{
  "id": "pet_12345",
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
  },
  "ruta": { ... }
}
```

---

## Implementación

### Python (backend)

```python
import h3

RESOLUTION = 9

def get_h3_index(lat: float, lng: float) -> str:
    """Obtiene el índice H3 para una coordenada."""
    return h3.latlng_to_cell(lat, lng, RESOLUTION)

def process_peticion(origen: dict, destino: dict) -> dict:
    """Procesa una petición agregando índices H3."""
    return {
        "origen": {
            **origen,
            "h3_index": get_h3_index(origen["lat"], origen["lng"])
        },
        "destino": {
            **destino,
            "h3_index": get_h3_index(destino["lat"], destino["lng"])
        }
    }
```

### JavaScript/TypeScript (si se necesita en frontend)

```typescript
import { latLngToCell } from 'h3-js';

const RESOLUTION = 9;

function getH3Index(lat: number, lng: number): string {
  return latLngToCell(lat, lng, RESOLUTION);
}
```

---

## Área de Interés (opcional)

El área de interés NO es necesaria para el cálculo de H3, pero puede usarse para:

1. **Validación**: Rechazar peticiones fuera de Trujillo
2. **Visualización**: Mostrar mapa de celdas activas
3. **Análisis**: Estadísticas por zona

### Definir área de interés

```python
import h3

# Polígono de Trujillo (definir coordenadas)
TRUJILLO_POLYGON = [
    (-8.05, -79.10),  # NO
    (-8.05, -78.95),  # NE
    (-8.15, -78.95),  # SE
    (-8.15, -79.10),  # SO
    (-8.05, -79.10),  # cerrar
]

# Obtener todas las celdas dentro del polígono
def get_celdas_trujillo():
    return h3.polygon_to_cells(TRUJILLO_POLYGON, RESOLUTION)

# Validar si una celda está en Trujillo
def is_in_trujillo(h3_index: str) -> bool:
    celdas_validas = get_celdas_trujillo()
    return h3_index in celdas_validas
```

---

## Casos de Uso

### 1. Análisis de demanda por zona

```python
from collections import Counter

# Contar peticiones por celda de origen
origen_counts = Counter(p["origen"]["h3_index"] for p in peticiones)

# Top 10 zonas con más demanda
top_zonas = origen_counts.most_common(10)
```

### 2. Matriz origen-destino

```python
# Crear matriz O-D por celdas H3
od_matrix = {}
for p in peticiones:
    key = (p["origen"]["h3_index"], p["destino"]["h3_index"])
    od_matrix[key] = od_matrix.get(key, 0) + 1
```

### 3. Visualización en mapa

```python
import h3

def celda_to_geojson(h3_index: str) -> dict:
    """Convierte celda H3 a GeoJSON para visualizar."""
    boundary = h3.cell_to_boundary(h3_index)
    return {
        "type": "Feature",
        "properties": {"h3_index": h3_index},
        "geometry": {
            "type": "Polygon",
            "coordinates": [boundary]
        }
    }
```

---

## Dependencias

### Python
```bash
pip install h3
```

### JavaScript/TypeScript
```bash
npm install h3-js
```

---

## Próximos pasos

- [ ] Definir polígono exacto del área de interés de Trujillo
- [ ] Integrar cálculo H3 en API existente
- [ ] Almacenar h3_index en cada petición
- [ ] Crear dashboard de análisis por zonas

---

## Referencias

- [Documentación oficial H3](https://h3geo.org/)
- [H3 Python API](https://uber.github.io/h3-py/)
- [H3 JavaScript API](https://github.com/uber/h3-js)
- [Visualizador H3](https://wolf-h3-viewer.glitch.me/)
