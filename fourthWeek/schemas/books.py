from pydantic import BaseModel


# Esquema que no contiene el id
class BookBase(BaseModel):
    title: str
    category: str
    year: int


# Esquema que contiene todas las propiedades del libro
class Book(BookBase):
    id: int