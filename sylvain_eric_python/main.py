from typing import Dict

from fastapi import FastAPI
from sqlalchemy import create_engine
from sylvain_eric_python.models.card import PokemonCard

description = """
My Hello World API
This is the best documentation
"""

app = FastAPI(title="Sylvain-Eric-Python", description=description, version="22-04-11")

eng = create_engine("sqlite:///db/db.sqlite")
con = eng.connect()

@app.get("/")
def home() -> Dict:
    return {"hello": "world"}

@app.post("/pokemon_card", status_code=201)
def create_card(body: PokemonCard) -> bool:
    return body
