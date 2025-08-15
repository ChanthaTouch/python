from view.database import Base, engine
from view.models import Book

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
