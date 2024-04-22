from pydantic import BaseModel


class InventoryLocation(BaseModel):
    location_id: int | None = None
    abbreviation: str | None = None
    name: str | None = None
    address: str | None = None
