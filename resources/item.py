from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.item import ModeloItem
from schemas import EsquemaItem, EsquemaAtualizacaoItem

blp = Blueprint("Itens", "itens", description="Operações nos itens")


@blp.route("/item/<string:id_item>")
class Item(MethodView):
    @blp.response(200, EsquemaItem)
    def get(self, id_item):
        item = ModeloItem.query.get_or_404(id_item)
        return item

    def delete(self, id_item):
        item = ModeloItem.query.get_or_404(id_item)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deletado."}

    @blp.arguments(EsquemaAtualizacaoItem)
    @blp.response(200, EsquemaItem)
    def put(self, dados_item, id_item):
        item = ModeloItem.query.get(id_item)

        if item:
            item.preco = dados_item["preco"]
            item.nome = dados_item["nome"]
        else:
            item = ModeloItem(id=id_item, **dados_item)

        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/item")
class ListaItem(MethodView):
    @blp.response(200, EsquemaItem(many=True))
    def get(self):
        return ModeloItem.query.all()

    @blp.arguments(EsquemaItem)
    @blp.response(201, EsquemaItem)
    def post(self, dados_item):
        item = ModeloItem(**dados_item)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Ocorreu um erro ao inserir o item.")

        return item
