import os
from sqlalchemy.orm import sessionmaker  # type: ignore

from .init_db import init_db  # type: ignore

db_server = os.getenv('DB_SERVER')

if not db_server:
  db_server = 'localhost'

SQLALCHEMY_DATABASE_URL = f"postgresql://user:password@{db_server}:5432/database"

engine = init_db(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
