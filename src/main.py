import flet as ft

import const
from pages.index import index_view
from pages.enviar import enviar_view
from pages.recibir import recibir_view


def main(page: ft.Page):
    page.title = const.WINDOW_TITLE
    page.window_width = const.WINDOW_WIDTH
    page.window_height = const.WINDOW_HEIGHT

    index = index_view()
    enviar = enviar_view()
    recibir = recibir_view()


    def route_change(route):
        page.views.clear()

        if page.route == '/':
            page.views.append(index)
            page.update()

        if page.route == '/enviar':
            page.views.append(enviar)
            page.update()

        if page.route == '/recibir':
            page.views.append(recibir)
            page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
