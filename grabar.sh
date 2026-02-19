#!/bin/bash
# Grabar audio de Google Meet + micrófono para Whisper
# Uso: ./grabar.sh [nombre_archivo]
# Presiona 'q' o Ctrl+C para detener la grabación

ARCHIVO="${1:-/tmp/meet_grabacion.wav}"
MIC="alsa_input.usb-EMEET_HD_Webcam_eMeet_C960_A230206000807238-02.analog-stereo"
MONITOR="alsa_output.pci-0000_00_1f.3.analog-stereo.monitor"

echo "=== GRABANDO MEET + MICRÓFONO ==="
echo "Micrófono: eMeet C960"
echo "Navegador: Monitor de Built-in Audio"
echo "Archivo:   $ARCHIVO"
echo ""
echo "Presiona 'q' para detener"
echo ""

ffmpeg -y \
  -f pulse -i "$MIC" \
  -f pulse -i "$MONITOR" \
  -filter_complex "amix=inputs=2:duration=longest" \
  -ac 1 -ar 16000 \
  "$ARCHIVO"

echo ""
echo "=== GRABACIÓN GUARDADA ==="
echo "Archivo: $ARCHIVO"
echo "Tamaño:  $(du -h "$ARCHIVO" 2>/dev/null | cut -f1)"
echo ""
echo "Para transcribir con Whisper:"
echo "  whisper $ARCHIVO --language es --model base"
