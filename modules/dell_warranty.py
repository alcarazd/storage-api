import json
from datetime import datetime
from modules.storage import (
    store_string, store_bytes
)


def add_st(fecha=None, st=None):
    print("Desde Modulo store")
    print(fecha, st)
    print("Exito")
    almacenable = {
        "service_tag": st,
        "fecha_de_ingreso": fecha,
    }
    nombre_de_archivo = f"{st}-{fecha}.json"
    datos = store_string(
        "dell/registros",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

def get_device_id(st=None):
    print("Desde modulo device_per_St")
    print(st, fecha)
    print("Exito")

def get_device_list(devices=None):
    print("Desde modulo all_device")
    print(st, fecha)
    print("Exito")

def get_device_id(warranty=None):
    print("Desde modulo void_report")
    print(st, fecha)
    print("Exito")

def get_device_out_warranty(*args, **kwargs):
    pass
