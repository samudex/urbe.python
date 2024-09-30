from sqlalchemy import Column, Integer, DECIMAL, String, DateTime
from sqlalchemy.sql import func
from database.session import Base


class Coworking(Base):
    # nombre de tabla
    __tablename__ = 'coworking'

    # definicion de columnas
    id = Column(Integer, primary_key=True)
    name = Column(String(127), nullable=False)
    location = Column(String(127), nullable=False)
    price_by_hour = Column(DECIMAL(10, 2), nullable=True)
    capacity = Column(Integer, nullable=False)
    is_available = Column(Integer, nullable=False)
