# Preguntas para definir con Eliana - Proceso Operativo
## Antes de diseñar el chatbot, necesitamos definir COMO funciona el seguimiento

---

## 1. LISTADO DE PACIENTES EN AIRTABLE

- ¿Ya existe el listado en Airtable o hay que crearlo?
- ¿Que datos tienen hoy de cada paciente? (nombre, telefono, fecha examen, diagnostico, etc.)
- ¿De donde salen esos datos? ¿Los ingresan manualmente? ¿Los exportan de algun sistema?
- ¿Quien es el responsable de cargar/actualizar los datos en Airtable?
- ¿Con que frecuencia se actualiza el listado? (despues de cada campana, semanal, etc.)
- ¿Cuantos pacientes tienen actualmente en la base de datos?
- ¿Cuantos pacientes nuevos entran aproximadamente por mes/campana?

---

## 2. QUIEN RECIBE EL SEGUIMIENTO

- ¿Se le escribe a TODOS los pacientes o solo a algunos?
- ¿Hay criterios para decidir a quien se le hace seguimiento? Por ejemplo:
  - Solo a los que recibieron gafas?
  - Solo a ciertos diagnosticos?
  - Solo a mayores de edad?
  - Solo a los que dieron consentimiento?
- ¿Hay pacientes que NO deberian recibir mensajes? (menores, personas sin WhatsApp, etc.)
- ¿El paciente debe dar consentimiento para recibir mensajes? (tema legal - reunion con Christoph sobre consentimiento informado)

---

## 3. CUANDO SE ESCRIBE

- ¿Cuanto tiempo despues de la entrega de gafas se hace el primer contacto?
  - Ejemplo: 3 dias? 7 dias? 15 dias?
- ¿Hay un segundo seguimiento? ¿Un tercero?
  - Ejemplo: 1ra vez a los 7 dias, 2da vez al mes, 3ra vez a los 3 meses?
- ¿Se escribe en algun horario especifico? (solo entre 8am-5pm? cualquier hora?)
- ¿Se escribe algun dia especifico de la semana o cualquier dia?
- ¿Se escribe los fines de semana?

---

## 4. CUANTAS VECES SE ESCRIBE

- Si el paciente NO responde al primer mensaje, ¿se le vuelve a escribir?
- ¿Cuantas veces maximo se intenta contactar a alguien que no responde?
- ¿Cuanto tiempo se espera entre un intento y otro?
- Si el paciente dice "ahora no puedo", ¿se le vuelve a escribir? ¿cuando?
- ¿Hay un limite de mensajes por paciente en total? (para no ser invasivos)

---

## 5. QUE PASA CON LAS RESPUESTAS

- Cuando un paciente responde, ¿quien revisa las respuestas?
- ¿Que pasa si un paciente reporta un problema con sus gafas?
  - ¿Quien lo atiende?
  - ¿Se le llama? ¿Se le agenda una cita?
  - ¿En cuanto tiempo se debe responder?
- ¿Quieren recibir alertas inmediatas cuando hay un problema? (email, WhatsApp a alguien del equipo?)
- ¿Quien es la persona responsable de dar seguimiento a los casos problematicos?

---

## 6. CAMPANAS Y CONTEXTO

- ¿Las campanas son en diferentes ubicaciones/ciudades?
- ¿El seguimiento se hace por campana? (Ej: "pacientes de la campana de Sogamoso del 15 de febrero")
- ¿Se quiere personalizar el mensaje segun la campana o ubicacion?
- ¿Hay diferentes tipos de campana? (ej: campana en colegio vs campana en comunidad)

---

## 7. PROCESO ACTUAL (sin chatbot)

- ¿Hoy hacen algun tipo de seguimiento? ¿Como?
- ¿Llaman por telefono? ¿Escriben por WhatsApp manual?
- ¿Que preguntas hacen actualmente cuando contactan a un paciente?
- ¿Que funciona bien del proceso actual que queremos mantener?
- ¿Que NO funciona del proceso actual que queremos mejorar?

---

## 8. TONO Y LENGUAJE

- ¿Como le hablan a los pacientes? ¿De tu o de usted?
- ¿Los pacientes hablan español o hay comunidades indigenas con otro idioma?
- ¿Hay pacientes que no saben leer? ¿Se deberia considerar mensajes de audio?
- ¿Usan algun saludo especial o marca de GoodVision en los mensajes?

---

## 9. CONSENTIMIENTO INFORMADO (tema pendiente con Christoph)

