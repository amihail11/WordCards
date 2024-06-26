from fastapi import FastAPI

from wordcards.api.routers import cards

app = FastAPI()

app.include_router(cards.card_router)
