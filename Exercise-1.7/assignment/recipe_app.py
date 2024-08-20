# Import necessary packages and modules
from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the database credentials from environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

# Create the database engine
engine = create_engine(f"mysql://{db_user}:{db_password}@{db_host}/{db_name}")

# Create the declarative base class
Base = declarative_base()

# Define the Recipe class inheriting from Base
class Recipe(Base):
    __tablename__ = "final_recipes"  # Fix the table name format

    # Define columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # Define __repr__ method
    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name} - Difficulty: {self.difficulty}>"
    
    # Define __str__ method
    def __str__(self):
        return (
            f"Recipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}\n"
            f"{'-'*40}"
        )
    
    # Define method to calculate difficulty based on ingredients and cooking time
    def calculate_difficulty(self):
        num_ingredients = len(self.return_ingredients_as_list())
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    # Define method to return ingredients as a list
    def return_ingredients_as_list(self):
        if self.ingredients:
            return self.ingredients.split(", ")
        else:
            return []

# Create the table in the database
Base.metadata.create_all(engine)

# Create the session class and bind it to the engine
Session = sessionmaker(bind=engine)
session = Session()

# Example usage:
# Add a new recipe
new_recipe = Recipe(name="Pasta", ingredients="Pasta, Tomato Sauce, Cheese", cooking_time=15)
new_recipe.calculate_difficulty()

# Add the recipe to the session and commit
session.add(new_recipe)
session.commit()

# Query and display all recipes
recipes = session.query(Recipe).all()
for recipe in recipes:
    print(recipe)

# Closing the session
session.close()
