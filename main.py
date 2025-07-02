from fastapi import FastAPI
from typing import Annotated

from fastapi import FastAPI, Query


app = FastAPI()

@app.get("/user")
def get_user():
    return {"id": 1, "name": "Mehedi Hasan"}

@app.get("/company")
def get_company():
    x = "vivasoft"
    return {"id": 101, "company name": "Vivasoft"}

@app.get("/status")
def get_status():
    return {"status": "Running"}

@app.put("/instruction")
def put_instrustion():
    return {"Instruction": "on going"}

@app.put("/doing/")
def put_doing():
    return{"office time" : "Doing"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results






# fixed something

@app.get('/')
async def read_results():
    results = await some_library()
    return results