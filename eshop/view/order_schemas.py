from marshmallow import Schema, fields


class OrderCreateDtoSchema(Schema):  # DTO - Data Transfer Object
    """Класс для сериализации/десериализации параметров заказа"""
    product_ids = fields.List(fields.Str(), required=True)


class OrderSchema(Schema):
    """Класс для сериализации/десериализации заказа"""

    class Meta:  # Список полей, которые будут обработаны - чтобы не отдавать наружу лишнего
        fields = ["id", "product_ids", "total"]

    id = fields.String()
    product_ids = fields.List(fields.Str())
    total = fields.Float()


class OrderGetManyParams(Schema):
    """Класс для сериализации/десериализации параметров заказа page и limit из header"""
    page = fields.Int(required=True)
    limit = fields.Int(required=True)
