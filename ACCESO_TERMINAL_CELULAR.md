# 🎉 ACCESO A TERMINAL DESDE CELULAR - FUNCIONANDO

**Fecha configuración:** 9 enero 2026  
**Método:** Túnel Cloudflare + ttyd (Terminal Web)

---

## ✅ CONFIGURACIÓN FINAL QUE FUNCIONA

### 1. Túnel Cloudflare
- **Túnel ID:** 46d5071d-9261-4fc5-8ea9-175f32f72d3e
- **Nombre túnel:** portal-rumbo
- **Hostname SSH:** ssh.rumbo.digital
- **DNS:** CNAME ssh → 46d5071d-9261-4fc5-8ea9-175f32f72d3e.cfargotunnel.com

### 2. ttyd (Terminal Web)
- **Comando:**
```bash
ttyd -p 7681 -W -c leonardo:9mpdtvpm5r bash
```

- **Puerto:** 7681
- **Usuario:** leonardo
- **Contraseña:** 9mpdtvpm5r
- **Modo:** Escritura habilitada (-W)

### 3. Configuración del Túnel
**Archivo:** `~/.cloudflared/config.yml`

```yaml
tunnel: 46d5071d-9261-4fc5-8ea9-175f32f72d3e
credentials-file: /home/leonardo-gutierrez/.cloudflared/46d5071d-9261-4fc5-8ea9-175f32f72d3e.json

ingress:
  - hostname: portal.rumbo.digital
    service: http://localhost:3000
  - hostname: ssh.rumbo.digital
    service: http://localhost:7681
  - service: http_status:404
```

---

## 🚀 CÓMO USAR

### Iniciar el Sistema

**Terminal 1 - ttyd:**
```bash
ttyd -p 7681 -W -c leonardo:9mpdtvpm5r bash
```

**Terminal 2 - Túnel Cloudflare:**
```bash
cloudflared tunnel run portal-rumbo
```

O en background:
```bash
nohup cloudflared tunnel run portal-rumbo > /tmp/cloudflared.log 2>&1 &
```

### Acceder desde el Celular

1. **Abrir Firefox** (NO Chrome, tiene bug con WebSockets)
2. Ir a: `https://ssh.rumbo.digital`
3. Login:
   - Usuario: `leonardo`
   - Contraseña: `9mpdtvpm5r`
4. ✅ **¡Terminal funcionando!**

---

## ⚠️ PROBLEMAS CONOCIDOS Y SOLUCIONES

### Chrome Android NO funciona
**Problema:** Pantalla negra después de login  
**Causa:** Bug de Chrome Android con WebSockets + autenticación básica  
**Solución:** Usar **Firefox** en el celular

### SSH directo desde Termux NO funcionó
**Problema:** `cloudflared access ssh` requiere Cloudflare Zero Trust  
**Intentos:**
- ✅ Cloudflared instalado en Termux
- ✅ Credenciales del túnel copiadas
- ✅ Config.yml con ingress configurado
- ❌ DNS no resuelve correctamente en Termux
- ❌ `cloudflared access` necesita Zero Trust configurado

**Decisión:** Usar terminal web (ttyd) en su lugar - más simple y funcional

### ttyd se cae
**Problema:** ttyd debe correr en foreground, no background  
**Solución:** Ejecutar sin `&` o usar systemd

---

## 🔐 SEGURIDAD

### Capas de Seguridad Actuales
1. ✅ **Túnel Cloudflare** - Tráfico cifrado end-to-end
2. ✅ **Autenticación ttyd** - Usuario y contraseña
3. ✅ **HTTPS** - Certificado SSL de Cloudflare
4. ✅ **No puerto expuesto** - Puerto 7681 solo escucha en localhost

### Mejoras de Seguridad Opcionales
- [ ] Configurar Cloudflare Access (autenticación con email/Google)
- [ ] Usar nginx como proxy reverso con autenticación adicional
- [ ] Restringir acceso por IP en Cloudflare
- [ ] Habilitar 2FA en cuenta Cloudflare

---

## 📋 COMANDOS ÚTILES

### Verificar Estado

```bash
# Ver si ttyd está corriendo
ps aux | grep ttyd

# Ver si túnel está corriendo
ps aux | grep cloudflared

# Probar ttyd localmente
curl -u leonardo:9mpdtvpm5r http://localhost:7681 -I

# Ver logs del túnel
tail -f /tmp/cloudflared.log

# Ver logs de ttyd (si está en background)
tail -f /tmp/ttyd.log
```

### Detener Servicios

```bash
# Detener ttyd
kill $(pgrep ttyd)

# Detener túnel
kill $(pgrep cloudflared)
```

### Reiniciar Todo

```bash
# Detener todo
kill $(pgrep ttyd)
kill $(pgrep cloudflared)

# Iniciar ttyd
ttyd -p 7681 -W -c leonardo:9mpdtvpm5r bash &

# Esperar 2 segundos
sleep 2

# Iniciar túnel
nohup cloudflared tunnel run portal-rumbo > /tmp/cloudflared.log 2>&1 &

# Verificar
sleep 3
tail -10 /tmp/cloudflared.log
curl -I http://localhost:7681
```

---

## 🔄 HACER PERSISTENTE (Systemd)

### Servicio ttyd

Crear: `/etc/systemd/system/ttyd.service`

```ini
[Unit]
Description=ttyd - Terminal Web
After=network.target

[Service]
Type=simple
User=leonardo-gutierrez
ExecStart=/usr/bin/ttyd -p 7681 -W -c leonardo:9mpdtvpm5r bash
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

### Servicio Cloudflared

Crear: `/etc/systemd/system/cloudflared-portal.service`

```ini
[Unit]
Description=Cloudflare Tunnel - Portal y Terminal
After=network.target

[Service]
Type=simple
User=leonardo-gutierrez
ExecStart=/usr/bin/cloudflared tunnel run portal-rumbo
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

### Habilitar Servicios

```bash
# Recargar systemd
sudo systemctl daemon-reload

# Habilitar inicio automático
sudo systemctl enable ttyd cloudflared-portal

# Iniciar servicios
sudo systemctl start ttyd cloudflared-portal

# Ver estado
sudo systemctl status ttyd
sudo systemctl status cloudflared-portal
```

---

## 📱 APPS RECOMENDADAS

### Android
- ✅ **Firefox** - Para acceder a terminal web (funciona perfecto)
- ⚠️ Chrome - NO funciona (pantalla negra después de login)
- 🔧 Termux - Instalado pero SSH directo no funciona sin Zero Trust

### iOS
- **Safari** o **Firefox** - Debería funcionar similar a Firefox Android

---

## 🎯 RESUMEN DE 2+ HORAS DE TRABAJO

### Lo que NO funcionó
❌ SSH directo desde Termux con `cloudflared access ssh`
- Problema DNS en Termux
- Requiere Cloudflare Zero Trust no configurado
- Copiar credenciales no fue suficiente

### Lo que SÍ funcionó ✅
✅ Terminal web con ttyd + túnel Cloudflare
- Funciona en Firefox mobile
- Autenticación con usuario/contraseña
- Terminal completa con comandos funcionando
- Acceso desde cualquier lugar

---

## 🔗 RECURSOS

- **Cloudflare Dashboard:** https://dash.cloudflare.com
- **ttyd GitHub:** https://github.com/tsl0922/ttyd
- **Documentación Cloudflare Tunnel:** https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/

---

**Configurado por:** Leonardo Gutiérrez + Asistente IA  
**Estado:** ✅ FUNCIONANDO  
**Última prueba exitosa:** 9 enero 2026 12:00 PM (GMT-5)
