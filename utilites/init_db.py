from sqlalchemy import create_engine
from app.data_access import SessionLocal
from app.models import Article
from app.main import DATABASE_URL


def init_db():
    engine = create_engine(DATABASE_URL)
    SessionLocal.configure(bind=engine)

    # Create the database tables
    from app.data_access import Base
    Base.metadata.create_all(bind=engine)

    # Add a dummy article to the database
    db = SessionLocal()
    dummy_article = Article(title="Dummy Title", description="Dummy Desc", body="Dummy Body")
    db.add(dummy_article)
    db.commit()
    db.close()


if __name__ == "__main__":
    init_db()