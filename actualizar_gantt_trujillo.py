#!/usr/bin/env python3
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

# Cargar el archivo .gan
tree = ET.parse('/home/leonardo-gutierrez/secretario/plan_trufi_proyecto_2025_2026.gan')
root = tree.getroot()

# Mapeo de IDs de tareas a su información actualizada
# complete: 0-100, start: fecha real, end: fecha real calculada
tareas_actualizadas = {
    # FASE 0 - Completadas
    '101': {'complete': 100, 'start': '2025-10-28', 'duration': 3, 'end': '2025-10-30'},
    '103': {'complete': 100, 'start': '2025-10-28', 'duration': 1, 'end': '2025-10-28'},
    
    # FASE 1 - Completadas
    '203': {'complete': 100, 'start': '2025-10-27', 'duration': 16, 'end': '2025-11-12'},
    '204': {'complete': 100, 'start': '2025-10-27', 'duration': 16, 'end': '2025-11-12'},
    
    # FASE 2 - Datos GTFS
    '301': {'complete': 100, 'start': '2025-10-29', 'duration': 33, 'end': '2025-12-01'},
    '302': {'complete': 0, 'start': '2025-11-20', 'duration': 10},  # Pendiente
    '303': {'complete': 100, 'start': '2025-11-06', 'duration': 26, 'end': '2025-12-02'},
    '304': {'complete': 100, 'start': '2025-11-13', 'duration': 19, 'end': '2025-12-02'},
    '305': {'complete': 100, 'start': '2025-11-24', 'duration': 0, 'end': '2025-11-24'},  # Acta (no AAR formal)
    '804': {'complete': 100, 'start': '2025-11-24', 'duration': 32, 'end': '2025-12-26'},
    '306': {'complete': 100, 'start': '2025-11-28', 'duration': 0, 'end': '2025-11-28'},  # Decisión
    '307': {'complete': 0, 'start': '2025-12-11', 'duration': 0},  # Cancelada
    '308': {'complete': 100, 'start': '2025-12-08', 'duration': 14, 'end': '2025-12-22'},
    '309': {'complete': 100, 'start': '2025-12-22', 'duration': 28, 'end': '2026-01-19'},  # Rehecha
    '310': {'complete': 0, 'start': '2026-01-09', 'duration': 0},  # Pendiente
    '311': {'complete': 100, 'start': '2025-12-22', 'duration': 0, 'end': '2025-12-22'},  # Validada
    
    # FASE 3 - Backend
    '401': {'complete': 0, 'start': '2025-11-12', 'duration': 0},  # Pendiente
    '402': {'complete': 80, 'start': '2025-11-12', 'duration': 71},  # 80% completado, extendido
    '403': {'complete': 0, 'start': '2025-12-10', 'duration': 5},  # Pendiente (depende de A302)
    '404': {'complete': 0, 'start': '2025-11-12', 'duration': 30},  # No iniciada (RT)
    '405': {'complete': 100, 'start': '2025-11-06', 'duration': 61, 'end': '2026-01-06'},
    '406': {'complete': 0, 'start': '2025-11-10', 'duration': 5},  # Pendiente para abril
    
    # FASE 4 - App
    '501': {'complete': 100, 'start': '2025-12-02', 'duration': 35, 'end': '2026-01-06'},
    '505': {'complete': 0, 'start': '2026-01-12', 'duration': 0},  # Pendiente - Branding bloqueante
    '502': {'complete': 0, 'start': '2026-01-12', 'duration': 5},  # Bloqueada por branding
    '503': {'complete': 0, 'start': '2026-01-12', 'duration': 20},  # No iniciada (RT)
    '504': {'complete': 0, 'start': '2026-02-09', 'duration': 5},  # Pendiente
    
    # FASE 5 - QA
    '603': {'complete': 0, 'start': '2026-02-09', 'duration': 10},  # Pendiente
    '601': {'complete': 0, 'start': '2026-02-23', 'duration': 10},  # Pendiente
    '604': {'complete': 0, 'start': '2026-01-19', 'duration': 0},  # Pendiente
    '605': {'complete': 0, 'start': '2026-03-09', 'duration': 10},  # Pendiente
    
    # FASE 6 - Producción (ajustar fechas: marzo lanzamiento, abril migración)
    '701': {'complete': 0, 'start': '2026-04-01', 'duration': 0},  # Mover a abril
    '702': {'complete': 0, 'start': '2026-04-01', 'duration': 7},  # Mover a abril
    '703': {'complete': 0, 'start': '2026-03-01', 'duration': 7},  # Mover a marzo (publicación)
    '704': {'complete': 0, 'start': '2026-03-10', 'duration': 5},  # Mover a marzo (go-live)
    
    # FASE 7 - Cierre (mantener en abril)
    '801': {'complete': 0, 'start': '2026-04-01', 'duration': 6},
    '802': {'complete': 0, 'start': '2026-04-10', 'duration': 2},
    '803': {'complete': 0, 'start': '2026-04-14', 'duration': 3},
}

print("Actualizando tareas en el archivo .gan...")

# Encontrar todas las tareas y actualizar
tasks_element = root.find('.//tasks')
for task in tasks_element.iter('task'):
    task_id = task.get('id')
    
    if task_id in tareas_actualizadas:
        info = tareas_actualizadas[task_id]
        
        # Actualizar completitud
        if 'complete' in info:
            task.set('complete', str(info['complete']))
            print(f"  Tarea {task_id}: {info['complete']}% completado")
        
        # Actualizar fecha de inicio
        if 'start' in info:
            task.set('start', info['start'])
        
        # Actualizar duración
        if 'duration' in info:
            task.set('duration', str(info['duration']))

# Actualizar descripción del proyecto con nota de actualización
project = root
desc = project.find('description')
if desc is not None:
    current_desc = desc.text if desc.text else ""
    new_desc = current_desc + " | ACTUALIZADO 22-ene-2026: Fechas reales, cambios de alcance (GTFS desde cero, lanzamiento marzo, migración abril)."
    desc.text = new_desc
    print("\nDescripción del proyecto actualizada.")

# Guardar el archivo actualizado
output_file = '/home/leonardo-gutierrez/secretario/plan_trufi_proyecto_2025_2026_ACTUALIZADO.gan'
tree.write(output_file, encoding='UTF-8', xml_declaration=True)

print(f"\n✅ Archivo actualizado guardado en: {output_file}")
print("\nResumen de cambios:")
print(f"  - {sum(1 for t in tareas_actualizadas.values() if t.get('complete') == 100)} tareas marcadas como completadas (100%)")
print(f"  - 1 tarea en progreso (80%)")
print(f"  - Fechas ajustadas según cronograma real")
print(f"  - Lanzamiento movido a marzo 2026")
print(f"  - Migración movida a abril 2026")