- ¿El consentimiento se va a manejar por WhatsApp?
- ¿Se envia antes o despues de la campana?
- ¿Es un documento que deben leer/escuchar y confirmar?
- ¿Es un flujo separado del seguimiento o va integrado?

---

## 10. METRICAS / QUE QUIEREN MEDIR

- ¿Que informacion es mas importante para GoodVision de este seguimiento?
- ¿Quieren ver reportes? ¿Con que frecuencia?
- ¿Hay datos especificos que pide la organizacion internacional (Christoph/Alemania)?
- ¿Los datos sirven para reportar a donantes o aliados?

---

## DECISIONES - Reunion con Eliana (2026-02-16)

### Lo que ya se definio:

| # | Pregunta | Respuesta | Estado |
|---|----------|-----------|--------|
| 1 | ¿Quien sube los datos a Airtable? | **Eliana**, manualmente | DEFINIDO |
| 2 | ¿Con que frecuencia se sube? | **Una vez a la semana** | DEFINIDO |
| 3 | ¿A quien se le hace seguimiento? | **Pacientes que recibieron lentes** a traves del programa de GoodVision | DEFINIDO |
| 4 | ¿De que periodo? | **Ultima semana** - para que la gente tenga recordacion cercana | DEFINIDO |
| 5 | ¿Sobre que se pregunta? | Sobre los **lentes** y sobre la **atencion** recibida | DEFINIDO |
| 6 | ¿Cuando se envian los mensajes? | Despues de que Eliana sube la lista semanal | DEFINIDO |
| 7 | ¿Se sube toda la DB o solo los relevantes? | Solo los que corresponde hacerles seguimiento (opcion preferida) O toda la DB con casilla de "producto" para filtrar | POR DEFINIR |

### Pendiente de definir con la jefe:

| # | Pregunta | Notas | Estado |
|---|----------|-------|--------|
| 8 | ¿Alcance temporal exacto? | Eliana no lo ha hablado con la jefe. Propuesta: ultima semana | PENDIENTE JEFE |
| 9 | ¿Horario de envio? | | POR DEFINIR |
| 10 | ¿Reintentos si no responde? | | POR DEFINIR |
| 11 | ¿Quien atiende los problemas reportados? | | POR DEFINIR |
| 12 | ¿Consentimiento previo requerido? | Pendiente reunion Christoph (consentimiento informado) | PENDIENTE CHRISTOPH |
| 13 | ¿Tono: tu o usted? | | POR DEFINIR |
| 14 | ¿Alertas a quien y como? | | POR DEFINIR |

---

## RESUMEN DEL PROCESO (definido con Eliana 2026-02-16)

```
PROCESO SEMANAL:

1. Eliana AGREGA pacientes nuevos a Airtable (lista aditiva, crece cada semana)
   - Solo pacientes que recibieron lentes esa semana por el programa GoodVision

2. El sistema detecta los pacientes NUEVOS (sin marca de contacto)
   y dispara automaticamente el flujo de seguimiento por WhatsApp

3. El chatbot hace las preguntas sobre:
   - Los lentes (como les fue, si estan bien)
   - La atencion recibida

4. El chatbot MARCA en Airtable los pacientes ya contactados
   (campo "estado_seguimiento": pendiente → contactado → completado)

5. Las respuestas se guardan en Airtable

6. Analisis semanal de resultados
```

### Modelo de datos en Airtable (necesario):

El campo clave es **estado_seguimiento** que controla todo el flujo:

| estado_seguimiento | Significado |
|-------------------|-------------|
| pendiente | Eliana acaba de subir al paciente, aun no se le ha escrito |
| enviado | El chatbot envio el mensaje, esperando respuesta |
| completado | El paciente respondio todas las preguntas |
| sin_respuesta | Se intentó contactar pero no respondio (despues de reintentos) |
| opt_out | El paciente pidio no recibir mas mensajes |
| requiere_atencion | El paciente reporto un problema → necesita seguimiento humano |

### Conexion tecnica Airtable → TextIt:
- **Opcion 1:** Airtable Automation - Cuando se crea un nuevo registro, hace webhook a TextIt para iniciar flujo
- **Opcion 2:** TextIt consulta Airtable periodicamente (polling) buscando registros "pendiente"
- **Recomendado:** Opcion 1 (mas inmediato, menos complejo)

### Ventajas de este modelo:
- Lista aditiva: no se pierde historico, la base crece
- Automatico: Eliana solo agrega pacientes, el sistema hace el resto
- Trazabilidad: se sabe exactamente que paso con cada paciente
- Recordacion cercana: se contacta la misma semana que recibieron lentes

### NOTA: Ya existe una estructura en Airtable (revisar que tiene)
