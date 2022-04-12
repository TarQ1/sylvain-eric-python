from typing import Optional

from pydantic import BaseModel


class PokemonCard(BaseModel):
    id: Optional[int] = None
    name: str
    hp: int
    energy_type: str
    level: int
    description: str
    attack_1: str
    attack_2: Optional[str] = None
