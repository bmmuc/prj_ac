from pydantic import BaseModel


class Book(BaseModel):
    id: int
    name: str
    isbn: str
    quantity: int


class Author(BaseModel):
    id: int
    name: str
