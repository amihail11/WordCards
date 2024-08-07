from fastapi import FastAPI

from wordcards.api.routers import card, deck, deck_card

app = FastAPI()

app.include_router(card.card_router)
app.include_router(deck.deck_router)
app.include_router(deck_card.deck_card_router)
