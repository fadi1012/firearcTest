import aiosqlite

from fastapi import FastAPI

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"


@app.on_event("startup")
async def startup_db_client():
    app.state.db = await aiosqlite.connect(DATABASE_URL)  # Use aiosqlite for database connection


@app.on_event("shutdown")
async def shutdown_db_client():
    app.state.db.close()


# Dependency to get the database connection
def get_db() -> aiosqlite.Connection:
    return app.state.db
