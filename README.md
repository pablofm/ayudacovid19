# Ayuda Covid 19

Este proyecto está probado con python 3.8.2.
Para instalarte este proyecto en primer lugar, deberías crear un entorno virtual para este proyecto (aunque este paso no es imprescindible).
Posteriormente los pasos habituales a cualquier proyecto django.
NOTA: Los correos se envían a través de celery, por lo que deberás lanzar una proceso independiente con el mismo con `celery -A coronavirus worker -l info`

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

## Importación de datos

En caso de que quieras importar datos de un excel que tengas, puedes hacerlo añadiendolos al fichero `importar_datos.csv`, dentro de las migraciones de las aplicaciones de colaboradores y peticiones, exactamente en `colaboradores/migrations/csv/plantilla_datos.csv` y `peticiones/migrations/csv/plantilla_datos.csv`. El delimitador del campo será el `;`.
Estos datos deben tener el formato 

    LATITUD;LONGITUD;NOMBRE;DISPONIBILIDAD;TELEFONO;CORREO;SERVICIO

## Fuentes

Incluye una app para contabilizar el número de peticiones que llegan de una determinada APP que haga uso del API REST.
Esta crea una key aleatoria (que deberá enviarse en cada petición POST, con la clave key) para cada una de las acciones 

Para ejecutar es necesario ejecutar el servidor así como celery


## API REST

Incluye un  API por si se quiere integrar el mapa con aplicaciones externas. En este caso, avisado a contacto@ayudacovid19.com, para poder hacer un seguimiento del "impacto" de vuestra aplicación (ver sección FUENTES)

### Colaboradores
#### Listar colaboradores
##### Request 
`GET /API/colaboradores/`
##### Response
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "id": 1,
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -5.984459,
          37.389091
        ]
      },
      "properties": {
        "nombre": "Pablo",
        "horario": "2",
        "mensaje": "Te ayudo en lo que quieras",
        "horario_verbose": "Todo el día"
      }
    }
  ]
}
```
#### Añadir nuevo colaborador
##### Request
`POST /API/colaboradores/`

```json
{
  "geom": {
    "type": "Point",
    "coordinates": [
      -5.984459,
      37.389091
    ]
  },
  "nombre": "Pablo",
  "email": "pablo@email.com",
  "telefono": "666666666",
  "mensaje": "Puedo ayudar con X, Y y Z",
  "horario": 1
}

```
``` python
# Donde horario puede tomar 3 valores:
    0 = "Mañanas"
    1 = "Tardes"
    2 = "Todo el día"
```

##### Response
```json
{
  "id": 1,
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [
      -5.984459,
      37.389091
    ]
  },
  "properties": {
    "horario_verbose": "Tardes",
    "nombre": "Pablo",
    "telefono": "666666666",
    "email": "pablo@email.com",
    "horario": "1",
    "mensaje": "Puedo ayudar con X, Y y Z"
  }
}
```


##### Pedir ayuda a un colaborador
```json
{
  "nombre": "Pablo",
  "email":"pablo@email.com",
  "telefono": "666666666",
  "mensaje": "Me gustaría que me ayudes con X, Y y Z",
  "colaborador": 1
}
```
  Donde colaborador es la ID de un colaborador existente en la BBDD.

### Peticiones
#### Listar peticiones
##### Request 
 : `GET /API/peticiones/`
##### Response
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -5.984459,
          37.389091
        ]
      },
      "properties": {
        "nombre": "Pablo",
        "mensaje": "Necesito X, Y y Z",
        "identificador": 1
      }
    }
  ]
}
```
#### Añadir nueva petición
##### Request
`POST /API/peticiones/`

```json
{
  "geom": {
    "type": "Point",
    "coordinates": [
      -5.984459,
      37.389091
    ]
  },
  "nombre": "Pablo",
  "email": "pablo@email.com",
  "telefono": "666666666",
  "mensaje": "Puedo ayudar con X, Y y Z"
}

```

##### Response
```json
{
  "id": 1,
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [
      -5.984459,
      37.389091
    ]
  },
  "properties": {
    "nombre": "Pablo",
    "telefono": "666666666",
    "email": "pablo@email.com",
    "mensaje": "Puedo ayudar con X, Y y Z",
    "atendida": false
  }
}
```


#### Ofrecer ayuda a una petición
```json
{
  "nombre": "Pablo",
  "email":"pablo@email.com",
  "telefono": "666666666",
  "mensaje": "Me gustaría que me ayudes con X, Y y Z",
  "peticion": 1
}
```
  Donde colaborador es la ID de una petición existente en la BBDD. Si la petición ya ha sido atendida, no permitirá la creación del objeto.

### Comercios
#### Listar comercios
##### Request 
 : `GET /API/comercios/`
##### Response
```json
{
  "type": "FeatureCollection",
  "features": [
      {
      "id": 1,
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -5.984459,
          37.389091
        ]
      },
      "properties": {
        "nombre": "Carnicería Pablo",
        "telefono": "666666666",
        "mensaje": "Abierto de L-V de 8 a 12"
      }
    }
  ]
}
```
#### Añadir nuevo comercio
##### Request
`POST /API/comercios/`

```json
{
  "geom": {
    "type": "Point",
    "coordinates": [
      -5.984459,
      37.389091
    ]
  },
  "nombre": "Carnicería Pablo",
  "telefono": "666666666",
  "mensaje": "Abierto de L-V de 8 a 12"
}

```
