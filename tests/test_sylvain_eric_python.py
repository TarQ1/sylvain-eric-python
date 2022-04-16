import os
import sys

from fastapi.testclient import TestClient

## Import the module, this is really terrible
test_dir = os.path.dirname(__file__)
main_module = os.path.join(test_dir, "..", "sylvain_eric_python")
sys.path.append(main_module)
import main  # type: ignore

client = TestClient(main.app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 404


## test create card
def test_create_card():
    response = client.post(
        "/pokemon_card",
        json={
            "name": "Pikachu",
            "hp": 100,
            "energy_type": "lightning",
            "level": 1,
            "description": "A pokemon",
            "attack_1": "Thunder",
            "attack_2": "Thunderbolt",
        },
    )
    assert response.status_code == 201


## test get card
def test_get_card():
    response = client.get("/pokemon_card/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Pikachu",
        "hp": 10,
        "energy_type": "lightning",
        "level": 3,
        "description": "pika pika",
        "attack_1": "tema la taille de l'arc électrique",
        "attack_2": None,
    }


## test put card
def test_put_card():
    response = client.put(
        "/pokemon_card/1",
        json={
            "name": "Pikachu",
            "hp": 100,
            "energy_type": "lightning",
            "level": 1,
            "description": "A pokemon",
            "attack_1": "Thunder",
            "attack_2": "Thunderbolt",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Pikachu",
        "hp": 100,
        "energy_type": "lightning",
        "level": 1,
        "description": "A pokemon",
        "attack_1": "Thunder",
        "attack_2": "Thunderbolt",
    }
