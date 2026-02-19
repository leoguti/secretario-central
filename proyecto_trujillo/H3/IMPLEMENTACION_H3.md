# Implementación H3 - Proyecto Trujillo

**Fecha:** 4 de febrero 2026
**Resolución:** 9 (~360m de borde)

---

## Función de Cálculo

```python
import h3

def calcular_h3(lat: float, lng: float) -> str:
    """Calcula el índice H3 para una coordenada."""
    return h3.latlng_to_cell(lat, lng, 9)
```

**Instalación:** `pip install h3`

---

## Ejemplo

```
ANTES:
{
  "origen_lat": -8.1116,
  "origen_lng": -79.0288,
  "destino_lat": -8.1050,
  "destino_lng": -79.0350,
  "timestamp": "2026-02-04T15:30:00Z"
}

DESPUÉS:
{
  "origen_lat": -8.1116,
  "origen_lng": -79.0288,
  "h3_origen": "89283082837ffff",      ← NUEVO
  "destino_lat": -8.1050,
  "destino_lng": -79.0350,
  "h3_destino": "89283082833ffff",     ← NUEVO
  "timestamp": "2026-02-04T15:30:00Z"
}
```

---

## Documentación

- https://h3geo.org/docs/
- https://uber.github.io/h3-py/api_quick_overview.html
