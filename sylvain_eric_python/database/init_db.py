from sqlalchemy import (  # type: ignore
    CheckConstraint,
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)


def init_db(SQLALCHEMY_DATABASE_URL):
    type_list = [
        "fire",
        "water",
        "fighting",
        "psychic",
        "darkness",
        "grass",
        "lightning",
        "metal",
        "normal",
    ]
    type_list_string = ""

    for t in type_list:
        type_list_string += f"'{t}', "

    type_list_string = type_list_string[:-2]

    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    meta = MetaData(engine)

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
        CheckConstraint(f"energy_type IN ({type_list_string})"),
    )

    try:
        cards.create()
    except Exception as e:
        print("Database already exists")

    return engine
