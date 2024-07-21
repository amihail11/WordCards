from fastapi import FastAPI

from wordcards.api.routers import card, deck

app = FastAPI()

app.include_router(card.card_router)
app.include_router(deck.deck_router)
