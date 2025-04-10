from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from .models import db

bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'chave-secreta-da-adega'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Importação dos blueprints
    from .routes import main
    from .auth.routes import auth
    from .client.routes import client_bp
    from .product.routes import product_bp  # ✅ Adicionado aqui

    # Registro dos blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(client_bp)
    app.register_blueprint(product_bp, url_prefix='/produto')  # ✅ Corrigido e mantido

    return app
