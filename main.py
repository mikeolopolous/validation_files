import os
from pathlib import Path

PATENTE = "m3977"

remote_path = Path("/Users/miguel/Downloads")
os.chdir(remote_path)
base_path = os.getcwd()
path = Path(base_path)

consecutivo = "001"
juliano = "err"
for p in path.glob(f"{PATENTE}{consecutivo}.{juliano}"):
    print(p)
