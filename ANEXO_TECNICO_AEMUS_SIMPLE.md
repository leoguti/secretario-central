# ANEXO A: Arquitectura Técnica del Sistema

Este anexo describe de forma general cómo funcionará el sistema de la aplicación móvil para AEMUS.

---

## A.1. ¿Cómo funciona el sistema?

El sistema tiene tres partes principales que trabajan juntas:

```
┌─────────────────────────────────────────────────────────┐
│                      USUARIOS                            │
│               (Pasajeros de AEMUS)                       │
│          Descargan la app en su celular                  │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              APLICACIÓN MÓVIL AEMUS                      │
│                                                          │
│   • Buscar cómo llegar de un punto a otro               │
│   • Ver dónde están los buses en el mapa                │
│   • Saber cuánto falta para que llegue el bus           │
│   • Consultar saldo de tarjeta (opcional)               │
│                                                          │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                 SERVIDORES EN LA NUBE                    │
│              (Administrados por Trufi)                   │
│                                                          │
│   • Calculan las mejores rutas para el usuario          │
│   • Reciben la ubicación de los 430 buses               │
│   • Envían información actualizada a la app             │
│                                                          │
└────────────────────────┬────────────────────────────────┘
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
┌──────────────────────┐    ┌──────────────────────┐
│   SISTEMA GPS        │    │    MOVILIZATE        │
│   DE AEMUS           │    │    (Opcional)        │
│                      │    │                      │
│ Los 430 buses envían │    │ Sistema de pagos     │
│ su ubicación cada    │    │ existente de AEMUS   │
│ pocos segundos       │    │                      │
└──────────────────────┘    └──────────────────────┘
```

---

## A.2. Componentes del Sistema

### La Aplicación Móvil

Es lo que los pasajeros descargan en su teléfono.

| Característica | Detalle |
|----------------|---------|
| Disponible en | Android (Google Play) e iOS (App Store) |
| Funciona en | Teléfonos con Android 6.0 o superior, iPhone con iOS 12 o superior |
| Requiere | Conexión a internet y GPS activado |
| Idioma | Español |

### Los Servidores en la Nube

Son computadoras en internet que hacen todo el trabajo pesado:

- **Calculan rutas:** Cuando un usuario pregunta "¿cómo llego de A a B?", el servidor calcula las mejores opciones usando las 4 rutas de AEMUS y otras rutas de Lima.

- **Procesan ubicaciones:** Reciben constantemente la posición de los 430 buses y la muestran en el mapa de la app.

- **Están siempre disponibles:** Funcionan 24 horas, 7 días a la semana, con copias de seguridad automáticas.

---

## A.3. ¿Qué datos se utilizan?

### Datos de las Rutas (GTFS)

GTFS es un formato estándar mundial para describir rutas de transporte público. Incluye:

- El recorrido exacto de cada ruta (por qué calles pasa)
- La ubicación de los paraderos
- Los horarios y frecuencias de servicio
- Información de los operadores

**Estos datos permiten que la app calcule rutas y que AEMUS aparezca en Google Maps.**

### Datos del GPS (Tiempo Real)

La app muestra dónde está cada bus en tiempo real gracias a:

- El sistema GPS que ya tiene AEMUS instalado en sus 430 buses
- Una conexión entre ese sistema y nuestros servidores
- Actualización cada pocos segundos en el mapa de la app

---

## A.4. Tecnologías Utilizadas

Todo el sistema usa tecnologías de **código abierto** (open source), lo que significa:

- No hay costos de licencias de software
- Son tecnologías probadas y usadas en todo el mundo
- AEMUS no queda "atado" a un solo proveedor

| Componente | Tecnología | Usado por |
|------------|------------|-----------|
| Aplicación móvil | Flutter | Google, Alibaba, BMW |
| Mapas | OpenStreetMap | Wikipedia de los mapas |
| Cálculo de rutas | OpenTripPlanner | Ciudades en todo el mundo |
| Servidores | Linux | 90% de internet |

---

## A.5. Seguridad

| Aspecto | Cómo se protege |
|---------|-----------------|
| Comunicaciones | Toda la información viaja encriptada (HTTPS) |
| Datos de usuarios | La app NO requiere registro ni guarda datos personales |
| Servidores | Protegidos con firewalls y monitoreo continuo |
| Respaldos | Copias de seguridad automáticas diarias |

---

## A.6. ¿De quién son los datos?

| Tipo de información | Propietario | Uso |
|---------------------|-------------|-----|
| Rutas y paraderos (GTFS) | AEMUS | Se publican para que aparezcan en Google Maps y otras apps |
| Estadísticas de uso de la app | AEMUS | Información privada para planificación interna |
| Ubicación de buses | AEMUS | Solo se muestra en la app, no se comparte con terceros |

**Importante:** Trufi administra la tecnología, pero todos los datos generados son propiedad exclusiva de AEMUS.

---

## A.7. Qué necesitamos de AEMUS

Para que el sistema funcione correctamente, necesitamos:

| Requisito | Descripción | Cuándo |
|-----------|-------------|--------|
| Acceso al GPS | Conexión al sistema que muestra la ubicación de los buses | Mes 3 |
| Branding | Logo, colores y elementos gráficos para personalizar la app | Mes 1 |
| Documentación MOVILIZATE | Si se desea integrar consulta de saldo (opcional) | Mes 4 |

---

*Este anexo es parte de la propuesta comercial AEMUS Lima - Trufi Association*
