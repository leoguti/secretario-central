# Distritos en área GTFS Trujillo

**Fecha:** 4 de febrero 2026
**Fuente:** OpenStreetMap via Overpass API
**GTFS:** trujillo-gtfsv6.zip

---

## Bounding Box de las rutas

```
min_lat: -8.2240322
max_lat: -7.852793
min_lon: -79.1232817
max_lon: -78.6849698
```

---

## Distritos encontrados (admin_level=8)

| # | Distrito | UBIGEO | Población | OSM ID |
|---|----------|--------|-----------|--------|
| 1 | Trujillo | 130101 | 314,939 | 1968056 |
| 2 | Víctor Larco Herrera | 130111 | 68,506 | 1968062 |
| 3 | La Esperanza | 130105 | 35,028 | 1968014 |
| 4 | El Porvenir | 130102 | 32,756 | 1968000 |
| 5 | Huanchaco | 130104 | 12,555 | 1968006 |
| 6 | Virú | 131201 | 11,295 | 1968061 |
| 7 | Otuzco | 130601 | 8,468 | 1968026 |
| 8 | Laredo | 130106 | 8,462 | 1968015 |
| 9 | Florencia de Mora | 130103 | 7,584 | 1968001 |
| 10 | Moche | 130107 | 6,794 | 1968022 |
| 11 | Chicama | 130202 | 4,348 | 1967993 |
| 12 | Salaverry | 130109 | 3,456 | 1968039 |
| 13 | Sinsicap | 130613 | 2,544 | 1968052 |
| 14 | Salpo | 130611 | 2,464 | 1968040 |
| 15 | Simbal | 130110 | 1,348 | 1968051 |
| 16 | Poroto | 130108 | 1,079 | 1968035 |
| 17 | La Cuesta | 130606 | 297 | 1968013 |
| 18 | Paranday | 130610 | 250 | 1968031 |

**Total:** 18 distritos

---

## Consulta Overpass utilizada

```
[out:json][timeout:120];
relation["boundary"="administrative"]["admin_level"="8"]
  (-8.2240322,-79.1232817,-7.852793,-78.6849698);
out tags;
```

Ejecutar en: https://overpass-turbo.eu/

---

## Consulta para obtener geometrías completas

```
[out:json][timeout:120];
relation["boundary"="administrative"]["admin_level"="8"]
  (-8.2240322,-79.1232817,-7.852793,-78.6849698);
out body;
>;
out skel qt;
```

---

## Notas

- UBIGEO = Código de ubicación geográfica de Perú (INEI)
- Población según datos de OSM (fuente INEI 2017)
- Los distritos principales del área metropolitana de Trujillo son:
  - Trujillo (centro)
  - Víctor Larco Herrera
  - La Esperanza
  - El Porvenir
  - Huanchaco
  - Florencia de Mora
  - Moche
  - Laredo
  - Salaverry
