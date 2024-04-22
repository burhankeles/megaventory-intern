from pydantic import BaseModel


class ProductSupplier(BaseModel):
    supplier_id: int | None = None
    product_id: int | None = None
