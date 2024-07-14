from fastapi import FastAPI

from wordcards.api.routers import cards, decks

app = FastAPI()

app.include_router(cards.card_router)
app.include_router(decks.deck_router)
