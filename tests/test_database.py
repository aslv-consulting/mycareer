from sqlmodel import Session
from mycareer.database import get_session

def test_get_session() -> None:
    with get_session() as session:
        assert isinstance(session, Session)
