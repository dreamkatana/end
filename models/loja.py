from db import db


class ModeloLoja(db.Model):
    __tablename__ = "lojas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)

    itens = db.relationship(
        "ModeloItem", back_populates="loja", lazy="dynamic", cascade="all, delete"
    )
