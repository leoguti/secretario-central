#!/bin/bash
# Script para monitorear el transcript de Google Meet en tiempo real

DOWNLOADS_DIR="$HOME/Descargas"
TRANSCRIPT_FILE="$DOWNLOADS_DIR/gmeet_transcript_live.txt"

echo "🎙️  Monitoreando transcript de Google Meet..."
echo "📁 Archivo: $TRANSCRIPT_FILE"
echo "🔄 Actualizando cada 5 segundos..."
echo "-------------------------------------------"
echo ""

while true; do
    if [ -f "$TRANSCRIPT_FILE" ]; then
        clear
        echo "🎙️  TRANSCRIPT EN VIVO - $(date '+%H:%M:%S')"
        echo "=================================================="
        echo ""
        cat "$TRANSCRIPT_FILE"
        echo ""
        echo "=================================================="
        echo "🔄 Última actualización: $(date '+%H:%M:%S')"
    else
        echo "⏳ Esperando transcript... (archivo no encontrado aún)"
    fi
    sleep 5
done
