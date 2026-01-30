# Políticas de Trabajo - Secretario

Este documento contiene las políticas, procedimientos y contexto de trabajo para el asistente Secretario.

## Organización y Roles

### Trufi Association
- **Leonardo Gutiérrez**: Business Development Manager / Project Manager
- **Rol**: Coordinación de proyectos en America Latina
- **Organización**: Trufi Association (ONG de transporte público con open-source/open-data)

### Transapp
- **Solange Muñoz**: Project Manager
- **Rol**: Proveedor técnico / Desarrollo de aplicativos móviles
- **Relación**: Partner técnico en proyectos (ejemplo: Trujillo)

### Clarificación importante
- **Trufi Association ≠ Transapp**
- Trufi coordina proyectos, Transapp ejecuta desarrollo técnico
- Leonardo representa a Trufi, NO a Transapp

## Proyectos Activos

### Proyecto Trujillo (Perú)
- **Cliente**: Municipalidad Provincial de Trujillo + GIZ/CIMO
- **⚠️ IMPORTANTE - Estructura Contractual**: El contrato con GIZ está a **nombre de Leonardo Gutiérrez** (persona natural), NO a nombre de Trufi Association
- **Objetivo**: Gestor de Flotas + GTFS + App de transporte público
- **Partners**:
  - Oscar Frank (Líder Componente 03 - CIMO)
  - Walter Alanya (Consultor técnico - Municipalidad)
  - Transapp (Desarrollo técnico)
  - Trufi (Coordinación proyecto)
  - Solange es directora de proyecto en transapp que es una empresa que esta haciendo la aplicacion para conductores nosotros hacemos la de usuario

#### Estado Actual (20 enero 2026)
- **Cronograma acordado (JourFix 20 ene 2026)**:
  - **Marzo 2026**: Presentaciones de la aplicación (lanzamiento)
  - **Abril 2026**: Migración a servidores de la Municipalidad
- **⚠️ Limitaciones GTFS**: Datos basados en plan de optimización (no validados en campo)
- **Temas críticos pendientes**: Branding final y publicación en stores
- **Pendiente verificar**: Segundo entregable y si incluye capacitaciones
- **Pendiente autorización**: Difusión pública del proyecto por parte de Trufi
- **APK v1 Android**: https://drive.google.com/drive/folders/1zQ-auSBrqhpTt6jOPn0RE9fTaNbAliaw?usp=drive_link (instalación manual)
- **OTP Web Debug**: https://otp.trujillo.trufi.dev/ (pruebas y validación de rutas)
- **Formulario hallazgos**: https://docs.google.com/forms/d/e/1FAIpQLSft81vCKXpVAwnoq3oN4gAJSiReaN6KOh5YfUo_CLieRWeVuQ/viewform
- **Compromiso**: GTFS con paradas actualizado para viernes 10 enero 2026
- **Contactos proyecto**: oscar.frank.rb@gmail.com, walanya.flores@gmail.com, david.jimenez@transconsult.com, debora.goncalves@logiteng.com, smunoz@transapp.cl

### Proyecto México (Toluca/Estado de México) - IMPORTANTE
- **Cliente**: Estado de México (Secretaría de Movilidad)
- **Proyecto**: Mejoras UI/UX Rutómetro + Integración Mexicable y Mexibus
- **Estado**: Propuesta enviada (16 diciembre 2025), respuesta positiva recibida
- **Reuniones regulares**: JourFix México Trufi-GIZ (cada 2 semanas los viernes)

#### Contactos Clave - PRIORITARIOS
- **Christoph Hanser**: President Trufi (christoph.hanser@trufi-association.org) - Muy importante
- **José Landín**: GIZ México (jose.landin@giz.de) - Muy importante, contacto principal GIZ
- **Leon Becker**: GIZ (leon.becker@giz.de) - Muy importante
- **Juan Manuel Carmona**: Estado de México (jm.carmona@edomex.gob.mx) - Cliente directo

#### Componentes del Proyecto
- Rutómetro (app existente)
- Integración con Mexicable (teleférico)
- Integración con Mexibus (BRT)
- Mejoras de UI/UX

