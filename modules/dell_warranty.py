from datetime import datetime
from modules.dell_warranty import payload



@app.get("/store")
def alamacenar_dato(service_tag = None):
	print("Desde Modulo")
	print(service_tag)
	para_almacenar = {"service_tag": service_tag, "fecha": fecha}
	json_text = json.dumps(para_almacenar)
	store_string(/servicetag_folder, para_almacenar)
	return("Exito")



def get_timestamp():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")


def timestamp_filename(filename):
    timestamp = get_timestamp()
    return "_".join([timestamp, filename])

from os import environ
from mimetypes import guess_type
from pathlib import Path

try:
    storage_dir = Path(environ["STORAGE_DIR"]).resolve()
except KeyError:
    raise Exception("No storage directory set")


def get_file_to_store(collection, filename):
    target = (storage_dir / collection / filename)
    if target.exists():
        raise Exception("File already exists")
    target.parent.mkdir(exist_ok=True, parents=True)
    return target


def store_bytes(collection, filename, blob):
    target = get_file_to_store(collection, filename)
    target.write_bytes(blob)


def store_string(collection, filename, text):
    target = get_file_to_store(collection, filename)
    target.write_text(text)


def query_storage(path=""):
    target = (storage_dir / path)
    if not target.exists():
        raise Exception("Does not exists")
    elif target.is_dir():
        return dict(
            path=str(target.relative_to(storage_dir)),
            type="directory",
            content=[str(p.relative_to(storage_dir)) for p in target.iterdir()]
        )
    elif target.is_file():
        mime = (guess_type(str(target)) or ["application/octet-stream"])[0]
        return dict(
            path=str(target.relative_to(storage_dir)),
            type="file",
            metadata=dict(
                mime=mime,
                size=target.stat().st_size,
            )
        )
    return {}


def get_storage_file(path=""):
    target = (storage_dir / path)
    if not target.exists() or not target.is_file():
        raise Exception("Does not exists")
    mime = (guess_type(str(target)) or ["application/octet-stream"])[0]
    return mime, target.read_bytes()

