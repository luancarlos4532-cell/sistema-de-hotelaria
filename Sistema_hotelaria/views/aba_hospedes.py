import flet as ft


# TELA 3 - HÓSPEDES
# =========================================================

def telahospedes(page):

    # Lista de exemplo. Depois poderá ser ligada ao MySQL.
    hospedes = [
        {
            "nome": "Ana Ribeiro",
            "cpf": "12345678901",
            "nascimento": "18/03/1992",
            "nacionalidade": "Brasileira",
            "email": "ana.ribeiro@email.com",
            "telefone": "(11) 99876-4321",
            "cep": "01415-001",
            "endereco": "Rua Bela Cintra, 420",
            "cidade": "São Paulo",
            "estado": "SP",
            "preferencias": "Prefere andar alto e travesseiros extras",
            "situacao": "Hospedado"
        },
        {
            "nome": "Beatriz Lima",
            "cpf": "23456789012",
            "nascimento": "12/08/1995",
            "nacionalidade": "Brasileira",
            "email": "beatriz.lima@email.com",
            "telefone": "(11) 98888-1111",
            "cep": "",
            "endereco": "",
            "cidade": "",
            "estado": "",
            "preferencias": "",
            "situacao": "Chegada hoje"
        },
        {
            "nome": "Carlos Mendes",
            "cpf": "34567890123",
            "nascimento": "05/11/1988",
            "nacionalidade": "Brasileira",
            "email": "carlos.mendes@email.com",
            "telefone": "(11) 97777-2222",
            "cep": "",
            "endereco": "",
            "cidade": "",
            "estado": "",
            "preferencias": "",
            "situacao": "Chegada hoje"
        },
        {
            "nome": "Fernanda Rocha",
            "cpf": "45678901234",
            "nascimento": "21/07/1990",
            "nacionalidade": "Brasileira",
            "email": "fernanda@email.com",
            "telefone": "(11) 96666-3333",
            "cep": "",
            "endereco": "",
            "cidade": "",
            "estado": "",
            "preferencias": "",
            "situacao": "Hospedado"
        },
        {
            "nome": "Juliana Martins",
            "cpf": "56789012345",
            "nascimento": "09/02/1994",
            "nacionalidade": "Brasileira",
            "email": "juliana@email.com",
            "telefone": "(11) 95555-4444",
            "cep": "",
            "endereco": "",
            "cidade": "",
            "estado": "",
            "preferencias": "",
            "situacao": "Hospedado"
        },
        {
            "nome": "Rafael Costa",
            "cpf": "67890123456",
            "nascimento": "14/06/1985",
            "nacionalidade": "Brasileira",
            "email": "rafael.costa@email.com",
            "telefone": "(11) 94444-5555",
            "cep": "",
            "endereco": "",
            "cidade": "",
            "estado": "",
            "preferencias": "",
            "situacao": "Hospedado"
        }
    ]

    area_hospedes = ft.Container(expand=True)
    mensagem = ft.Text("", size=11, color="#8a354a")

    def mostrar_lista():
        campo_busca = ft.TextField(
            label="Buscar nome, CPF ou e-mail",
            prefix_icon=ft.Icons.SEARCH,
            expand=True
        )

        linhas = ft.Column(spacing=0, scroll=ft.ScrollMode.AUTO)

        def montar_linhas():
            linhas.controls.clear()
            busca = (campo_busca.value or "").lower()

            encontrados = 0

            for indice, hospede in enumerate(hospedes):
                texto = (
                    hospede["nome"] + " " +
                    hospede["cpf"] + " " +
                    hospede["email"]
                ).lower()

                if busca in texto:
                    encontrados += 1

                    cor = (
                        "#8a354a"
                        if hospede["situacao"] == "Hospedado"
                        else "#315D91"
                    )

                    linha = ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Icon(
                                        ft.Icons.PERSON_OUTLINED,
                                        size=18,
                                        color="#8a354a"
                                    ),
                                    width=32,
                                    height=32,
                                    bgcolor="#F5E5E9",
                                    border_radius=20,
                                    alignment=ft.Alignment.CENTER
                                ),
                                ft.Text(
                                    hospede["nome"],
                                    size=11,
                                    weight=ft.FontWeight.BOLD,
                                    expand=2
                                ),
                                ft.Text(
                                    hospede["email"],
                                    size=10,
                                    expand=2
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        "• " + hospede["situacao"],
                                        size=10,
                                        color=cor
                                    ),
                                    bgcolor="#EEF2F7" if cor == "#315D91" else "#F5E5E9",
                                    padding=6,
                                    border_radius=6,
                                    expand=1
                                ),
                                ft.TextButton(
                                    "Editar",
                                    on_click=lambda e, i=indice: mostrar_formulario(i)
                                ),
                                ft.TextButton(
                                    "Excluir",
                                    on_click=lambda e, i=indice: excluir_hospede(i)
                                )
                            ],
                            spacing=8
                        ),
                        padding=10,
                        border=ft.Border.only(
                            bottom=ft.BorderSide(1, "#EEEEEE")
                        )
                    )

                    linhas.controls.append(linha)

            quantidade.value = str(encontrados) + " hóspedes encontrados"
            page.update()

        def pesquisar(e):
            montar_linhas()

        quantidade = ft.Text(
            str(len(hospedes)) + " hóspedes",
            size=10,
            color="#777777"
        )

        botao_buscar = ft.Button(
            content=ft.Text("Buscar"),
            bgcolor="#F5E5E9",
            color="#701c33",
            on_click=pesquisar
        )

        cabecalho = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("Nome", size=10, color="#777777", expand=2),
                    ft.Text("Contato", size=10, color="#777777", expand=2),
                    ft.Text("Situação", size=10, color="#777777", expand=1),
                    ft.Text("Ações", size=10, color="#777777")
                ],
                spacing=8
            ),
            padding=10,
            bgcolor="#FAFAFA"
        )

        tabela = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[campo_busca, botao_buscar],
                        spacing=8
                    ),
                    cabecalho,
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

        botao_cadastrar = ft.Button(
            content=ft.Text("＋ Cadastrar hóspede"),
            bgcolor="#B51F4B",
            color="white",
            on_click=lambda e: mostrar_formulario(None)
        )

        area_hospedes.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(
                            "Hóspedes",
                            size=25,
                            weight=ft.FontWeight.BOLD,
                            color="#263238"
                        ),
                        ft.Container(expand=True),
                        botao_cadastrar
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

    def excluir_hospede(indice):
        nome = hospedes[indice]["nome"]
        hospedes.pop(indice)
        mensagem.value = "Cadastro de " + nome + " excluído."
        mostrar_lista()

    def mostrar_formulario(indice=None):
        editando = indice is not None

        if editando:
            dados = hospedes[indice]
            nome_tela = "Editar hóspede"
            texto_botao = "Salvar alterações"
        else:
            dados = {
                "nome": "",
                "cpf": "",
                "nascimento": "",
                "nacionalidade": "Brasileira",
                "email": "",
                "telefone": "",
                "cep": "",
                "endereco": "",
                "cidade": "",
                "estado": "",
                "preferencias": "",
                "situacao": "Chegada hoje"
            }
            nome_tela = "Cadastrar hóspede"
            texto_botao = "Cadastrar hóspede"

        campo_nome = ft.TextField(
            label="Nome completo *",
            value=dados["nome"],
            expand=True
        )
        campo_cpf = ft.TextField(
            label="CPF *",
            value=dados["cpf"],
            expand=True
        )
        campo_nascimento = ft.TextField(
            label="Data de nascimento *",
            value=dados["nascimento"],
            expand=True
        )
        campo_nacionalidade = ft.TextField(
            label="Nacionalidade *",
            value=dados["nacionalidade"],
            expand=True
        )
        campo_email = ft.TextField(
            label="E-mail *",
            value=dados["email"],
            expand=True
        )
        campo_telefone = ft.TextField(
            label="Celular com DDD *",
            value=dados["telefone"],
            expand=True
        )
        campo_cep = ft.TextField(
            label="CEP (opcional)",
            value=dados["cep"],
            expand=True
        )
        campo_endereco = ft.TextField(
            label="Endereço e número (opcional)",
            value=dados["endereco"],
            expand=True
        )
        campo_cidade = ft.TextField(
            label="Cidade (opcional)",
            value=dados["cidade"],
            expand=True
        )
        campo_estado = ft.TextField(
            label="Estado (opcional)",
            value=dados["estado"],
            width=150
        )
        campo_preferencias = ft.TextField(
            label="Preferências de hospedagem (opcional)",
            value=dados["preferencias"],
            multiline=True,
            min_lines=2,
            max_lines=3
        )

        aviso = ft.Text(
            "Os campos com * são obrigatórios.",
            size=10,
            color="#777777"
        )

        resumo = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(ft.Icons.SHIELD_OUTLINED, color="#8a354a", size=24),
                    ft.Text(
                        "Um cadastro, todas as estadias",
                        weight=ft.FontWeight.BOLD,
                        color="#701c33"
                    ),
                    ft.Text(
                        "Confira as informações antes de salvar. "
                        "Esses dados poderão ser usados nas reservas e "
                        "no histórico do hóspede.",
                        size=11,
                        color="#777777"
                    ),
                    ft.Divider(),
                    ft.Text(
                        "Privacidade em primeiro lugar",
                        weight=ft.FontWeight.BOLD,
                        color="#701c33"
                    ),
                    ft.Text(
                        "Evite inserir informações sensíveis no campo "
                        "de preferências.",
                        size=11,
                        color="#777777"
                    )
                ],
                spacing=10
            ),
            padding=15,
            bgcolor="#FFFFFF",
            border_radius=10,
            width=230
        )

        def voltar(e):
            mensagem.value = ""
            mostrar_lista()

        def salvar(e):
            nome = (campo_nome.value or "").strip()
            cpf = "".join(
                caractere for caractere in (campo_cpf.value or "")
                if caractere.isdigit()
            )
            nascimento = (campo_nascimento.value or "").strip()
            nacionalidade = (campo_nacionalidade.value or "").strip()
            email = (campo_email.value or "").strip()
            telefone = (campo_telefone.value or "").strip()

            if (
                nome == "" or len(cpf) != 11 or nascimento == ""
                or nacionalidade == "" or "@" not in email
                or telefone == ""
            ):
                aviso.value = (
                    "Revise os campos: nome, CPF com 11 números, "
                    "nascimento, nacionalidade, e-mail válido e telefone."
                )
                aviso.color = "#B51F4B"
                page.update()
                return

            for i, outro in enumerate(hospedes):
                if outro["cpf"] == cpf and i != indice:
                    aviso.value = "Já existe um hóspede cadastrado com esse CPF."
                    aviso.color = "#B51F4B"
                    page.update()
                    return

            novo_hospede = {
                "nome": nome,
                "cpf": cpf,
                "nascimento": nascimento,
                "nacionalidade": nacionalidade,
                "email": email,
                "telefone": telefone,
                "cep": campo_cep.value or "",
                "endereco": campo_endereco.value or "",
                "cidade": campo_cidade.value or "",
                "estado": campo_estado.value or "",
                "preferencias": campo_preferencias.value or "",
                "situacao": dados["situacao"]
            }

            if editando:
                hospedes[indice] = novo_hospede
                mensagem.value = "Cadastro atualizado com sucesso!"
            else:
                hospedes.append(novo_hospede)
                mensagem.value = "Hóspede cadastrado com sucesso!"

            mostrar_lista()

        formulario = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.TextButton(
                                "‹ Voltar para Hóspedes",
                                on_click=voltar
                            )
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        nome_tela,
                                        size=25,
                                        weight=ft.FontWeight.BOLD,
                                        color="#263238"
                                    ),
                                    ft.Text(
                                        "Uma boa experiência começa por um cadastro bem cuidado.",
                                        size=11,
                                        color="#777777"
                                    )
                                ],
                                spacing=4,
                                expand=True
                            ),
                            ft.Text(
                                " * Campos obrigatórios",
                                size=10,
                                color="#777777"
                            )
                        ]
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Preencha ou confira os dados para continuar.",
                            size=11,
                            color="#8a354a"
                        ),
                        padding=12,
                        bgcolor="#F8EEF1",
                        border_radius=8
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(
                                            "♙  Dados pessoais",
                                            weight=ft.FontWeight.BOLD,
                                            color="#701c33"
                                        ),
                                        ft.Row([campo_nome, campo_cpf]),
                                        ft.Row([campo_nascimento, campo_nacionalidade]),
                                        ft.Divider(),
                                        ft.Text(
                                            "⌖  Contato e endereço",
                                            weight=ft.FontWeight.BOLD,
                                            color="#701c33"
                                        ),
                                        ft.Row([campo_email, campo_telefone]),
                                        ft.Row([campo_cep, campo_endereco]),
                                        ft.Row([campo_cidade, campo_estado]),
                                        campo_preferencias,
                                        aviso,
                                        ft.Row(
                                            controls=[
                                                ft.TextButton(
                                                    "Cancelar",
                                                    on_click=voltar
                                                ),
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
                scroll=ft.ScrollMode.AUTO
            ),
            expand=True
        )

        area_hospedes.content = formulario
        page.update()

    mostrar_lista()
    return area_hospedes


# =========================================================
