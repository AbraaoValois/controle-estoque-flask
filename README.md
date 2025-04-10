# 📦 Controle de Estoque com Flask

Sistema web simples para controle de estoque, desenvolvido com Flask. Ideal para pequenos comércios ou projetos de estudo.

## 🚀 Funcionalidades

- ✅ Cadastro de usuários (registro e login)
- 📦 Cadastro de produtos com nome, quantidade e preço
- 🔁 Movimentação de estoque (entrada e saída)
- ❌ Exclusão de produtos
- 🔒 Acesso restrito a usuários autenticados
- 🎨 Interface limpa e responsiva com Bootstrap

## 🧰 Tecnologias

- Python 3
- Flask
- Flask-Login
- Flask-Bcrypt
- SQLAlchemy (ORM)
- SQLite (banco de dados local)
- Bootstrap 5 (estilização)
- Render (para deploy)

## ⚙️ Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/controle-estoque-flask.git
cd controle-estoque-flask

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # no Windows
# ou
source venv/bin/activate  # no Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute o app
flask run
