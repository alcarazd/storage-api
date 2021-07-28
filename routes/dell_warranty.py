from json import dumps as json_dumps
import bottle
from modules.bottles import BottleJson
import json
from time import time
from modules.auth import auth_required
from modules.storage import store_string, get_storage_file
from models.example import ExampleRecord

import bottle
from modules.bottles import BottleJson
from modules.dell_warranty import add_st
from modules.dell_warranty import get_device_id
from modules.dell_warranty import get_device_list
from modules.dell_warranty import get_device_out_warranty

app = BottleJson()

@app.get("/")


@app.post("/store")
def store(*args, **kwargs):
    payload = bottle.request.query
    print(payload.dict)
    try:
	#
       fecha = str(payload['fecha'])
       year, month, date = [int(x) for x in fehca.split("-")]
       print("datos validos")
       respuesta =  add_st(**payload)
       raise bottle.HTTPError(201)
    except:
       print("Datos invalidos")
       raise bottle.HTTPError(400)
    raise bottle.HTTPError(500)
    
    try:
	st = str(payload['service_tag'])
	if len(st) == 0:
	print("datos validos")
	respuesta = add_st(**payload)
	raise bottle.HTTPError(201)
     except:
	print("datos invalidos")
    	raise bottle.HTTPError(400)
     raise bottle.HTTPError(500)

@app.get("/info/list")
def all_device(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
       devices = str(payload['device_list'])
       print("datos validos")
       respuesta = get_device_list(**payload)
       raise bottle.HTTPError(201)
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(500)


@app.get("/info/<code>")
def devices_per_st(*args,**kwargs):
    payload = bottle.request.json
    print(payload)
    try:
       device = str(payload['device_id'])
       print("datos validos")
       respuesta = get_device_id(**payload)
       raise bottle.HTTPError(201)
    except:
	print("datos invalidos")
	raise bottle.HTTPError(400)
    raise bottle.HTTPError(500)



@app.get("/void")
def void_report(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
       warranty = str(payload['out_warranty'])
       print("datos validos")
       respuesta = get_device_out_warranty(**payload)
       raise bottle.HTTPError(201)
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(500)



