# Topología de Red - Valsalice

**Fecha:** 2026-02-03
**Ubicación:** Colegio Valsalice, Fusagasugá, Cundinamarca

---

## Diagrama General

```
                                    ┌─────────────────────────────────────────┐
                                    │            INTERNET                      │
                                    │         192.168.100.x                    │
                                    └─────────────┬───────────────────────────┘
                                                  │
                                                  │ eth8 (WAN)
                                                  ▼
                              ┌───────────────────────────────────────────────┐
                              │                                               │
                              │              UDM PRO "valsalice"              │
                              │              192.168.31.1                     │
                              │              MAC: 74:ac:b9:5e:24:6d           │
                              │                                               │
                              │   Puertos LAN: eth0-eth7                      │
                              │   Firmware: 4.4.6                             │
                              │   Network: 10.0.162                           │
                              │   Protect: 6.2.88                             │
                              │                                               │
                              └───────────────────┬───────────────────────────┘
                                                  │
                                                  │ Puerto 2
                                                  ▼
                              ┌───────────────────────────────────────────────┐
                              │                                               │
                              │              SWITCH US48                      │
                              │              192.168.30.33                    │
                              │              MAC: e0:63:da:e5:e6:1e           │
                              │              Modelo: UniFi Switch 48          │
                              │                                               │
                              └───────┬───────────────┬───────────────┬───────┘
                                      │               │               │
              ┌───────────────────────┘               │               └───────────────────────┐
              │                                       │                                       │
              ▼                                       ▼                                       ▼
    ┌─────────────────┐                   ┌─────────────────┐                     ┌─────────────────┐
    │   Access Points │                   │  Switch Hikvision│                    │    Cámaras      │
    │   (WiFi)        │                   │  (No gestionado) │                    │   Directas      │
    │                 │                   │  Biblioteca      │                    │                 │
    │                 │                   │  Casa Salesiana  │                    │                 │
    └─────────────────┘                   └────────┬────────┘                     └─────────────────┘
                                                   │
                                                   │
                              ┌────────────────────┼────────────────────┐
                              │                    │                    │
                              ▼                    ▼                    ▼
                    ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
                    │  Cámara 114     │  │  Otros equipos  │  │  Internet zona  │
                    │  Entrada Interno│  │  zona residencia│  │  residencia     │
                    │  Residencia     │  │                 │  │                 │
                    │  192.168.31.114 │  │                 │  │                 │
                    └─────────────────┘  └─────────────────┘  └─────────────────┘
```

---

## Dispositivos de Red Gestionados (UniFi)

### Gateway Principal

| Parámetro | Valor |
|-----------|-------|
| **Nombre** | valsalice |
| **Modelo** | UDM PRO |
| **IP LAN** | 192.168.31.1 |
| **IP WAN** | 192.168.100.4 |
| **MAC** | 74:ac:b9:5e:24:6d |
| **Firmware** | 4.4.6 |
| **Ubicación** | Rack principal |

### Switches Gestionados

| Nombre | Modelo | IP | MAC | Puertos | Ubicación |
|--------|--------|-----|-----|---------|-----------|
| (principal) | US48 | 192.168.30.33 | e0:63:da:e5:e6:1e | 48 | Rack principal |
| (retirado?) | USMINI | 192.168.31.190 | 74:ac:b9:a9:e9:ce | 5 | ¿? (no responde) |

### Access Points

| Nombre | Modelo | IP | MAC | Ubicación |
|--------|--------|-----|-----|-----------|
| 01-RECTORIA | U7LR | 192.168.31.131 | 74:ac:b9:66:5c:2d | Rectoría |
| 02-COMEDOR | U7LR | 192.168.30.32 | 74:ac:b9:66:5b:11 | Comedor |
| 03-CAPILLA RESIDENCIA | U7LR | 192.168.31.185 | 74:ac:b9:66:5c:71 | Capilla Residencia |
| 04-Sala Informatica | U7LR | 192.168.30.70 | 74:ac:b9:66:5d:42 | Sala de Informática |
| 05-SALA DE PROFESORES | U7LR | 192.168.31.154 | f4:92:bf:cc:12:3d | Sala de Profesores |
| 06-PASTORAL | U7LR | 192.168.31.62 | f4:92:bf:cc:22:a3 | Pastoral |

---

## Dispositivos NO Gestionados

### Switches No Gestionados

| Nombre | Marca | Modelo | IP | Ubicación | Conecta a | Notas |
|--------|-------|--------|-----|-----------|-----------|-------|
| Switch Biblioteca | Hikvision | ¿? (PoE) | N/A | Biblioteca Casa Salesiana | Zona Residencia | Sin gestión, solo PoE básico |

---

## Segmentos de Red

| Segmento | Rango | VLAN | Uso |
|----------|-------|------|-----|
| LAN Principal | 192.168.30.0/23 | - | Todos los dispositivos |
| Rango .30.x | 192.168.30.1-254 | - | Clientes DHCP |
| Rango .31.x | 192.168.31.1-254 | - | Cámaras, APs, infraestructura |
| WAN | 192.168.100.x | - | Conexión a Internet |

---

## Cámaras UniFi Protect

### Por Zona/Ubicación

#### Zona Colegio
| # | Nombre | IP | MAC | Puerto/Switch |
|---|--------|-----|-----|---------------|
| 126 | colegio-2do-piso | 192.168.31.126 | 74:83:c2:3f:c0:92 | US48 |
| 127 | colegio-piso-3 | 192.168.31.127 | 74:83:c2:3f:c0:45 | US48 |
| 128 | colegio-piso-4 | 192.168.31.128 | 74:83:c2:3f:ba:03 | US48 |

