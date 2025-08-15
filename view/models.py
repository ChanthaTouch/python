from sqlalchemy import Column, Integer, String
from view.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    price = Column(String(20), nullable=False)
