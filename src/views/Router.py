import flet as ft

from views.index_view import index_view
from views.send_view import send_view
from views.receive_view import receive_view


class Router:
    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            '/': index_view(page),
            '/send': send_view(page),
            '/receive': receive_view(page),
        }
        self.body = ft.Container(content=self.routes['/'], alignment=ft.alignment.center)

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()


