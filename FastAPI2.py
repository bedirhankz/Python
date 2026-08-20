from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
itemsread=[]
app = FastAPI()
class Item(BaseModel):
    name: str
    price: float
    stock: int
    catalog: Optional[str] = None
@app.post("/items/")
def create_item(item: Item):
    item_dict = item.model_dump()
    item.stock = max(0, item.stock)
    item_dict["stock"] = item.stock
    if item.stock == 0:
        item_dict.update({"message": "Item is out of stock"})
    else:
        item_dict.update({"message": "Item is in stock"})
        itemsread.append(item_dict)
    return item_dict
@app.get("/items/")
def read_items():
    return itemsread