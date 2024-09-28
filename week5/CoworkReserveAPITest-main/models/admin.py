from sqlalchemy import Column, Integer, String
from database.session import Base


class Admin(Base):
    # nombre de tabla
    __tablename__ = 'admin'

    # definicion de columnas
    id = Column(Integer, primary_key=True)
    name = Column(String(127), nullable=False)
    email = Column(String(127), unique=True, nullable=False)
    password = Column(String(127), nullable=False)