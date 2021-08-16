# Descripcion general del proyecto

El presente proyecto consiste en un sistema de registro de equipos DELL el cual los almacena. La finalidad es que el personal de 
la empresa registre los nuevos equipos adquiridos para que posteriormente cuando esten por vencer sus garantias, puedan agilizar
los planes de reemplazo de una manera mas optima que la actual, dado que el sistema plantea brindarles toda la informacion 
necesaria contenida en los service tag(ST) de los equipos.

### Mercado/Sector

Este proyecto esta pensado para las empresas del sector medico que adquieren dispositivos de la marca DELL al mismo tiempo 
que adquieren licencias para dichos equipos, para las empresas del sector es de suma importancia el manejo de su informacion y
la continuidad del negocio por lo cual es importante para ellas mantener sus equipos actualizados tanto en software como
en hardware. 


## Modelado de datos

En el modelado de datos la estructura es una parte fundamental y debe de realizarse previo al inicio del proyecto, para el
funcionamiento adecuado y posibles cambios o el desarrollo del mismo. El proyecto presentara las siguientes entidades: 

- Usuario(Nombre, estatus, num_empleado)

- Equipo(servicetag, fecha_ingreso, marca, fecha_expiracion)



## Interacciones de datos y operaciones de datos

 Las interacciones de datos se refiere a la manera en la que funciona el proyecto. Algunas intereacciones de este proyecto
son las siguientes:


### Operacion de Usuario

- Registrar usuario

	- Solicitar nombre y numero de empleado
	- El numero de empleado se asigna a todos los empleados

### Actualizacion de usuario

- Dar de baja usuarios

### Operacion de equipos

- Solicitar servicetag, fecha de ingreso
- La fecha de expiracion se buscara en /dell/info/<id>
- Dar de baja equipos


## Consultas de datos

Las consultas de datos sirven para obtener informacion especifica sobre los datos ya almacenados. A continuacion algunas
de las posibles consultas de este proyecto


 - Solicitar datos del equipo
	- Por ST

```

 curl http://localhost:8080/dell/info/<id> \
 -X GET
 '''

 - Lista de equipos
	- Todos
	- ST

```

```

 curl http://localhost:8080/dell/info/list \
 -X GET


 ```
 - Garantia
	- Todos 
	- ST

## Rutas HTTP

A continuacion, se presentan las rutas HTTP con su descipcion.

| Path                  | Descripción |
| --------------------- | ----------- |
| /dell/store           | En esta ruta se almacenan los numeros de serie de los equipos ingresados por los usuarios                       |
| /dell/info/<id>       | En esta ruta se encuentra la informacion por ID de los equipos en propiedad                                     |
| /dell/info/list         | En esta ruta se encuentra la informacion de todos los equipos en propiedad                                      |
| /dell/void            | En esta ruta se encuentran los numeros de serie de los equipos de los cuales su garantia ha expirado            |



## Ejemplos de mensajes HTTP que aceptara y emitira el servidor


### Registro de usuario

        {
        "nombre": "Daniel Alcaraz",
        "num_empleado": "XXXXX"

        }


- Respuesta de registro de usuario exitoso

        {"numero de empleado":"Daniel Alcaraz"}

- Mensaje de fallo

        { "code": 500, "message":"error message"}

```
  -X POST \
  -H 'Content-Type': applications/json' \
  -d '{"st": "AAB234K", "fecha:" "2004-12-23"}'

```

### Registro de equipo
        {"st": "xxxxxxxxxxxxx", "fecha_ingreso": "2000-01-01"}

- Respuesta de registro de usuario exitoso

        {"st":"XX-XX-XX-00"}

- Mensaje de fallo

        {"code": 500, "message":"error message"}


## Ejemplo de interacciones con el servidor e Implementacion de rutas para los recursos


**POST/EQUIPO**
 - recibe una estructura de registro de equipo
 - 201, registra equipo, regresa estrutura de st para el nuevo equipo
 - D.O.M regresa estructura de mensaje de fallo

 
