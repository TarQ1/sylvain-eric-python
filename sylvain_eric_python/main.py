from typing import List

import grpc
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import sylvain_eric_python.repositories.pokemoncard as repo  # type: ignore
from sylvain_eric_python import auth_pb2, auth_pb2_grpc
from sylvain_eric_python.models.card import PokemonCard  # type: ignore
from sylvain_eric_python.models.login import LoginRequest, LoginResponse  # type: ignore
from sylvain_eric_python.models.register import RegisterRequest  # type: ignore

description = """
Pokémon Card API:
Interact with a pokémon card database
"""

app = FastAPI(title="Pokémon Card API",
              description=description, version="2.0.0")


# Dependency
def get_db():
    from .database.database import SessionLocal  # type: ignore

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/pokemon_card", status_code=201)
def create_card(body: PokemonCard, db: Session = Depends(get_db)) -> int:
    """
    Create a new card
    """

    id = repo.create_card(body, db)

    if id <= 0:
        raise HTTPException(status_code=404, detail="Card not found")

    return id


@app.get("/pokemon_card/{id}", status_code=200)
def get_card(id: int, db: Session = Depends(get_db)) -> PokemonCard:
    """
    Get a card by id
    """

    card = repo.get_card(id, db)

    if card == None:
        raise HTTPException(status_code=404, detail="Card not found")

    return card


@app.get("/pokemon_cards", status_code=200)
def get_cards(db: Session = Depends(get_db)) -> List[PokemonCard]:
    """
    Get all cards in the database
    """

    card_list = repo.get_cards(db)

    if card_list == None:
        raise HTTPException(status_code=500, detail="Could not get all cards")

    return card_list


@app.put("/pokemon_card/{id}", status_code=200)
def update_card(body: PokemonCard, db: Session = Depends(get_db)) -> PokemonCard:
    """
    Update a card's information
    """

    res = repo.update_card(body, db)

    if res == None:
        raise HTTPException(status_code=404, detail="Card not found")

    return res


@app.delete("/pokemon_card/{id}", status_code=200)
def delete_card(id: int, db: Session = Depends(get_db)) -> bool:
    """
    Delete a card from the database
    """

    res = repo.delete_card(id, db)

    if not res:
        raise HTTPException(status_code=500, detail="Could not delete card")

    return res


@app.post("/auth/register", status_code=201)
def register(body: RegisterRequest, db: Session = Depends(get_db)) -> bool:
    with grpc.insecure_channel('py_grpc:8001') as channel:
        stub = auth_pb2_grpc.AuthServiceStub(channel)

        message = auth_pb2.RegisterRequest()
        message.username = body.username
        message.password = body.password

        response = stub.Register(message)
        print(response.user)
        print(response.error)


@app.post("/auth/login", status_code=201)
def login(body: LoginRequest, db: Session = Depends(get_db)) -> LoginResponse:
    # TODO talk to grpc service
    return None
