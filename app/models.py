from sqlalchemy import Column, Integer, String
from app.data_access import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    body = Column(String)