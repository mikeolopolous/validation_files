import os
import shutil
import flet as ft

from pathlib import Path


def send_view(page):
    HOME_PATH = Path.home()
    REMOTE_PATH = 'M:\\'
    LOCAL_PATH = str(HOME_PATH) + '\\Downloads\\'
    PATENTE = '3977'


    def make_copy(e):
        os.chdir(f'{REMOTE_PATH}\\Enviar')

        if prefijo_dropdown.value != '' and consecutivo_textfield.value != '' and juliano_textfield.value != '':
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
                content=ft.Text('Todos los campos son obligatorios', text_align=ft.TextAlign.CENTER),
                bgcolor=ft.colors.RED_300
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
            ft.dropdown.Option('E'),
            ft.dropdown.Option('d'),
            ft.dropdown.Option('m'),
        ]
    )

    consecutivo_textfield = ft.TextField(
        label='Consecutivo del archivo',
        hint_text='Por ejemplo: "123"',
        input_filter=ft.NumbersOnlyInputFilter(),
        border_color=ft.colors.BLUE_500,
        border=ft.colors.BLUE_500,
    )

    juliano_textfield = ft.TextField(
        label='Día juliano',
        hint_text='Por ejemplo: "123"',
        border_color=ft.colors.BLUE_500,
        border=ft.colors.BLUE_500,
    )

    nueva_extension_textfield = ft.TextField(
        label='Nueva extensión del archivo',
        hint_text='Por ejemplo: "var"',
        border_color=ft.colors.BLUE_500,
        border=ft.colors.BLUE_500,
    )

    content = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[ft.Text(value='Enviar archivos', size=35, color=ft.colors.RED_500)],
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
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.ElevatedButton(
                                    text='Subir archivo',
                                    style=ft.ButtonStyle(
                                        padding=20,
                                        color={ft.MaterialState.DEFAULT: ft.colors.BLACK},
                                        bgcolor={
                                            ft.MaterialState.DEFAULT: ft.colors.BLUE_500,
                                            ft.MaterialState.PRESSED: ft.colors.BLUE_900,
                                        },
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                ),
                                ft.ElevatedButton(
                                    text='Copiar archivo',
                                    style=ft.ButtonStyle(
                                        padding=20,
                                        color={ft.MaterialState.DEFAULT: ft.colors.BLACK},
                                        bgcolor={
                                            ft.MaterialState.DEFAULT: ft.colors.GREEN_300,
                                            ft.MaterialState.PRESSED: ft.colors.GREEN_700,
                                        },
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                    on_click=make_copy
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        ],
    )

    return content
