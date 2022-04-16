from typing import List

from fastapi import FastAPI, HTTPException

import sylvain_eric_python.repositories.pokemoncard as repo  # type: ignore
from sylvain_eric_python.models.card import PokemonCard  # type: ignore

description = """
My Hello World API
This is the best documentation
"""


app = FastAPI(title="Sylvain-Eric-Python", description=description, version="22-04-11")


@app.post("/pokemon_card", status_code=201)
def create_card(body: PokemonCard) -> int:
    id = repo.create_card(body)

    if id <= 0:
        raise HTTPException(status_code=500, detail="Could not create card")

    return id


@app.get("/pokemon_card/{id}", status_code=200)
def get_card(id: int) -> PokemonCard:
    card = repo.get_card(id)

    if card == None:
        raise HTTPException(status_code=404, detail="Card not found")

    return card


@app.get("/pokemon_cards", status_code=200)
def get_cards() -> List[PokemonCard]:
    card_list = repo.get_cards()

    if card_list == None:
        raise HTTPException(status_code=500, detail="Could get all cards")

    return card_list


@app.put("/pokemon_card/{id}", status_code=200)
def update_card(body: PokemonCard) -> PokemonCard:
    res = repo.update_card(body)

    if res == None:
        raise HTTPException(status_code=404, detail="Card not found")

    return res


@app.delete("/pokemon_card/{id}", status_code=200)
def delete_card(id: int) -> bool:
    res = repo.delete_card(id)

    if not res:
        raise HTTPException(status_code=500, detail="Could not delete card")

    return res
