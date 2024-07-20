from sqlalchemy.orm import Session

from wordcards.models.card_deck import card_deck


def find_all_card_decks(db: Session):
    return db.query(card_deck).all()
