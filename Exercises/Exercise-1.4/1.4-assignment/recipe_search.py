import pickle

def display_recipe(recipe):
    """
    Display the details of a recipe.
    """
    print(f"Recipe Name: {recipe.get('Name')}")
    print(f"Cooking Time: {recipe.get('Cooking Time')} minutes")
    print(f"Ingredients: {', '.join(recipe.get('Ingredients', []))}")
    print(f"Difficulty: {recipe.get('Difficulty')}")
    print()

def search_ingredient(data):
    """
    Search for recipes containing a specified ingredient.
    """
    all_ingredients = data.get('all_ingredients', [])
    
    if not all_ingredients:
        print("No ingredients found.")
        return
    
    # Display available ingredients
    print("Available ingredients:")
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index}: {ingredient}")
    
    try:
        # Get user input
        index = int(input("Enter the number corresponding to the ingredient you want to search for: "))
        ingredient_searched = all_ingredients[index]
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid number.")
        return

    # Search for recipes containing the ingredient
    recipes_list = data.get('recipes_list', [])
    
    found = False
    for recipe in recipes_list:
        if ingredient_searched in recipe.get('Ingredients', []):
            display_recipe(recipe)
            found = True
    
    if not found:
        print(f"No recipes found containing the ingredient '{ingredient_searched}'.")

def main():
    filename = input("Enter the filename containing the recipe data: ")
    
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    # Call the search_ingredient function
    search_ingredient(data)

if __name__ == "__main__":
    main()
