from marshmallow import Schema, fields


class EsquemaItemSimples(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    preco = fields.Float(required=True)


class EsquemaLojaSimples(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str()


class EsquemaItem(EsquemaItemSimples):
    id_loja = fields.Int(required=True, load_only=True)
    loja = fields.Nested(EsquemaLojaSimples(), dump_only=True)


class EsquemaAtualizacaoItem(Schema):
    nome = fields.Str()
    preco = fields.Float()


class EsquemaLoja(EsquemaLojaSimples):
    itens = fields.List(fields.Nested(EsquemaItemSimples()), dump_only=True)
