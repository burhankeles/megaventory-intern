from pydantic import BaseModel


class ProductLocation(BaseModel):
    product_sku: str | None = None
    product_quantity: int | None = None
    location_id: int | None = None
