#!/usr/bin/env python3
import xml.etree.ElementTree as ET

# Cargar el archivo .gan
tree = ET.parse('/home/leonardo-gutierrez/secretario/plan_trufi_proyecto_2025_2026.gan')
root = tree.getroot()

print("Actualizando tareas de branding...")

tasks_element = root.find('.//tasks')
for task in tasks_element.iter('task'):
    task_id = task.get('id')
    
    # A402 - Branding oficial recibido (HITO)
    if task_id == '505':
        task.set('start', '2026-02-05')
        task.set('duration', '0')  # Es un hito
        task.set('complete', '0')
        print(f"  A402 (Branding): 5 febrero 2026 (hito)")
    
    # A403 - Integración con branding (1 semana después)
    if task_id == '502':
        task.set('start', '2026-02-12')
        task.set('duration', '7')  # 1 semana = 7 días
        task.set('complete', '0')
        print(f"  A403 (Integración): 12 febrero 2026 (7 días)")

# Guardar
tree.write('/home/leonardo-gutierrez/secretario/plan_trufi_proyecto_2025_2026.gan', 
           encoding='UTF-8', xml_declaration=True)

print("\n✅ Archivo actualizado")
