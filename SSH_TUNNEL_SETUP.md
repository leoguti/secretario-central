# SSH Tunnel - Acceso Remoto Secretario

## 📋 Configuración Actual

**Túnel SSH:** `ssh.rumbo.digital`  
**Túnel ID:** `46d5071d-9261-4fc5-8ea9-175f32f72d3e` (compartido con portal-rumbo)  
**Usuario SSH:** `leonardo-gutierrez`  
**Proyecto:** `/home/leonardo-gutierrez/secretario`

---

## 📱 Conectarse desde Celular

### Android: Termux

1. **Instalar Termux** desde F-Droid o Play Store
2. **Instalar cloudflared en Termux:**
```bash
pkg install wget
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64
chmod +x cloudflared-linux-arm64
mv cloudflared-linux-arm64 $PREFIX/bin/cloudflared
```

3. **Conectarse:**
```bash
ssh -o ProxyCommand="cloudflared access ssh --hostname %h" leonardo-gutierrez@ssh.rumbo.digital
```

### iOS: OpenTerm / Blink Shell

Similar a Android, necesitas instalar cloudflared y usar el mismo comando SSH.

---

## 💻 Conectarse desde Computadora

### Linux/Mac

```bash
# Instalar cloudflared (si no lo tienes)
# En Ubuntu/Debian:
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb

# Conectarse
ssh -o ProxyCommand="cloudflared access ssh --hostname %h" leonardo-gutierrez@ssh.rumbo.digital
```

### Configuración SSH permanente (~/.ssh/config)

```
Host secretario
    HostName ssh.rumbo.digital
    User leonardo-gutierrez
    ProxyCommand cloudflared access ssh --hostname %h
```

Luego solo ejecutar: `ssh secretario`

---

## 🚀 Estado del Túnel

### Verificar que el túnel está corriendo
```bash
ps aux | grep cloudflared
```

### Ver logs del túnel
```bash
tail -f /tmp/cloudflared.log
```

### Iniciar túnel (si está detenido)
```bash
nohup cloudflared tunnel run portal-rumbo > /tmp/cloudflared.log 2>&1 &
```

### Detener túnel
```bash
# Encontrar PID
ps aux | grep cloudflared | grep -v grep

# Detener con PID
kill <PID>
```

---

## 📁 Archivos de Configuración

### Configuración del Túnel
**Ubicación:** `~/.cloudflared/config.yml`

```yaml
tunnel: 46d5071d-9261-4fc5-8ea9-175f32f72d3e
credentials-file: /home/leonardo-gutierrez/.cloudflared/46d5071d-9261-4fc5-8ea9-175f32f72d3e.json

ingress:
  - hostname: portal.rumbo.digital
    service: http://localhost:3000
  - hostname: ssh.rumbo.digital
    service: ssh://localhost:22
  - service: http_status:404
```

### DNS Cloudflare
- **CNAME:** `ssh.rumbo.digital` → `46d5071d-9261-4fc5-8ea9-175f32f72d3e.cfargotunnel.com`

---

## 🔐 Seguridad

### Autenticación
- ✅ Solo acceso con clave SSH (autenticación por contraseña deshabilitada)
- ✅ Tráfico cifrado end-to-end con Cloudflare
- ✅ No expone puerto 22 directamente
- ✅ Sin necesidad de IP pública estática

### Agregar clave SSH desde celular

```bash
# En Termux, generar clave si no tienes
ssh-keygen -t ed25519 -C "celular-termux"

# Copiar clave pública al servidor (desde PC o cuando estés conectado)
ssh-copy-id -o ProxyCommand="cloudflared access ssh --hostname %h" leonardo-gutierrez@ssh.rumbo.digital
```

---

## 🛠️ Comandos Útiles al Conectarse

### Acceder al proyecto
```bash
cd ~/secretario
```

### Activar entorno virtual (si usas uno)
```bash
source venv/bin/activate  # si existe
```

### Ejecutar scripts
```bash
python app.py
python revisar_importante.py
```

### Ver archivos importantes
```bash
cat PROYECTO_ACTUAL.md
cat POLITICAS_TRABAJO.md
```

---

## 🆘 Troubleshooting

### Error: "Connection refused"
**Causa:** Túnel no está corriendo

**Solución:**
```bash
# En el servidor
nohup cloudflared tunnel run portal-rumbo > /tmp/cloudflared.log 2>&1 &
```

### Error: "Permission denied (publickey)"
**Causa:** Clave SSH no configurada

**Solución:**
```bash
# Copiar tu clave pública al servidor
ssh-copy-id -o ProxyCommand="cloudflared access ssh --hostname %h" leonardo-gutierrez@ssh.rumbo.digital
```

### DNS no resuelve
**Causa:** Propagación DNS o caché

**Solución:**
```bash
# Verificar DNS
dig ssh.rumbo.digital +short

# Debería mostrar: 46d5071d-9261-4fc5-8ea9-175f32f72d3e.cfargotunnel.com
```

---

## 📝 Notas Importantes

1. **Túnel Cloudflare es GRATUITO**
2. **Sin límites de conexiones SSH**
3. **No requiere abrir puertos en router/firewall**
4. **Comparte el mismo túnel con portal.rumbo.digital**
5. **Backup del config:** `~/.cloudflared/config.yml.backup`

---

## 🔄 Hacer Persistente el Túnel (Opcional)

### Crear servicio systemd

```bash
sudo systemctl edit --force --full cloudflared-portal.service
```

Contenido:
```ini
[Unit]
Description=Cloudflare Tunnel - Portal y SSH
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

Comandos:
```bash
sudo systemctl daemon-reload
sudo systemctl enable cloudflared-portal
sudo systemctl start cloudflared-portal
```

---

**Fecha de configuración:** 9 de enero de 2026  
**Configurado por:** Leonardo Gutiérrez
