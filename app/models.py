from pydantic import BaseModel


class Article(BaseModel):
    id: int
    title: str
    description: str
    body: str
