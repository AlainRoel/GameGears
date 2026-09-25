# 🎮 GameGears

O **GameGears** é um aplicativo desenvolvido em **Python com Flet** para gerenciamento de uma biblioteca pessoal de jogos.

A aplicação permite cadastrar, visualizar, editar e excluir jogos, mantendo os dados salvos em um arquivo **JSON**. Também é possível adicionar capas aos jogos, atribuir status, notas e escrever uma crítica pessoal.

O projeto foi desenvolvido como atividade acadêmica do curso de **Análise e Desenvolvimento de Sistemas (ADS)** do Instituto Federal do Amapá (IFAP).

Na matéria Linguagem de Programação III ministrado pelo Professor Leo Serrao

---

## 🎯 Objetivo

O objetivo do GameGears é oferecer uma forma simples de organizar uma biblioteca pessoal de jogos, permitindo registrar informações importantes sobre cada título e acompanhar o progresso de cada jogo.

Além de servir como uma biblioteca pessoal, o projeto foi desenvolvido para aplicar conceitos de:

- Desenvolvimento de interfaces gráficas;
- Programação em Python;
- Programação orientada a eventos;
- CRUD;
- Manipulação de arquivos JSON;
- Persistência de dados;
- Validação de informações;
- Organização de projetos;
- Manipulação de imagens;
- Uso de Git e GitHub.

---

## 🚀 Funcionalidades

O GameGears possui as seguintes funcionalidades:

### ➕ Cadastrar jogos

É possível adicionar novos jogos à biblioteca informando:

- Nome do jogo;
- Plataforma;
- Gênero;
- Ano de lançamento;
- Status;
- Nota;
- Crítica;
- Capa do jogo.

Os campos **Nome, Plataforma, Gênero, Ano e Status** são obrigatórios.

A **nota, crítica e capa são opcionais**.

---

### 📚 Visualizar biblioteca

Todos os jogos cadastrados são apresentados na seção:

**"Minha biblioteca"**

Cada jogo é apresentado em um cartão contendo suas principais informações:

- 🖼️ Capa;
- 🎮 Nome;
- 🕹️ Plataforma;
- 🎯 Gênero;
- 📅 Ano de lançamento;
- 📌 Status;
- ⭐ Nota;
- 📝 Crítica.

Quando um jogo não possui uma capa personalizada, o sistema utiliza uma imagem padrão.

Quando o jogo não possui uma nota, o sistema apresenta:

`—`

---

### ✏️ Editar jogos

É possível selecionar qualquer jogo cadastrado e alterar suas informações.

Durante a edição, o sistema permite modificar:

- Nome;
- Plataforma;
- Gênero;
- Ano;
- Status;
- Nota;
- Crítica;
- Capa.

A edição permite atualizar informações de jogos que já estão cadastrados sem precisar excluí-los e cadastrá-los novamente.

---

### 🗑️ Excluir jogos

É possível excluir jogos da biblioteca.

Antes da exclusão, o GameGears apresenta uma janela de confirmação perguntando se o usuário realmente deseja excluir o jogo.

Isso ajuda a evitar exclusões acidentais.

---

## 🖼️ Capas dos jogos

O GameGears permite selecionar uma imagem do computador para utilizar como capa do jogo.

São aceitos arquivos nos formatos:

- PNG
- JPG
- JPEG
- WEBP

As imagens selecionadas são copiadas para a pasta:

```text
capas/
```

Cada imagem recebe um nome único utilizando um identificador UUID, evitando conflitos entre arquivos.

Quando nenhum arquivo é selecionado, o sistema utiliza uma imagem padrão localizada em:

```text
assets/imagem_padrao.png
```
## 📌 Status dos jogos

O GameGears permite definir um status para cada jogo cadastrado. O usuário pode escolher entre quatro opções: **Quero jogar**, para jogos que ainda não foram iniciados; **Jogando**, para jogos que estão atualmente em andamento; **Zerado**, para jogos que já foram concluídos; e **Abandonei**, para jogos que não foram concluídos e não estão mais sendo jogados. Para facilitar a identificação, cada status é apresentado visualmente com uma cor diferente na biblioteca.

