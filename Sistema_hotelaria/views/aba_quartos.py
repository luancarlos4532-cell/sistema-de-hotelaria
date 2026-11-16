import flet as ft


# TELA 4 - QUARTOS
# =========================================================

def telaquartos(page):

    quartos = [
        {
            "numero": "204",
            "andar": "2º andar",
            "categoria": "Deluxe casal",
            "capacidade": "2 hóspedes",
            "camas": "1 cama de casal",
            "area": "28",
            "diaria": "380,00",
            "situacao": "Disponível",
            "comodidades": ["Wi-Fi", "Ar-condicionado", "TV", "Frigobar"],
            "observacoes": "Quarto silencioso, com vista para o jardim."
        },
        {
            "numero": "208",
            "andar": "2º andar",
            "categoria": "Standard casal",
            "capacidade": "2 hóspedes",
            "camas": "1 cama de casal",
            "area": "22",
            "diaria": "320,00",
            "situacao": "Ocupado",
            "comodidades": ["Wi-Fi", "TV"],
            "observacoes": ""
        },
        {
            "numero": "305",
            "andar": "3º andar",
            "categoria": "Deluxe twin",
            "capacidade": "2 hóspedes",
            "camas": "2 camas de solteiro",
            "area": "26",
            "diaria": "350,00",
            "situacao": "Disponível",
            "comodidades": ["Wi-Fi", "Ar-condicionado", "TV"],
            "observacoes": ""
        }
    ]

    area_quartos = ft.Container(expand=True)
    mensagem = ft.Text("", size=11, color="#8a354a")

    def mostrar_lista():
        busca = ft.TextField(
            label="Buscar número ou categoria do quarto",
            prefix_icon=ft.Icons.SEARCH,
            expand=True
        )
        linhas = ft.Column(spacing=0, scroll=ft.ScrollMode.AUTO)
        quantidade = ft.Text("", size=10, color="#777777")

        def montar_linhas():
            linhas.controls.clear()
            termo = (busca.value or "").lower()
            total = 0

            for indice, quarto in enumerate(quartos):
                if termo not in (
                    quarto["numero"] + " " + quarto["categoria"]
                ).lower():
                    continue

                total += 1
                cor = "#27805A" if quarto["situacao"] == "Disponível" else "#8a354a"

                linhas.controls.append(
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Text(quarto["numero"], size=11, weight=ft.FontWeight.BOLD, expand=1),
                                ft.Text(quarto["categoria"], size=11, expand=2),
                                ft.Text(quarto["andar"], size=10, expand=1),
                                ft.Text(quarto["capacidade"], size=10, expand=1),
                                ft.Text("R$ " + quarto["diaria"], size=10, expand=1),
                                ft.Text(quarto["situacao"], size=10, color=cor, expand=1),
                                ft.TextButton(
                                    "Editar",
                                    on_click=lambda e, i=indice: mostrar_formulario(i)
                                )
                            ],
                            spacing=8
                        ),
                        padding=10,
                        border=ft.Border.only(bottom=ft.BorderSide(1, "#EEEEEE"))
                    )
                )

            quantidade.value = str(total) + " quartos encontrados"
            page.update()

        def pesquisar(e):
            montar_linhas()

        tabela = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            busca,
                            ft.Button(
                                content=ft.Text("Buscar"),
                                bgcolor="#F5E5E9",
                                color="#701c33",
                                on_click=pesquisar
                            )
                        ],
                        spacing=8
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Text("Quarto", size=10, color="#777777", expand=1),
                                ft.Text("Categoria", size=10, color="#777777", expand=2),
                                ft.Text("Andar", size=10, color="#777777", expand=1),
                                ft.Text("Capacidade", size=10, color="#777777", expand=1),
                                ft.Text("Diária", size=10, color="#777777", expand=1),
                                ft.Text("Situação", size=10, color="#777777", expand=1),
                                ft.Text("Ações", size=10, color="#777777")
                            ],
                            spacing=8
                        ),
                        padding=10,
                        bgcolor="#FAFAFA"
                    ),
                    linhas,
                    ft.Divider(color="#EEEEEE"),
                    quantidade
                ],
                spacing=10
            ),
            padding=15,
            bgcolor="#FFFFFF",
            border_radius=10
        )

        area_quartos.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text("Quartos", size=25, weight=ft.FontWeight.BOLD, color="#263238"),
                                ft.Text("Gerencie o inventário e a disponibilidade dos quartos.", size=11, color="#777777")
                            ],
                            spacing=3,
                            expand=True
                        ),
                        ft.Button(
                            content=ft.Text("＋ Cadastrar quarto"),
                            bgcolor="#B51F4B",
                            color="white",
                            on_click=lambda e: mostrar_formulario(None)
                        )
                    ]
                ),
                mensagem,
                tabela
            ],
            spacing=15,
            expand=True,
            scroll=ft.ScrollMode.AUTO
        )

        montar_linhas()
        page.update()

    def mostrar_formulario(indice=None):
        editando = indice is not None

        if editando:
            dados = quartos[indice]
            titulo = "Editar quarto " + dados["numero"]
            texto_botao = "Salvar alterações"
        else:
            dados = {
                "numero": "",
                "andar": "",
                "categoria": "",
                "capacidade": "",
                "camas": "",
                "area": "",
                "diaria": "",
                "situacao": "Disponível",
                "comodidades": [],
                "observacoes": ""
            }
            titulo = "Cadastrar quarto"
            texto_botao = "Cadastrar quarto"

        numero = ft.TextField(label="Número do quarto *", value=dados["numero"], expand=True)
        andar = ft.Dropdown(
            label="Andar *",
            value=dados["andar"] if dados["andar"] else None,
            options=[
                ft.dropdown.Option("Térreo"),
                ft.dropdown.Option("1º andar"),
                ft.dropdown.Option("2º andar"),
                ft.dropdown.Option("3º andar"),
                ft.dropdown.Option("4º andar"),
                ft.dropdown.Option("5º andar")
            ],
            expand=True
        )
        categoria = ft.Dropdown(
            label="Categoria *",
            value=dados["categoria"] if dados["categoria"] else None,
            options=[
                ft.dropdown.Option("Standard casal"),
                ft.dropdown.Option("Standard twin"),
                ft.dropdown.Option("Deluxe casal"),
                ft.dropdown.Option("Deluxe twin"),
                ft.dropdown.Option("Suíte"),
                ft.dropdown.Option("Suíte família")
            ],
            expand=True
        )
        capacidade = ft.Dropdown(
            label="Capacidade de hóspedes *",
            value=dados["capacidade"] if dados["capacidade"] else None,
            options=[
                ft.dropdown.Option("1 hóspede"),
                ft.dropdown.Option("2 hóspedes"),
                ft.dropdown.Option("3 hóspedes"),
                ft.dropdown.Option("4 hóspedes"),
                ft.dropdown.Option("5 hóspedes"),
                ft.dropdown.Option("6 hóspedes")
            ],
            expand=True
        )
        camas = ft.Dropdown(
            label="Configuração de camas *",
            value=dados["camas"] if dados["camas"] else None,
            options=[
                ft.dropdown.Option("1 cama de solteiro"),
                ft.dropdown.Option("2 camas de solteiro"),
                ft.dropdown.Option("1 cama de casal"),
                ft.dropdown.Option("1 cama de casal e 1 solteiro"),
                ft.dropdown.Option("2 camas de casal")
            ],
            expand=True
        )
        area = ft.TextField(label="Área em m² (opcional)", value=dados["area"], expand=True)
        diaria = ft.TextField(label="Diária base (R$) *", value=dados["diaria"], expand=True)
        situacao = ft.Dropdown(
            label="Situação inicial *",
            value=dados["situacao"],
            options=[
                ft.dropdown.Option("Disponível"),
                ft.dropdown.Option("Ocupado"),
                ft.dropdown.Option("Em limpeza"),
                ft.dropdown.Option("Em manutenção")
            ],
            expand=True
        )
        comodidades = ft.TextField(
            label="Comodidades (separe por vírgula)",
            value=", ".join(dados["comodidades"]),
            hint_text="Ex.: Wi-Fi, Ar-condicionado, TV, Frigobar"
        )
        observacoes = ft.TextField(
            label="Observações (opcional)",
            value=dados["observacoes"],
            multiline=True,
            min_lines=2,
            max_lines=3
        )
        aviso = ft.Text("* Campos obrigatórios.", size=10, color="#777777")

        resumo = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(ft.Icons.BED_OUTLINED, size=25, color="#8a354a"),
                    ft.Text(
                        "Novo quarto" if not editando else "Quarto " + dados["numero"],
                        weight=ft.FontWeight.BOLD,
                        color="#701c33"
                    ),
                    ft.Text("Aurora Jardins · São Paulo, SP", size=10, color="#777777"),
                    ft.Divider(),
                    ft.Text("Organize seu inventário", weight=ft.FontWeight.BOLD, color="#701c33"),
                    ft.Text(
                        "Use um número exclusivo para identificar o quarto. "
                        "Defina a categoria, a capacidade e a diária base.",
                        size=11,
                        color="#777777"
                    ),
                    ft.Text(
                        "Depois de cadastrar, o quarto poderá ser consultado e editado nesta aba.",
                        size=11,
                        color="#777777"
                    ),
                    ft.Text("Os campos com * são obrigatórios.", size=10, color="#8a354a")
                ],
                spacing=10
            ),
            padding=15,
            bgcolor="#FFFFFF",
            border_radius=10,
            width=230
        )

        def voltar(e):
            mostrar_lista()

        def salvar(e):
            num = (numero.value or "").strip()
            valor_diaria = (diaria.value or "").strip()

            if (
                num == "" or not andar.value or not categoria.value
                or not capacidade.value or not camas.value
                or valor_diaria == "" or not situacao.value
            ):
                aviso.value = "Preencha todos os campos obrigatórios."
                aviso.color = "#B51F4B"
                page.update()
                return

            for i, outro in enumerate(quartos):
                if outro["numero"] == num and i != indice:
                    aviso.value = "Já existe um quarto com esse número."
                    aviso.color = "#B51F4B"
                    page.update()
                    return

            novo = {
                "numero": num,
                "andar": andar.value,
                "categoria": categoria.value,
                "capacidade": capacidade.value,
                "camas": camas.value,
                "area": area.value or "",
                "diaria": valor_diaria,
                "situacao": situacao.value,
                "comodidades": [
                    item.strip()
                    for item in (comodidades.value or "").split(",")
                    if item.strip()
                ],
                "observacoes": observacoes.value or ""
            }

            if editando:
                quartos[indice] = novo
                mensagem.value = "Quarto atualizado com sucesso!"
            else:
                quartos.append(novo)
                mensagem.value = "Quarto cadastrado com sucesso!"

            mostrar_lista()

        area_quartos.content = ft.Column(
            controls=[
                ft.TextButton("‹ Voltar para quartos", on_click=voltar),
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(titulo, size=25, weight=ft.FontWeight.BOLD, color="#263238"),
                                ft.Text(
                                    "Adicione um quarto ao inventário do Aurora Jardins."
                                    if not editando else
                                    "Atualize os dados e as comodidades deste quarto.",
                                    size=11,
                                    color="#777777"
                                )
                            ],
                            spacing=3,
                            expand=True
                        ),
                        ft.Text("* Campos obrigatórios", size=10, color="#777777")
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text("Identificação do quarto", weight=ft.FontWeight.BOLD, color="#701c33"),
                                    ft.Row([numero, andar]),
                                    ft.Row([categoria, capacidade]),
                                    ft.Row([camas, area]),
                                    ft.Divider(),
                                    ft.Text("Tarifa e disponibilidade", weight=ft.FontWeight.BOLD, color="#701c33"),
                                    ft.Row([diaria, situacao]),
                                    ft.Text(
                                        "A disponibilidade também é atualizada pela operação e pelas reservas.",
                                        size=10,
                                        color="#777777"
                                    ),
                                    ft.Divider(),
                                    ft.Text("Comodidades", weight=ft.FontWeight.BOLD, color="#701c33"),
                                    comodidades,
                                    observacoes,
                                    aviso,
                                    ft.Row(
                                        controls=[
                                            ft.TextButton("Cancelar", on_click=voltar),
                                            ft.Button(
                                                content=ft.Text(texto_botao),
                                                bgcolor="#B51F4B",
                                                color="white",
                                                on_click=salvar
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.END
                                    )
                                ],
                                spacing=12
                            ),
                            padding=15,
                            bgcolor="#FFFFFF",
                            border_radius=10,
                            expand=True
                        ),
                        resumo
                    ],
                    spacing=15,
                    vertical_alignment=ft.CrossAxisAlignment.START
                )
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
        page.update()

    mostrar_lista()
    return area_quartos
