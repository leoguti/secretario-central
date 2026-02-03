# Diagnóstico UDM Pro - Valsalice

**Fecha:** 2026-02-03
**Ubicación:** Fusagasugá, Cundinamarca, Colombia
**Hostname:** valsalice

---

## Información del Sistema

| Parámetro | Valor |
|-----------|-------|
| **Dispositivo** | UniFi Dream Machine Pro |
| **Firmware UDM Pro** | 4.4.6 |
| **Network** | 10.0.162 |
| **Protect** | 6.2.88 |
| **Kernel** | Linux 4.19.152-ui-alpine (aarch64) |
| **Uptime** | 7 días, 21 horas |
| **CPU** | 4 cores ARM (Alpine V2) |
| **CPU Temp** | 43.5°C |
| **CPU Load** | 27.1% |

---

## Memoria

| Tipo | Usado | Total | Porcentaje |
|------|-------|-------|------------|
| **RAM** | 2.8 GB | 3.9 GB | 72% |
| **Swap** | 957 MB | 6.7 GB | 14% |
| **Disponible** | 760 MB | - | - |

### Procesos principales por memoria:
- Java (UniFi Network): 690 MB
- UniFi Protect: 397 MB
- MST (transcoder): 227 MB
- Node22: 169 MB
- MSR: 165 MB
- MongoDB: 165 MB

---

## Almacenamiento

### Disco Principal (Video/Grabaciones)

| Parámetro | Valor |
|-----------|-------|
| **Modelo** | WDC WD102PURZ-85BXPY0 (WD Purple) |
| **Serial** | VCGE30SM |
| **Capacidad** | 10 TB (9.1 TB usables) |
| **Usado** | 8.6 TB |
| **Libre** | 50 GB |
| **Uso** | 100% |
| **RPM** | 7200 |
| **Horas encendido** | 39,776 hrs (~4.5 años 24/7) |
| **Temperatura** | 51°C (Min: 17°C / Max: 59°C) |
| **SMART Status** | PASSED |

### Atributos SMART

| Atributo | Valor | Estado |
|----------|-------|--------|
| Raw_Read_Error_Rate | 0 | OK |
| Reallocated_Sector_Ct | 0 | OK |
| Seek_Error_Rate | 0 | OK |
| Spin_Retry_Count | 0 | OK |
| Current_Pending_Sector | 0 | OK |
| Offline_Uncorrectable | 0 | OK |
| UDMA_CRC_Error_Count | 0 | OK |

### Otras particiones

| Partición | Tamaño | Usado | Montaje |
|-----------|--------|-------|---------|
| /boot/firmware | 2.0 GB | 93% | Sistema |
| overlay (/) | 9.4 GB | 41% | Root |
| /var/log | 976 MB | 28% | Logs |
| /persistent | 2.0 GB | 30% | Config |

---

## UniFi Protect

| Parámetro | Valor |
|-----------|-------|
| **Cámaras** | ~22 |
| **Grabaciones almacenadas** | 8.6 TB |
| **Antigüedad grabaciones** | 2023 - 2026 (3 años) |
| **Base de datos** | PostgreSQL 14 |
| **Estado** | Sin errores recientes |

### Estructura de grabaciones:
```
/srv/unifi-protect/video/
├── 2023/
├── 2024/
├── 2025/
├── 2026/
└── pool/
```

---

## Redes Configuradas

| Interfaz | IP | Función |
|----------|-----|---------|
| **br0** | 192.168.31.1/23 | LAN Principal |
| **eth8** | 192.168.100.4/24 | WAN (Internet) |

### Rango LAN
- 192.168.30.0 - 192.168.31.255 (/23)

### Conectividad WAN
- Latencia a 8.8.8.8: 2.9 ms promedio
- Pérdida de paquetes: 0%

---

## Servicios Activos

