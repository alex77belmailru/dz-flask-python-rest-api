from flask import Flask, request
from marshmallow import ValidationError

from eshop.businsess_logic.order_usecases import order_create, order_get_many, order_get_by_id
from eshop.businsess_logic.product_usecases import product_get_many, product_get_by_id, product_create
from eshop.view.order_schemas import OrderCreateDtoSchema, OrderSchema, OrderGetManyParams
from eshop.view.product_schemas import ProductSchema, ProductGetManyParams, ProductCreateDtoSchema

app = Flask(__name__)


# order views

@app.post("/api/v1/order")
def order_create_endpoint():
    """Эндпоинт для создания заказа"""
    try:
        order_create_dto = OrderCreateDtoSchema().load(request.json)  # load - десериализация body post-запроса
    except ValidationError as err:  # ошибка валидации
        return err.messages, 400
    print(order_create_dto)
    try:
        order = order_create(
            product_ids=order_create_dto['product_ids']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return OrderSchema().dump(order)


@app.get("/api/v1/order")
def order_get_many_endpoint():
    """Эндпоинт для получения списка заказов"""
    try:
        order_get_many_params = OrderGetManyParams().load(request.args)  # load - десериализация аргументов из header
    except ValidationError as err:  # ошибка валидации - в аргументах нет page&limit
        return err.messages, 400

    order = order_get_many(
        page=order_get_many_params['page'],
        limit=order_get_many_params['limit'],
    )

    return OrderSchema(many=True).dump(order)


@app.get("/api/v1/order/<id>")
def order_get_by_id_endpoint(id):
    """Эндпоинт для получения заказа по ID"""
    order = order_get_by_id(id)

    if order is None:
        return {
            "error": 'Not found'
        }, 404

    return OrderSchema().dump(order)


# product views

@app.post("/api/v1/product")
def product_create_endpoint():
    """Эндпоинт для создания продукта"""
    try:
        product_create_dto = ProductCreateDtoSchema().load(request.json)  # load - десериализация body post-запроса
    except ValidationError as err:  # ошибка валидации
        return err.messages, 400
    try:
        product = product_create(
            name=product_create_dto['name'],
            price=product_create_dto['price'],
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return ProductSchema().dump(product)


@app.get("/api/v1/product")
def product_get_many_endpoint():
    """Эндпоинт для получения списка продуктов"""
    try:
        product_get_many_params = ProductGetManyParams().load(request.args)  # десериализация аргументов из header
    except ValidationError as err:  # ошибка валидации - в аргументах нет page&limit
        return err.messages, 400

    product = product_get_many(
        page=product_get_many_params['page'],
        limit=product_get_many_params['limit'],
    )

    return ProductSchema(many=True).dump(product)


@app.get("/api/v1/product/<id>")
def product_get_by_id_endpoint(id):
    """Эндпоинт для получения продукта по ID"""
    product = product_get_by_id(id)

    if product is None:
        return {
            "error": 'Not found'
        }, 404

    return ProductSchema().dump(product)


def run_server():
    app.run()
