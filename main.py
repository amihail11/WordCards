"""
Main module for WordCards application.

"""

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("wordcards.api.__init__:app", host="0.0.0.0", port=8000, reload=True)
