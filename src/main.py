import os
import shutil
import customtkinter as ctk
from pathlib import Path
from tkinter import messagebox

BLUE_COLOR = "#227C9D"
GREEN_COLOR = "#17C3B2"
YELLOW_COLOR = "#FFCB77"
RED_COLOR = "#FE6D73"

ORIGINAL_PATH = Path.home()

PATH_ORIGEN = "M:\\"
PATH_DESTINO = str(ORIGINAL_PATH) + "\\Downloads\\"
PATENTE = "3977"


def set_checkbox():
    checkbox_value = check_var.get()
    if checkbox_value == "on":
        os.chdir(f"{PATH_ORIGEN}\\Recibir")
    else:
        os.chdir(f"{PATH_ORIGEN}\\Enviar")


def make_copy():
    set_checkbox()
    consecutivo = consecutivo_txt.get()
    juliano = juliano_txt.get().strip()
    extension = extension_txt.get()

    prefix = "m"
    if juliano != "err" and check_var.get() == "on":
        prefix = "k"

    nombre_original = f"{prefix}{PATENTE}{consecutivo}.{juliano}"
    nombre_con_extension = nombre_original + "." + extension

    archivos = os.listdir()

    if consecutivo == "" or juliano == "":
        messagebox.showwarning(title="Error en los valores",
                               message="Revisa el consecutivo o juliano")

    elif nombre_original not in archivos:
        messagebox.showerror(title="Error en búsqueda",
                             message="No se encontró el archivo")
    else:
        if extension != "":
            shutil.copy(src=os.getcwd() + "\\" + nombre_original, dst=PATH_DESTINO)
            os.rename(PATH_DESTINO + nombre_original, PATH_DESTINO + nombre_con_extension)
        else:
            shutil.copy(src=os.getcwd() + "\\" + nombre_original, dst=PATH_DESTINO)

        messagebox.showinfo(message="Copia realizada")
        

root = ctk.CTk()
height_screen = root.winfo_screenheight()
width_screen = root.winfo_screenwidth()
x = round(width_screen - 100)
y = round(height_screen / 2)
root.geometry(f"400x450+{x}+{y}")
root.resizable(False, False)
root.title("Duplicador de archivos SAAIM3")

title_label = ctk.CTkLabel(root,
                           text="Copia de SAAIM3",
                           font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=5, pady=(10, 20))

frame = ctk.CTkFrame(root)
frame.pack(fill="x", padx=25)

checkbox_frame = ctk.CTkFrame(frame)
checkbox_frame.pack(padx=25, pady=(10, 5), fill="both")
check_var = ctk.StringVar(value="off")

checkbox = ctk.CTkCheckBox(checkbox_frame,
                           text="Archivo de respuesta",
                           variable=check_var,
                           command=set_checkbox,
                           onvalue="on",
                           offvalue="off")
checkbox.pack(padx=25, pady=(5, 10))

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

root.mainloop()
