from sqlalchemy.orm import Session
from app.models import Article


class DataAccessLayer:
    @classmethod
    def get_all_articles(cls, db: Session) -> list[Article]:
        return db.query(Article).all()

    @classmethod
    def get_article_by_id(cls, db: Session, article_id: int) -> Article:
        return db.query(Article).filter(Article.id == article_id).first()

    @classmethod
    def update_article_by_id(cls, db: Session, article_id: int, updated_article: Article) -> Article:
        article = db.query(Article).filter(Article.id == article_id).first()
        if article:
            for attr, value in updated_article.dict().items():
                setattr(article, attr, value)
            db.commit()
            db.refresh(article)
        return article

    @classmethod
    def delete_article_by_id(cls, db: Session, article_id: int) -> bool:
        article = db.query(Article).filter(Article.id == article_id).first()
        if article:
            db.delete(article)
            db.commit()
            return True
        return False
