# Dell Waranty Query and Store

Este proyecto almacena el numero de serie de los equipos de computo de la marca DELL, y consulta la existesia de su garantia
dependiendo de las fechas de expiracion se mostraran los datos de los proximos equipos por realizar reemplazos.

##Que es lo que quiero lograr:
Este proyecto tiene como objetivo agilizar los reemplazos de equipos de computo de la marca DELL en una empresa X con el fin 
de acelerar el proceso de cambio de equipos que se encuentra fuera de garantia y suponen un riesgo para la empresa X.

##El proyecto consiste en:
El pyoyecto consiste en que el encargado o los encargados de los movimientos de equipos ingresen los numeros de serie de los
equipos de computo, para que estos sean consultados en el sitio web de DELL "Dell Warranty" y obtener las fechas de 
expiracion para posteriormente desplegarlas en una pagina segun su proximidad a expirar para llevar un mejor orden y 
metodos de consultas sobre los equipos.



## API

| Path                  | Descripción |
| --------------------- | ----------- |
| /dell/store           | En esta ruta se almacenan los numeros de serie de los equipos ingresados por los usuarios                       |
| /dell/info/<id>       | En esta ruta se encuentra la informacion por ID de los equipos en propiedad                                     |
| /dell/void            | En esta ruta se encuentran los numeros de serie de los equipos de los cuales su garantia ha expirado            |


#Nota 
Las rutas contaran con autenticacion de usuario de manera que solo los usuarios registrados podran ver y registrar los equipos


# Archivos Relacionados

 - `routes/dell-warranty.py`

Prefijos de almacenamiento: 

 - `dell-warranty/`

Tablas de Base de Datos

> Pendiente o Nulo
