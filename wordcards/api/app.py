from fastapi import FastAPI

from wordcards.api.routers import card, deck, deck_card, user, user_card, user_deck

app = FastAPI()

app.include_router(card.card_router)
app.include_router(deck.deck_router)
app.include_router(deck_card.deck_card_router)
app.include_router(user.user_router)
app.include_router(user_deck.user_deck_router)
app.include_router(user_card.user_card_router)
