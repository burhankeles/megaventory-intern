from pydantic import BaseModel


class Product(BaseModel):
    product_id: int | None = None
    sku: int | None = None
    description: str | None = None
    sale_price: float | None = None
    purchase_price: float | None = None