### Proyecto Boyacá (Colombia)
- **App**: BusBoy
- **Estado**: Expansión a todo el departamento de Boyacá
- **Datos**: 600 líneas de bus del Terminal Tunja

### Proyecto CampoLimpio
- **Plataformas**:
  - **TextIt**: Notificaciones llegan a leogiga@gmail.com
  - **360Dialog**: Notificaciones llegan a info@rumbo.digital
- **Pagos**: Mensuales para ambas plataformas
- **Monitoreo**: Revisar notificaciones de facturación y estado de servicios

### Plantillas WhatsApp Business
- **Plataforma**: WhatsApp Business API vía 360Dialog
- **Notificaciones**: Llegan a info@rumbo.digital
- **Estado reciente** (6 enero 2026):
  - ✅ Plantilla "andrea_nueva" aprobada en español
  - ✅ Plantilla "andrea_nueva" aprobada en inglés
- **Proceso**: Las plantillas deben ser aprobadas por WhatsApp Business Team antes de usarse
- **⚠️ IMPORTANTE**: Monitorear correos de notification@facebookmail.com en info@rumbo.digital para conocer estado de aprobaciones/rechazos de plantillas

### Infraestructura - DigitalOcean
- **Notificaciones**: Llegan a info@rumbo.digital
- **Nota**: Droplet de OMUS fue destruido por falta de pago en cuenta DigitalOcean
- **Monitoreo**: Revisar alertas de facturación y estado de droplets

### Proyecto Lima/AEMUS (Perú) - Cliente Potencial IMPORTANTE
- **Contacto**: Ing. Luis Edgardo Ramírez García (leramirez@urbanito.com.pe)
- **Empresa**: URBANITO / AEMUS
- **WhatsApp**: +51 955 550 191
- **App existente**: MOVILIZATE (430 buses, 4 rutas, servicio al Aeropuerto Jorge Chávez)
- **Sistema actual**: 
  - Tarjeta inteligente integrada (pago entre rutas)
  - GPS en tiempo real con rastreo de buses
  - App con consulta de saldo y predicción de llegadas
  - Sistema de recaudo electrónico centralizado
- **Interés**: 
  - Generación y validación GTFS con datos GPS reales
  - Integración GTFS en plataforma MOVILIZATE existente
  - Mejoras/evolución de app actual (NO desarrollo desde cero)
  - Visibilidad en Google Maps y plataformas globales
- **Estado**: Propuesta enviada (16 abril 2025), respondió positivamente (31 dic 2025)
- **Reunión actual**: 9 enero 2026 10:00 AM
- **🔴 COMPROMISO CRÍTICO**: Enviar propuesta actualizada el **19 de enero 2026**
- **Contexto ATU**: 
  - ATU (Autoridad Transporte Urbano) regula todo el transporte en Lima
  - Metropolitano tiene GTFS, transporte convencional NO
  - AEMUS es operador moderno del sector convencional
  - Oportunidad: Ser caso piloto de digitalización para ATU
- **Partner técnico**: Haroldo Montealegre (haroldo.montealegre@sima-its.com) - Plataforma SIMA

### Proyecto Cali (Colombia) - Potencial
- **Estado**: En conversación con GIZ
- **Financiamiento**: Posible "Kleinstprojekt" de Embajada Alemana
- **Objetivo**: Implementar live routing (GPS tiempo real)
- **Reunión**: Propuesta para enero 2026 (después del 19)

## Procedimientos de Comunicación

### Respuestas a Correos

#### Protocolo General
1. Revisar contexto completo del thread
2. Identificar quién representa cada organización
3. Usar lenguaje claro sobre roles (Trufi vs partners técnicos)
4. Proponer fechas concretas cuando sea necesario
5. Hacer preguntas específicas sobre información faltante

#### Ejemplo: Correos sobre implementación técnica
```
❌ Incorrecto: "Nuestro equipo técnico (Transapp)..."
✅ Correcto: "El equipo técnico de Transapp..." 
✅ Correcto: "Desde Trufi coordinaremos con Transapp para..."
```

### Coordinación con Partners Técnicos

