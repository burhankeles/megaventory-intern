from pydantic import BaseModel


class ProductClient(BaseModel):
    client_id: int | None = None
    product_id: int | None = None
