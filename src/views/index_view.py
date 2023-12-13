import flet as ft


def index_view(page):
    content = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[ft.Text(value='Copia de archivos SAAIM3', size=35)],
            ),
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
                            src='assets/logo_lw.png',
                            width=400,
                            height=400,
                        ),
                    ],
                ),
            ),
        ],
    )

    return content
