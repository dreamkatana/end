from db import db


class ModeloItem(db.Model):
    __tablename__ = "itens"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=False, nullable=False)
    preco = db.Column(db.Float(precision=2), unique=False, nullable=False)

    id_loja = db.Column(
        db.Integer, db.ForeignKey("lojas.id"), unique=False, nullable=False
    )
    loja = db.relationship("ModeloLoja", back_populates="itens")
