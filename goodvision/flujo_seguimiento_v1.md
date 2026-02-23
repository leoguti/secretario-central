# Flujo de Seguimiento Post-Entrega de Lentes - GoodVision Colombia
## Version: 1.1 - Actualizado 2026-02-16

---

## Objetivo del flujo
Contactar pacientes despues de la entrega de lentes para:
1. Verificar que los lentes estan bien (PRIORIDAD - Christoph)
2. Conocer la experiencia del paciente
3. Detectar problemas tempranos
4. Recopilar feedback sobre las campanas

---

## Proceso semanal

1. **Eliana agrega** pacientes nuevos a Airtable (los que recibieron lentes esa semana)
2. **El sistema detecta** los nuevos automaticamente (estado = "pendiente")
3. **Se envia** el mensaje de consentimiento por WhatsApp
4. **El chatbot** hace las preguntas (5 pasos, ~3 minutos)
5. **Las respuestas** se guardan en Airtable
6. **Si hay problemas** → alerta para seguimiento humano
7. **Analisis semanal** de resultados

---

## Campo de control en Airtable: estado_seguimiento

| estado_seguimiento | Significado | Como llego ahi |
|---|---|---|
| pendiente | Nuevo, sin contactar | Eliana lo subio |
| enviado | Se le envio mensaje, esperando | El chatbot envio el primer mensaje |
| completado | Respondio todas las preguntas | Termino el flujo |
| sin_respuesta | No respondio en 4 dias (3 intentos) | Vencio el tiempo |
| opt_out | Dijo "No deseo participar" | Eligio opcion 2 en consentimiento |
| requiere_atencion | Reporto problema con lentes | Necesita seguimiento humano |

---

## FLUJO PRINCIPAL: Seguimiento de lentes

---

### PASO 0: Consentimiento informado

**Trigger:** Airtable detecta nuevo paciente (estado = "pendiente")
**Accion:** Cambiar estado a "enviado" y enviar mensaje:

```
Hola {nombre}, somos GoodVision Colombia.

Usted recibio lentes a traves de nuestro programa y queremos
hacerle un breve seguimiento por WhatsApp.

Antes de comenzar, necesitamos su autorizacion:

- Le enviaremos preguntas cortas sobre sus lentes y la atencion
  que recibio
- Sus respuestas son voluntarias y confidenciales
- Sus datos solo seran usados por GoodVision Colombia para mejorar
  el servicio
- Puede dejar de participar en cualquier momento respondiendo
  "SALIR"

¿Acepta participar en este seguimiento?
1. Si, acepto participar
2. No deseo participar
```

**Si responde 1 (Si):** → ir a PASO 1

**Si responde 2 (No):**
```
Entendido {nombre}, respetamos su decision. No le enviaremos
mas mensajes sobre este tema.

Si en algun momento necesita ayuda con sus lentes o tiene alguna
consulta, puede escribirnos a este numero con gusto.

¡Le deseamos lo mejor! - GoodVision Colombia
```
→ Cambiar estado a "opt_out" en Airtable → [FIN]

**Si responde algo que no es 1 ni 2:**
```
Disculpe {nombre}, no logramos entender su respuesta.

Por favor responda con el numero de su opcion:
1. Si, acepto participar
2. No deseo participar
```

**Si vuelve a responder algo invalido (segundo intento):**
```
No pudimos procesar su respuesta. Si desea participar en el
seguimiento, puede escribirnos "SI" en cualquier momento.

¡Que tenga un buen dia! - GoodVision Colombia
```
→ Registrar en Airtable como "sin_respuesta" → [FIN]

---

### ESTRATEGIA DE REINTENTOS (si no responde al consentimiento)

**Dia 1:** Se envia el mensaje de consentimiento → esperar 24 horas

**Dia 2 - Recordatorio (solo si no respondio):**
```
Hola {nombre}, le escribimos ayer de parte de GoodVision Colombia.
Queriamos saber como le fue con sus lentes.

Si desea participar, solo responda:
1. Si, acepto participar
2. No deseo participar
```
→ Esperar 48 horas mas

**Dia 4 - Mensaje final (solo si no respondio al recordatorio):**
```
Hola {nombre}, GoodVision Colombia. No queremos incomodarle,
este sera nuestro ultimo mensaje.

Si en algun momento desea contarnos como le fue con sus lentes,
puede escribirnos a este numero cuando guste.

¡Le deseamos lo mejor!
```
→ Cambiar estado a "sin_respuesta" en Airtable → No se vuelve a escribir → [FIN]

