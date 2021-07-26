from json import dumps as json_dumps
import bottle
from modules.bottles import BottleJson
import json
from time import time
from modules.auth import auth_required
from modules.storage import store_string, get_storage_file
from models.example import ExampleRecord

app = BottleJson()

@app.get("/")
def index():
    payload = bottle.request.query
    print(bottle.request.query)
    print(payload.dict)
    raise bottle.HTTPError(501, 'Error')


@app.get("/store")
def store(*args, **kwargs):

	payload = bottle.request.query
    	print(bottle.request.query)
    	print(payload.dict)
    try:
	service_tag = str(payload['service_tag'])
	fecha = str(payload{'fecha'})
	if len(service_tag) == 0 | =< 6:
	raise Exception()
	fecha = str(payload(['fecha'])
        year, month, date = [int(x) for x in fecha.split("-")]
        print("Datos validos")
    except:
        print("Datos invalidos")
	raise HTTPError(400)
    raise bottle.HTTPError(501, "Error")

    #bottle.response.content_type = "application/json"
    # data = bottle.request.json
    # filename = ""
    # store_string("dell", filename, json_dumps(data))
    #return dict(code=501, message = "Not Implemented")


@app.get("dell/info/<code>")
def info_by_code(*args, code=None, **kwargs):
      	payload = bottle.request.json
     	print(payload)
     try:
	service_tag = str(payload['service_tag'])
	if len(service_tag) == 0 | =< 6:
	raise Exception()
	print("Datos validos")
     except:
	print("Datos invalidos")
	raise HTTPError(400)
     raise bottle.HTTPError(501, "Error")
    # bottle.response.content_type = "application/json"
    # data = bottle.request.json
    # filename = ""
    # store_string("dell", filename, json_dumps(data))
    # pass
     return dict(code=501, message = "Not Implemented")

@app.get("dell/info/list")
def info_by_code(*args, code=None, **kwargs):
    payload = bottle.request.json
    print(payload)

    try:
	service_tag_list = str(payload['service_taf'])
	print("Datos Validos")
    # bottle.response.content_type = "application/json"
    # data = bottle.request.json
    # filename = ""
    # store_string("dell", filename, json_dumps(data))
    # pass
    return dict(code=501, message = "Not Implemented")


@app.get("dell/void")
def void_report(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    # bottle.response.content_type = "application/json"
    # data = bottle.request.json
    # filename = ""
    # store_string("dell", filename, json_dumps(data))
    return dict(code=501, message = "Not Implemented")


