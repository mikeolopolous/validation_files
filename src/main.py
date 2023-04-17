import os
import shutil
from pathlib import Path
import customtkinter as ctk

BLUE_COLOR = "#227C9D"
GREEN_COLOR = "#17C3B2"
YELLOW_COLOR = "#FFCB77"
RED_COLOR = "#FE6D73"

# PATH_REMOTO = "\\192.168.11.99\LWOperacionMZO\Enviar"

PATH_ORIGEN = "/Users/miguel/Downloads/"
PATH_DESTINO = "/Users/miguel/Documents/"
PREFIX = "m"
PATENTE = "3977"


def make_copy():
    consecutivo = consecutivo_txt.get()
    juliano = juliano_txt.get()
    extension = extension_txt.get()

    nombre_original = f"{PREFIX}{PATENTE}{consecutivo}.{juliano}"
    nombre_con_extension = nombre_original + "." + extension

    archivos = os.listdir()
    if consecutivo == "" or juliano == "":
        message_text.set("Revisa el consecutivo o juliano")
        message_label.configure(textvariable=message_text,
                                text_color=YELLOW_COLOR,
                                font=ctk.CTkFont(size=20, weight="bold"))

        message_label.pack(padx=5, pady=(10, 20))

    elif nombre_original in archivos:
        if extension != "":
            shutil.copy(src=PATH_ORIGEN + nombre_original, dst=PATH_DESTINO)
            os.rename(PATH_DESTINO + nombre_original, PATH_DESTINO + nombre_con_extension)
        else:
            shutil.copy(src=PATH_ORIGEN + nombre_original, dst=PATH_DESTINO)
        
        message_text.set("¡Copia realizada!")
        message_label.configure(textvariable=message_text,
                                text_color=GREEN_COLOR,
                                font=ctk.CTkFont(size=20, weight="bold"))
        
        message_label.pack(padx=5, pady=(10, 20))

    else:
        message_text.set("¡No se encontró el archivo!")
        message_label.configure(textvariable=message_text,
                                text_color=RED_COLOR,
                                font=ctk.CTkFont(size=20, weight="bold"))

        message_label.pack(padx=5, pady=(10, 20))


remote_path = Path(PATH_ORIGEN)
os.chdir(remote_path)

root = ctk.CTk()
root.geometry("400x450")
root.resizable(False, False)
root.title("Duplicador de archivos SAAIM3")

message_text = ctk.StringVar()

title_label = ctk.CTkLabel(root,
                           text="Copia de SAAIM3",
                           font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=5, pady=(10, 20))

frame = ctk.CTkFrame(root)
frame.pack(fill="x", padx=25)

consecutivo_frame = ctk.CTkFrame(frame)
consecutivo_frame.pack(padx=25, pady=(10, 5), fill="both")
consecutivo_label = ctk.CTkLabel(consecutivo_frame,
                                 text="Consecutivo de archivo:",
                                 font=ctk.CTkFont(size=16, weight="bold"))
consecutivo_label.pack()

consecutivo_txt = ctk.CTkEntry(consecutivo_frame,
                               width=80,
                               height=25,
                               border_width=2,
                               border_color=BLUE_COLOR,
                               corner_radius=5,
                               font=("Helvetica", 14))
consecutivo_txt.pack(padx=25, pady=(5, 10))

juliano_frame = ctk.CTkFrame(frame)
juliano_frame.pack(padx=25, pady=(10, 5), fill="both")
juliano_label = ctk.CTkLabel(juliano_frame,
                             text="Día juliano:",
                             font=ctk.CTkFont(size=16, weight="bold"))
juliano_label.pack()

juliano_txt = ctk.CTkEntry(juliano_frame,
                             width=80,
                             height=25,
                             border_width=2,
                             border_color=BLUE_COLOR,
                             corner_radius=5,
                             font=("Helvetica", 14))
juliano_txt.pack(padx=25, pady=(5, 10))

extension_frame = ctk.CTkFrame(frame)
extension_frame.pack(padx=25, pady=(10, 5), fill="both")
extension_label = ctk.CTkLabel(extension_frame,
                                 text="Extensión:",
                                 font=ctk.CTkFont(size=16, weight="bold"))
extension_label.pack()

extension_txt = ctk.CTkEntry(extension_frame,
                               width=120,
                               height=25,
                               border_width=2,
                               border_color=BLUE_COLOR,
                               corner_radius=5,
                               font=("Helvetica", 14))
extension_txt.pack(padx=25, pady=(5, 10))

btn_obtener = ctk.CTkButton(frame,
                            width=150,
                            height=35,
                            font=('Helvetica', 18),
                            text="OBTENER",
                            fg_color=BLUE_COLOR,
                            hover_color=GREEN_COLOR,
                            corner_radius=3,
                            command=make_copy)
btn_obtener.pack(padx=10, pady=(15, 20))

message_label = ctk.CTkLabel(root)

root.mainloop()
