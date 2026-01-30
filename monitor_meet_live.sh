#!/bin/bash
# Monitor Google Meet transcript and report new content every 10 seconds

TRANSCRIPT_FILE="$HOME/Descargas/gmeet_transcript_live.txt"
LAST_SIZE=0

echo "🎙️ MONITOREANDO REUNIÓN EN VIVO"
echo "================================"
echo "Actualizando cada 10 segundos..."
echo ""

while true; do
    if [ -f "$TRANSCRIPT_FILE" ]; then
        CURRENT_SIZE=$(wc -c < "$TRANSCRIPT_FILE" 2>/dev/null || echo "0")
        
        if [ "$CURRENT_SIZE" -gt "$LAST_SIZE" ]; then
            echo "📥 NUEVO CONTENIDO DETECTADO - $(date '+%H:%M:%S')"
            echo "----------------------------------------"
            
            # Show only the new content
            tail -c +$((LAST_SIZE + 1)) "$TRANSCRIPT_FILE" | head -20
            
            echo ""
            echo "💬 Resumen: $(tail -c +$((LAST_SIZE + 1)) "$TRANSCRIPT_FILE" | wc -w) nuevas palabras"
            echo "=========================================="
            echo ""
            
            LAST_SIZE=$CURRENT_SIZE
        fi
    else
        echo "⏳ Esperando transcript inicial..."
    fi
    
    sleep 10
done
