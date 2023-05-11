from typing import List, Dict, Any
from plot import generate_plot
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from collections import defaultdict

app = FastAPI() # Creating API service instance

dbase = defaultdict(list) # Solution for key-value database


class Item(BaseModel): # One entry contains timestamp and it's data
    tstamp: float
    data: List[Dict[str, Any]]


@app.get("/data/{item_id}") 
def read_item(item_id: int): # Get plot with id's plots.
    path: str = generate_plot(dbase[item_id], item_id)
    return FileResponse(path)


@app.put("/id/{id}")
def put_to_db(id: int, item: Item): # Add entry to "database"
    dbase[id].append(item.dict())
