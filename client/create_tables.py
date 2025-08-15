from view.database import Base, engine
from clientmodel import Client

print("Creating tables in the database...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")
