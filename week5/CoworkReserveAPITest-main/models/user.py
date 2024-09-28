from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database.session import Base


class User(Base):
    # nombre de tabla
    __tablename__ = 'user'

    # definicion de columnas
    id = Column(Integer, primary_key=True)
    name = Column(String(127), nullable=False)
    email = Column(String(127), unique=True, nullable=False)
    password = Column(String(127), nullable=False)
    created_at = Column(DateTime, server_default=func.now())