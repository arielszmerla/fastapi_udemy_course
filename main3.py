from fastapi import FastAPI, HTTPException
from pathlib import Path


app = FastAPI()


@app.get("/products/{product_id}")
async def read_product(product_id: int):
    return {"product_id": product_id}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users/me")
async def read_current_user():
    return {"user_id": "the data for the current user"}


from enum import Enum


class DeviceType(str, Enum):
    smartphone = "smartphone"
    tablet = "tablet"
    laptop = "laptop"


@app.get("/devices/{device_type}")
async def get_device(device_type: DeviceType):
    return {"device_type": device_type}


@app.get("/docs/{file_path:path}")
async def read_document(file_path: str):
    file_location = Path("docs") / file_path
    if not file_location.exists() or not file_location.is_file():
        raise HTTPException(status_code=404, detail="File not found")

    with open(file_location, "r") as file:
        content = file.read()

    return {"content": content}


Products_db = [
    {"product_name": "Soap"},
    {"product_name": "Shampoo"},
    {"product_name": "Toothpaste"},
    {"product_name": "Toilet Paper"},
]


@app.get("/products/")
async def read_products(offset: int = 0, range: int = 10):
    return Products_db[offset : offset + range]


@app.get("/books/{book_id}")
async def read_book(book_id: str, q=None):
    if q:
        return {"book_id": book_id, "q": q}
    return {"book_id": book_id}
