
## ThinkPad L14 Gen 1 (20U6) - Fan descontrolado y actualización de BIOS

### Problema
El ventilador se dispara constantemente sin razón térmica aparente (CPU 25°C, GPU 24°C).

### Diagnóstico
- **thermald** está muerto porque no soporta AMD Ryzen (solo Intel)
- El sensor del fan reporta 0 RPM aunque se escucha girando
- El fan está en modo `auto` controlado por BIOS/EC
- El EC (Embedded Controller v1.17) es el responsable del control del fan

### Solución: Actualizar BIOS + EC
- **BIOS actual**: R19ET52W (1.36) / EC: R19HT33W (1.17)
- **BIOS nueva**: R19ET55W (1.39) / EC: R19HT35W (1.19)
- Fuente: https://support.lenovo.com/us/en/downloads/ds545476

### Procedimiento desde Linux
1. `sudo apt install genisoimage`
2. `wget -O /tmp/r19ur29w.iso https://download.lenovo.com/pccbbs/mobiles/r19ur29w.iso`
3. `geteltorito -o /tmp/bios-l14.img /tmp/r19ur29w.iso`
4. Conectar USB, identificar con `lsblk`, desmontar particiones
5. `sudo dd if=/tmp/bios-l14.img of=/dev/sdX bs=1M status=progress && sudo sync`
6. Reiniciar, F12, bootear desde USB, dejar flashear con cargador conectado

### Notas adicionales
- thinkfan SÍ funciona en AMD (usa thinkpad_acpi, no depende del CPU)
- fwupd ofrece v1.37 pero solo actualiza PSP de AMD, no el EC
- La v1.39 de Lenovo web incluye EC 1.19 que es donde está el fix del fan
- Fecha: 2026-01-30
