from typing import Optional

from pydantic import BaseModel


class PokemonCard(BaseModel):
    id: Optional[int] = None
    name: str = ""
    hp: int = 0
    energy_type: str = ""
    level: int = 0
    description: str = ""
    attack_1: str = ""
    attack_2: Optional[str] = None
