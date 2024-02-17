from typing import List, Optional

from eshop.businsess_logic.product import Product

_products: List[Product] = [
    Product(
        id='1',
        name='Телевизор',
        price=15,
    ),
    Product(
        id='2',
        name='Кофемашина',
        price=10,
    ),
    Product(
        id='3',
        name='Ноутбук',
        price=12,
    )
]


def save(product: Product):
    """Сохраняет продукт в репозитории"""
    _products.append(product)


def delete_by_id(id: str):
    """Удаляет продукт по ID из репозитория"""
    global _products
    _products = [p for p in _products if p.id != id]


def get_by_id(id: str) -> Optional[Product]:
    """Возвращает продукт по ID из репозитория"""
    return next((p for p in _products if p.id == id), None)


def get_many(page: int = 0, limit: int = 10):
    """Возвращает список продуктов"""
    start = page * limit
    end = start + limit
    return _products[start:end]


def create_product_id():
    """Создание ID для нового продукта"""
    if _products:
        return int(_products[-1].id) + 1
    else:
        return 1
