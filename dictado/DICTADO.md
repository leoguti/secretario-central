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

## Instalacion manual

### 1. Paquetes

```bash
sudo apt install -y ffmpeg curl jq wl-clipboard ydotool ydotoold libnotify-bin
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

### 5. API key

```bash
mkdir -p ~/.config/dictado
echo 'OPENAI_API_KEY="sk-proj-TU_KEY_AQUI"' > ~/.config/dictado/.env
chmod 600 ~/.config/dictado/.env
```

### 6. Hotkey F9 en GNOME

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
| `~/.config/dictado/.env` | API key (permisos 600) |
| `/etc/udev/rules.d/80-uinput.rules` | Permisos uinput |
| `/etc/systemd/system/ydotoold.service` | Daemon ydotool |
| `/tmp/dictado.log` | Log de sesion |

## Notas tecnicas

- **ffmpeg -f pulse** en vez de arecord: arecord corta la grabacion en las pausas con PipeWire
- **kill -INT** para parar ffmpeg: cierra el WAV con headers correctos
- **sg input** como wrapper de ydotool: permite usar ydotool sin re-login tras agregar el grupo
- Grabacion maxima: 2 minutos (configurable con `-t` en ffmpeg)
- Costo: ~$0.006/minuto de audio (Whisper API)
