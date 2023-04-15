import os
import shutil
from pathlib import Path

PREFIX = "m"
PATENTE = "3977"
PATH_ORIGEN = "/Users/miguel/Downloads/"
PATH_DESTINO = "/Users/miguel/Documents/"

consecutivo = "001"
juliano = "err"

remote_path = Path(PATH_ORIGEN)
os.chdir(remote_path)
# base_path = os.getcwd()
# path = Path(base_path)

# for p in path.glob(f"{PREFIX}{PATENTE}{consecutivo}.{juliano}"):
#     print(p)

nombre_original = f"{PREFIX}{PATENTE}{consecutivo}.{juliano}"

archivos = os.listdir()
for archivo in archivos:
    if archivo == nombre_original:
        shutil.copy(src=PATH_ORIGEN + nombre_original, dst=PATH_DESTINO)
        break
