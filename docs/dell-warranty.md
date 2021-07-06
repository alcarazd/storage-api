# Dell Waranty Query and Store

Este proyecto almacena el numero de serie de los equipos de computo de la marca DELL, y consulta la existesia de su garantia
dependiendo de las fechas de expiracion se mostraran los datos de los proximos equipos por realizar reemplazos.

# Que es lo que quiero lograr:

Este proyecto tiene como objetivo agilizar los reemplazos de equipos de computo de la marca DELL en una empresa X con el fin 
de acelerar el proceso de cambio de equipos que se encuentra fuera de garantia y suponen un riesgo para la empresa X.

# El proyecto consiste en:
El pyoyecto consiste en que el encargado o los encargados de los movimientos de equipos ingresen los numeros de serie de los
equipos de computo, para que estos sean consultados en el sitio web de DELL "Dell Warranty" y obtener las fechas de 
expiracion para posteriormente desplegarlas en una pagina segun su proximidad a expirar para llevar un mejor orden y 
metodos de consultas sobre los equipos.

# Sector 


# Ejemplos de interacciones con el servidor

# API

| Path                  | Descripción |
| --------------------- | ----------- |
| /dell/store           | En esta ruta se almacenan los numeros de serie de los equipos ingresados por los usuarios                       |
| /dell/info/<id>       | En esta ruta se encuentra la informacion por ID de los equipos en propiedad                                     |
| /dell/void            | En esta ruta se encuentran los numeros de serie de los equipos de los cuales su garantia ha expirado            |


# Nota
 
Las rutas contaran con autenticacion de usuario de manera que solo los usuarios registrados podran ver y registrar los equipos


# Archivos Relacionados

 - `routes/dell-warranty.py`

Prefijos de almacenamiento: 

 - `dell-warranty/`

Tablas de Base de Datos

> Pendiente o Nulo

Para el control del sistema de garantias, tendremos las siguientes entidades:

	Usuario(Nombre,estatus,num_empleado)
	Equipo(servicetag,fecha_ingreso,marca,fecha_expiracion)



# Operaciones de Almacenamiento de datos 

	#Operacion de Usuario

	# Registrar usuario

	  - Solicitar nombre y numero de empleado
	  - El numero de empleado se asigna a todos los empleados
	# Actualizacion de usuario

	  -Dar de baja usuarios
	
	# Operacion de equipos

	 - Solicitar servicetag, fecha de ingreso
	 - La fecha de expiracion se buscara en /dell/info/<id>
	 - Dar de baja equipos

# Operaciones de consulta de datos

	- Solicitar datos del equipo
		- Basicos
		- Garantia
# Estructura de solicitud de solicitud y respuesta

## Registro de usuario 

	{
	"nombre": "Daniel Alcaraz",
	"num_empleado": "XXXXX"

	} 


# Respuesta de registro de usuario exitoso

	{"numero de empleado":"Daniel Alcaraz"}
# Mensaje de fallo

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

# Implementacion de rutas para los recursos 
**GET/USUARIO**
 - 200 regresa una lista de usuarios
 - D.0.M regresa mensaje de falo de formato **json**

**POST/EQUIPO**
 - recibe una estructura de registro de equipo
 - 201, registra equip, regresa estrutura de st para el nuevo equipo
 - D.O.M regresa estructura de mensaje de fallo

**GET/EQUIPO**
 - 200 regresa una lista de equipos 
 - D.0.M regresa un mensaje de fallo de formato **json**

**GET/EQUIPO/ST**
 - 200, datos de equipo con service tag
 - D.0.M, regresa un mensaje de fallo de formato **json**

