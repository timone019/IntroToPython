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
        if (self.difficulty is None):
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
                print("\n" + str(recipe))  # Add a newline before each recipe for better visibility

# Create the 'tea' recipe
tea = Recipe('Tea', 5)
tea.add_ingredients('Tea Leaves', 'Sugar', 'Water')

# Create the 'coffee' recipe
coffee = Recipe('Coffee', 5)
coffee.add_ingredients('Coffee Powder', 'Sugar', 'Water')

# Create the 'cake' recipe
cake = Recipe('Cake', 50)
cake.add_ingredients('Sugar', 'Butter', 'Eggs', 'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk')

# Create the 'banana smoothie' recipe
banana_smoothie = Recipe('Banana Smoothie', 5)
banana_smoothie.add_ingredients('Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes')

# Wrap the recipes into a list called 'recipes_list'
recipes_list = [tea, coffee, cake, banana_smoothie]

# Print each recipe in the list
for recipe in recipes_list:
    print(recipe)
    print()  # Add a newline for better readability

# Search for recipes containing 'Water'
print("Recipes containing 'Water':")
Recipe.recipe_search(recipes_list, 'Water')
print()

# Search for recipes containing 'Sugar'
print("\nRecipes containing 'Sugar':\n")
Recipe.recipe_search(recipes_list, 'Sugar')
print()

# Search for recipes containing 'Bananas'
print("Recipes containing 'Bananas':")
Recipe.recipe_search(recipes_list, 'Bananas')
print()