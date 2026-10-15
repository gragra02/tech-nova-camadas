# 🛒 TechNova Store – E-commerce Backend & Assistente Virtual

Projeto desenvolvido para a disciplina de **Linguagem de Programação III** do curso de **Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)** da **Faculdade Municipal de Palhoça (FMP)**, sob orientação do Prof. Rafael N. R.

O objetivo deste projeto é aplicar na prática os conceitos de **Programação Orientada a Objetos (POO)**, **Modelagem de Banco de Dados Relacional**, **ORM do Django**, **Painel Administrativo customizado** e integração com o **Frontend via Serialização JSON** através de um Chatbot interativo.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.12+**
* **Django 5.x** (Framework Web, ORM, Migrations, Admin & Serializers)
* **SQLite3** (Banco de Dados Relacional padrão de desenvolvimento)
* **HTML5 & CSS3** (Interface responsiva do Assistente Virtual)
* **JavaScript (Vanilla JS)** (Lógica de conversação do Chatbot e consumo de dados em JSON)

---

## 🗂️ Arquitetura e Modelagem de Dados (Parte 1)

O sistema modela a camada de persistência da loja online **TechNova Store** por meio de **6 classes inter-relacionadas** no arquivo `core/models.py`:

1. **`Categoria`**: Organiza os produtos da loja (`nome`, `descricao`, `criado_em`).
2. **`Produto`**: Representa os itens à venda, com relacionamento `ForeignKey` (1:N) com `Categoria` e controle de `estoque` e `preco`.
3. **`Cliente`**: Armazena os dados cadastrais dos clientes (`nome`, `email`, `telefone`, `cpf` único).
4. **`Endereco`**: Possui relacionamento `OneToOneField` (1:1) com `Cliente`, guardando os dados de entrega (`logradouro`, `numero`, `bairro`, `cidade`, `estado`, `cep`, `padrao`).
5. **`Pedido`**: Registra as compras realizadas, relacionando `Cliente` e `Endereco` (`ForeignKey`), além de controlar o `status` (`pendente`, `pago`, `enviado`, `entregue`, `cancelado`) e o valor `total`.
6. **`ItemPedido`**: Tabela associativa dos itens de um `Pedido` com `Produto`, contendo sobrescrita do método `save()` (POO) para calcular automaticamente o `preco_unitario` e o `preco_total` com base na quantidade.

### Painel Administrativo (`core/admin.py`)
Todos os 6 modelos foram registrados no **Django Admin** utilizando o decorator `@admin.register()`, contando com:
* Colunas customizadas (`list_display`)
* Filtros laterais rápidos (`list_filter`)
* Barras de pesquisa avançadas (`search_fields`), incluindo buscas por campos de tabelas relacionadas.

---

## 🤖 Assistente Virtual TechNova (Parte 2)

Na página inicial do sistema (`/`), o usuário conta com o **Assistente Virtual TechNova**, um chatbot interativo que:
* Saúda o visitante e pergunta seu nome;
* Lista em tempo real todas as categorias cadastradas no banco de dados (comando `"ver categorias"`);
* Pesquisa produtos pelo nome digitado e retorna o nome completo, preço formatado e a respectiva categoria.

### Como o Chatbot acessa o Banco de Dados? (Serialização)
O código JavaScript do navegador não acessa o banco de dados diretamente. O fluxo ocorre em 3 etapas:
1. **Consulta via ORM (`views.py`)**: A view `chatbot` busca os objetos `Categoria` e `Produto` no banco de dados usando `objects.all()`.
2. **Serialização para JSON**: Utilizamos `django.core.serializers.serialize('json', ...)` para converter as instâncias complexas das classes Python/Django em strings no formato universal **JSON**.
3. **Injeção Segura no Template (`chatbot.html`)**: Os dados serializados são passados ao JavaScript com o filtro `escapejs` e convertidos em objetos nativos com `JSON.parse()`, permitindo buscas rápidas no lado do cliente.

---

## ⚙️ Como Executar o Projeto Localmente

### 1. Clonar o repositório
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd Views-Templates-e-Arquitetura-em-Camadas
```

### 2. Instalar o Django
Caso utilize um ambiente virtual (`venv`), ative-o antes. Em seguida, instale o Django:
```bash
pip install django
```

### 3. Executar as Migrações do Banco de Dados
Na pasta onde se encontra o arquivo `manage.py`, execute:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Criar um Superusuário (para acessar o Admin)
```bash
python manage.py createsuperuser
```

### 5. Popular o Banco via Django Shell (Opcional)
Abra o shell interativo:
```bash
python manage.py shell
```
Cole o script de criação de categorias, produtos, cliente e pedido disponível no roteiro da Aula 07 e digite `exit()` ao finalizar.

### 6. Iniciar o Servidor
```bash
python manage.py runserver
```

* **Acessar o Chatbot (Frontend):** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Acessar o Painel Administrativo:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📁 Estrutura Principal do Projeto

```text
meu_site/
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       └── chatbot.html   # Interface e lógica JS do Assistente Virtual
│   ├── admin.py               # Configuração dos 6 models no Django Admin
│   ├── models.py              # Camada de persistência (6 classes POO)
│   ├── urls.py                # Rota principal do app core
│   └── views.py               # View do chatbot com serialização JSON
├── meu_site/
│   ├── settings.py
│   └── urls.py                # Rotas globais do projeto
├── db.sqlite3                 # Banco de dados SQLite
├── manage.py
└── README.md
```

---

## 👩‍💻 Autoria

Desenvolvido por **Grazi** – Estudante de Análise e Desenvolvimento de Sistemas (FMP).