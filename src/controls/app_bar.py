import flet as ft


def navbar(page):
    navbar = ft.AppBar(
        leading=ft.Icon(
            name=ft.icons.AUTO_AWESOME_MOTION,
            color=ft.colors.BLUE_500,
            size=36,
        ),
        title=ft.Text(
            value='Epson',
            color=ft.colors.BLUE_300,
            size=32
        ),
        bgcolor=ft.colors.GREY_900,
        actions=[
            ft.IconButton(
                icon=ft.icons.ARROW_CIRCLE_UP,
                icon_color=ft.colors.BLUE_500,
                icon_size=36,
                tooltip='Enviar a prevalidador',
                on_click=lambda _: page.go(route='/send')
            ),
            ft.IconButton(
                icon=ft.icons.ARROW_CIRCLE_DOWN,
                icon_color=ft.colors.BLUE_500,
                icon_size=36,
                tooltip='Respuesta de prevalidador',
                on_click=lambda _: page.go(route='/receive')
            ),
        ],
    )

    return navbar
