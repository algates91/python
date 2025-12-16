
from pydantic import BaseModel

class Inventory(BaseModel):
    warehouse: str
    product: str
    quantity: int



