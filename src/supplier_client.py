from pydantic import BaseModel


class SupplierClient(BaseModel):
    supplier_client_id: int | None = None
    type: str | None = None
    name: str | None = None
    email: str | None = None
    shipping_address: str | None = None
    phone_number: int | None = None
