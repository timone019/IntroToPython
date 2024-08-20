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

# Function 1: create_recipe
def create_recipe():
    name = input("Enter the recipe name (max 50 characters): ")
    if len(name) > 50 or not name.isalnum():
        print("Invalid recipe name!")
        return
    
    ingredients = []
    num_ingredients = int(input("How many ingredients? "))
    for _ in range(num_ingredients):
        ingredient = input("Enter an ingredient: ")
        ingredients.append(ingredient)
    ingredients_str = ", ".join(ingredients)
    
    cooking_time = input("Enter the cooking time (in minutes): ")
    if not cooking_time.isnumeric():
        print("Invalid cooking time!")
        return
    
    recipe_entry = Recipe(name=name, ingredients=ingredients_str, cooking_time=int(cooking_time))
    recipe_entry.calculate_difficulty()
    
    # Add the recipe to the session
    session.add(recipe_entry)
    session.commit()
    print("Recipe added successfully!")
    
# Function 2: view_all_recipes
def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
        return
    
    for recipe in recipes:
        print(recipe)

# Function 3: search_by_ingredients
def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("No recipes found.")
        return
    
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    for result in results:
        temp_ingredients = result[0].split(", ")
        for ingredient in temp_ingredients:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    print("Available ingredients:")
    for idx, ingredient in enumerate(all_ingredients):
        print(f"{idx+1}. {ingredient}")
    
    selected_indices = input("Enter the numbers of ingredients to search for, separated by spaces: ").split()
    
    if not all(idx.isnumeric() and 0 < int(idx) <= len(all_ingredients) for idx in selected_indices):
        print("Invalid selection.")
        return
    search_ingredients = [all_ingredients[int(idx)-1] for idx in selected_indices]
    conditions = [Recipe.ingredients.like(f"%{ingredient}%") for ingredient in search_ingredients]
    
    results = session.query(Recipe).filter(*conditions).all()
    
    if results:
        for recipe in results:
            print(recipe)
    else:
        print("No recipes found with the selected ingredients.")
        
# Function 4: edit_recipe
def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes found.")
        return
    
    results = session.query(Recipe.id, Recipe.name).all()
    for recipe_id, name in results:
        print(f"{recipe_id}. {name}")
    
    selected_id = input("Enter the ID of the recipe you want to edit: ")
    if not selected_id.isnumeric():
        print("Invalid ID!")
        return
    
    recipe_to_edit = session.query(Recipe).filter_by(id=int(selected_id)).first()
    if not recipe_to_edit:
        print("Recipe not found.")
        return
    
    print(f"1. Name: {recipe_to_edit.name}")
    print(f"2. Ingredients: {recipe_to_edit.ingredients}")
    print(f"3. Cooking Time: {recipe_to_edit.cooking_time}")
    
    attribute_to_edit = input("Enter the number of the attribute you'd like to edit: ")
    if attribute_to_edit not in ["1", "2", "3"]:
        print("Invalid selection!")
        return
    
    if attribute_to_edit == "1":
        new_name = input("Enter the new recipe name (max 50 characters): ")
        if len(new_name) > 50 or not new_name.isalnum():
            print("Invalid recipe name!")
            return
        recipe_to_edit.name = new_name
    elif attribute_to_edit == "2":
        new_ingredients = []
        num_ingredients = int(input("How many ingredients? "))
        for _ in range(num_ingredients):
            ingredient = input("Enter an ingredient: ")
            new_ingredients.append(ingredient)
        recipe_to_edit.ingredients = ", ".join(new_ingredients)
    elif attribute_to_edit == "3":
        new_cooking_time = input("Enter the new cooking time (in minutes): ")
        if not new_cooking_time.isnumeric():
            print("Invalid cooking time!")
            return
        recipe_to_edit.cooking_time = int(new_cooking_time)
    
    recipe_to_edit.calculate_difficulty()
    session.commit()
    print("Recipe updated successfully!")
    
# Function 5: delete_recipe
def delete_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes found.")
        return
    
    results = session.query(Recipe.id, Recipe.name).all()
    for recipe_id, name in results:
        print(f"{recipe_id}. {name}")
    
    selected_id = input("Enter the ID of the recipe you want to delete: ")
    if not selected_id.isnumeric():
        print("Invalid ID!")
        return
    
    recipe_to_delete = session.query(Recipe).filter_by(id=int(selected_id)).first()
    if not recipe_to_delete:
        print("Recipe not found.")
        return
    
    confirm = input(f"Are you sure you want to delete {recipe_to_delete.name}? (yes/no): ")
    if confirm.lower() == "yes":
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted successfully!")
    else:
        print("Delete operation canceled.")
            
                    
# Example usage:
# Add a new recipe
# new_recipe = Recipe(name="Pasta", ingredients="Pasta, Tomato Sauce, Cheese", cooking_time=15)
# new_recipe.calculate_difficulty()

# Add the recipe to the session and commit
# session.add(new_recipe)
# session.commit()

# Query and display all recipes
recipes = session.query(Recipe).all()
for recipe in recipes:
    print(recipe)

# Closing the session
session.close()
