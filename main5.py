from fastapi import FastAPI, HTTPException
from pathlib import Path
from pydantic import BaseModel
from typing import Union, List, Dict, Any, Optional


app = FastAPI()


@app.get("/books/{title}")
async def read_book(title: str, autor: str = None, genre: str = None):

    return {"title": title, "autor": autor, "genre": genre}
