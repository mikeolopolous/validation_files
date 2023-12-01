import flet as ft


def index_view():
    return ft.View(
        route='/',
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            leading=ft.Icon(
                name=ft.icons.AUTO_AWESOME_MOTION,
                color=ft.colors.BLUE_500,
                size=36,
            ),
            title=ft.Text(
                value='Inicio',
                color=ft.colors.BLUE_300,
                size=35
            ),
            bgcolor=ft.colors.GREY_900,
            actions=[
                ft.IconButton(
                    icon=ft.icons.ARROW_CIRCLE_UP,
                    icon_color=ft.colors.BLUE_500,
                    icon_size=36,
                    tooltip='Enviar a prevalidador',
                    on_click=lambda e: e.page.go(route='/enviar')
                ),
                ft.IconButton(
                    icon=ft.icons.ARROW_CIRCLE_DOWN,
                    icon_color=ft.colors.BLUE_500,
                    icon_size=36,
                    tooltip='Respuesta de prevalidador',
                    on_click=lambda e: e.page.go(route='/recibir')
                ),
            ],
        ),
        controls=[
            ft.Text(value='Copia de archivos SAAIM3', size=35),
            ft.Container(
                width=550,
                height=620,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.GREY_900,
                border_radius=ft.border_radius.all(5),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                            src='../../imgs/logo_lw.png',
                            width=400,
                            height=400,
                        ),
                    ]
                )
            )
        ]
    )
