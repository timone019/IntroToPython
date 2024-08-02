import pickle

def calc_difficulty(cooking_time, num_ingredients):
    """
    Determine the difficulty level of the recipe based on cooking time and number of ingredients.
    """
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = 'Easy'
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = 'Medium'
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = 'Intermediate'
    else:
        difficulty = 'Hard'
    
    return difficulty

def take_recipe():
    """
    Take the recipe details from the user and return a dictionary containing the recipe attributes.
    """
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = input("Enter the ingredients separated by commas: ").split(", ")

    # Calculate difficulty
    num_ingredients = len(ingredients)
    difficulty = calc_difficulty(cooking_time, num_ingredients)

    # Gather attributes into a dictionary
    recipe = {
        'Name': name,
        'Cooking Time': cooking_time,
        'Ingredients': ingredients,
        'Difficulty': difficulty
    }

    return recipe

def save_recipe(recipe, filename='recipes.bin'):
    """
    Save the recipe to a binary file.
    """
    try:
        with open(filename, 'ab') as file:
            pickle.dump(recipe, file)
    except Exception as e:
        print(f"Error saving recipe: {e}")

if __name__ == "__main__":
    recipe = take_recipe()
    save_recipe(recipe)
    print("Recipe saved successfully!")
