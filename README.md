# controle-estoque-flask
Aplicação web para controle de estoque desenvolvida com Flask, com autenticação de usuários, cadastro de produtos e movimentação de entrada e saída.

# 📦 Controle de Estoque com Flask

Sistema simples de controle de estoque desenvolvido em Python utilizando Flask. Permite autenticação de usuários, cadastro de produtos, movimentação de entrada/saída e exclusão de itens.

## 🚀 Funcionalidades

- Registro e login de usuários
- Cadastro de novos produtos
- Visualização do estoque atual
- Movimentações de entrada e saída
- Exclusão de produtos
- Interface amigável e responsiva

## 💻 Tecnologias utilizadas

- Python 3
- Flask
- Flask-Login
- Flask-Bcrypt
- SQLAlchemy
- SQLite
- Bootstrap 5
- Render (para deploy)

## 🛠️ Como rodar localmente

```bash
git clone https://github.com/seu-usuario/controle-estoque-flask.git
cd controle-estoque-flask
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
flask run
