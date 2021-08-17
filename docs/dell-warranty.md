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

# Casos de uso 

- El usuario desea agregar un nuevo equipo
 - Para ello el usuario debe ingresar los campos requeridos para almacenar un equipo, los cuales son:
	st(servicetag) y fecha de ingreso.
 - Si el usuario registra datos invalidos, se le mostrara un eror HTML 400 con el mensaje 
   "Datos invalidos"
  - Ejemplo de curl de registro exitoso con POST:
```
curl http://localhost:8080/dell/store -X POST -H 'Content-Type: application/json' -d '{"st": "QQP126K", "fecha": "12-12-2020"}'

```

- El usuario desea consultar la garantia de un equipo en especifico.
 - En entos casos el st es el identificador del equipo con el cual pueden consultar
   la informacion directamente.
 - Si el usuario utiliza una ruta o un st que sea incorrecto o no exista, se le mostrara un error HTML 500
   con el mensaje de "Error interni"
 - Ejemplo de curl para una consulta especifica con GET
```
curl http://localhost:8080/dell/info/list/QQP126K -X GET

```

 - El usuario desea consultar todas las garantias de los equipos.
  - Para ello el usuario debe utilizar la ruta especifica.
  - Si el usuario utiliza una ruta o un ID incorrecto o que no exista, se le mostrara un error HTML 500 con el mensaje
    "Error interno"
  - Ejemplo de curl para mostrar todas las garantias con GET.

```
curl http://localhost:8080/dell/info/list -X GET 

```


- El usuario registro los datos incorrectos, por lo cual desea actualizarlos.
 - Para actualizarlos, es necesario ingresar los campos ya registrados, con diferencia de la fecha que sera reemplazada
 - Si el usuario registra los datos incorrectamente, se mostrara un error HTML 400 con un mensaje de
    "Datos invalidos"
 - Ejemplo de curl para la actualizacion con POST:

```
curl http://localhost:8080/dell/store -X POST -H 'Content-Type: application/json' -d '{"st": "QQP126K", "fecha": "12-10-2020"}'

```


# Planeacion del desarrollo del frontend

El desarrollo del frontend requiere de un análisis profundo en cuanto a las funcionalidades del proyecto se refiere.
Todas y cada una de las funciones deben de ir acore con lo establecido en el backend. La base de dicha interfaz será
estructura en un archivo HTML, que en conjunto con funciones de JavaScrip y CSS se le dara vida al proyecto, y el proposito 
es que la interfaz sea amigable para el usuario.

- El servidor debe poder procesar las consultas para GET, UPDATE y POST, de las siguientes variables dentro de la API:
numerios de serie y fechas de ingreso de los equipos.

- Que las validaciones para el registro de datos incorrectos esten funcionando para evitar errores en la extraccion de la
informacion de la pagina de DELL.

- Que el inicio de sesion de la pagina funcione correctamente ademas de que asigne los permisos correspondientes

## Para el login se plantea lo siguiente

Que se presenten dos campos de texto en los que se ingresen las credenciales del usuario los cuales son "usuario" y 
"password" respectivamente, y con un boton para ingresar que se encuentre debajo. Los usuarios ya se encuentran creados.

Se planea agregar el logo y colores de la empresa.

![Login](https://github.com/alcarazd/storage-api/blob/master/docs/assets/dell-warranty-0001-login_page.png)

## Para la pagina de agregar equipos se plantea lo siguiente:

Que se presenten dos campos de texto en los cuales se registren los datos del equipo adquirido los cuales son el 
servicetag y la fecha de registro del equipo respectivamente, y con un boton debajo para agregar el equipo
una vez llenados los datos solicitados.

![Add](https://github.com/alcarazd/storage-api/blob/master/docs/assets/dell-warranty-0002-add_page.png)

## Para la pagina de eliminar equipos se plantea lo siguiente:

Que se presente un campo de texto en el cual se ingrese servicetag de un equipo ya registrado, con un checkbox 
de confirmacion debajo antes del boton de eliminar.

![Delete](https://github.com/alcarazd/storage-api/blob/master/docs/assets/dell-warranty-0003-delete-page.png)

## Para la pagina de inicio se plantea lo siguiente:

Se plantea que se observen en el inicio los servicetag de los equipos los cuales esten proximos a expirar, agregar 
una barra de busqueda en la parte superior para realizar una busqueda especifica por servicetag. Esta pagina debe de ser
capaz de realizar consultas y ejecutar la funcion para mostrar los equipos.

![Info](https://github.com/alcarazd/storage-api/blob/master/docs/assets/dell-warranty-0004_info_page.png)

# Documentacion para continuar el trabajo

Se encuentra como pendiente la puesta en marcha de la funcion correspondiente a la consulta de informacion de los equipos,
de la se quiere extraer la informacion de la fecha de expiracion de los equipos que se encuentran almacenados en la funcion
de store. Dado que la pagina de DELL que se encuentra disponible trabaja de una forma en la que arroja una pagina tras otra
dificultando la extraccion de la informacion, el cuerpo de la funcion ya se encuentra en _modules_ y _routes_ pero es
necesario contar una _APIKEY_ para poder utilizar el API en el cual se encuentra el inventario de equipos de DELL,
el cual contiene los atributos y metricas de los equipos.

Para obtener la _APIKEY_ es necesario entrar al portal de DELL para estar en contacto con los encargados, esto
puede tomar alrededor de 2 meses para personas que no cuentan con un puesto de tecnico en el portal de DELL.

Una vez obtenida la _APIKEY_ en _routes_ se deben de reemplazar el valor de la _APIKEY_ por la correspondiente y en _URL_
Se debe agregar la liga correspondiente al area con acceso a las metricas y atributos de los equipos.

Dentro de _modules_ se encuentra la funcion _get__warr__from__dell_ en la cual ya se indica la estructura de consulta
a los recursos en _res_ por parte del _URL_ , se agrego una verificacion sobre el estado de la liga.

En la parte inferior se buscan las variables correspondientes a la garantia, descripcion del equipo(modelo), cuando 
terminan las garantias y el dia de entrega de los equipos, para imprimir los datos.

Tambien se muestra la relacion del estado de la garantia contra el nivel de soporte correspondiente.

Solo se deben de modificar los datos que se desean consultar y mostrar, se pueden ver el resto de atributos disponibles
desde la API.