**Resumen reintentos:**
- Maximo 3 mensajes en total (original + 2 reintentos)
- Dia 1 → Dia 2 (24h) → Dia 4 (48h mas)
- Despues del dia 4: no se insiste mas

---

### PASO 1: Saludo e inicio de preguntas

```
¡Gracias {nombre}! Le haremos unas preguntas cortas,
no tomara mas de 3 minutos.
```

---

### PASO 2: Estado de los lentes (PREGUNTA CLAVE)

```
¿Como le ha ido con sus lentes nuevos? ¿Ve bien con ellos?
1. Si, veo muy bien
2. Mas o menos, tengo algunas molestias
3. No, no veo bien con ellos
4. No los he usado todavia
```

**Si responde 1 (Si, veo muy bien):** → ir a PASO 3

**Si responde 2 (Mas o menos):**
```
Lamentamos escuchar eso. ¿Que tipo de molestia tiene?
1. Me duele la cabeza cuando los uso
2. Veo borroso con ellos
3. Me molestan en la nariz o las orejas
4. Otro problema
```

**Si responde 4 (Otro problema):**
```
Por favor describanos brevemente que problema tiene con sus lentes.
```
→ Capturar respuesta abierta

```
Gracias por contarnos. Vamos a revisar su caso y alguien
de nuestro equipo se comunicara con usted pronto para ayudarle.
```
→ Crear alerta en Airtable: "REQUIERE ATENCION"
→ ir a PASO 3

**Si responde 3 (No veo bien):**
```
Entendemos su preocupacion. Es importante que revisemos sus lentes.
¿Le gustaria que le contactemos para programar una revision?
1. Si, por favor
2. No por ahora
```

**Si elige 1 (Si, por favor):**
```
Perfecto, alguien de GoodVision Colombia le contactara en los proximos
dias para coordinar una revision. Gracias por avisarnos.
```
→ Crear alerta URGENTE en Airtable: "REVISION NECESARIA"
→ ir a PASO 3

**Si responde 4 (No los he usado):**
```
Entendemos. ¿Hay alguna razon por la que no los ha usado?
1. No me quedaron bien / son incomodos
2. No he tenido tiempo
3. Prefiero no decir
```
```
Gracias por su respuesta. Le recomendamos empezar a usarlos
y si tiene cualquier molestia, escribanos a este numero.
```
→ Registrar razon en Airtable
→ ir a PASO 3

---

### PASO 3: Experiencia en la campana

```
Ahora nos gustaria saber sobre su experiencia cuando nos visito.
¿Como fue la atencion que recibio en la campana de GoodVision Colombia?
1. Excelente
2. Buena
3. Regular
4. Mala
```

**Si responde 3 (Regular) o 4 (Mala):**
```
Lamentamos que su experiencia no haya sido la mejor.
¿Nos podria contar brevemente que podemos mejorar?
```
→ Capturar respuesta abierta
→ Registrar en Airtable como feedback negativo
→ ir a PASO 4

**Si responde 1 (Excelente) o 2 (Buena):** → ir a PASO 4

---

### PASO 4: Importancia del servicio

```
¿Que tan importante fue para usted que GoodVision Colombia
llegara a su comunidad?
1. Muy importante, no tenia otra opcion
2. Importante, me facilito mucho las cosas
3. Poco importante, tengo otras opciones
```

---

### PASO 5: Cierre y despedida

```
Muchas gracias por su tiempo, {nombre}. Sus respuestas nos
ayudan a mejorar nuestro servicio.

Recuerde que si tiene cualquier problema con sus lentes, puede
escribirnos a este numero y le ayudaremos.

¡Que tenga un excelente dia! - GoodVision Colombia
```
→ Guardar todas las respuestas en Airtable
→ Cambiar estado a "completado"
→ [FIN]

---

## FLUJO DE MENSAJES ENTRANTES (cuando el paciente escribe por su cuenta)

Cuando alguien escribe al numero de WhatsApp, el sistema revisa
el campo **estado_seguimiento** en Airtable y responde segun el caso:

---

### Caso 1: Paciente que RECHAZO (estado = "opt_out")

```
¡Hola {nombre}! Que gusto que nos escriba.
Vemos que anteriormente prefirio no participar en nuestro
seguimiento, lo cual respetamos totalmente.

¿En que podemos ayudarle hoy?
1. Quiero participar ahora en el seguimiento
2. Tengo un problema con mis lentes
3. Tengo una consulta
```
→ Si elige 1: cambiar estado a "pendiente" e iniciar flujo desde PASO 1

---

### Caso 2: Paciente que NO RESPONDIO (estado = "sin_respuesta")

