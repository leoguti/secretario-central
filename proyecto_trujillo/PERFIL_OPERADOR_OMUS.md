# Perfil: Operador/a de Infraestructura - Plataforma OMUS

## Contexto

La plataforma OMUS (Observatorio de Movilidad Urbana Sostenible) de Trujillo es una aplicación web compuesta por varios servicios que corren en contenedores Docker sobre un servidor Linux (VPS). La persona encargada debe poder mantener la plataforma funcionando, resolver problemas comunes y realizar tareas de mantenimiento rutinario.

## Conocimientos mínimos requeridos

### 1. Linux y línea de comandos
- Manejo básico de terminal Linux (navegación de archivos, permisos, edición de texto)
- Conexión remota por SSH a un servidor
- Conocimiento básico de systemd (revisar estado de servicios, reiniciarlos)
- Manejo de cron jobs (para programar backups)

### 2. Docker
- Entender qué es un contenedor y cómo funciona Docker Compose
- Saber ejecutar comandos básicos: `docker ps`, `docker logs`, `docker compose up -d`, `docker compose down`, `docker compose restart`
- Saber reconstruir un contenedor: `docker compose up -d --build`
- Revisar logs de contenedores para diagnosticar problemas

### 3. Bases de datos
- Conocimiento básico de MySQL (la plataforma usa MySQL 8.0)
- Saber ejecutar un respaldo (backup) con `mysqldump` y restaurarlo
- Poder conectarse a la base de datos para consultas básicas

### 4. Redes y DNS
- Entender conceptos básicos de DNS (apuntar un dominio a un servidor)
- Conocimiento básico de HTTPS/SSL (la renovación de certificados es automática, pero debe saber verificar que funcione)
- Entender qué es un reverse proxy (el sistema usa uno para enrutar tráfico)

### 5. Git (básico)
- Saber clonar un repositorio y hacer `git pull` para obtener actualizaciones
- No se requiere que sepa desarrollar, solo descargar versiones nuevas del código

## Tareas típicas de mantenimiento

| Tarea | Frecuencia | Descripción |
|-------|------------|-------------|
| Verificar que los servicios estén corriendo | Semanal | Revisar `docker ps` y los logs |
| Respaldos de base de datos | Diario (automatizado) | Configurar y verificar que los backups de MySQL se ejecuten |
| Actualizar la plataforma | Cuando se libere una versión | Hacer `git pull` y reconstruir contenedores |
| Regenerar datos GTFS | Cuando cambien rutas de transporte | Ejecutar desde el panel de administración |
| Renovar tokens de TextIt | Cuando expiren | Actualizar el archivo `.env` con el nuevo token |
| Actualizar URLs de Power BI | Cuando cambien los dashboards | Actualizar desde el panel de administración o API |
| Monitorear espacio en disco | Mensual | Verificar que el servidor tenga espacio suficiente |
| Revisar certificados SSL | Mensual | Verificar que la renovación automática funcione |

## Servicios externos que debe conocer (no administrar)

- **TextIt**: Plataforma del chatbot de WhatsApp. Debe saber dónde va el token de acceso.
- **Power BI**: Dashboards embebidos. Debe saber actualizar las URLs si cambian.
- **DigitalOcean** (o proveedor de VPS): Debe poder acceder al panel para reiniciar el servidor en caso extremo.

## Arquitectura simplificada

```
Internet → Reverse Proxy (SSL automático)
              ├── omus.tmt.gob.pe/     → Frontend (Flutter Web en Nginx)
              └── omus.tmt.gob.pe/api/ → Backend (.NET 8) → MySQL 8.0
```

Todos los componentes corren como contenedores Docker en el mismo servidor.

## Perfil profesional sugerido

- Técnico/a en sistemas, redes o informática
- Experiencia con servidores Linux (al menos 1 año)
- Experiencia básica con Docker
- No se requiere experiencia en desarrollo de software
- Deseable: experiencia con servicios en la nube (DigitalOcean, AWS, o similar)
