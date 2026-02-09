# Notas JourFix - Proyecto Trujillo
**Fecha:** 3 de febrero de 2026
**Reunión:** Seguimiento Proyecto Trujillo

---

## Asistentes
- Oscar Frank (CIMO)
- Equipo de Oscar
- Leonardo Gutiérrez (Trufi)

---

## Temas Discutidos

### 1. Pruebas de la Aplicación
- Oscar y su equipo están trabajando en pruebas del app de Trujillo
- Realizaron pruebas de dos aplicaciones:
  - **TransApp** - Driver app (app para conductores)
  - **App planificadora de rutas** - App de Trufi para usuarios
- Oscar quiere mostrar los resultados de sus pruebas

**Comentarios de las pruebas:**
- Han hecho cotejo de paradas físicas vs paradas registradas en el GTFS
- Detectaron que algunas paradas no están registradas en el GTFS
- **Oscar enviará un correo con las paradas** (faltantes/a revisar)
- **Respuesta (Trufi):** Si no hay ruta, no se pone parada (las paradas dependen de las rutas definidas)

### 2. Problema del PBF (OpenStreetMap)
- Se incluyó el dato completo pero se subió un PBF parcial
- Ese es el problema identificado
- **Acción:** Pedir a Luz que incluya el PBF completo (con la caminata)
- **Conclusión:** Este es el problema principal identificado
- **Leonardo:** Ya se identificó el problema, se entregará mañana (4 feb) una versión mejorada
- **Nota:** El problema que reporta Oscar es específicamente sobre problemas de caminata

### 3. Problemas de Conectividad (Oscar)
- Al hacer consultas, el dispositivo perdía conectividad
- OTP se desconectaba, mostraba errores tipo "intente nuevamente"
- No lograba enviar la ruta
- Posiblemente ocurre en zonas donde no hay rutas definidas
- **Revisar:** ¿Cuál es el mensaje de error cuando se consulta en zonas sin servicio?

### 4. Confusión con Códigos de Rutas
- Se confundían mucho: les salía que tenían que tomar la M05 "en lo mismo"
- Es un tema de cómo están definidas las rutas
- Posiblemente los códigos están repetidos
- Depende de cómo se asignaron los códigos
- **Conclusión:** Es un problema de codificación
- Hay rutas con desviación que tienen el mismo código
- Un mismo código sirve para varios recorridos (causa confusión)
- **Importante:** No es un problema de la app, es un problema de la codificación (datos fuente)

### 5. Aclaración sobre Paradas Faltantes
- Las paradas que no están es porque no hay ruta del GTFS que pase por allí
- Por eso se excluyeron muchas paradas

### 6. Mejora Solicitada: Identificación Visual de Paradas
- **Problema:** No se identifica visualmente la parada en la ruta
- **Solicitud:** Resaltar/destacar la parada en el mapa
- **Prioridad:** Importante - Agregar esta funcionalidad

### 7. Mejora UI: Color Amarillo
- El color amarillo no ayuda mucho, no se ve bien
- **Acción:** Corregir UI, cambiar color

### 8. Búsqueda: Balneario Huanchaco
- Balneario Huanchaco no aparece en la búsqueda
- **Acción:** Revisar/agregar este punto de interés

### 9. Textos en Inglés
- Hay algunos resultados/textos que aparecen en inglés
- **Acción:** Revisar y traducir al español
- **Nota:** La app se basa en la última versión terminada recientemente en Ruanda



---

## Acuerdos y Decisiones



---

## Tareas Pendientes

| Tarea | Responsable | Fecha Límite | Estado |
|-------|-------------|--------------|--------|
|  |  |  |  |

---

## Notas Adicionales



---

*Notas tomadas por:* Leonardo Gutiérrez
*Última actualización:* 2026-02-03
