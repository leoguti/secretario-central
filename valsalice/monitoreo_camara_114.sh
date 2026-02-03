#!/bin/bash
# Monitoreo de cámara 192.168.31.114 (entrada-interno-residencia)
# Detecta caídas y las registra en un log

CAMARA_IP="192.168.31.114"
CAMARA_NOMBRE="entrada-interno-residencia"
LOG_FILE="/home/leonardo/secretario/valsalice/log_camara_114.txt"
INTERVALO=60  # segundos entre pings

echo "=== Iniciando monitoreo de $CAMARA_NOMBRE ($CAMARA_IP) ===" | tee -a "$LOG_FILE"
echo "Fecha inicio: $(date)" | tee -a "$LOG_FILE"
echo "Intervalo: cada $INTERVALO segundos" | tee -a "$LOG_FILE"
echo "Log: $LOG_FILE" | tee -a "$LOG_FILE"
echo "Presiona Ctrl+C para detener" | tee -a "$LOG_FILE"
echo "---" | tee -a "$LOG_FILE"

while true; do
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    PING_RESULT=$(ping -c 3 -W 5 $CAMARA_IP 2>&1)
    LOSS=$(echo "$PING_RESULT" | grep -oP '\d+(?=% packet loss)')

    if [ "$LOSS" = "0" ]; then
        # Online - solo mostrar en pantalla, no en log
        echo "[$TIMESTAMP] OK - $CAMARA_NOMBRE online (0% loss)"
    else
        # Pérdida o caída - registrar en log
        echo "[$TIMESTAMP] ALERTA - $CAMARA_NOMBRE: $LOSS% packet loss" | tee -a "$LOG_FILE"
        if [ "$LOSS" = "100" ]; then
            echo "[$TIMESTAMP] CAÍDA - $CAMARA_NOMBRE NO RESPONDE" | tee -a "$LOG_FILE"
        fi
    fi

    sleep $INTERVALO
done
