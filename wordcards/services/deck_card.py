from sqlalchemy.orm import Session

from wordcards.models.deck_card import DeckCard


def find_all_decks_cards(db: Session):
    return db.query(DeckCard).all()
