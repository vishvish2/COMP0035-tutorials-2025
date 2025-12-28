import pytest
from sqlmodel import create_engine, SQLModel, Session
from sqlmodel.pool import StaticPool

from activities.starter.playing_cards import Suit, Rank, Deck, create_cards_db


@pytest.fixture
def deck_cards():
    suit_values = [Suit(suit=s) for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']]
    rank_values = [Rank(rank=str(r)) for r in
                   [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']]
    deck_cards = Deck(suits=suit_values, ranks=rank_values)
    yield deck_cards


@pytest.fixture
def session():
    """Create a new database session for a test."""
    db_path = ":memory:"
    engine = create_cards_db(db_path=db_path)
    with Session(engine) as session:
        yield session