- curl http://localhost:8080/dell-warranty/dell/store -X POST -H "Content-Type: application/json" --data '{​​​​​​​"st": "fecha_ingreso"}​​​​​​​'


**GET/EQUIPO**
 - 200 regresa una lista de equipos
 - D.0.M regresa un mensaje de fallo de formato **json**

- curl http://localhost:8080/dell-warranty/dell/info/list

**GET/EQUIPO/ST**
 - 200, datos de equipo con service tag
 - D.0.M, regresa un mensaje de fallo de formato **json**

- curl http://localhost:8080/dell-warranty/dell/info<id>


## Verificacion y autentificacion de usuario

Los usuarios estan autorizados a consultar informacion y dar de alta nuevos equipos.
Sin embargo, no esta permitido que los eliminen.

- Eliminar equipos de la base de datos. (`app:dell:write:all`)
- Permiso para ver (`app:dell:read:only`)



# Documento de plan de implementacion 

## Aspecto General

Este proyecto esta pensado para ayudar al manejo y control interno de los equipos, con la interaccion de la tecnologia y
automatizacion.

Este proyecto se encuentra en desarrollo ya que la empresa cuenta con un sistema con funciones parecidas pero que satisface
otras necesidades.

## Motivacion y necesidad que llevaronn a la existencia de este proyecto?

Lo que me motivo a realizar este proyecto fue la experiencia al realizar la actividad de reemplazos de equipo de la forma
actual, bastante complicada al tener que recabar informacion en distintos sitios y el tiempo que transcurre para llevarlo 
acabo y que con los recursos que cuenta la empresa se puede automatizar.


## Quienes son los afectados por este problema que soluciono el proyecto

Los efectados por la solucion de este proyecto son el departamento de TI quienes podran mejorar su proceso de reemplazo de equipos
y todo el personal que utiliza estos equipos dado que tendran equipos actualizados y con menores problemas de hardware gracias
a contar con la garantia.

## Cual es la solucion especifica que plantea este proyecto?

Almacenar la informacion basica de todos los equipos que entren a la empresa y que se ordenen de manera que muestren 
los equipos que estan proximos a expirar para llevar acabo el reemplazo.

## Que recursos se necesitan para iniciar el trabajo sobre este proyecto?

- Datos de los equipos actuales en posesion 
- Base de datos
- Pagina de DELL warranty

## Que clase de trabajo operativo resulta de culminar y desplegar este proyecto?

La actualizacion de la informacion de los equipos que se encuentran en la empresa, agregar los nuevos equipos, y dar
de bajo los equipos que han salido

## Aspecto Tecnico

### Modulos de codigo necesarios:

- Modulos de rutas los cuales brindad una estructura a la negacion de las funcionalidades


- Modulo de funciones, funciones de almacenamiento y utileria de la cual depende la funcionalidad del proyecto
como es donde se guardara la informacion y las fechas en las que se basa. 


## Metodos de almacenamiento requeridos:

- Sistema de archivos local 

## Plan para codificacion de los modulos:

- 1. Rutas
- 2. Funciones

Se deben de crear primeramente los modulos/rutas para realizar pruebas de funcionamiento para ser tomado como base
para la creacion de las funciones del programa para mantenerlo de una manera mas simple de utilizar.
 

## Plan para la verificacion de la calidad del producto:

Las pruebas se realizaran dando de alta los ST de los nuevos equipos por parte de los usuarios que tienen el permisos para
agregar los equipos al proyecto ingresando los datos solicitados para que estos traten de ser eliminados por ellos y 
demostrar que solo los usuarios autorizados tienen el privilegio para eliminar equipos del sistema.

> ## Plan para el despliegue del proyecto de codigo:
 

> ## Plan para realizar reportes de operacion y estatus del programa:

# Evaluacion - Computo en la nube:

Este proyecto almacena el numero de serie de los equipos de computo de la marca DELL, y consulta la existesia de su garantia
dependiendo de las fechas de expiracion se mostraran los datos de los proximos equipos por realizar reemplazos.


### Archivos Relacionados

 - `routes/dell-warranty.py`

Prefijos de almacenamiento: 

 - `dell-warranty/`

Tablas de Base de Datos

> Pendiente o Nulo

- 1.  Crear un fork del proyecto storage-api _Señalar cual es el commit-hash a partir de haber realizado el fork_.

| Concepto                  | Commit Hash                                |
| ---------------------    | ----------- |
| Creacion de fork          | _2855652bd49e4f4c5aa6fe9fee33327fe2186e4b_ |



- 2. Crear los archivos correspondientes a su proyecto, y someterlos a control de versiones. _Señalar el commit hash que contiene_
_la creacion de dichos archivos_

| Conepto                  | Commit Hash |
| ---------------------    | ----------- |
| Creacion de docs/dell-warranty                  | _1bec3e4077876caf065791fb5423306eadd121dd_ |
| Creacion de modules/dell-warranty.py            | _1860ea56b6a59f6d5242efc509ddbb7f0a4eee5f_ |



- 3. Crear todas las rutas especificadas en su archivo de documentacion dentro de su archivo en la carpeta de routes, y todas 
deben responder 501, con _Content-Type:_  _application/son_.


| Concepto                  | Commit Hash |
| ---------------------     | ----------- |                               
| Creacion de rutas         | _9846a076b59af907a49faf90f8b1ab950bf369b5_ |


- 4. Crear en la carpeta de modulos funciones que emulen las interacciones con el almacen de archivos o datos.

| Concepto                  | Commit Hash                                |
| ---------------------    | ----------- |
| Creacion de funciones     | _1860ea56b6a59f6d5242efc509ddbb7f0a4eee5f_ |


- 5. Crear un mock ups.

La imagen de **docs/assets/dell-warranty-0001-login_page.png** muestra un formulario de ingreso a la aplicacion 
en el cual se solicitan los datos del usuario, nombre de usuario **username** y la contraseña **password**, al llenar
los campos se debe de presionar el boton de **login** para ingresar.



![Login](https://github.com/alcarazd/storage-api/blob/master/docs/assets/dell-warranty-0001-login_page.png)



La imagen de **docs/assets/dell-warranty-0002-add_page.png** muestra un formulario con el cual los usuarios pueden
dar de alta los nuevos equipos adquridos. Se solicita el service tag del equipo o **(ST)** junto con la fecha de 
ingreso del mismo al llenar esos campos se debe de dar clic sobre el boton de **agregar** para añadir el equipo.

![Add](https://github.com/alcarazd/storage-api/blob/master/docs/assets/dell-warranty-0002-add_page.png)

La imagen de **docs/assets/dell-warranty-0003-delete-page.png** muestra un formulario para eliminar equipos
solicitando el service tag del equipo a eliminar, para poder llevar esta accion acabo se debe de marcar la casilla
para confirmar antes de dar clic sobre el boton **eliminar**.


![Delete](https://github.com/alcarazd/storage-api/blob/master/docs/assets/dell-warranty-0003-delete-page.png)

__NOTA__ Se debe contar con autorizacion para eliminar equipos.

La imagen de **docs/assets/dell-warranty-0004_info_page.png** muestra una ventana en la cual los equipos
proximos a expirar apareceran, para que el personal comience con la logistica del reemplazo (mostrando el service tag).


![Info](https://github.com/alcarazd/storage-api/blob/master/docs/assets/dell-warranty-0004_info_page.png)

| Concepto                  | Commit Hash                                |
| ---------------------    | ----------- |
| Creacion de mock-ups     | _b2f11a0798261fd3028dd8bee329dd39a6492628_ |
| Explicacion de mock-ups     | _b16301b72edddf892f423d443e9d09072a58417f_ |