```
¡Hola {nombre}! Que bueno saber de usted. Le habiamos
escrito hace unos dias de parte de GoodVision Colombia.

¿Le gustaria contarnos como le fue con sus lentes? Son solo
unas preguntas cortas.
1. Si, hagamos el seguimiento
2. Tengo un problema con mis lentes
3. Tengo una consulta
```
→ Si elige 1: cambiar estado a "enviado" e iniciar flujo desde PASO 1

---

### Caso 3: Paciente que YA COMPLETO (estado = "completado")

```
¡Hola {nombre}! Gracias por escribirnos de nuevo.

¿En que podemos ayudarle?
1. Tengo un problema con mis lentes
2. Tengo una consulta
```

---

### Caso 4: Contacto NUEVO (no esta en Airtable)

```
¡Hola! Bienvenido/a al canal de WhatsApp de GoodVision Colombia.

¿En que podemos ayudarle?
1. Tengo un problema con mis lentes
2. Tengo una consulta
```

---

### Caso 5: Paciente EN PROCESO (estado = "enviado")

→ Continua el flujo donde iba

---

### Respuestas comunes para mensajes entrantes:

**Si elige "Tengo un problema con mis lentes":**
```
Lamentamos escuchar eso. Por favor cuentenos brevemente
que problema tiene con sus lentes.
```
→ Capturar respuesta abierta
→ Alerta en Airtable: "REQUIERE ATENCION"

**Si elige "Tengo una consulta":**
```
Con gusto. Escriba su consulta y un miembro de nuestro equipo
le respondera en horario de oficina (lunes a viernes,
8:00 am a 5:00 pm).
```
→ Capturar respuesta abierta
→ Notificar al equipo

**Si escribe cualquier otra cosa:**
```
Gracias por escribirnos. No logramos entender su mensaje.

Por favor responda con el numero de su opcion:
1. [opciones segun su caso]
```

---

## COMANDO ESPECIAL: SALIR

En cualquier momento del flujo, si el paciente escribe "SALIR":

```
Entendido {nombre}, hemos detenido el seguimiento.
No le enviaremos mas mensajes.

Si cambia de opinion, puede escribirnos cuando guste.
¡Que este bien! - GoodVision Colombia
```
→ Cambiar estado a "opt_out" en Airtable → [FIN]

---

## Datos a capturar en Airtable por cada paciente

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| nombre | Texto | Nombre del paciente |
| telefono | Telefono | Numero WhatsApp |
| ubicacion_campana | Texto | Donde fue atendido |
| fecha_entrega_lentes | Fecha | Cuando recibio los lentes |
| fecha_seguimiento | Fecha | Cuando se envio el seguimiento |
| estado_seguimiento | Opcion | pendiente/enviado/completado/sin_respuesta/opt_out/requiere_atencion |
| estado_lentes | Opcion | bien/molestias/mal/no_usados |
| tipo_molestia | Opcion | dolor_cabeza/borroso/incomodidad_fisica/otro |
| detalle_problema | Texto largo | Si reporto problema, descripcion |
| requiere_atencion | Checkbox | Si necesita seguimiento humano |
| calificacion_campana | Opcion | excelente/buena/regular/mala |
| feedback_campana | Texto largo | Comentarios sobre la campana |
| importancia_servicio | Opcion | muy_importante/importante/poco_importante |
| intentos_contacto | Numero | Cuantas veces se intento contactar |
| fecha_ultimo_contacto | Fecha | Ultima interaccion |
| notas | Texto largo | Notas adicionales del equipo |

---

## Webhook TextIt → Airtable

**Momentos de envio:**
1. Al iniciar el flujo (cambiar estado a "enviado")
2. Al detectar problema con lentes (alerta inmediata)
3. Al finalizar el flujo (guardar todas las respuestas, cambiar estado a "completado")
4. Al agotar reintentos (cambiar estado a "sin_respuesta")
5. Al recibir opt-out (cambiar estado a "opt_out")

---

## Notas para implementacion en TextIt

- Usar **campos de contacto** para: nombre, ubicacion_campana, fecha_entrega
- Usar **resultados de flujo** (@results) para almacenar respuestas
- Configurar **triggers** por palabra clave para el flujo de reingreso
- Configurar **trigger global** para la palabra "SALIR"
- Los mensajes deben ser cortos y claros (poblacion de bajos recursos)
- Usar numeros (1, 2, 3) para las opciones (mas facil en WhatsApp)
- Considerar que algunos pacientes pueden no saber leer bien → mantener mensajes simples
