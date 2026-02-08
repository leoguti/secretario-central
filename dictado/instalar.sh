#!/bin/bash
# instalar.sh - Instala el sistema de dictado por voz en una máquina nueva
# Requisitos: Ubuntu 24.04+ con Wayland, micrófono USB
# Uso: bash instalar.sh

set -euo pipefail

echo "=== Instalando sistema de dictado por voz ==="

# 1. Dependencias
echo "[1/6] Instalando paquetes..."
sudo apt install -y ffmpeg curl jq wl-clipboard ydotool ydotoold libnotify-bin

# 2. ydotoold daemon
echo "[2/6] Configurando ydotoold..."
if [ ! -f /etc/systemd/system/ydotoold.service ]; then
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
fi
sudo systemctl daemon-reload
sudo systemctl enable --now ydotoold

# 3. Permisos uinput (para ydotool en Wayland)
echo "[3/6] Configurando permisos uinput..."
echo 'KERNEL=="uinput", GROUP="input", MODE="0660"' | sudo tee /etc/udev/rules.d/80-uinput.rules > /dev/null
sudo chmod 0660 /dev/uinput
sudo chown root:input /dev/uinput
sudo usermod -aG input "$USER"

# 4. Copiar script
echo "[4/6] Instalando script dictado..."
mkdir -p ~/.local/bin
cp dictado ~/.local/bin/dictado
chmod +x ~/.local/bin/dictado

# 5. API key
echo "[5/6] Configurando API key..."
mkdir -p ~/.config/dictado
if [ ! -f ~/.config/dictado/.env ]; then
    read -rp "Ingresa tu OpenAI API key: " API_KEY
    echo "OPENAI_API_KEY=\"$API_KEY\"" > ~/.config/dictado/.env
    chmod 600 ~/.config/dictado/.env
    echo "   API key guardada en ~/.config/dictado/.env"
else
    echo "   ~/.config/dictado/.env ya existe, saltando..."
fi

# 6. Atajo de teclado F9 en GNOME
echo "[6/6] Configurando hotkey F9..."
EXISTING=$(gsettings get org.gnome.settings-daemon.plugins.media-keys custom-keybindings 2>/dev/null)
if [[ "$EXISTING" != *"dictado"* ]]; then
    gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings \
        "['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/']"
    gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ \
        name 'Dictado'
    gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ \
        command "$HOME/.local/bin/dictado"
    gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ \
        binding 'F9'
fi

echo ""
echo "=== Instalacion completa ==="
echo ""
echo "IMPORTANTE: Cierra sesion y vuelve a entrar para que el grupo 'input' surta efecto."
echo ""
echo "Uso:"
echo "  F9 → empieza a grabar"
echo "  F9 → para, transcribe y escribe el texto donde este el cursor"
echo ""
echo "Log: /tmp/dictado.log"
