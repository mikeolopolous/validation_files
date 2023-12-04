import flet as ft


def recibir_view():
    consecutivo_textfield = ft.TextField(
        label='Consecutivo del archivo',
        hint_text='Por ejemplo "123"',
        autofocus=True,
        border_color=ft.colors.BLUE_500,
        border=ft.colors.BLUE_500,
    )

    juliano_textfield = ft.TextField(
        label='Día juliano',
        hint_text='Por ejemplo: "123"',
        border_color=ft.colors.BLUE_500,
        border=ft.colors.BLUE_500,
    )

    nueva_situacion_textfield = ft.TextField(
        label='Nueva extensión del archivo',
        hint_text='Por ejemplo "var"',
        border_color=ft.colors.BLUE_500,
        border=ft.colors.BLUE_500,
    )

    return ft.View(
        route='/recibir',
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            leading=ft.Icon(
                name=ft.icons.ARROW_CIRCLE_DOWN_SHARP,
                color=ft.colors.BLUE_500,
                size=36,
            ),
            title=ft.Text(value='Recibir prevalidador', color=ft.colors.BLUE_GREY_500),
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(
                    icon=ft.icons.ARROW_CIRCLE_UP,
                    icon_color=ft.colors.BLUE_500,
                    icon_size=36,
                    tooltip='Enviar a prevalidador',
                    on_click=lambda e: e.page.go(route='/enviar'),
                ),
                ft.IconButton(
                    icon=ft.icons.ARROW_CIRCLE_DOWN,
                    icon_color=ft.colors.RED_500,
                    icon_size=36,
                ),
            ]
        ),
        controls=[
            ft.Text(
                value='Recibir archivos',
                size=35,
                color=ft.colors.RED_500,
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
                            controls=[consecutivo_textfield],
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[juliano_textfield],
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[nueva_situacion_textfield],
                        ),
                        ft.Row(
                            alignment=  ft.MainAxisAlignment.SPACE_AROUND,
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
                                ),
                            ],
                        )
                    ],
                ),
            ),
        ],
    )
