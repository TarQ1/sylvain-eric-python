from typing import List

from fastapi import FastAPI, HTTPException

import sylvain_eric_python.repositories.pokemoncard as repo  # type: ignore
from sylvain_eric_python.models.card import PokemonCard  # type: ignore

description = """
Pokémon Card API:
Interact with a pokémon card database
"""

app = FastAPI(title="Pokémon Card API", description=description, version="1.0.0")


@app.post("/pokemon_card", status_code=201)
def create_card(body: PokemonCard) -> int:
    """
    Create a new card
    """

    id = repo.create_card(body)

    if id <= 0:
        raise HTTPException(status_code=500, detail="Could not create card")

    return id


@app.get("/pokemon_card/{id}", status_code=200)
def get_card(id: int) -> PokemonCard:
    """
    Get a card by id
    """

    card = repo.get_card(id)

    if card == None:
        raise HTTPException(status_code=404, detail="Card not found")

    return card


@app.get("/pokemon_cards", status_code=200)
def get_cards() -> List[PokemonCard]:
    """
    Get all cards in the database
    """

    card_list = repo.get_cards()

    if card_list == None:
        raise HTTPException(status_code=500, detail="Could get all cards")

    return card_list


@app.put("/pokemon_card/{id}", status_code=200)
def update_card(body: PokemonCard) -> PokemonCard:
    """
    Update a card's information
    """

    res = repo.update_card(body)

    if res == None:
        raise HTTPException(status_code=404, detail="Card not found")

    return res


@app.delete("/pokemon_card/{id}", status_code=200)
def delete_card(id: int) -> bool:
    """
    Delete a card from the database
    """

    res = repo.delete_card(id)

    if not res:
        raise HTTPException(status_code=500, detail="Could not delete card")

    return res
