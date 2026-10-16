# 🚀 TechNova Store - Arquitetura em Camadas (MVT) e Django 

Repositório estruturado para a **Aula 08 – Views, Templates e Arquitetura em Camadas** do curso de Análise e Desenvolvimento de Sistemas (FMP). O projeto evolui a arquitetura de backend do e-commerce TechNova Store, aplicando separação de responsabilidades (Model, View, Template) e preparando a base para futuras integrações com APIs REST e automação por RPA.

---

## 🛠️ Tecnologias Utilizadas
* **Python 3.12**
* **Django Framework** (ORM, Templates, Views, Serializers)
* **SQLite** (Banco de dados relacional local)
* **HTML5 & CSS3** (Interface web e componentização com templates base)
* **Git & GitHub** (Controle de versão e versionamento de código)

---

## 📂 Nova Estrutura do Projeto (Arquitetura em Camadas)

O projeto foi reestruturado para desacoplar as regras de negócio e organizar o código de forma modular e profissional:

```text
meu_site/
├── core/
│   ├── migrations/             # Histórico de migrações do banco de dados
│   ├── models/                 # Camada de Dados (POO e ORM)
│   │   ├── __init__.py
│   │   ├── categoria.py        # Modelo de Categorias de Produtos
│   │   └── produto.py          # Modelo de Produtos
│   ├── views/                  # Camada de Controle e Lógica
│   │   ├── __init__.py
│   │   ├── cliente_views.py    # Controladores de Clientes
│   │   └── produto_views.py    # Controladores de Produtos e Serialização JSON
│   ├── templates/              # Camada de Apresentação (Interface)
│   │   └── core/
│   │       ├── base.html       # Template base com layout responsivo e navbar
│   │       └── produtos_lista.html # Listagem dinâmica de produtos
│   ├── admin.py                # Configuração avançada do Django Admin
│   ├── apps.py
│   └── urls.py                 # Rotas e endpoints do app core
├── meu_site/                   # Configurações centrais do projeto Django
└── manage.py                   # Utilitário de linha de comando do Django

⚙️ Como Executar o Projeto
Siga os passos abaixo para rodar o projeto na sua máquina:

Clone o repositório:

Bash
git clone [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)
cd NOME-DO-REPO
Aplique as migrações no banco de dados:

Bash
python manage.py makemigrations
python manage.py migrate
Inicie o servidor de desenvolvimento:

Bash
python manage.py runserver
Acesse no navegador:

Listagem de Produtos (HTML): http://127.0.0.1:8000/produtos/

API JSON de Produtos: http://127.0.0.1:8000/api/produtos/

Painel Administrativo: http://127.0.0.1:8000/admin/

Autoria
Desenvolvido por Graziele da Silva

Faculdade Municipal de Palhoça (FMP) — Curso de Tecnologia em Análise e Desenvolvimento de Sistemas (ADS).

