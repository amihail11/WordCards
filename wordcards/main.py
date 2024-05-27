"""
Main module for WordCards application.

"""

from wordcards.api.app import app
from wordcards.api.routers import cards
from wordcards.database import engine
from wordcards.models import card

card.Base.metadata.create_all(bind=engine)

app.include_router(cards.router)


@app.get("/")
async def get_root():
    """get the root page of the app"""
    return {"success": True}