#### Transapp (Solange)
- Desarrollo de aplicativos móviles
- Revisión técnica de GTFS
- Publicación en tiendas de apps
- **Leonardo coordina pero NO ejecuta el desarrollo técnico**

#### Oscar Frank / Walter Alanya
- Representantes del proyecto CIMO/Municipalidad
- Proveen datos oficiales (paraderos, rutas)
- Coordinan accesos municipales

## Políticas de Datos - GTFS

### Estrategia de Paradas (Establecida 31/12/2024)
- **Usar SOLO paradas oficiales** proporcionadas por autoridades
- **Agregar paradas de inicio y fin** en todas las rutas (obligatorio)
- **NO generar paradas sintéticas** excepto inicio/fin necesarias
- **Diferenciar route_short_name** entre ida y vuelta
- **Actualización flexible**: GTFS puede actualizarse si hay datos nuevos

### Proceso de Validación
1. Recibir datos oficiales de autoridad local
2. Generar GTFS con paradas oficiales + inicio/fin
3. Validación técnica por partner (ej: Transapp)
4. Iteraciones según feedback
5. Publicación final

## Accesos y Permisos

### Tiendas de Aplicaciones (Play Store / App Store)

#### Protocolo Estándar
1. **Desarrollo y pruebas**: En tiendas de Trufi/Transapp
2. **Validación completa**: Antes de migrar
3. **Publicación final**: En tiendas del cliente (ej: Municipalidad)
4. **Acceso remoto**: Solo para paso final de producción

#### Sesiones Remotas con Clientes
- Coordinar fechas específicas con anticipación
- Definir horario laboral del cliente
- Listar actividades exactas a realizar
- Partner técnico ejecuta, Trufi supervisa/coordina

## Calendario y Disponibilidad

### Appointment Schedule (Google Calendar)
- **URL**: https://calendar.app.google/1B8uUb5HxfVLrFUB7
- **Tipo**: Reuniones de 30 minutos
- **Disponibilidad**: Solo mañanas (horario Colombia GMT-5)
- **Uso**: Compartir con clientes y colaboradores para agendar reuniones

### Fechas Clave 2026
- **12-17 enero**: Leonardo de viaje (no disponible)
- **A partir 15 enero**: Sesión remota Play Console/App Store (Trujillo) - sugerido por Walter
- **19+ enero**: Christoph Hanser regresa, disponible para call Colombia/Cali

### Zona Horaria
- **Colombia**: GMT-5
- **Perú**: GMT-5
- **Chile (Transapp)**: GMT-3

## Contactos Clave

### Trufi Association
- Christoph Hanser: President (christoph.hanser@trufi-association.org)
- Leonardo Gutiérrez: Business Development Manager
- Luz Choque: App Manager

### Partners Técnicos
- Solange Muñoz: Project Manager Transapp (smunoz@transapp.cl)

### Clientes/Instituciones
- Oscar Frank: CIMO Líder Componente 03 (oscar.frank.rb@gmail.com)
- Walter Alanya: Consultor Municipalidad Trujillo (walanya.flores@gmail.com)
- Michael Engelskirchen: GIZ (michael.engelskirchen@giz.de)

## Plataformas de Comunicación

### Slack (Workspace Trufi) - COMUNICACIÓN PRINCIPAL
- **Cuenta**: leogiga@gmail.com
- **Configuración**: User token (actúa como usuario, no como bot)
- **Importancia**: ⚠️ **Canal principal de comunicación de Trufi Association**
- **Monitoreo**: Revisar frecuentemente, alta prioridad
- **Canales clave**: 
  - #announcements (anuncios oficiales)
  - #team-developers (desarrollo técnico)
  - #team-data (datos y GTFS)
  - #proj-driver-app (proyecto gestor de flotas)
  - #team-product-ownership (product management)
  - #team-ito (ITO team)
- **Uso**: Coordinación de equipo, decisiones de proyecto, comunicación diaria

