import datetime as dt
import bottle
from modules.bottles import BottleJson
from modules.dell_warranty import (
    add_st,
    get_device_id,
    get_device_list,
    get_device_out_warranty
)

app = BottleJson()


@app.post("/store")
def store(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        st = str(payload['st'])
        fecha = dt.date.fromisoformat(payload['fecha'])
        if len(st) == 0:
            raise Exception()
        print("dato validos")
        respuesta = add_st(**payload)
        print(respuesta)
        print("apunto de terminar")
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)

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
