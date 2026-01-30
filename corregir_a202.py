#!/usr/bin/env python3
import xml.etree.ElementTree as ET

# Cargar el archivo .gan
tree = ET.parse('/home/leonardo-gutierrez/secretario/plan_trufi_proyecto_2025_2026.gan')
root = tree.getroot()

print("Corrigiendo A202...")

tasks_element = root.find('.//tasks')
for task in tasks_element.iter('task'):
    task_id = task.get('id')
    
    # A202 - Compatibilidad GTFS-gestor (preliminar) - PENDIENTE
    if task_id == '303':
        task.set('complete', '0')
        print(f"  ⚠️ A202: Marcada como PENDIENTE (0%)")

# Guardar
tree.write('/home/leonardo-gutierrez/secretario/plan_trufi_proyecto_2025_2026.gan', 
           encoding='UTF-8', xml_declaration=True)

print("\n✅ Archivo actualizado")
