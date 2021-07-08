# Dell Waranty Query and Store

## Mercado/Sector

## Que es lo que quiero lograr:

Este proyecto tiene como objetivo agilizar los reemplazos de equipos de computo de la marca DELL en una empresa Medica con el fin
de acelerar el proceso de cambio de equipos que se encuentra fuera de garantia y suponen un riesgo para la empresa Medica.

## El proyecto consiste en:
El pyoyecto consiste en que el encargado o los encargados de los movimientos de equipos ingresen los numeros de serie de los
equipos de computo, para que estos sean consultados en el sitio web de DELL "Dell Warranty" y obtener las fechas de
expiracion para posteriormente desplegarlas en una pagina segun su proximidad a expirar para llevar un mejor orden y
metodos de consultas sobre los equipos
 

## Modelado de datos

Para el control del sistema de este proyecto tendremos las siguietes entidades

- Usuario(Nombre,estatus,num_empleado)

- Equipo(servicetag,fecha_ingreso,marca,fecha_expiracion)



## Interacciones de datos y operaciones de datos

 Operaciones de Almacenamiento de datos

# Operacion de Usuario

### Registrar usuario

- Solicitar nombre y numero de empleado
- El numero de empleado se asigna a todos los empleados
### Actualizacion de usuario

- Dar de baja usuarios

### Operacion de equipos

- Solicitar servicetag, fecha de ingreso
- La fecha de expiracion se buscara en /dell/info/<id>
- Dar de baja equipos


## Consultas de datos

### Operaciones de consulta de datos

 - Solicitar datos del equipo
 - Basicos
 - Garantia

## Rutas HTTP


# API

| Path                  | Descripción |
| --------------------- | ----------- |
| /dell/store           | En esta ruta se almacenan los numeros de serie de los equipos ingresados por los usuarios                       |
| /dell/info/<id>       | En esta ruta se encuentra la informacion por ID de los equipos en propiedad                                     |
| /dell/void            | En esta ruta se encuentran los numeros de serie de los equipos de los cuales su garantia ha expirado            |



## Ejemplos de mensajes HTTP

## Estructura de solicitud de solicitud y respuesta

## Registro de usuario

        {
        "nombre": "Daniel Alcaraz",
        "num_empleado": "XXXXX"

        }


## Respuesta de registro de usuario exitoso

        {"numero de empleado":"Daniel Alcaraz"}
## Mensaje de fallo

        {
        "code": 500,
        "message":"error message"}

## Estructura de solicitud de solicitud y respuesta

# Registro de equipo
        {
        "st": "xxxxxxxxxxxxx",
        "fecha_ingreso": "2000-01-01"}

# Respuesta de registro de usuario exitoso

        {"st":"XX-XX-XX-00"}
# Mensaje de fallo

        {
        "code": 500,
        "message":"error message"}


## Ejemplo de interacciones con el servidor

## Implementacion de rutas para los recursos
**GET/USUARIO**
 - 200 regresa una lista de usuarios
 - D.0.M regresa mensaje de falo de formato **json**

- curl http://localhost:8080/dell-warranty/json -X GET -H "Content-Type: application/json" --data '{​​​​"usuarios"}

**POST/EQUIPO**
 - recibe una estructura de registro de equipo
 - 201, registra equip, regresa estrutura de st para el nuevo equipo
 - D.O.M regresa estructura de mensaje de fallo

    
- curl http://localhost:8080/dell-warranty/json -X POST -H "Content-Type: application/json" --data '{​​​​​​​"st": "fecha_ingreso"}​​​​​​​'



**GET/EQUIPO**
 - 200 regresa una lista de equipos
 - D.0.M regresa un mensaje de fallo de formato **json**

- curl http://localhost:8080/dell-warranty/json -X GET -H "Content-Type: application/json" --data '{​​​​"equipos")>

