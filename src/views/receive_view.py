import os
import shutil
import flet as ft

from typing import Dict
from pathlib import Path


def receive_view(page):
    HOME_PATH = Path.home()
    REMOTE_PATH = 'M:\\'
    LOCAL_PATH = str(HOME_PATH) + '\\Downloads\\'
    PATENTE = '3977'

    prog_bars: Dict[str, ft.ProgressRing] = {}
    files = ft.Ref[ft.Column]()
    upload_button = ft.Ref[ft.ElevatedButton]()


    def make_copy(e):
        os.chdir(f'{REMOTE_PATH}\\Recibir')

        if prefijo_dropdown.value != '' and consecutivo_textfield.value != '' and juliano_textfield != '':
            prefijo = prefijo_dropdown.value.strip()
            consecutivo = consecutivo_textfield.value.strip()
            juliano = juliano_textfield.value.strip()
            nueva_extension = nueva_extension_textfield.value.strip()

            nombre_original = f'{prefijo}{PATENTE}{consecutivo}.{juliano}'
            archivos_list = os.listdir()

            if nombre_original in archivos_list:
                shutil.copy(
                    src=os.getcwd() + '\\' + nombre_original,
                    dst=LOCAL_PATH
                )

                if nueva_extension != '':
                    nombre_con_extension = nombre_original + '.' + nueva_extension
                    os.rename(src=LOCAL_PATH + nombre_original, dst=LOCAL_PATH + nombre_con_extension)

                page.snack_bar = ft.SnackBar(
                    content=ft.Text('Archivo copiado', text_align=ft.TextAlign.CENTER, size=20),
                    bgcolor=ft.colors.GREEN_200
                )
                page.snack_bar.duration = 3000
                page.snack_bar.open = True
                page.update()
            else:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text('No se encontró el archivo', text_align=ft.TextAlign.CENTER, size=20),
                    bgcolor=ft.colors.RED_300
                )
                page.snack_bar.duration = 3000
                page.snack_bar.open = True
                page.update()
        else:
            page.snack_bar = ft.SnackBar(
                content=ft.Text('Todos los campos son obligatorios', text_align=ft.TextAlign.CENTER, size=20),
                bgcolor=ft.colors.RED_300
            )
            page.snack_bar.duration = 3000
            page.snack_bar.open = True
            page.update()


    def file_picker_result(e: ft.FilePickerResultEvent):
        upload_button.current.disabled = True if e.files is None else False
        prog_bars.clear()
        # files.current.controls.clear()
        if e.files is not None:
            for f in e.files:
                prog = ft.ProgressRing(value=0, bgcolor=ft.colors.RED, width=20, height=20)
                prog_bars[f.name] = prog
                files.current.controls.append(
                    ft.Row(
                        controls=[prog, ft.Text(f.name)]
                    )
                )
        page.update()


    def on_upload_progress(e: ft.FilePickerUploadEvent):
        prog_bars[e.file_name].value = e.progress
        prog_bars[e.file_name].update()


    def upload_file(e):
        if file_picker.result is not None and file_picker.result.files is not None:
            os.chdir(f'{REMOTE_PATH}\\Recibir')
            file_name = file_picker.result.files[0].name
            path_send_file = file_picker.result.files[0].path
            path = f'{os.getcwd()}\\{file_name}'

            copy_file = shutil.copy(
                src=path_send_file,
                dst=path
            )

            if copy_file is not None:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text('Archivo cargado correctamente', text_align=ft.TextAlign.CENTER, size=20),
                    bgcolor=ft.colors.GREEN_200
                )
                page.snack_bar.duration = 3000
                page.snack_bar.open = True
                page.update()


    prefijo_dropdown = ft.Dropdown(
        width=100,
        label='Prefijo',
        border_color=ft.colors.BLUE_500,
        border=ft.colors.BLUE_500,
        options=[
            ft.dropdown.Option('A'),
            ft.dropdown.Option('D'),
            ft.dropdown.Option('m'),
            ft.dropdown.Option('k'),
        ]
    )

    consecutivo_textfield = ft.TextField(
        label='Consecutivo del archivo',
        hint_text='Por ejemplo "123"',
        input_filter=ft.NumbersOnlyInputFilter(),
        border_color=ft.colors.BLUE_500,
        border=ft.colors.BLUE_500,
    )

    juliano_textfield = ft.TextField(
        label='Día juliano o entensión',
        hint_text='Por ejemplo: "123" o "cin"',
        border_color=ft.colors.BLUE_500,
        border=ft.colors.BLUE_500,
    )

    nueva_extension_textfield = ft.TextField(
        label='Nueva extensión del archivo',
        hint_text='Por ejemplo "var"',
        border_color=ft.colors.BLUE_500,
        border=ft.colors.BLUE_500,
    )

    file_picker = ft.FilePicker(
        on_result=file_picker_result,
        on_upload=on_upload_progress
    )

    page.overlay.append(file_picker)

    content = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[ft.Text(value='Recibir archivos', size=35, color=ft.colors.RED_500)]
            ),
            ft.Container(
                width=550,
                height=620,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.GREY_900,
                border_radius=ft.border_radius.all(5),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[prefijo_dropdown, consecutivo_textfield],
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[juliano_textfield],
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[nueva_extension_textfield],
                        ),
                        ft.Row(
                            alignment=  ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.ElevatedButton(
                                    text='Seleccionar archivo',
                                    style=ft.ButtonStyle(
                                        padding=20,
                                        color={ft.MaterialState.DEFAULT: ft.colors.BLACK},
                                        bgcolor={
                                            ft.MaterialState.DEFAULT: ft.colors.BLUE_200,
                                            ft.MaterialState.HOVERED: ft.colors.BLUE_500,
                                            ft.MaterialState.PRESSED: ft.colors.BLUE_700,
                                        },
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                    icon=ft.icons.FOLDER_OPEN_ROUNDED,
                                    on_click=lambda _: file_picker.pick_files()
                                ),
                                ft.ElevatedButton(
                                    text='Copiar archivo',
                                    style=ft.ButtonStyle(
                                        padding=20,
                                        color={ft.MaterialState.DEFAULT: ft.colors.BLACK},
                                        bgcolor={
                                            ft.MaterialState.DEFAULT: ft.colors.GREEN_300,
                                            ft.MaterialState.HOVERED: ft.colors.GREEN_500,
                                            ft.MaterialState.PRESSED: ft.colors.GREEN_700,
                                        },
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                    on_click=make_copy
                                ),
                            ],
                        ),
                        ft.Row(
                            ref=files,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.ElevatedButton(
                                    text='Subir archivo',
                                    ref=upload_button,
                                    style=ft.ButtonStyle(
                                        padding=20,
                                        color={ft.MaterialState.DEFAULT: ft.colors.BLACK},
                                        bgcolor={
                                            ft.MaterialState.DEFAULT: ft.colors.YELLOW_300,
                                            ft.MaterialState.HOVERED: ft.colors.YELLOW_500,
                                            ft.MaterialState.PRESSED: ft.colors.YELLOW_700,
                                        },
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                    icon=ft.icons.UPLOAD_FILE_ROUNDED,
                                    on_click=upload_file,
                                    disabled=True,
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        ],
    )

    return content
