import json
from datetime import datetime
from modules.storage import (
    store_string, store_bytes,
    query_storage, get_storage_file
)

#Function to add a device

def add_st(fecha=None, st=None):
    print("Desde Modulo store")
    print(fecha, st)
    print("Exito")
# data that is goind to be stored
    almacenable = {
        "service_tag": st,
        "fecha_de_ingreso": fecha,
    }
# how date is goint to be stored and where
    nombre_de_archivo = f"{st}-{fecha}.json"
    datos = store_string(
# File name
        "dell/registros",
        nombre_de_archivo,
        json.dumps(almacenable)
    ) #returns data
    return datos

## function to get a device by st or date

def get_device_id(st=None):
    print("Desde modulo device_per_St")
    print(st, fecha)
    print("Exito")

# function to get all devices stored 

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

#Function to get details from DELL webpage

def get_warr_from_dell(svctag):
    res = requests.get(URL.format(svctag))

    if res.status_code != 200:
        sys.stderr.write('[%s] Caught %i as the response code.\n' % (svctag, res.status_code))
        sys.stderr.write('[%s] Unable to get details for given service tag.\n'
                % svctag)
        return False

    fault = res.json['GetAssetWarrantyResponse']['GetAssetWarrantyResult']['Faults']
    if fault is not None:
        sys.stderr.write("[%s] Failed to find details. Sure it's a valid TAG?\n" % svctag )
        return False

    asset = res.json['GetAssetWarrantyResponse']['GetAssetWarrantyResult']['Response']['DellAsset']
    model = asset['MachineDescription']
    ent = asset['Warranties']['Warranty']
    shipped = asset['ShipDate']

    print 'Service Tag:        ', svctag
    print ' Model:             ', model
    print ' Shipped:           ', shipped, '\n'
    print '{0:<20} {1:>15}'.format(*('Warranty Ends','ServiceLevelDescription'))
    for warr in [(d['EndDate'],d['ServiceLevelDescription']) for d in ent]:
        print '{0:<20} {1:>15}'.format(*warr)
