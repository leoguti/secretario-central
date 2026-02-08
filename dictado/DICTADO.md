# Dictado por Voz para Claude Code

Sistema de dictado por voz que usa Whisper API (OpenAI) para transcribir audio y escribirlo directamente en la terminal o cualquier ventana activa.

## Requisitos

- Ubuntu 24.04+ con Wayland (GNOME)
- Micrófono USB (probado con eMeet C960)
- API key de OpenAI (https://platform.openai.com/api-keys)
- Conexion a internet

## Instalacion rapida

```bash
cd dictado/
bash instalar.sh
```

Luego cerrar sesion y volver a entrar (para que el grupo `input` surta efecto).

## API key: 1Password (recomendado) o .env

### Opcion A: 1Password (sin archivos .env)

El script lee la key directo de 1Password cada vez. No se guarda nada en disco.

```bash
# Instalar 1Password CLI
curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
  sudo gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] https://downloads.1password.com/linux/debian/$(dpkg --print-architecture) stable main" | \
  sudo tee /etc/apt/sources.list.d/1password-cli.list
sudo apt update && sudo apt install -y 1password-cli

# Configurar cuenta
eval $(op signin)

# Guardar la API key en 1Password
op item create --category Password --title "OpenAI API Key" 'password=sk-proj-TU_KEY_AQUI'
```

Ventaja: cambias la key en 1Password y funciona en todas tus maquinas.

### Opcion B: Archivo .env (fallback)

```bash
mkdir -p ~/.config/dictado
echo 'OPENAI_API_KEY="sk-proj-TU_KEY_AQUI"' > ~/.config/dictado/.env
chmod 600 ~/.config/dictado/.env
```

El script intenta 1Password primero. Si no esta disponible, usa el .env.

## Instalacion manual

### 1. Paquetes

```bash
sudo apt install -y pipewire curl jq wl-clipboard ydotool ydotoold libnotify-bin
```

### 2. ydotoold (daemon para escribir en Wayland)

```bash
sudo bash -c 'cat > /etc/systemd/system/ydotoold.service << EOF
[Unit]
Description=ydotool daemon
After=multi-user.target

[Service]
ExecStart=/usr/bin/ydotoold
Restart=always

[Install]
WantedBy=multi-user.target
EOF'
sudo systemctl daemon-reload
sudo systemctl enable --now ydotoold
```

### 3. Permisos uinput

```bash
echo 'KERNEL=="uinput", GROUP="input", MODE="0660"' | sudo tee /etc/udev/rules.d/80-uinput.rules
sudo chmod 0660 /dev/uinput
sudo chown root:input /dev/uinput
sudo usermod -aG input $USER
```

### 4. Script

```bash
cp dictado ~/.local/bin/dictado
chmod +x ~/.local/bin/dictado
```

### 5. Hotkey F9 en GNOME

```bash
gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings \
    "['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/']"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ \
    name 'Dictado'
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ \
    command "$HOME/.local/bin/dictado"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ \
    binding 'F9'
```

## Uso

1. **F9** → empieza a grabar (notificacion: "Grabando...")
2. Hablar normalmente, las pausas no cortan la grabacion
3. **F9** → para grabacion, transcribe via Whisper API, escribe texto en la ventana activa

Si ydotool no funciona (antes de re-login), el texto queda en el portapapeles → **Ctrl+Shift+V** para pegar.

## Archivos

| Archivo | Descripcion |
|---|---|
| `~/.local/bin/dictado` | Script principal |
| `op://Private/OpenAI API Key/password` | API key en 1Password |
| `~/.config/dictado/.env` | API key fallback (opcional) |
| `/etc/udev/rules.d/80-uinput.rules` | Permisos uinput |
| `/etc/systemd/system/ydotoold.service` | Daemon ydotool |
| `/tmp/dictado.log` | Log de sesion |

## Notas tecnicas

- **pw-record** para grabar: nativo de PipeWire, no se corta en pausas (arecord y ffmpeg si)
- **kill -INT** para parar pw-record: cierra el WAV con headers correctos
- **sg input** como wrapper de ydotool: permite usar ydotool sin re-login tras agregar el grupo
- **1Password > .env**: el script intenta `op read` primero, fallback a .env
- Grabacion maxima: 5 minutos
- Costo: ~$0.006/minuto de audio (Whisper API)
