from sqlalchemy.orm import Session

from wordcards.models.deck_card import deck_card


def find_all_decks_cards(db: Session):
    return db.query(deck_card).all()
