# Reunión CampoLimpio - Externos

**Fecha:** 10 de febrero de 2026
**Tipo:** Reunión de externos

## Asistentes

- Daniel Pineda (plataforma web y contenido de cursos)
- Roberto
- Sarah Roberto
- Angela
- Ivan
- Leonardo Gutiérrez

---

## 1. Hackeo a la página de CampoLimpio (semana pasada)

**Reporta Daniel Pineda:**

- La semana pasada hackearon la página de CampoLimpio
- Metieron contenido de ventas y reemplazaron la página inicial
- Hubo intentos de cambio de clave en dos ocasiones
- Para llegar a ese nivel, ya tenían conocimiento del correo del titular
- El correo del titular no estaba tan expuesto, pero se puede encontrar vía registros DNS u otros métodos
- En algún momento hubo una brecha de información
- Después de escanear, confirmaron que solo fueron afectados CampoLimpio y SEHXMED (empresa de Estados Unidos)
- No fue un hackeo dirigido/personal, fue automatizado (bots)

### Posible origen de la brecha

- Al contador le intentaron hackear el correo (incidente de un millón de pesos)
- Probablemente la brecha vino por ahí
- No se logró determinar exactamente cómo fue la brecha
- Pudo haber sido algo tan simple como una contraseña guardada en algún computador o compartida en algún momento

### Segundo intento

- En el segundo intento accedieron a la clave del hosting
- El hosting colaboró bien: proporcionó registros mostrando intentos de acceso

### Acciones tomadas

- Se instaló un Firewall (herramienta gratuita)
- Se analizó y eliminó el contenido dañado/corrupto
- Se cambiaron todas las claves: panel, hosting, absolutamente todo
- Se activó autenticación de dos factores (2FA)
- Daniel sigue haciendo monitoreo/escaneos, no ha detectado nada más

### Recomendaciones de seguridad

- Manejar un solo titular de correo para todas las credenciales (Rachel Lewis parece ser el más adecuado)
- Si hay un problema, ese titular respalda toda la información
- Revisar y eliminar extensiones de Chrome no originales o widgets sospechosos que ya no estén habilitados

---

## 2. Plataforma LMS (cursos)

- El LMS está sobre WordPress
- Se maneja a través de un plugin
- La instalación completa está radicada en WordPress

---

*Notas tomadas por: Leonardo Gutiérrez*
