import datetime as dt
import bottle
from modules.bottles import BottleJson
from BeautifulSoup import BeautifulSoup
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
    try:
       respuesta = get_device_list()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)


@app.get("/info/<code>")
def devices_per_st(*args,code=None, **kwargs):
    try:
        respuesta = get_device_list(st=code)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


@app.get("/void")
def void_report(*args, **kwargs):
    try:
       respuesta = get_device_out_warranty(html_string)
    except:
	raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

#Web scrapping tool#

#URL de DELL warranty#
#Prueba de cambio de nombre#

for n in payload("st")
url = request.get("https://www.dell.com/support/home/en-us/product-support/servicetag/(n)")

soup = bs4.BeautifulSoup(r.content, "html.parser")
table = soup.find('ps-inlineWarranty',{'class': "warrantyExpiringLabel mb-0 mr-3"})
html_string = str(table)

