from sqlalchemy import Column, Integer, String  # type: ignore
from sqlalchemy.orm import declarative_base  # type: ignore

Base = declarative_base()  # type: ignore


class PokemonCardDbo(Base):  # type: ignore
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hp = Column(Integer)
    energy_type = Column(String)
    level = Column(Integer)
    description = Column(String)
    attack_1 = Column(String)
    attack_2 = Column(String)
