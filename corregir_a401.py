#!/usr/bin/env python3
import xml.etree.ElementTree as ET

# Cargar el archivo .gan
tree = ET.parse('/home/leonardo-gutierrez/secretario/plan_trufi_proyecto_2025_2026.gan')
root = tree.getroot()

print("Corrigiendo A401...")

tasks_element = root.find('.//tasks')
for task in tasks_element.iter('task'):
    task_id = task.get('id')
    
    # A401 - Construcción de aplicación
    if task_id == '501':
        task.set('start', '2025-12-02')
        task.set('duration', '35')  # Hasta 6 enero
        task.set('complete', '100')
        print(f"  ✅ A401: 2 dic 2025 - 6 ene 2026 (35 días, 100% completada)")

# Guardar
tree.write('/home/leonardo-gutierrez/secretario/plan_trufi_proyecto_2025_2026.gan', 
           encoding='UTF-8', xml_declaration=True)

print("\n✅ Archivo actualizado")
