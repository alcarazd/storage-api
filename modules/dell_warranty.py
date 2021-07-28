import json
from datetime import datetime
from modules.storage import (
    store_string, store_bytes,
    query_storage, get_storage_file
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

def get_device_list(devices=None, st=None):
    query_result = query_storage(
        "dell/registros",
    )
    if devices is None and st is None:
        return query_result["content"]
    if st is not None:
        return [
           r
           for r in query_result["content"]
           if st in r
        ]

def get_device_out_warranty(*args, **kwargs):
    pass
