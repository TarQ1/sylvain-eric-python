from sqlalchemy.orm import sessionmaker  # type: ignore

from .init_db import init_db  # type: ignore

SQLALCHEMY_DATABASE_URL = "sqlite:///db/db.sqlite"

engine = init_db(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
