import os
import shutil
from pathlib import Path
import customtkinter as ctk

PATH_ORIGEN = "/Users/miguel/Downloads/"
PATH_DESTINO = "/Users/miguel/Documents/"
PREFIX = "m"
PATENTE = "3977"

remote_path = Path(PATH_ORIGEN)
os.chdir(remote_path)

root = ctk.CTk()
root.geometry("400x500")
root.title("Duplicador de archivos SAAIM3")

title_label = ctk.CTkLabel(root, text="Copia de SAAIM3",
                           font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=5, pady=(10, 20))

frame = ctk.CTkFrame(root)
frame.pack(fill="x", padx=25)

consecutivo_frame = ctk.CTkFrame(frame)
consecutivo_frame.pack(padx=25, pady=(10, 5), fill="both")
consecutivo_label = ctk.CTkLabel(consecutivo_frame, text="Consecutivo de archivo:",
                                 font=ctk.CTkFont(weight="bold"))
consecutivo_label.pack()

juliano_frame = ctk.CTkFrame(frame)
juliano_frame.pack(padx=25, pady=(10, 5), fill="both")
juliano_label = ctk.CTkLabel(juliano_frame, text="Día juliano:",
                                 font=ctk.CTkFont(weight="bold"))
juliano_label.pack()

custom_name_frame = ctk.CTkFrame(frame)
custom_name_frame.pack(padx=25, pady=(10, 5), fill="both")
custom_name_label = ctk.CTkLabel(custom_name_frame, text="Extensión:",
                                 font=ctk.CTkFont(weight="bold"))
custom_name_label.pack()

consecutivo = "001"
juliano = "err"
nombre_original = f"{PREFIX}{PATENTE}{consecutivo}.{juliano}"

# archivos = os.listdir()
# for archivo in archivos:
#     if archivo == nombre_original:
#         shutil.copy(src=PATH_ORIGEN + nombre_original, dst=PATH_DESTINO)
#         break

root.mainloop()