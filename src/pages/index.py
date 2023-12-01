import flet as ft


def index_view():
    return ft.View(
        route='/',
        appbar=ft.AppBar(
            leading=ft.Icon(
                name=ft.icons.AUTO_AWESOME_MOTION,
                color=ft.colors.BLUE_500,
                size=36,
            ),
            title=ft.Text(value='Menú principal', color=ft.colors.BLUE_GREY_500),
            bgcolor=ft.colors.SURFACE_VARIANT,
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
    )