#### Zona Exteriores
| # | Nombre | IP | MAC | Puerto/Switch |
|---|--------|-----|-----|---------------|
| 101 | patio-principal | 192.168.31.101 | b4:fb:e4:ff:ee:89 | US48 |
| 111 | patio-deportes | 192.168.31.111 | 74:83:c2:3f:c0:84 | US48 |
| 120 | patio-central | 192.168.31.120 | 74:83:c2:3f:bf:95 | US48 |
| 121 | exterior-carretera | 192.168.31.121 | 74:83:c2:3f:c0:9f | US48 |
| 122 | cancha-desde-porteria | 192.168.31.122 | 74:83:c2:3f:c0:83 | US48 |

#### Zona Lagos
| # | Nombre | IP | MAC | Puerto/Switch | Notas |
|---|--------|-----|-----|---------------|-------|
| 103 | lago-grande-1 | 192.168.31.103 | b4:fb:e4:ff:e8:3d | US48 | Latencia 6.5ms |
| 107 | casa-perro-lagos-2 | 192.168.31.107 | b4:fb:e4:ff:e9:3e | US48 | Latencia 6.4ms |

#### Zona Residencia / Casa Salesiana
| # | Nombre | IP | MAC | Puerto/Switch | Notas |
|---|--------|-----|-----|---------------|-------|
| 110 | rectoria | 192.168.31.110 | 74:83:c2:3f:c0:89 | US48 | |
| 112 | respaldo-residencia | 192.168.31.112 | 18:e8:29:08:1e:20 | US48 | |
| 114 | entrada-interno-residencia | 192.168.31.114 | 74:83:c2:3f:c0:a4 | **Hikvision** | ⚠️ INTERMITENTE |
| 123 | panoramica-residencia | 192.168.31.123 | 74:83:c2:3f:c0:9c | US48 | |

#### Zona Invernadero / Avenida
| # | Nombre | IP | MAC | Puerto/Switch |
|---|--------|-----|-----|---------------|
| 118 | esquina-invernadero | 192.168.31.118 | 74:83:c2:3f:bc:36 | US48 |
| 119 | esquina-inv-avenida | 192.168.31.119 | 74:83:c2:3f:c0:51 | US48 |

#### Zona Producción / Finca
| # | Nombre | IP | MAC | Puerto/Switch |
|---|--------|-----|-----|---------------|
| 113 | pasillo-gallinero | 192.168.31.113 | 74:83:c2:3f:c0:a2 | US48 |
| 124 | fabrica | 192.168.31.124 | 74:83:c2:3f:c0:46 | US48 |
| 125 | establo | 192.168.31.125 | 74:83:c2:3f:c0:a0 | US48 |

#### Zona Entradas
| # | Nombre | IP | MAC | Puerto/Switch |
|---|--------|-----|-----|---------------|
| 116 | entrada-cecil | 192.168.31.116 | 74:83:c2:3f:bf:15 | US48 |

---

## Rutas Críticas / Puntos de Falla

### Ruta 1: Zona Residencia (PROBLEMÁTICA)

```
UDM Pro → US48 → [Cable?] → Switch Hikvision (Biblioteca) → Cámara 114
                    ↑
            PUNTO DE FALLA IDENTIFICADO
```

**Problema:** Caídas intermitentes que afectan cámara 114 e internet de la zona.

**Historial de caídas:**
- 2025-10-21, 2025-11-04, 2025-11-08, 2025-11-13
- 2025-11-19, 2025-12-02, 2025-12-29
- 2026-01-24, 2026-01-26

**Acción requerida:** Revisar cable de uplink del switch Hikvision.

---

## Credenciales de Acceso

| Dispositivo | IP | Usuario | Método |
|-------------|-----|---------|--------|
| UDM Pro | 192.168.31.1 | root | SSH |
| UDM Pro | 192.168.31.1 | admin | Web UI |
| Switch Hikvision | N/A | N/A | No gestionable |

---

## Diagrama Físico (Por completar en sitio)

```
RACK PRINCIPAL                    BIBLIOTECA CASA SALESIANA
┌─────────────┐                   ┌─────────────┐
│   UDM PRO   │                   │   Switch    │
│             │                   │  Hikvision  │
├─────────────┤     Cable ?m      ├─────────────┤
│    US48     │◄─────────────────►│   (PoE)     │
│             │                   │             │
└─────────────┘                   └──────┬──────┘
                                         │
                                         │ Cable ?m
                                         ▼
                                  ┌─────────────┐
                                  │  Cámara 114 │
                                  │  Entrada    │
                                  │  Residencia │
                                  └─────────────┘
```

### Información por completar en sitio:

- [ ] Longitud del cable UDM/US48 → Switch Hikvision
- [ ] Longitud del cable Switch Hikvision → Cámara 114
- [ ] Modelo exacto del Switch Hikvision
- [ ] Número de puertos del Switch Hikvision
- [ ] Otros dispositivos conectados al Switch Hikvision
- [ ] Tipo de cable (Cat5e, Cat6, exterior/interior)
- [ ] Ruta física del cableado

---

## Historial de Cambios

| Fecha | Cambio | Responsable |
|-------|--------|-------------|
| 2026-02-03 | Documento inicial creado | - |
| | | |

---

*Actualizado: 2026-02-03*
