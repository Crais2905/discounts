from fastapi import Query
from typing import Optional
from db.models import Product


def product_filters(
    name: Optional[str] = Query(None, description='Filter by name'),
    min_discount_percent: Optional[int] = Query(None, description='Filter by min discount persent'),
    max_discount_percent: Optional[int] = Query(None, description='Filter by max discount persent'),
    min_new_price: Optional[float] = Query(None, description='Filter by min price'),
    max_new_price: Optional[float] = Query(None, description='Filter by max price'),

):
    filters = []
    if name:
        filters.append(Product.name.ilike(f'%{name}%'))
    elif min_discount_percent:
        filters.append(Product.discount_percent > min_discount_percent)
    elif max_discount_percent:
        filters.append(Product.discount_percent < max_discount_percent)
    elif min_new_price:
        filters.append(Product.new_price > min_new_price)
    elif max_new_price:
        filters.append(Product.new_price < max_new_price)

    return filters
    