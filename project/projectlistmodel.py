from sqlalchemy import Column, Integer, String
from database import Base

class Projectlist(Base):
    __tablename__ = "projectlist"  # Double underscore before and after

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String(255),nullable=False)
    project_name = Column(String(225), nullable=False)
    start_date = Column(String(225), nullable=False)
    end_date = Column(String(225), nullable=False)
    location = Column(String(225), nullable=False)
    budget = Column(String(225),nullable=False)
    min_labour = Column(String(225), nullable=False)
    variant_extra_OT = Column(String(225), nullable=False)
    team_OT_limit = Column(String(225), nullable=False)

