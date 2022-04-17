import pytest
from sqlalchemy.orm import sessionmaker  # type: ignore

import sylvain_eric_python.main as main  # type: ignore
from sylvain_eric_python.models.card import PokemonCard  # type: ignore


@pytest.fixture
def db():
    from sylvain_eric_python.database.init_db import init_db  # type: ignore

    engine = init_db("sqlite://")
    try:
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        return db
    except Exception as e:
        print(e)


@pytest.fixture
def mock_card():
    mock_card = PokemonCard()
    mock_card.name = "test"
    mock_card.energy_type = "fire"
    mock_card.level = 1
    mock_card.hp = 1
    mock_card.description = "test"
    mock_card.attack_1 = "test"
    mock_card.attack_2 = "test"
    return mock_card


## test get card but none exist
def test_get_card(db):
    try:
        main.get_card(1, db)
    except Exception as e:
        assert e.status_code == 404


## test create one card
def test_create_card(db, mock_card):
    response = main.create_card(mock_card, db)
    assert response == 1


def test_add_card_then_delete(db, mock_card):
    response = main.create_card(mock_card, db)
    assert response == 1
    response = main.delete_card(1, db)
    assert response == 1


def test_get_card_after_delete(db, mock_card):
    response = main.create_card(mock_card, db)
    assert response == 1
    response = main.delete_card(1, db)
    assert response == 1
    try:
        main.get_card(1, db)
    except Exception as e:
        assert e.status_code == 404


def test_get_cards(db, mock_card):
    response = main.create_card(mock_card, db)
    assert response == 1
    response = main.create_card(mock_card, db)
    assert response == 2
    response = main.get_cards(db)
    card_one = mock_card.copy()
    card_one.id = 1
    card_two = mock_card
    card_two.id = 2
    assert response == [card_one, card_two]


def test_get_cards_empty_db(db):
    response = main.get_cards(db)
    assert response == []


def test_update_card(db, mock_card):
    response = main.create_card(mock_card, db)
    assert response == 1
    mock_card.name = "test2"
    mock_card.id = 1
    response = main.update_card(mock_card, db)
    assert response.name == "test2"
