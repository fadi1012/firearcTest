import aiosqlite
from fastapi import Depends, HTTPException

from app.main import get_db
from app.models import Article


class DataAccessLayer:
    @classmethod
    def get_all_articles(cls, db: aiosqlite.Connection = Depends(get_db)) -> list[Article]:
        cursor = await db.cursor()

        # Execute the SQL query to get all articles
        await cursor.execute("SELECT * FROM articles")
        articles_data = await cursor.fetchall()

        # Convert the database results to Article objects using a list comprehension
        articles = [
            Article(id=article_data[0], title=article_data[1], description=article_data[2], body=article_data[3])
            for article_data in articles_data
        ]

        # Close the cursor
        await cursor.close()

        return articles

    @classmethod
    def get_article_by_id(cls, article_id: int, db: aiosqlite.Connection = Depends(get_db)) -> Article:
        cursor = await db.cursor()

        # Execute the SQL query to get an article by ID
        await cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
        article_data = await cursor.fetchone()

        if not article_data:
            raise HTTPException(status_code=404, detail="Article not found")

        article = Article(id=article_data[0], title=article_data[1], description=article_data[2], body=article_data[3])

        # Close the cursor
        await cursor.close()

        return article

    @classmethod
    def update_article_by_id(cls, article_id: int, updated_article: Article,
                             db: aiosqlite.Connection = Depends(get_db)) -> Article:
        cursor = await db.cursor()

        # Execute the SQL query to update an article by ID
        await cursor.execute(
            "UPDATE articles SET title = ?, description = ?, body = ? WHERE id = ?",
            (updated_article.title, updated_article.description, updated_article.body, article_id)
        )

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Article not found")

        # Commit the transaction
        await db.commit()

        # Close the cursor
        await cursor.close()

        return updated_article

    @classmethod
    def delete_article_by_id(cls, article_id: int, db: aiosqlite.Connection = Depends(get_db)) -> bool:
        cursor = await db.cursor()

        # Execute the SQL query to delete an article by ID
        await cursor.execute("DELETE FROM articles WHERE id = ?", (article_id,))

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Article not found")

        # Commit the transaction
        await db.commit()

        # Close the cursor
        await cursor.close()

        return True

    @classmethod
    def create_article(cls, article: Article, db: aiosqlite.Connection = Depends(get_db)):
        cursor = await db.cursor()

        # Execute the SQL query to insert the article
        await cursor.execute(
            "INSERT INTO articles (title, description, body) VALUES (?, ?, ?)",
            (article.title, article.description, article.body)
        )

        # Commit the transaction
        await db.commit()

        # Close the cursor
        await cursor.close()

        return article
