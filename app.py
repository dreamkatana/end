from flask import Flask, render_template
from flask_smorest import Api

from db import db

import models

from resources.item import blp as BlueprintItem
from resources.loja import blp as BlueprintLoja


def criar_app(url_db=None):
    """
    Cria e configura a aplicação Flask.

    Parâmetros:
    url_db (str): O URL do banco de dados. Se nenhum for fornecido, um banco de dados SQLite será usado por padrão.

    Retorna:
    app: Uma instância da aplicação Flask.
    """

    app = Flask(__name__)
    app.config["API_TITLE"] = "API REST de Lojas"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = url_db or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(BlueprintItem)
    api.register_blueprint(BlueprintLoja)

    @app.route("/")
    def home():
        return render_template('index.html')

    return app
app = criar_app()