### LinkedIn - DESARROLLO DE NEGOCIOS Y NETWORKING
- **Cuenta**: Vinculada a leonardo.gutierrez@trufi-association.org
- **Importancia**: ⚠️ **Fuente crítica de oportunidades comerciales y contactos del sector**
- **Monitoreo**: Analizar notificaciones de LinkedIn en correo regularmente
- **Método de acceso**: Parseo de notificaciones recibidas vía email (legal y seguro)
- **Tipo de oportunidades a identificar**:
  - **Contactos del sector movilidad**: Funcionarios de gobierno, directores de transporte, instituciones
  - **Solicitudes de conexión relevantes**: Personas en cargos de decisión en transporte público
  - **Publicaciones de interés**: Licitaciones, proyectos nuevos, iniciativas de movilidad
  - **Ofertas laborales**: Business development, consultoría en transporte
- **Sectores prioritarios**:
  - Autoridades de transporte (Secretarías, Municipalidades)
  - ONGs de movilidad (ITDP, WRI, etc.)
  - Empresas de tecnología de transporte
  - Instituciones financiadoras (GIZ, BID, Banco Mundial)
- **⚠️ POLÍTICA**: Revisar oportunidades de LinkedIn **semanalmente** para no perder contactos clave
- **Ejemplos de valor**: 
  - Diego Jiménez (Secretario Transporte Cundinamarca) - cliente potencial
  - Julio César Hernández (ITDP México) - alianza estratégica con GIZ
  - Martha Ibañez (Transmilenio Bogotá) - expertise técnico en BRT

## Cuentas de Correo Configuradas

### Correo Trufi (Trabajo)
- **Email**: leonardo.gutierrez@trufi-association.org
- **Uso**: Comunicaciones oficiales de Trufi, proyectos, coordinación

### Correo Personal
- **Email**: leogiga@gmail.com
- **Uso**: Personal + Notificaciones de TextIt (CampoLimpio)

### Correo Familiar/Cuentas
- **Email**: mylupigo@gmail.com
- **Responsable**: Esposa de Leonardo
- **⚠️ IMPORTANTE**: Esta cuenta maneja renovaciones de servicios, cuentas y temas financieros familiares
- **Monitoreo crítico**: Correos relacionados con pagos, renovaciones y servicios del hogar

### Correo Rumbo Digital
- **Email**: info@rumbo.digital
- **Uso**: Notificaciones de 360Dialog (CampoLimpio), soporte técnico
- **Servidor IMAP**: imap.secureserver.net (GoDaddy)
- **Acceso**: Configurado vía IMAP con credenciales en `.env` (RUMBO_PASSWORD)
- **Cliente**: `central/imap_client.py` - función `get_rumbo_client()`

### Alias de Correo para IA (Secretario-IA)
- **Email**: leogiga+secretario-ia@gmail.com
- **Uso**: EXCLUSIVO para acciones automatizadas del sistema de IA
- **Propósito**: Diferenciación clara entre acciones humanas y automatizadas
- **🚨 POLÍTICA CRÍTICA**: 
  - ✅ **SIEMPRE** usar este alias para envíos automáticos
  - ❌ **NUNCA** enviar correos desde leogiga@gmail.com directamente
  - ❌ **NUNCA** enviar desde leonardo.gutierrez@trufi-association.org automáticamente
  - Esta política protege la confianza y transparencia con colaboradores

## Monitoreo de Oportunidades y Licitaciones

### DevEx (Development Exchange)
- **Cuenta**: leonardo.gutierrez@trufi-association.org
- **Plataforma**: https://www.devex.com
- **Propósito**: Monitoreo de licitaciones y oportunidades de desarrollo internacional
- **Configuración** (6 enero 2026):
  - ✅ Procurement Alert (diario) - licitaciones internacionales
  - ✅ Money Matters (semanal) - oportunidades de financiamiento
  - ✅ Alerta personalizada "Urban Mobility LATAM" (diaria)
- **Búsqueda guardada**: "urban mobility digital solutions"
- **Filtros activos**: Funding > Tenders & Grants
- **Método de monitoreo**: Parseo automático de emails de DevEx
- **Frecuencia de revisión**: Semanal (automático)
- **Sectores relevantes**:
  - Movilidad urbana sostenible
  - Transporte público digital
  - GTFS y datos abiertos de transporte
  - Infraestructura de movilidad en LATAM
