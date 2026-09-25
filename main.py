import flet as ft
import shutil
from pathlib import Path
import uuid

from dados.jogos import carregar_jogos, salvar_jogos


def main(page: ft.Page):
    page.title = "GameList"
    page.window.width = 750
    page.window.height = 750

    file_picker = ft.FilePicker()
    caminho_capa = None
    jogo_em_edicao = None

    PASTA_CAPAS = Path("capas")
    PASTA_CAPAS.mkdir(exist_ok=True)

    async def selecionar_capa(e):
        nonlocal caminho_capa

        arquivos = await file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["png", "jpg", "jpeg", "webp"],
        )

        if arquivos:
            caminho_capa = arquivos[0].path
            print("CAPA SELECIONADAD:", caminho_capa)

            imagem_capa.src = caminho_capa
            imagem_capa.visible = True
            imagem_capa.update()

    titulo = ft.Text(
        "🎮 GameGears",
        size=50,
        weight=ft.FontWeight.W_900,
    )

    subtitulo = ft.Text(
        "Sua biblioteca pessoal de jogos",
        size=18,
    )

    texto_edicao = ft.Text(
        "",
        size=16,
        weight=ft.FontWeight.BOLD,
    )

    mensagem = ft.Text(
        "",
        color=ft.Colors.RED,
        size=14,
    )

    nome = ft.TextField(
        label="Nome do jogo",
        width=415,
    )

    plataforma = ft.TextField(
        label="Plataforma",
        width=200,
    )

    genero = ft.TextField(
        label="Gênero",
        width=200,
    )

    ano = ft.TextField(
        label="Ano de lançamento",
        width=150,
    )

    status = ft.Dropdown(
        label="Status",
        width=170,
        options=[
            ft.DropdownOption(key="Quero jogar", text="Quero jogar"),
            ft.DropdownOption(key="Jogando", text="Jogando"),
            ft.DropdownOption(key="Zerado", text="Zerado"),
            ft.DropdownOption(key="Abandonei", text="Abandonei"),
        ],
    )

    nota = ft.Dropdown(
        label="Nota",
        width=120,
        options=[
            ft.DropdownOption(key=str(i), text=str(i))
            for i in range(11)
        ],
    )

    imagem_capa = ft.Image(
        src="imagem_padrao.png",
        width=150,
        height=200,
        fit=ft.BoxFit.COVER,
        visible=False
    )

    lista_jogos = ft.Column()

    def editar_jogo(jogo):
        nonlocal jogo_em_edicao
        nonlocal caminho_capa

        jogo_em_edicao = jogo
        caminho_capa = None

        texto_edicao.value = f"✏️ Editando: {jogo['nome']}"
        botao_adicionar.content = "Salvar alteração"

        nome.value = jogo["nome"]
        plataforma.value = jogo["plataforma"]
        genero.value = jogo["genero"]
        ano.value = str(jogo["ano"])
        status.value = jogo["status"]
        nota.value = jogo["nota"]
        critica.value = jogo["critica"]

        if jogo.get("imagem"):
            imagem_capa.src = jogo["imagem"]
            imagem_capa.visible = True
        else:
            imagem_capa.visible = False

        page.update()

    def confirmar_exclusao(jogo):
        dialogo = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmar exclusão"),
            content=ft.Text(
                f"Tem certeza que deseja excluir o jogo '{jogo['nome']}'?"
            ),
            actions=[
                ft.Button(
                    "Cancelar",
                    on_click=lambda e: page.pop_dialog(),
                ),
                ft.Button(
                    "Excluir",
                    on_click=lambda e: confirmar_e_excluir(jogo),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.show_dialog(dialogo)

    def confirmar_e_excluir(jogo):
        page.pop_dialog()

        excluir_jogo(jogo)

    def excluir_jogo(jogo):
        jogos = carregar_jogos()

        jogos = [
            item
            for item in jogos
            if item["id"] != jogo["id"]
        ]

        salvar_jogos(jogos)

        mensagem.value = "Jogo excluído com sucesso!"
        mensagem.color = ft.Colors.GREEN

        mostrar_jogos()

    def mostrar_jogos():
        jogos = carregar_jogos()

        lista_jogos.controls.clear()

        for jogo in jogos:
            nota_jogo = jogo["nota"] if jogo["nota"] is not None else "—"

            caminho_imagem = jogo.get("imagem")

            if jogo["status"] == "Zerado":
                cor_status = ft.Colors.GREEN
            elif jogo["status"] == "Jogando":
                cor_status = ft.Colors.BLUE
            elif jogo["status"] == "Quero jogar":
                cor_status = ft.Colors.ORANGE
            else:
                cor_status = ft.Colors.RED

            if not caminho_imagem:
                caminho_imagem = "imagem_padrao.png"

            card_jogo = ft.Card(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Image(
                                src=caminho_imagem,
                                width=130,
                                height=180,
                                fit=ft.BoxFit.COVER,
                            ),

                            ft.Column(
                                [
                                    ft.Text(
                                        jogo["nome"],
                                        size=22,
                                        weight=ft.FontWeight.BOLD,
                                    ),

                                    ft.Text(
                                        f"{jogo['plataforma']} • {jogo['genero']}",
                                        size=14,
                                    ),

                                    ft.Text(
                                        f"Ano: {jogo['ano']}",
                                        size=14,
                                    ),

                                    ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.Text(
                                                    f"● {jogo['status']}",
                                                    size=14,
                                                    weight=ft.FontWeight.BOLD,
                                                    color=cor_status,
                                                ),
                                                padding=8,
                                                border_radius=8,
                                            ),

                                            ft.Container(
                                                content=ft.Text(
                                                    f"★ {nota_jogo}",
                                                    size=14,
                                                    weight=ft.FontWeight.BOLD,
                                                ),
                                                padding=8,
                                                border_radius=8,
                                            ),
                                        ],
                                        spacing=10,
                                    ),

                                    ft.Text(
                                        f'"{jogo["critica"]}"'
                                        if jogo["critica"]
                                        else "Sem crítica.",
                                        size=14,
                                        italic=True,
                                    ),

                                    ft.Row(
                                        [
                                            ft.Button(
                                                "Editar",
                                                icon=ft.Icons.EDIT,
                                                on_click=lambda e, jogo=jogo: editar_jogo(
                                                    jogo),
                                            ),
                                            ft.Button(
                                                "Excluir",
                                                icon=ft.Icons.DELETE,
                                                on_click=lambda e, jogo=jogo: confirmar_exclusao(
                                                    jogo),
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                ],
                                spacing=8,
                                expand=True,
                            ),
                        ],
                        spacing=20,
                    ),
                    padding=20,
                    width=600,
                )
            )

            lista_jogos.controls.append(card_jogo)

        lista_jogos.update()

    botao_capa = ft.Button(
        "🖼️ Selecionar capa",
        on_click=selecionar_capa,
    )

    critica = ft.TextField(
        label="Crítica",
        width=400,
        multiline=True,
        min_lines=3,
        max_lines=5,
    )

    def adicionar_jogo(e):
        nonlocal caminho_capa
        nonlocal jogo_em_edicao

        if not nome.value:
            mensagem.value = "Digite o nome do jogo!"
            page.update()
            return

        if not plataforma.value:
            mensagem.value = "Digite a plataforma!"
            page.update()
            return

        if not genero.value:
            mensagem.value = "Digite o gênero!"
            page.update()
            return

        if not ano.value:
            mensagem.value = "Digite o ano de lançamento!"
            page.update()
            return

        if not str(ano.value).isdigit():
            mensagem.value = "O ano deve conter apenas números!"
            page.update()
            return

        ano_jogo = int(ano.value)

        if ano_jogo < 1950 or ano_jogo > 2026:
            mensagem.value = "Digite um ano entre 1950 e 2026!"
            page.update()
            return

        if nota.value is not None and nota.value != "":
            if not str(nota.value).isdigit():
                mensagem.value = "A nota deve conter apenas números!"
                page.update()
                return

            nota_jogo = int(nota.value)

            if nota_jogo < 0 or nota_jogo > 10:
                mensagem.value = "A nota deve estar entre 0 e 10!"
                page.update()
                return
        else:
            nota_jogo = None

        if not status.value:
            mensagem.value = "Selecione o status!"
            page.update()
            return

        mensagem.value = ""

        jogos = carregar_jogos()

        if jogo_em_edicao:
            for jogo in jogos:
                if jogo["id"] == jogo_em_edicao["id"]:
                    print("ID encontrado:", jogo["id"])
                    print("Nome antigo:", jogo["nome"])
                    print("Nome novo:", nome.value)

                    jogo["nome"] = nome.value
                    jogo["plataforma"] = plataforma.value
                    jogo["genero"] = genero.value
                    jogo["ano"] = ano_jogo
                    jogo["status"] = status.value
                    jogo["nota"] = nota_jogo
                    jogo["critica"] = critica.value

                    if caminho_capa:
                        extensao = Path(caminho_capa).suffix
                        nome_imagem = f"{uuid.uuid4()}{extensao}"
                        destino = PASTA_CAPAS / nome_imagem
                        shutil.copy2(caminho_capa, destino)
                        jogo["imagem"] = str(destino).replace("\\", "/")

                    break

            salvar_jogos(jogos)

            mensagem.value = "Jogo atualizado com sucesso!"
            mensagem.color = ft.Colors.GREEN

            jogo_em_edicao = None

            nome.value = ""
            plataforma.value = ""
            genero.value = ""
            ano.value = ""
            status.value = None
            nota.value = None
            critica.value = ""

            texto_edicao.value = ""
            botao_adicionar.content = "Adicionar jogo"

            caminho_capa = None
            imagem_capa.visible = False

            mostrar_jogos()
            page.update()

        else:
            novo_id = max(
                (jogo["id"] for jogo in jogos),
                default=0
            ) + 1

            print("CAMINHO DA CAPA:", caminho_capa)

            imagem_jogo = None

            if caminho_capa:
                extensao = Path(caminho_capa).suffix
                nome_imagem = f"{uuid.uuid4()}{extensao}"
                destino = PASTA_CAPAS / nome_imagem

                shutil.copy2(caminho_capa, destino)

                imagem_jogo = str(destino).replace("\\", "/")

            jogo = {
                "id": novo_id,
                "nome": nome.value,
                "plataforma": plataforma.value,
                "genero": genero.value,
                "ano": ano_jogo,
                "status": status.value,
                "nota": nota_jogo,
                "critica": critica.value,
                "imagem": imagem_jogo,
            }

            jogos.append(jogo)

            salvar_jogos(jogos)

            mensagem.value = "Jogo salvo com sucesso!"
            mensagem.color = ft.Colors.GREEN

            nome.value = ""
            plataforma.value = ""
            genero.value = ""
            ano.value = ""
            status.value = None
            nota.value = None
            critica.value = ""

            caminho_capa = None
            imagem_capa.src = "image_padrão.png"

            mostrar_jogos()

            imagem_capa.visible = True

            page.update()

    botao_adicionar = ft.Button(
        content="Adicionar jogo",
        width=200,
        on_click=adicionar_jogo,
    )

    conteudo = ft.Column(
        [
            titulo,
            subtitulo,
            texto_edicao,
            mensagem,
            ft.Text(
                "🎮 Informações do jogo",
                size=18,
                weight=ft.FontWeight.BOLD,
            ),

            nome,
            ft.Row(
                [
                    plataforma,
                    genero,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15,
            ),
            ft.Row(
                [
                    ano,
                    status,
                    nota,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15,
            ),
            critica,
            imagem_capa,
            botao_capa,
            botao_adicionar,

            ft.Container(height=20),

            ft.Text(
                "📚 Minha biblioteca",
                size=22,
                weight=ft.FontWeight.BOLD,
            ),
            lista_jogos,
        ],
        scroll=ft.ScrollMode.AUTO,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(
        ft.Row(
            [
                conteudo,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,

        )
    )
    mostrar_jogos()


ft.run(main, assets_dir="assets")
