from fastapi import FastAPI, Depends

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.models import Article

app = FastAPI()

# Create a database connection during application startup
DATABASE_URL = "sqlite:///./test.db"  # Replace with your database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@app.on_event("startup")
async def startup_db_client():
    app.state.db = SessionLocal()


@app.on_event("shutdown")
async def shutdown_db_client():
    app.state.db.close()


# Dependency to get the database session
def get_db() -> Session:
    return app.state.db


@app.post("/articles", response_model=Article)
def create_article(article: Article, db: Session = Depends(get_db)):
    db.add(article)
    db.commit()
    db.refresh(article)
    return article
