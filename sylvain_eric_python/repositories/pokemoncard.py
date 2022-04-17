from typing import List, Optional

from sqlalchemy import Column, Integer, String  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore

from sylvain_eric_python.models.card import PokemonCard  # type: ignore


class PokemonCardDbo(declarative_base()):  # type: ignore
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hp = Column(Integer)
    energy_type = Column(String)
    level = Column(Integer)
    description = Column(String)
    attack_1 = Column(String)
    attack_2 = Column(String)


def model_to_dbo(model: PokemonCard) -> PokemonCardDbo:
    """
    Translate a model to a dbo
    """
    dbo = PokemonCardDbo()
    dbo.id = model.id
    dbo.name = model.name
    dbo.hp = model.hp
    dbo.energy_type = model.energy_type
    dbo.level = model.level
    dbo.description = model.description
    dbo.attack_1 = model.attack_1
    dbo.attack_2 = model.attack_2
    return dbo


def dbo_to_model(dbo: PokemonCardDbo) -> PokemonCard:
    """
    Translate a dbo to a model
    """
    model = PokemonCard()
    model.id = dbo.id
    model.name = dbo.name
    model.hp = dbo.hp
    model.energy_type = dbo.energy_type
    model.level = dbo.level
    model.description = dbo.description
    model.attack_1 = dbo.attack_1
    model.attack_2 = dbo.attack_2
    return model


def create_card(model: PokemonCard, ses) -> int:
    """
    Create a card and return the id of the card created
    """
    try:
        dbo = model_to_dbo(model)
        ses.add(dbo)
        ses.commit()
        ses.refresh(dbo)
    except Exception as e:
        return -1

    return dbo.id


def get_card(id: int, ses) -> PokemonCard:
    """
    Get a card by id
    """
    dbo = ses.query(PokemonCardDbo).filter_by(id=id).first()

    if dbo == None:
        return None

    return dbo_to_model(dbo)


def get_cards(ses) -> Optional[List[PokemonCard]]:
    """
    Get all cards
    """

    dbo_list: List[PokemonCardDbo] = ses.query(PokemonCardDbo).order_by(PokemonCardDbo.id).all()

    if dbo_list == None:
        return None

    poke_list: List[PokemonCard] = list(map(lambda x: dbo_to_model(x), dbo_list))

    return poke_list


def update_card(model: PokemonCard, ses) -> PokemonCard:
    """
    Update a card and return the updated model
    """
    try:
        dbo = ses.query(PokemonCardDbo).filter(PokemonCardDbo.id == model.id).first()

        if dbo.name != model.name:
            dbo.name = model.name

        if dbo.hp != model.hp:
            dbo.hp = model.hp

        if dbo.energy_type != model.energy_type:
            dbo.energy_type = model.energy_type

        if dbo.level != model.level:
            dbo.level = model.level

        if dbo.description != model.description:
            dbo.description = model.description

        if dbo.attack_1 != model.attack_1:
            dbo.attack_1 = model.attack_1

        if dbo.attack_2 != model.attack_2:
            dbo.attack_2 = model.attack_2

        ses.commit()
        return model
    except Exception as e:
        return None


def delete_card(id: int, ses) -> bool:
    """
    Delete a card and return a bool if sucessfull false otherwise
    """
    try:
        dbo = ses.query(PokemonCardDbo).filter(PokemonCardDbo.id == id).first()
        ses.delete(dbo)
        ses.commit()
    except:
        return False
    return True
