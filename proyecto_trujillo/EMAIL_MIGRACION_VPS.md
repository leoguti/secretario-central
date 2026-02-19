Estimados,

Con respecto a la infraestructura de la plataforma OMUS, les comparto los detalles:

## Situación actual

El sistema se encuentra desplegado en un VPS (servidor virtual privado) en DigitalOcean, que actualmente está bajo nuestra cuenta. Los componentes que corren en el servidor son:

- **Frontend**: Aplicación web Flutter servida por Nginx
- **Backend**: API en .NET 8
- **Base de datos**: MySQL 8.0
- **Reverse proxy**: Manejo automático de certificados SSL y enrutamiento

Todo funciona mediante contenedores Docker dentro del mismo servidor.

## Acceso a la plataforma

El acceso a la plataforma se entregó durante la entrega del proyecto el año pasado. Si necesitan que se los reenviemos, con gusto lo hacemos.

## Migración del VPS

Es totalmente posible migrar el servidor a una cuenta de DigitalOcean gestionada por ustedes. Podemos guiarlos en este proceso, que básicamente consiste en:

1. Crear una cuenta propia en DigitalOcean
2. Transferir el Droplet (VPS) desde nuestra cuenta a la de ustedes
3. Actualizar la configuración de DNS del dominio para que apunte correctamente

Es un procedimiento estándar que DigitalOcean soporta. Podemos dedicarle tiempo para acompañarlos y asegurarnos de que todo quede funcionando correctamente.

## Acceso SSH al servidor

Si además necesitan acceso directo al servidor por SSH (línea de comandos), necesitaríamos que nos envíen una **clave pública SSH** de la persona que vaya a acceder. Con esa clave los damos de alta en el servidor de forma segura. Si necesitan orientación sobre cómo generar esta clave, con gusto les explicamos el procedimiento.

## Plazo

No hay apuro de nuestra parte. Podemos mantener el servidor en nuestra cuenta **hasta finales de marzo** sin ningún problema, mientras ustedes definen los detalles internamente: la cuenta de DigitalOcean, el personal encargado, los accesos que necesiten, etc. Queremos que tengan tranquilidad para organizar todo esto a su ritmo.

Quedamos atentos a cualquier consulta.

Saludos cordiales
