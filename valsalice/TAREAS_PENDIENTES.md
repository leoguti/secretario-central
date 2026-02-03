# Tareas Pendientes - Valsalice

**Fecha:** 2026-02-03
**Ubicación:** Colegio Valsalice, Fusagasugá

---

## Tareas Físicas / Presenciales

### 1. Televisor Rectoría
- [ ] Poner activo el televisor en la rectoría del colegio
- **Ubicación:** Rectoría
- **Prioridad:** Media

### 2. Acceso Padre Gregorio
- [ ] Configurar acceso desde su celular a las cámaras/sistema
- **Usuario:** Padre Gregorio
- **Prioridad:** Alta

### 3. Cámara Restaurante Escolar
- [ ] Revisar/reparar cámara del restaurante escolar
- **Ubicación:** Restaurante escolar
- **Prioridad:** Media

### 4. Cámara Portería - NO FUNCIONA
- [ ] Reparar cámara de portería (no funciona)
- **Ubicación:** Portería
- **Prioridad:** Alta
- **Estado:** No funcional

### 5. Acceso Rector Harrison
- [ ] Dar acceso a cámaras al rector Harrison
- **Usuario:** Rector Harrison
- **Prioridad:** Alta

### 6. Desactivar Acceso Sebastián Julio
- [ ] Remover/desactivar accesos de Sebastián Julio
- **Usuario:** Sebastián Julio
- **Prioridad:** Alta
- **Acción:** Desactivar

### 7. Cámara Lago / Entrada Residencia - INTERMITENTE + INTERNET
- [ ] Revisar infraestructura de red - PROBLEMA DE CABLE TRONCAL
- **IP:** 192.168.31.114
- **Nombre:** 114-entrada-interno-residencia
- **MAC:** 74:83:c2:3f:c0:a4
- **Problema:** Caídas intermitentes que afectan TAMBIÉN el internet
- **Prioridad:** **CRÍTICA**
- **Latencia:** 0.3ms (cuando funciona)

#### Historial de caídas (desde logs):
| Fecha | Hora |
|-------|------|
| 2025-10-21 | 05:13 |
| 2025-11-04 | 23:39 |
| 2025-11-08 | 07:13 |
| 2025-11-13 | 05:16, 12:38 |
| 2025-11-19 | 06:02 |
| 2025-12-02 | 14:16 |
| 2025-12-29 | 05:38 |
| 2026-01-24 | 05:27 |
| 2026-01-26 | 15:23 |

#### Diagnóstico:
- **Patrón:** Caídas frecuentes en madrugada (05:00-07:00)
- **Causa probable:** Cable troncal dañado o switch intermedio fallando
- **Afecta:** Cámara 114 + conectividad internet

#### Acciones requeridas:
1. [ ] Identificar ruta física del cable de la cámara 114
2. [ ] Revisar switch intermedio (si existe)
3. [ ] Inspeccionar conectores RJ45 y patch panel
4. [ ] Verificar si hay daño por agua/humedad
5. [ ] Probar reemplazar cable si es accesible

#### Cámaras del Lago (verificar también):
| Cámara | IP | Latencia | Estado |
|--------|-----|----------|--------|
| 103-lago-grande-1 | 192.168.31.103 | 6.5ms | Online |
| 107-casa-perro-lagos-2 | 192.168.31.107 | 6.4ms | Online |

**Nota:** Las cámaras del lago tienen latencia alta (6-7ms), posible WiFi o cable largo.

---

## Inventario de Cámaras

| IP | Nombre | MAC | Estado |
|----|--------|-----|--------|
| 192.168.31.101 | patio-principal | b4:fb:e4:ff:ee:89 | Online |
| 192.168.31.103 | lago-grande-1 | b4:fb:e4:ff:e8:3d | Online |
| 192.168.31.107 | casa-perro-lagos-2 | b4:fb:e4:ff:e9:3e | Online |
| 192.168.31.110 | rectoria | 74:83:c2:3f:c0:89 | Online |
| 192.168.31.111 | patio-deportes | 74:83:c2:3f:c0:84 | Online |
| 192.168.31.113 | pasillo-gallinero | 74:83:c2:3f:c0:a2 | Online |
| 192.168.31.114 | entrada-interno-residencia | 74:83:c2:3f:c0:a4 | **Intermitente** |
| 192.168.31.116 | entrada-cecil | 74:83:c2:3f:bf:15 | Online |
| 192.168.31.118 | esquina-invernadero | 74:83:c2:3f:bc:36 | Online |
| 192.168.31.119 | esquina-inv-avenida | 74:83:c2:3f:c0:51 | Online |
| 192.168.31.120 | patio-central | 74:83:c2:3f:bf:95 | Online |
| 192.168.31.121 | exterior-carretera | 74:83:c2:3f:c0:9f | Online |
| 192.168.31.122 | cancha-desde-porteria | 74:83:c2:3f:c0:83 | Online |
| 192.168.31.123 | panoramica-residencia | 74:83:c2:3f:c0:9c | Online |
| 192.168.31.124 | fabrica | 74:83:c2:3f:c0:46 | Online |
| 192.168.31.125 | establo | 74:83:c2:3f:c0:a0 | Online |
| 192.168.31.126 | colegio-2do-piso | 74:83:c2:3f:c0:92 | Online |
| 192.168.31.127 | colegio-piso-3 | 74:83:c2:3f:c0:45 | Online |
| 192.168.31.128 | colegio-piso-4 | 74:83:c2:3f:ba:03 | Online |

**Total:** 19 cámaras detectadas

---

## Resumen de Prioridades

| # | Tarea | Prioridad | Estado |
|---|-------|-----------|--------|
| 2 | Acceso Padre Gregorio | **Alta** | Pendiente |
| 4 | Cámara portería | **Alta** | No funciona |
| 5 | Acceso Rector Harrison | **Alta** | Pendiente |
| 6 | Desactivar Sebastián Julio | **Alta** | Pendiente |
| 7 | Cámara 114 (intermitente) | **Alta** | Monitorear |
| 1 | Televisor rectoría | Media | Pendiente |
| 3 | Cámara restaurante escolar | Media | Pendiente |

---

## Script de Monitoreo

Para monitorear la cámara problemática, ejecutar:

```bash
# Monitoreo continuo (cada 30 segundos)
watch -n 30 'ping -c 3 192.168.31.114'

# O desde el UDM Pro por SSH:
ssh root@192.168.31.1 'while true; do date; ping -c 3 192.168.31.114 | tail -1; sleep 60; done'
```

---

## Acciones para Usuarios en Protect

### Agregar usuario:
```
Protect → Settings → Users → Add User
```

### Desactivar usuario:
```
Protect → Settings → Users → [Usuario] → Disable/Remove
```

---

*Actualizado: 2026-02-03*