---

## ⭐ Sistema de notas

O GameGears permite atribuir uma nota de **0 a 10** para cada jogo. Esse campo é opcional, permitindo que jogos que ainda não foram jogados ou avaliados sejam cadastrados normalmente. Quando uma nota é informada, ela é apresentada no cartão do jogo. Caso o jogo ainda não possua uma avaliação, o sistema apresenta o símbolo **—**, indicando que não existe uma nota cadastrada.

---

## 📝 Crítica pessoal

Cada jogo também pode receber uma crítica ou comentário pessoal sobre a experiência do usuário. Esse campo é opcional e, quando preenchido, a crítica é apresentada no cartão correspondente ao jogo. Caso nenhuma crítica tenha sido cadastrada, o sistema apresenta a mensagem **"Sem crítica."**.

---

## ✅ Validação dos dados

Antes de salvar um jogo, o GameGears realiza algumas validações para evitar o cadastro de informações incorretas ou incompletas. Os campos **Nome, Plataforma, Gênero, Ano e Status** são obrigatórios e precisam ser preenchidos para que o cadastro seja realizado.

O ano de lançamento deve conter somente números e estar dentro do intervalo definido pelo sistema, entre **1950 e 2026**. A nota também passa por validação e deve conter somente números entre **0 e 10**. Entretanto, a nota pode ser deixada em branco, pois seu preenchimento não é obrigatório.

Quando alguma informação obrigatória não é preenchida ou apresenta um formato inválido, o sistema informa o usuário por meio de uma mensagem e impede o salvamento até que o problema seja corrigido.

---

## 💾 Persistência dos dados

Os dados cadastrados no GameGears são armazenados no arquivo **`jogos.json`**, permitindo que as informações permaneçam disponíveis mesmo depois que o aplicativo seja fechado.

Ao iniciar o aplicativo, os dados existentes no arquivo JSON são carregados automaticamente e apresentados na biblioteca. Sempre que um jogo é adicionado, editado ou excluído, o arquivo é atualizado para manter os dados sincronizados com as alterações realizadas pelo usuário.

---

## 🔄 CRUD

O GameGears implementa as quatro operações fundamentais de um sistema **CRUD**. A operação **Create (Criar)** é utilizada para cadastrar novos jogos na biblioteca. A operação **Read (Ler)** permite carregar e visualizar os jogos que já foram cadastrados. A operação **Update (Atualizar)** permite editar as informações de um jogo existente. Por fim, a operação **Delete (Excluir)** permite remover um jogo da biblioteca, utilizando uma confirmação antes da exclusão.

Dessa forma, o projeto demonstra na prática a utilização de um sistema CRUD desenvolvido com **Python e Flet**, utilizando um arquivo **JSON** para a persistência dos dados.

---

## 🛠️ Tecnologias utilizadas

O GameGears foi desenvolvido utilizando **Python 3.13.6** e **Flet 1.0.1** para a construção da aplicação e de sua interface gráfica. Para a persistência dos dados foi utilizado o formato **JSON**, enquanto o controle de versão do projeto foi realizado utilizando **Git** e o armazenamento e compartilhamento do código foi feito por meio do **GitHub**.

### Bibliotecas utilizadas

O projeto utiliza módulos nativos do Python para realizar diferentes tarefas. O módulo **json** é utilizado para leitura e gravação dos dados no arquivo JSON. O módulo **pathlib** é utilizado para trabalhar com caminhos e arquivos do sistema. O módulo **shutil** é utilizado para realizar operações relacionadas às imagens, como a cópia das capas selecionadas pelo usuário. Já o módulo **uuid** é utilizado para gerar identificadores únicos para as imagens armazenadas na pasta de capas.

Os principais módulos utilizados são:

`json`, `pathlib`, `shutil` e `uuid`.

---

