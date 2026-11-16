SISTEMA_HOTELARIA - CÓDIGO SEPARADO POR ABAS

Estrutura:
Sistema_Hotelaria_separado/
├── main.py
├── requirements.txt
└── views/
    ├── __init__.py
    ├── telaprincipal.py
    ├── aba_visao_geral.py
    ├── aba_reservas.py
    ├── aba_hospedes.py
    └── aba_quartos.py

O que cada arquivo faz:
- main.py: inicia o aplicativo Flet.
- views/telaprincipal.py: contém a barra lateral e a navegação entre as abas.
- views/aba_visao_geral.py: contém somente a tela Visão Geral.
- views/aba_reservas.py: contém somente a tela Reservas.
- views/aba_hospedes.py: contém as telas de visualizar, cadastrar e editar hóspedes.
- views/aba_quartos.py: contém as telas de listar, cadastrar e editar quartos.
- views/__init__.py: permite importar os módulos da pasta views.

Como executar:
1. Abra esta pasta no VS Code.
2. No terminal, execute: pip install -r requirements.txt
3. Execute: python main.py

Os arquivos foram separados a partir do código atual. Os dados continuam em memória e não são salvos no MySQL.