- **Tipos de oportunidades**:
  - Tenders (licitaciones)
  - Grants (subsidios)
  - RFPs (Request for Proposals)
  - Contract Awards (adjudicaciones)
- **⚠️ IMPORTANTE**: Los emails de DevEx llegan a leonardo.gutierrez@trufi-association.org y son analizados automáticamente para identificar oportunidades HOT

#### Proceso de Análisis de Correos DevEx (Establecido 7 enero 2026)
- **Formato de correos**: HTML con títulos embebidos en estructura de tablas
- **Método de extracción**:
  1. Obtener correo vía Gmail API en formato 'full'
  2. Extraer body HTML desde payload (base64 decode)
  3. Usar HTMLParser para parsear enlaces con href="devex.com/funding/tenders" o "devex.com/funding/pipeline"
  4. Capturar texto entre tags `<a>` como títulos de oportunidades
- **Sistema de scoring automático**:
  - **+4 puntos**: Palabras "transport", "transit", "mobility"
  - **+5 puntos**: Región LATAM/Caribe (Colombia, Peru, Mexico, etc.)
  - **+3 puntos**: "app", "mobile", "bus", "metro"
  - **+2 puntos**: "digital", "software", "platform", "urban", "city"
  - **+1 punto**: "data", "system", "infrastructure"
- **Clasificación de prioridad**:
  - 🔴 **Alta prioridad** (score ≥ 5): Revisar URGENTE, potencial inmediato
  - 🟡 **Media prioridad** (score 2-4): Evaluar viabilidad
  - ⚪ **Baja/Sin relevancia** (score 0-1): Ignorar o archivo
- **Criterios de relevancia para Trufi**:
  - ✅ Transporte público + Tecnología digital
  - ✅ Región LATAM o similar a proyectos existentes
  - ✅ Apps móviles, GTFS, plataformas de movilidad
  - ⚠️ Infraestructura sin componente digital = revisar detalle
  - ❌ Solo infraestructura física civil = no relevante
  - ❌ Apps genéricas sin relación a transporte = no relevante
- **Limitación técnica**: Los correos solo contienen títulos, NO descripción completa. Para análisis detallado se debe acceder a devex.com con credenciales

### Portales Nacionales de Compras Públicas (Futuro)
- **SECOP Colombia**: https://www.colombiacompra.gov.co (tiene API pública)
- **OSCE Perú**: https://portal.osce.gob.pe (web services públicos)
- **CompraNet México**: https://compranet.hacienda.gob.mx (buscador público)
- **Estrategia**: Monitoreo periódico de licitaciones relacionadas con GIZ, movilidad, transporte
- **Estado**: Por implementar según necesidad

## Dominios y Servicios

### GoDaddy
- **Cuenta**: Cuenta personal (leogiga@gmail.com)

#### Dominios Activos
- **rumbo.digital**: Dominio principal para servicios
- *(Otros dominios profesionales según necesidad)*

#### Dominios NO Renovar
- **EXPEREST.COM**: 
  - Comprado originalmente para familiar
  - **Decisión**: NO renovar, dejar expirar
  - **Fecha expiración**: 27 diciembre 2025 (ya expirado)
  - **Acción**: Ignorar notificaciones de renovación de GoDaddy
  - **Documentado**: 3 enero 2026

## Políticas de Automatización y IA

### Uso de Alias para Identificación de IA
- **Principio fundamental**: Transparencia total sobre acciones automatizadas
- **Alias oficial**: leogiga+secretario-ia@gmail.com
- **Aplicaciones**:
  - Actualizaciones automáticas en Google Sheets
  - Procesamiento de recibos/documentos
  - Notificaciones del sistema
  - Cualquier acción NO iniciada directamente por Leonardo

### Restricciones de Correo Electrónico
- ❌ **PROHIBIDO**: Enviar correos desde cuentas principales sin autorización explícita
- ✅ **PERMITIDO**: Usar alias secretario-ia para comunicaciones automatizadas
- ⚠️ **Excepciones**: Solo con confirmación explícita de Leonardo en cada caso

---

**Última actualización**: 4 de enero de 2026
**Mantenido por**: Leonardo Gutiérrez con asistencia de Secretario
