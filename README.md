# Ayuda Covid 19

Este proyecto está probado con python 3.8.2.

Para instalarte este proyecto en primer lugar, deberías crear un entorno virtual para este proyecto (aunque este paso no es imprescindible).

Posteriormente los pasos habituales a cualquier proyecto django.

1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py runserver


## Plantilla de datos a importar

En caso de que quieras importar datos de un excel que tengas, puedes hacerlo añadiendolos al fichero `importar_datos.csv`, dentro de las migraciones de las aplicaciones de colaboradores y peticiones, exactamente en `colaboradores/migrations/csv/plantilla_datos.csv` y `peticiones/migrations/csv/plantilla_datos.csv`. El delimitador del campo será el `;`.
Estos datos deben tener el formato 

>    LATITUD;LONGITUD;NOMBRE;DISPONIBILIDAD;TELEFONO;CORREO;SERVICIO
