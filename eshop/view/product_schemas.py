from marshmallow import Schema, fields


class ProductCreateDtoSchema(Schema):  # DTO - Data Transfer Object
    """Класс для сериализации/десериализации параметров продукта"""
    name = fields.String()
    price = fields.Float()


class ProductSchema(Schema):
    """Класс для сериализации/десериализации продукта"""

    class Meta:  # Список полей, которые будут обработаны - чтобы не отдавать наружу лишнего
        fields = ["id", "name", "price"]

    id = fields.String()
    name = fields.String()
    price = fields.Float()


class ProductGetManyParams(Schema):
    """Класс для сериализации/десериализации параметров продукта page и limit из header"""
    page = fields.Int(required=True)
    limit = fields.Int(required=True)
