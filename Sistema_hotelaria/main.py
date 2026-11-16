import flet as ft
from views import telaprincipal


def main(page: ft.Page):
    page.title = "Sistema de Hotelaria - Estadia"
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#F5F5F5"

    tela = telaprincipal.navegar(page)
    page.add(tela)


ft.run(main=main)