**GET/EQUIPO/ST**
 - 200, datos de equipo con service tag
 - D.0.M, regresa un mensaje de fallo de formato **json**

- curl http://localhost:8080/dell-warranty/json -X GET -H "Content-Type: application/json" --data '{​​​​"st")>


## Verificacion y autentificacion de usuario

Los usuarios estan autorizados a consultar informacion y dar de alta nuevos equipos.
Sin embargo, no esta permitido que los eliminen.

- Eliminar equipos de la base de datos. (app:dell:write:all)

# Documento de plan de implementacion (Aspecto General)

## Motivacion y necesidad que llevaronn a la existencia de este proyecto?

Este proyecto tiene como objetivo agilizar los reemplazos de equipos de computo de la marca DELL en una empresa Medica con el fin
de acelerar el proceso de cambio de equipos que se encuentra fuera de garantia y suponen un riesgo para la empresa X.


## Quienes son los afectados por este problema que soluciono el proyecto

Los efectados por la solucion de este proyecto son el departamento de TI quienes podran mejorar su proseso de reemplazo de equipos
y todo el personal que utiliza estos equipos dado que tendran equipos actualizados y con menores problemas de hardware gracias
a contar con la garantia

## Cual es la solucion especifica que plantea este proyecto?

Almacenar la informacion basica de todos los equipos que entren a la empresa y que se ordenen de manera que muestren 
los equipos que estan proximos a expirar para llevar acabo el reemplazo

## Que recursos se necesitan para iniciar el trabajo sobre este proyecto?

- Datos de los equipos actuales en posesion 
- Base de datos
- Pagina de DELL warranty

## Que clase de trabajp operativo resulta de culminar y desplegar este proyecto?

La actualizacion de la informacion de los equipos que se encuentran en la empresa, agregar los nuevos equipos, y dar
de bajo los equipos que han salido

## Documento de plan de implementacion (Aspecto Tecnico)

## Modulos de codigo necesarios:

- Modulos de rutas
- Modulo de funciones 


## Metodos de almacenamiento requeridos:

- Sistema de archivos local 

## Plan para codificacion de los modulos:

- 1. Rutas
- 2. Funciones
 

## Plan para la verificacion de la calidad del producto:

Las pruebas se realizaran dando de alta los ST de los nuevos equipos por parte de los usuarios que tienen el permisos para
agregar los equipos al proyecto ingresando los datos solicitados para que estos traten de ser eliminados por ellos y 
demostrar que solo los usuarios autorizados tienen el privilegio para elilimar equipos del sistema.

## Plan para el despliegue del proyecto de codigo:

Que pasos seguir para realizar el projecto 

## Plan para realizar reportes de operacion y estatus del programa:

# Requisito para las descripciones del aspecto tecnico:

Este proyecto almacena el numero de serie de los equipos de computo de la marca DELL, y consulta la existesia de su garantia
dependiendo de las fechas de expiracion se mostraran los datos de los proximos equipos por realizar reemplazos.



### Archivos Relacionados

 - `routes/dell-warranty.py`

Prefijos de almacenamiento: 

 - `dell-warranty/`

Tablas de Base de Datos

> Pendiente o Nulo

- Crear un fork del proyecto storage-api

_2855652bd49e4f4c5aa6fe9fee33327fe2186e4b_

- Crear los archivos correspondientes a su proyecto y someterlos a control de versiones

	- Rutas _9846a076b59af907a49faf90f8b1ab950bf369b5_
	- Modulos _1860ea56b6a59f6d5242efc509ddbb7f0a4eee5f_

- Crear todas las rutas especificadas en su archivo de documentacion dentro de su archivo en la carpeta de routes, y todas deben responder 501, con _Content-Type:_  _application/son_

_114f2a27b96d35730c8d88ccc83c9654665e0c0f_

- Crear en la carpeta de modulos funciones que emulen las interacciones con el almacen de archivos o datos

- Crear un mock ups
