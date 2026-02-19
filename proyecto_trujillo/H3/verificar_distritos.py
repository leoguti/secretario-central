#!/usr/bin/env python3
"""
Verifica qué distritos (admin_level=8) realmente intersectan con las rutas GTFS.
"""

import csv
import json
import requests
from collections import defaultdict

# Archivo shapes.txt del GTFS
SHAPES_FILE = "/home/leonardo-gutierrez/secretario/proyecto_trujillo/gtfs_temp/shapes.txt"

def cargar_puntos_rutas():
    """Carga todos los puntos de las rutas desde shapes.txt"""
    puntos = []
    with open(SHAPES_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            puntos.append({
                'lat': float(row['shape_pt_lat']),
                'lon': float(row['shape_pt_lon'])
            })
    print(f"Cargados {len(puntos)} puntos de rutas")
    return puntos

def obtener_distrito_punto(lat, lon):
    """Consulta Overpass para obtener el distrito de un punto específico"""
    query = f"""
    [out:json][timeout:10];
    is_in({lat},{lon})->.a;
    relation(pivot.a)["boundary"="administrative"]["admin_level"="8"];
    out tags;
    """
    try:
        response = requests.post(
            "https://overpass-api.de/api/interpreter",
            data={'data': query},
            timeout=15
        )
        data = response.json()
        if data.get('elements'):
            elem = data['elements'][0]
            return {
                'id': elem['id'],
                'name': elem['tags'].get('name', 'Sin nombre'),
                'ubigeo': elem['tags'].get('pe:ubigeo', ''),
                'population': elem['tags'].get('population', '')
            }
    except Exception as e:
        pass
    return None

def main():
    print("=== Verificando distritos que intersectan con rutas GTFS ===\n")

    puntos = cargar_puntos_rutas()

    # Muestrear puntos (cada 500 para no sobrecargar Overpass)
    paso = max(1, len(puntos) // 200)
    muestra = puntos[::paso]
    print(f"Verificando {len(muestra)} puntos de muestra...\n")

    distritos_encontrados = {}

    for i, punto in enumerate(muestra):
        if i % 20 == 0:
            print(f"Procesando punto {i+1}/{len(muestra)}...")

        distrito = obtener_distrito_punto(punto['lat'], punto['lon'])
        if distrito and distrito['id'] not in distritos_encontrados:
            distritos_encontrados[distrito['id']] = distrito
            print(f"  → Nuevo distrito: {distrito['name']}")

    print(f"\n=== RESULTADO ===")
    print(f"Distritos que intersectan con rutas: {len(distritos_encontrados)}\n")

    # Ordenar por población
    distritos_lista = sorted(
        distritos_encontrados.values(),
        key=lambda x: int(x['population'] or 0),
        reverse=True
    )

    print("| # | Distrito | UBIGEO | Población | OSM ID |")
    print("|---|----------|--------|-----------|--------|")
    for i, d in enumerate(distritos_lista, 1):
        pop = f"{int(d['population']):,}" if d['population'] else "N/A"
        print(f"| {i} | {d['name']} | {d['ubigeo']} | {pop} | {d['id']} |")

    # Guardar IDs para consulta Overpass
    ids = [str(d['id']) for d in distritos_lista]
    print(f"\n=== Consulta Overpass para estos distritos ===")
    print(f"""
[out:json][timeout:120];
(
  relation(id:{','.join(ids)});
);
out body;
>;
out skel qt;
""")

if __name__ == "__main__":
    main()
