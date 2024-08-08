class Recipe:
    all_ingredients = set()  # Class variable to track all ingredients across recipes

    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None
        self.calculate_difficulty()

    # Getter and setter for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Getter and setter for cooking_time
    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        self.calculate_difficulty()  # Recalculate difficulty if cooking time changes

    # Method to add ingredients
    def add_ingredients(self, *ingredients):
        self.ingredients.extend(ingredients)
        self.update_all_ingredients()
        self.calculate_difficulty()  # Recalculate difficulty if ingredients are updated

    # Getter for ingredients
    def get_ingredients(self):
        return self.ingredients

    # Method to calculate difficulty
    def calculate_difficulty(self):
        if self.cooking_time < 10:
            if len(self.ingredients) < 4:
                self.difficulty = 'Easy'
            else:
                self.difficulty = 'Medium'
        else:
            if len(self.ingredients) < 4:
                self.difficulty = 'Intermediate'
            else:
                self.difficulty = 'Hard'

    # Getter for difficulty
    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    # Method to search for an ingredient
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    # Method to update all_ingredients class variable
    def update_all_ingredients(self):
        Recipe.all_ingredients.update(self.ingredients)

    # String representation of the recipe
    def __str__(self):
        return (
            f"Recipe: {self.name}\n"
            f"Ingredients: {', '.join(self.ingredients)}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}"
        )

    @staticmethod
    def recipe_search(data, search_term):
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
                
                # Create a new recipe
recipe = Recipe('Pasta Salad', 15)

# Add ingredients to the recipe
recipe.add_ingredients('Pasta', 'Tomatoes', 'Olives', 'Feta')

# Print the recipe details
print(recipe)

# Check if an ingredient is in the recipe
print(recipe.search_ingredient('Pasta'))  # Output: True
print(recipe.search_ingredient('Cheese'))  # Output: False

# Get the list of all unique ingredients across recipes
print(Recipe.all_ingredients)  # Output: {'Pasta', 'Tomatoes', 'Olives', 'Feta'}
                
# Example Usage
recipe1 = Recipe('Pasta Salad', 15)
recipe1.add_ingredients('Pasta', 'Tomatoes', 'Olives', 'Feta')

recipe2 = Recipe('Fruit Salad', 5)
recipe2.add_ingredients('Apples', 'Bananas', 'Oranges')

recipe3 = Recipe('Omelette', 10)
recipe3.add_ingredients('Eggs', 'Milk', 'Salt', 'Pepper')

# List of recipes
recipes = [recipe1, recipe2, recipe3]

# Search for recipes containing 'Tomatoes'
Recipe.recipe_search(recipes, 'Tomatoes')

# Create an object named 'tea' under the Recipe class
tea = Recipe('Tea', 5)

# Add ingredients to the 'tea' recipe
tea.add_ingredients('Tea Leaves', 'Sugar', 'Water')

# Display the string representation of the 'tea' object
print(tea)

# Create the 'tea' recipe
tea = Recipe('Tea', 5)
tea.add_ingredients('Tea Leaves', 'Sugar', 'Water')
print(tea)

# Create the 'coffee' recipe
coffee = Recipe('Coffee', 5)
coffee.add_ingredients('Coffee Powder', 'Sugar', 'Water')
print(coffee)

# Create the 'cake' recipe
cake = Recipe('Cake', 50)
cake.add_ingredients('Sugar', 'Butter', 'Eggs', 'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk')
print(cake)

# Create the 'banana smoothie' recipe
banana_smoothie = Recipe('Banana Smoothie', 5)
banana_smoothie.add_ingredients('Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes')
print(banana_smoothie)
