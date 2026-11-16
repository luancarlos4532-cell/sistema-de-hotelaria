import flet as ft
import datetime


# TELA 2 - RESERVAS
# =========================================================

def telareservas(page):

    # Dados de exemplo para preencher a lista.
    reservas = [
        {
            "hospede": "Ana Ribeiro",
            "iniciais": "AR",
            "quarto": "204",
            "datas": "06 nov → 09 nov",
            "status": "Confirmada"
        },
        {
            "hospede": "Carlos Mendes",
            "iniciais": "CM",
            "quarto": "208",
            "datas": "06 nov → 09 nov",
            "status": "Confirmada"
        },
        {
            "hospede": "Beatriz Lima",
            "iniciais": "BL",
            "quarto": "401",
            "datas": "06 nov → 10 nov",
            "status": "Confirmada"
        },
        {
            "hospede": "Rafael Costa",
            "iniciais": "RC",
            "quarto": "112",
            "datas": "05 nov → 07 nov",
            "status": "Hospedado"
        },
        {
            "hospede": "Juliana Martins",
            "iniciais": "JM",
            "quarto": "305",
            "datas": "04 nov → 08 nov",
            "status": "Hospedado"
        },
        {
            "hospede": "Fernanda Rocha",
            "iniciais": "FR",
            "quarto": "310",
            "datas": "03 nov → 07 nov",
            "status": "Hospedado"
        }
    ]

    aba_selecionada = {"valor": "Ativas"}

    titulo = ft.Text(
        "Reservas",
        size=25,
        weight=ft.FontWeight.BOLD,
        color="#263238"
    )

    lista_reservas = ft.Column(spacing=0, scroll=ft.ScrollMode.AUTO)

    campo_busca = ft.TextField(
        hint_text="Buscar hóspede ou nº da reserva",
        prefix_icon=ft.Icons.SEARCH,
        height=43,
        text_size=12,
        border_radius=8,
        expand=True,
        on_change=lambda e: atualizar_lista()
    )

    filtro_status = ft.Dropdown(
        value="Todos os status",
        options=[
            ft.dropdown.Option("Todos os status"),
            ft.dropdown.Option("Confirmada"),
            ft.dropdown.Option("Hospedado")
        ],
        width=160,
        height=43,
        text_size=11
    )

    texto_quantidade = ft.Text(
        "1–6 de 74 reservas",
        size=10,
        color="#7A7A7A"
    )

    formulario_nova = ft.Container(visible=False)

    def mostrar_mensagem(mensagem):
        aviso = ft.SnackBar(content=ft.Text(mensagem))
        page.overlay.append(aviso)
        aviso.open = True
        page.update()

    def abrir_formulario(e):
        formulario_nova.visible = not formulario_nova.visible
        page.update()

    campo_cpf = ft.TextField(label="CPF do hóspede", expand=True)
    campo_quarto = ft.Dropdown(
        label="Número do quarto",
        hint_text="Selecione um quarto",
        options=[
            ft.dropdown.Option("204"),
            ft.dropdown.Option("208"),
            ft.dropdown.Option("305")
        ],
        expand=True
    )

    # Campos de data que abrem o calendário ao serem clicados.
    campo_entrada = ft.TextField(
        label="Check-in",
        hint_text="Selecione a data",
        read_only=True,
        expand=True,
        suffix_icon=ft.Icons.CALENDAR_MONTH
    )

    campo_saida = ft.TextField(
        label="Check-out",
        hint_text="Selecione a data",
        read_only=True,
        expand=True,
        suffix_icon=ft.Icons.CALENDAR_MONTH
    )

    hoje = datetime.datetime.now()

    def selecionar_checkin(e):
        if e.control.value:
            campo_entrada.value = e.control.value.strftime("%d/%m/%Y")
            seletor_checkout.first_date = e.control.value
            campo_saida.value = ""
            seletor_checkout.value = None
            page.update()

    def selecionar_checkout(e):
        if e.control.value:
            campo_saida.value = e.control.value.strftime("%d/%m/%Y")
            page.update()

    seletor_checkin = ft.DatePicker(
        first_date=hoje,
        last_date=datetime.datetime(2030, 12, 31),
        help_text="Selecione a data de check-in",
        on_change=selecionar_checkin
    )

    seletor_checkout = ft.DatePicker(
        first_date=hoje,
        last_date=datetime.datetime(2030, 12, 31),
        help_text="Selecione a data de check-out",
        on_change=selecionar_checkout
    )

    campo_entrada.on_click = lambda e: page.show_dialog(seletor_checkin)
    campo_saida.on_click = lambda e: page.show_dialog(seletor_checkout)

    def salvar_reserva(e):
        nome = campo_cpf.value.strip() if campo_cpf.value else ""
        quarto = campo_quarto.value.strip() if campo_quarto.value else ""

        if nome == "" or quarto == "":
            mostrar_mensagem("Preencha o nome do hóspede e o quarto.")
            return

        if not campo_entrada.value or not campo_saida.value:
            mostrar_mensagem("Selecione as datas de check-in e check-out.")
            return

        data_entrada = seletor_checkin.value
        data_saida = seletor_checkout.value

        if data_entrada and data_saida and data_saida.date() <= data_entrada.date():
            mostrar_mensagem("O check-out deve ser depois do check-in.")
            return

        reservas.insert(
            0,
            {
                "hospede": nome,
                "iniciais": "".join(
                    [parte[0] for parte in nome.split()[:2]]
                ).upper(),
                "quarto": quarto,
                "datas": campo_entrada.value + " → " + campo_saida.value,
                "status": "Confirmada"
            }
        )

        campo_cpf.value = ""
        campo_quarto.value = ""
        campo_entrada.value = ""
        campo_saida.value = ""
        seletor_checkin.value = None
        seletor_checkout.value = None
        seletor_checkout.first_date = hoje
        formulario_nova.visible = False
        aba_selecionada["valor"] = "Ativas"
        atualizar_abas()
        atualizar_lista()
        mostrar_mensagem("Reserva cadastrada com sucesso!")

    formulario_nova.content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Nova reserva",
                    size=16,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Row([campo_cpf, campo_quarto]),
                ft.Row([campo_entrada, campo_saida]),
                ft.Row(
                    controls=[
                        ft.TextButton(
                            "Cancelar",
                            on_click=abrir_formulario
                        ),
                        ft.Button(
                            content=ft.Text("Salvar reserva"),
                            bgcolor="#8a354a",
                            color="white",
                            on_click=salvar_reserva
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END
                )
            ],
            spacing=12
        ),
        padding=15,
        bgcolor="#FFFFFF",
        border_radius=10
    )

    def mudar_status(reserva):
        reserva["status"] = "Hospedado"
        atualizar_lista()
        mostrar_mensagem("Check-in realizado!")

    def mostrar_detalhes(reserva):
        detalhes = ft.AlertDialog(
            modal=True,
            title=ft.Text("Detalhes da reserva"),
            content=ft.Column(
                controls=[
                    ft.Text("Hóspede: " + reserva["hospede"]),
                    ft.Text("Quarto: " + reserva["quarto"]),
                    ft.Text("Período: " + reserva["datas"]),
                    ft.Text("Status: " + reserva["status"])
                ],
                tight=True,
                spacing=10
            ),
            actions=[
                ft.TextButton(
                    "Fechar",
                    on_click=lambda e: fechar_detalhes(detalhes)
                )
            ]
        )
        page.dialog = detalhes
        detalhes.open = True
        page.update()

    def fechar_detalhes(dialogo):
        dialogo.open = False
        page.update()

    def atualizar_abas():
        for nome, botao in botoes_abas.items():
            selecionado = aba_selecionada["valor"] == nome
            botao.style = ft.ButtonStyle(
                color="#701c33" if selecionado else "#777777",
                side=ft.BorderSide(
                    0,
                    "#701c33" if selecionado else "#FFFFFF"
                ),
                shape=ft.RoundedRectangleBorder(radius=0)
            )
        page.update()

    botoes_abas = {}

    def selecionar_aba(nome):
        aba_selecionada["valor"] = nome
        atualizar_abas()
        atualizar_lista()

    def criar_aba(nome, texto):
        botao = ft.TextButton(
            texto,
            on_click=lambda e, nome=nome: selecionar_aba(nome)
        )
        botoes_abas[nome] = botao
        return botao

    abas = ft.Row(
        controls=[
            criar_aba("Ativas", "Ativas · 74"),
            criar_aba("Chegadas hoje", "Chegadas hoje · 12"),
            criar_aba("Saídas hoje", "Saídas hoje · 9"),
            criar_aba("Histórico", "Histórico")
        ],
        spacing=12,
        scroll=ft.ScrollMode.AUTO
    )

    def atualizar_lista():
        lista_reservas.controls.clear()

        busca = (campo_busca.value or "").lower()
        status_escolhido = filtro_status.value

        filtradas = []

        for reserva in reservas:
            nome = reserva["hospede"].lower()
            quarto = reserva["quarto"].lower()

            corresponde_busca = busca in nome or busca in quarto
            corresponde_status = (
                status_escolhido == "Todos os status"
                or reserva["status"] == status_escolhido
            )

            if aba_selecionada["valor"] == "Ativas":
                corresponde_aba = True
            elif aba_selecionada["valor"] == "Chegadas hoje":
                corresponde_aba = reserva["status"] == "Confirmada"
            elif aba_selecionada["valor"] == "Saídas hoje":
                corresponde_aba = reserva["status"] == "Hospedado"
            else:
                corresponde_aba = True

            if corresponde_busca and corresponde_status and corresponde_aba:
                filtradas.append(reserva)

        for reserva in filtradas:
            hospedado = reserva["status"] == "Hospedado"
            cor_status = "#8a354a" if hospedado else "#315D91"
            texto_acao = "Detalhes" if hospedado else "Check-in"

            linha = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                reserva["iniciais"],
                                size=10,
                                color="#8a354a",
                                weight=ft.FontWeight.BOLD
                            ),
                            bgcolor="#F5E5E9",
                            width=30,
                            height=30,
                            border_radius=20,
                            alignment=ft.Alignment.CENTER
                        ),
                        ft.Text(
                            reserva["hospede"],
                            size=11,
                            weight=ft.FontWeight.BOLD,
                            expand=2
                        ),
                        ft.Text(reserva["quarto"], size=11, expand=1),
                        ft.Text(reserva["datas"], size=10, expand=2),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    width=6,
                                    height=6,
                                    bgcolor=cor_status,
                                    border_radius=10
                                ),
                                ft.Text(
                                    reserva["status"],
                                    size=10,
                                    color=cor_status
                                )
                            ],
                            spacing=5,
                            expand=1
                        ),
                        ft.TextButton(
                            texto_acao,
                            on_click=(
                                lambda e, r=reserva: mostrar_detalhes(r)
                                if r["status"] == "Hospedado"
                                else mudar_status(r)
                            )
                        )
                    ],
                    spacing=8
                ),
                padding=10,
                border=ft.Border.only(
                    bottom=ft.BorderSide(1, "#EEEEEE")
                )
            )

            lista_reservas.controls.append(linha)

        texto_quantidade.value = (
            str(len(filtradas)) + " reservas encontradas"
        )

        if len(filtradas) == 0:
            lista_reservas.controls.append(
                ft.Container(
                    content=ft.Text(
                        "Nenhuma reserva encontrada.",
                        color="#777777",
                        size=12
                    ),
                    padding=20
                )
            )

        page.update()

    cabecalho_tabela = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("Hóspede / reserva", size=10, color="#777777", expand=2),
                ft.Text("Quarto", size=10, color="#777777", expand=1),
                ft.Text("Check-in / check-out", size=10, color="#777777", expand=2),
                ft.Text("Status", size=10, color="#777777", expand=1),
                ft.Text("Ações", size=10, color="#777777", expand=1)
            ],
            spacing=8
        ),
        padding=10,
        bgcolor="#FAFAFA"
    )

    botao_nova = ft.Button(
        content=ft.Text("＋ Nova reserva"),
        color="white",
        bgcolor="#B51F4B",
        on_click=abrir_formulario
    )

    barra_filtros = ft.Row(
        controls=[
            campo_busca,
            filtro_status,
            ft.OutlinedButton(
                "Aplicar",
                on_click=lambda e: atualizar_lista()
            )
        ],
        spacing=8
    )

    tabela = ft.Container(
        content=ft.Column(
            controls=[
                abas,
                ft.Divider(color="#EEEEEE"),
                barra_filtros,
                ft.Container(height=5),
                cabecalho_tabela,
                lista_reservas,
                ft.Divider(color="#EEEEEE"),
                ft.Row(
                    controls=[
                        texto_quantidade,
                        ft.Container(expand=True),
                        ft.Text("‹    1    2    3    …    13    ›", size=10)
                    ]
                )
            ],
            spacing=10
        ),
        padding=15,
        bgcolor="#FFFFFF",
        border_radius=10
    )

    atualizar_abas()
    atualizar_lista()

    return ft.Column(
        controls=[
            ft.Row(
                controls=[
                    titulo,
                    ft.Container(expand=True),
                    botao_nova
                ]
            ),
            formulario_nova,
            tabela
        ],
        spacing=15,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )


# =========================================================