## 📁 Estrutura do projeto

O projeto está organizado em diferentes arquivos e pastas, cada um com uma função específica dentro da aplicação.

A pasta **`assets/`** contém os recursos utilizados pela interface, incluindo a imagem padrão exibida quando um jogo não possui uma capa personalizada. A pasta **`capas/`** armazena as imagens selecionadas pelo usuário para utilizar como capas dos jogos.

A pasta **`dados/`** contém o arquivo **`jogos.py`**, responsável pelas operações relacionadas ao armazenamento dos dados. Esse arquivo possui as funções utilizadas para carregar os jogos do arquivo JSON e salvar as alterações realizadas na biblioteca.

O arquivo **`main.py`** é o arquivo principal da aplicação e concentra a interface do GameGears, a interação com o usuário, o cadastro, a edição, a exclusão, as validações e a apresentação dos jogos.

O arquivo **`jogos.json`** é utilizado para armazenar permanentemente os dados da biblioteca. O arquivo **`.gitignore`** define arquivos e pastas que não devem ser enviados para o repositório Git, como o ambiente virtual e arquivos temporários do Python.

A estrutura básica do projeto é:

```text
GameList/
│
├── assets/
│   └── imagem_padrao.png
│
├── capas/
│   └── capas dos jogos
│
├── dados/
│   └── jogos.py
│
├── .gitignore
├── jogos.json
├── main.py
└── README.md
```
## ▶️ Como executar o projeto

Para executar o GameGears, primeiro é necessário clonar o repositório disponível no GitHub. No terminal, utilize o comando:

```bash
git clone https://github.com/AlainRoel/GameGears.git
```

Depois, entre na pasta do projeto:

```bash
cd GameGears
```

No Windows, recomenda-se criar um ambiente virtual para instalar e utilizar as dependências do projeto de forma isolada:

```bash
python -m venv .venv
```

Depois de criar o ambiente virtual, ele pode ser ativado com:

```powershell
.\.venv\Scripts\Activate.ps1
```

Com o ambiente virtual ativado, instale o Flet utilizando:

```bash
pip install flet
```

Após a instalação, o aplicativo pode ser executado com:

```bash
flet run main.py
```

---

## 🌐 Execução pelo navegador

O Flet também permite executar o GameGears diretamente no navegador. Para isso, com o ambiente virtual ativado e o Flet instalado, utilize:

```bash
flet run --web main.py
```

Dessa forma, a aplicação poderá ser executada utilizando o navegador em vez de uma janela convencional do aplicativo.

---

## 📖 Pesquisa e documentação

Durante o desenvolvimento do GameGears foram consultadas a **documentação oficial do Flet** e outras fontes relacionadas ao desenvolvimento da aplicação. A pesquisa foi utilizada para compreender e utilizar os recursos disponíveis na versão atual do Flet, incluindo componentes de interface, eventos, botões, caixas de diálogo, seleção de arquivos e execução da aplicação.

A documentação oficial do Flet está disponível em:

https://flet.dev/docs/

A consulta à documentação também foi importante para adaptar a aplicação às versões atuais da biblioteca e garantir o funcionamento dos recursos utilizados no projeto.

---

## 🎓 Contexto acadêmico

O GameGears foi desenvolvido como atividade acadêmica do curso de **Análise e Desenvolvimento de Sistemas (ADS)** do **Instituto Federal do Amapá (IFAP)**.

A atividade teve como objetivo desenvolver uma aplicação utilizando Flet que apresentasse as operações de **Criar, Ler, Atualizar e Excluir (CRUD)**, permitindo também a persistência dos dados em arquivo.

O projeto buscou aplicar, de forma prática, conhecimentos relacionados à programação em Python, desenvolvimento de interfaces gráficas, manipulação de arquivos, persistência de dados, validação de informações e organização de um projeto de software.

---

## 👨‍💻 Autor

**Alain Roel Rodrigues dos Santos Junior**

Projeto desenvolvido para fins acadêmicos.