| Servicio | Estado | Función |
|----------|--------|---------|
| unifi-protect | Activo | NVR/Cámaras |
| nginx | Activo | Web Server |
| mongod | Activo | UniFi Network DB |
| PostgreSQL 14 | Activo | Protect DB |
| dnsmasq | Activo | DHCP/DNS |
| ubnt_ai_daemon | Activo | Detección IA |
| wifiman-speedtest | Activo | Speed Test |
| rabbitmq | Activo | Message Queue |
| teleportd | Activo | Remote Access |

---

## Puertos en Escucha (Principales)

| Puerto | Servicio |
|--------|----------|
| 80 | nginx (HTTP) |
| 443/8444 | nginx (HTTPS) |
| 7441 | Management Service |
| 7447 | RTSP Streams |
| 8901 | WiFiman Speed Test |
| 27117 | MongoDB |
| 53 | DNS (dnsmasq) |

---

## Errores Detectados

### Kernel (dmesg)
```
[quic_sm_reassemble_func#1025]: failed to allocate reassemble cont.
```
- **Frecuencia:** Alta (repetitivo)
- **Causa:** DPI sin memoria suficiente para paquetes QUIC
- **Impacto:** Bajo - No afecta funcionamiento
- **Solución:** Desactivar DPI si no se usa

### Logs del Sistema
```
dpi-flow-stats: ubnt-dpi-util: connect: The socket was closed due to a timeout
mca-ctrl: service_json dump fail, retry
```
- **Causa:** Timeouts ocasionales en DPI
- **Impacto:** Bajo

---

## Riesgos Identificados

### CRÍTICO

| Riesgo | Descripción | Acción |
|--------|-------------|--------|
| **Disco lleno** | Solo 50GB libres de 9.1TB | Reducir retención de video o eliminar grabaciones antiguas |

### MODERADO

| Riesgo | Descripción | Acción |
|--------|-------------|--------|
| **Disco con 4.5 años** | Vida útil ~5-7 años para WD Purple | Planificar reemplazo en 12-18 meses |
| **Memoria RAM alta** | 72% usado + swap activo | Monitorear, normal para 22 cámaras |
| **Boot al 93%** | Poco espacio para actualizaciones | Vigilar |

### BAJO

| Riesgo | Descripción | Acción |
|--------|-------------|--------|
| **Errores QUIC** | DPI con problemas de memoria | Desactivar DPI si no se usa |

---

## Mantenimiento Recomendado

### Inmediato (Esta semana)

1. **Liberar espacio en disco de video**
   - Protect → Settings → Recording → Retention
   - Reducir a 30-60 días máximo
   - O eliminar carpetas 2023/2024 manualmente

### Mensual

2. **Reiniciar UDM Pro** - Recomendado cada 30 días
3. **Verificar actualizaciones** de firmware
4. **Revisar estado SMART** del disco

### Trimestral

5. **Respaldar configuración** del UDM Pro
6. **Revisar logs** de errores

### Anual

7. **Planificar reemplazo de HDD** (disco tiene 4.5 años de uso 24/7)
8. **Evaluar necesidad de más RAM** si se agregan cámaras

---

## Comandos Útiles SSH

```bash
# Conectar
ssh root@192.168.31.1

# Ver temperatura CPU
ubnt-systool cputemp

# Ver carga CPU
ubnt-systool cpuload

# Estado SMART del disco
smartctl -a /dev/sda

# Espacio en disco
df -h

# Uso de memoria
free -h

# Servicios fallidos
systemctl --failed

# Logs críticos
journalctl -p err -n 50
```

---

## Información de Acceso

| Parámetro | Valor |
|-----------|-------|
| **IP LAN** | 192.168.31.1 |
| **Usuario SSH** | root |
| **Web UI** | https://192.168.31.1 |

---

## Notas Adicionales

- Grabaciones desde 2023 ocupan la mayoría del espacio
- 22 cámaras generan ~8.6TB en 3 años
- El sistema está estable pero el disco necesita limpieza urgente
- No hay cámaras desconectadas actualmente
- Red funcionando sin pérdida de paquetes

---

*Reporte generado: 2026-02-03 07:45 COT*
