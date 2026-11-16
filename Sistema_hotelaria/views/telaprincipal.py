import flet as ft
from . import aba_visao_geral, aba_reservas, aba_hospedes, aba_quartos


# =========================================================
# NAVEGAÇÃO PRINCIPAL
# =========================================================

def navegar(page):

    conteudo = ft.Container(content=None, expand=True)

    titulo_cabecalho = ft.Text(
        "Visão geral",
        weight=ft.FontWeight.BOLD
    )

    nomes_menu = [
        (ft.Icons.DASHBOARD_OUTLINED, "Visão Geral"),
        (ft.Icons.CALENDAR_MONTH_OUTLINED, "Reservas"),
        (ft.Icons.PEOPLE_OUTLINED, "Hóspedes"),
        (ft.Icons.BED_OUTLINED, "Quartos")
    ]

    menu_items = []

    def mudar_pagina(indice):
        if indice == 0:
            conteudo.content = aba_visao_geral.telavisãogeral()
        elif indice == 1:
            conteudo.content = aba_reservas.telareservas(page)
        elif indice == 2:
            conteudo.content = aba_hospedes.telahospedes(page)
        elif indice == 3:
            conteudo.content = aba_quartos.telaquartos(page)

        titulo_cabecalho.value = nomes_menu[indice][1]

        for i, item in enumerate(menu_items):
            if i == indice:
                item.bgcolor = "#8a354a"
                item.content.controls[0].color = "#ffffff"
                item.content.controls[1].color = "#ffffff"
            else:
                item.bgcolor = None
                item.content.controls[0].color = "#c98697"
                item.content.controls[1].color = "#c98697"

        page.update()

    # MENU LATERAL
    for i, (icone, nome) in enumerate(nomes_menu):
        item = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(
                        icone,
                        color="#ffffff" if i == 0 else "#c98697"
                    ),
                    ft.Text(
                        nome,
                        color="#ffffff" if i == 0 else "#c98697"
                    )
                ],
                spacing=12
            ),
            padding=12,
            border_radius=10,
            bgcolor="#8a354a" if i == 0 else None,
            on_click=lambda e, i=i: mudar_pagina(i)
        )
        menu_items.append(item)

    rail = ft.Column(
        controls=menu_items,
        spacing=10
    )

    # LOGO
    logo = ft.Row(
        controls=[
            ft.Icon(ft.Icons.APARTMENT, color="white", size=25),
            ft.Column(
                controls=[
                    ft.Text(
                        "Estadia",
                        size=20,
                        color="white",
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Text(
                        "GESTÃO HOTELEIRA",
                        size=8,
                        color="#9a5365"
                    )
                ],
                spacing=0
            )
        ],
        spacing=8
    )

    # IDENTIFICAÇÃO DO HOTEL
    hotel = ft.Container(
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text("Aurora Jardins", size=11, color="white"),
                        ft.Text("São Paulo, SP", size=8, color="#c98697")
                    ],
                    spacing=3,
                    expand=True
                ),
                ft.Icon(ft.Icons.UNFOLD_MORE, size=14, color="#c98697")
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        padding=10,
        border=ft.Border.all(1, "#84364c"),
        border_radius=8
    )

    ajuda = ft.Row(
        controls=[
            ft.Icon(ft.Icons.HELP_OUTLINE, size=14, color="#c98697"),
            ft.Text("Central de ajuda", size=9, color="#c98697")
        ],
        spacing=8
    )

    perfil = ft.Row(
        controls=[
            ft.CircleAvatar(
                content=ft.Text("MC", size=9, color="#701c33"),
                bgcolor="#f5e5e9",
                radius=12
            ),
            ft.Column(
                controls=[
                    ft.Text("Marina Costa", size=9, color="white"),
                    ft.Text("Gerente de recepção", size=7, color="#c98697")
                ],
                spacing=2
            )
        ],
        spacing=8
    )

    nome_operacao = ft.Text(
        "OPERAÇÃO",
        size=12,
        color="#cd889a"
    )

    barra_lateral = ft.Container(
        content=ft.Column(
            controls=[
                logo,
                ft.Container(height=8),
                hotel,
                ft.Container(height=5),
                nome_operacao,
                rail,
                ft.Container(expand=True),
                ajuda,
                ft.Container(height=10),
                perfil
            ],
            spacing=10,
            expand=True
        ),
        bgcolor="#701c33",
        width=200,
        padding=10
    )

    # CABEÇALHO
    cabecalho = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("Operação"),
                ft.Icon(ft.Icons.CHEVRON_RIGHT),
                titulo_cabecalho,
                ft.Container(expand=True),
                ft.Icon(ft.Icons.NOTIFICATIONS_NONE),
                ft.Text("MC")
            ]
        ),
        padding=15,
        bgcolor="#FFFFFF"
    )

    conteudo.content = aba_visao_geral.telavisãogeral()

    area_principal = ft.Column(
        controls=[
            cabecalho,
            ft.Container(
                content=conteudo,
                padding=20,
                expand=True
            )
        ],
        expand=True,
        spacing=0
    )

    barravertical = ft.Row(
        controls=[
            barra_lateral,
            ft.VerticalDivider(width=1, color="#84364c"),
            ft.Container(
                content=area_principal,
                expand=True,
                bgcolor="#F5F5F5"
            )
        ],
        expand=True,
        spacing=0
    )

    return barravertical


# =========================================================
