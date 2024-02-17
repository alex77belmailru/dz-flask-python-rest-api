from typing import Optional, List

from eshop.businsess_logic.product import Product
from eshop.data_access.product_repo import get_many, get_by_id, create_product_id, save


def product_create(name: str, price: float):
    """Создание продукта"""
    product = Product(
        id=create_product_id(),
        name=name,
        price=price,
    )
    save(product)
    return product


def product_get_by_id(id: str) -> Optional[Product]:
    """Получение продукта по его ID"""
    return get_by_id(id)


def product_get_many(page: int, limit: int) -> List[Product]:
    """Получение списка продуктов"""
    return get_many(page=page, limit=limit)
