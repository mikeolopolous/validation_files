import flet as ft

import const

from views.Router import Router
from controls.app_bar import navbar


def main(page: ft.Page):
    page.theme_mode = 'dark'
    page.title = const.WINDOW_TITLE
    page.window_width = const.WINDOW_WIDTH
    page.window_height = const.WINDOW_HEIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.appbar = navbar(page)
    router = Router(page)

    page.on_route_change = router.route_change

    page.add(
        router.body
    )

    page.go('/')


ft.app(target=main, assets_dir='assets')
