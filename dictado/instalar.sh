#!/bin/bash
# instalar.sh - Instala el sistema de dictado por voz en una máquina nueva
# Requisitos: Ubuntu 24.04+ con Wayland, micrófono USB
# Uso: bash instalar.sh

set -euo pipefail

echo "=== Instalando sistema de dictado por voz ==="

# 1. Dependencias
echo "[1/7] Instalando paquetes..."
sudo apt install -y pipewire curl jq wl-clipboard ydotool ydotoold libnotify-bin

# 2. ydotoold daemon
echo "[2/7] Configurando ydotoold..."
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
echo "[3/7] Configurando permisos uinput..."
echo 'KERNEL=="uinput", GROUP="input", MODE="0660"' | sudo tee /etc/udev/rules.d/80-uinput.rules > /dev/null
sudo chmod 0660 /dev/uinput
sudo chown root:input /dev/uinput
sudo usermod -aG input "$USER"

# 4. Copiar script
echo "[4/7] Instalando script dictado..."
mkdir -p ~/.local/bin
cp dictado ~/.local/bin/dictado
chmod +x ~/.local/bin/dictado

# 5. API key (1Password o manual)
echo "[5/7] Configurando API key..."
if command -v op &>/dev/null; then
    echo "   1Password CLI detectado."
    echo "   Verificando acceso a 'op://Private/OpenAI API Key/password'..."
    if op read "op://Private/OpenAI API Key/password" &>/dev/null; then
        echo "   API key encontrada en 1Password. No se necesita archivo .env."
    else
        echo "   No se encontro la key en 1Password."
        echo "   Guarda tu OpenAI API key en 1Password con:"
        echo "     op item create --category Password --title 'OpenAI API Key' 'password=sk-proj-TU_KEY'"
    fi
else
    echo "   1Password CLI no instalado. Usando archivo .env."
    mkdir -p ~/.config/dictado
    if [ ! -f ~/.config/dictado/.env ]; then
        read -rp "   Ingresa tu OpenAI API key: " API_KEY
        echo "OPENAI_API_KEY=\"$API_KEY\"" > ~/.config/dictado/.env
        chmod 600 ~/.config/dictado/.env
        echo "   API key guardada en ~/.config/dictado/.env"
    else
        echo "   ~/.config/dictado/.env ya existe, saltando..."
    fi
fi

# 6. 1Password CLI (opcional)
echo "[6/7] 1Password CLI..."
if ! command -v op &>/dev/null; then
    echo "   (Opcional) Para usar 1Password en vez de .env:"
    echo "   https://developer.1password.com/docs/cli/get-started/"
else
    echo "   1Password CLI ya instalado ($(op --version))"
fi

# 7. Atajo de teclado F9 en GNOME
echo "[7/7] Configurando hotkey F9..."
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
echo "API key: 1Password (op://Private/OpenAI API Key/password) o ~/.config/dictado/.env"
echo "Log: /tmp/dictado.log"
