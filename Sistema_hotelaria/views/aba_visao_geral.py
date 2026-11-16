import flet as ft


# TELA 1 - VISÃO GERAL
# =========================================================

def telavisãogeral():

    titulo = ft.Text(
        "Visão Geral",
        size=25,
        weight=ft.FontWeight.BOLD,
        color="#263238"
    )

    card1 = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Taxa de Ocupação"),
                ft.Text("75%", size=30, weight=ft.FontWeight.BOLD)
            ],
            spacing=10
        ),
        padding=15,
        bgcolor="#FFFFFF",
        border_radius=10,
        expand=1
    )

    card2 = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Reservas Ativas"),
                ft.Text("74", size=30, weight=ft.FontWeight.BOLD)
            ],
            spacing=10
        ),
        padding=15,
        bgcolor="#FFFFFF",
        border_radius=10,
        expand=1
    )

    card3 = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Quartos Disponíveis"),
                ft.Text("13", size=30, weight=ft.FontWeight.BOLD)
            ],
            spacing=10
        ),
        padding=15,
        bgcolor="#FFFFFF",
        border_radius=10,
        expand=1
    )

    cards = ft.Row(
        controls=[card1, card2, card3],
        spacing=20
    )

    ver_reservas = ft.Row(
        controls=[
            ft.Text("Ver reservas", color="#701C33"),
            ft.Icon(ft.Icons.ARROW_RIGHT_ALT, color="#701C33", size=20)
        ],
        alignment=ft.MainAxisAlignment.END
    )

    chegadas = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Próximas chegadas",
                    size=20,
                    weight=ft.FontWeight.BOLD
                ),
                ver_reservas,
                ft.Text("Reservas com chegada pendente hoje"),
                ft.Divider(),
                ft.Row(
                    controls=[
                        ft.Text("Ana Ribeiro", weight=ft.FontWeight.BOLD),
                        ft.Text("204 - Deluxe casal"),
                        ft.Container(expand=True),
                        ft.Text("15:00")
                    ]
                ),
                ft.Divider(),
                ft.Row(
                    controls=[
                        ft.Text("Carlos Mendes", weight=ft.FontWeight.BOLD),
                        ft.Text("208 - Deluxe casal"),
                        ft.Container(expand=True),
                        ft.Text("15:30")
                    ]
                ),
                ft.Divider(),
                ft.Row(
                    controls=[
                        ft.Text("Beatriz Lima", weight=ft.FontWeight.BOLD),
                        ft.Text("401 - Suíte"),
                        ft.Container(expand=True),
                        ft.Text("16:00")
                    ]
                )
            ],
            spacing=15
        ),
        padding=20,
        bgcolor="#FFFFFF",
        border_radius=10
    )

    return ft.Column(
        controls=[titulo, cards, chegadas],
        spacing=20,
        scroll=ft.ScrollMode.AUTO
    )


# =========================================================
