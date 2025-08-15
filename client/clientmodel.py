from sqlalchemy import Column, Integer, String
from view.database import Base

class Client(Base):
    __tablename__ = "client"  #  two underscores before and after

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    website = Column(String(255), nullable=False)
