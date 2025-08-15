from database import Base, engine
from projectlistmodel import Projectlist

print("Creating table in the database...")
Base.metadata.create_all(bind=engine)
print("Table created successfull.")