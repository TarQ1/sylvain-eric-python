import os

from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore


def init_db(SQLALCHEMY_DATABASE_URL):
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    meta = MetaData(engine)

    users = Table(
        "users",
        meta,
        Column("id", Integer, primary_key=True),
        Column("username", String),
        Column("password", String),
    )

    try:
        users.create()
    except Exception as e:
        print("Database already exists")

    return engine


db_server = os.getenv('DB_SERVER')

if not db_server:
    db_server = 'localhost'

SQLALCHEMY_DATABASE_URL = f"postgresql://user:password@{db_server}:5432/database"

engine = init_db(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
