import os
from contextlib import contextmanager
from typing import Generator
from sqlmodel import Session, create_engine

database_url: str = os.getenv("DATABASE_URL", "sqlite:///mycareer_test.db")

connect_args: dict = {"check_same_thread": False}
engine = create_engine(database_url, connect_args=connect_args)

@contextmanager
def get_session() -> Generator[Session, None, None]:
    """Get a new database session.

    Yields:
        Session: A new database session.
    """
    with Session(engine) as session:
        yield session
