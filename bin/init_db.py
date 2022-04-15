from sqlalchemy import (  # type: ignore
    CheckConstraint,
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)


def init_db():
    type_list = ["fire", "water", "fighting", "psychic", "darkness", "grass", "lightning", "metal"]
    type_list_string = ""
    for t in type_list:
        type_list_string += f"'{t}', "
    type_list_string = type_list_string[:-2]

    eng = create_engine("sqlite:///db/db.sqlite")

    meta = MetaData(eng)
    cards = Table(
        "cards",
        meta,
        Column("id", Integer, primary_key=True),
        Column("name", String),
        Column("energy_type", String),
        Column("level", Integer),
        Column("hp", Integer),
        Column("description", String),
        Column("attack_1", String),
        Column("attack_2", String),
        CheckConstraint(f"type IN ({type_list_string})"),
    )

    cards.create()
