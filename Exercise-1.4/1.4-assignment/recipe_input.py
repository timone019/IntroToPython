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

def main():
    filename = input("Enter the filename to load recipes from (or save to): ")

    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found. Creating a new recipe list.")
        data = {'recipes_list': [], 'all_ingredients': []}
    except Exception as e:
        print(f"An error occurred: {e}. Creating a new recipe list.")
        data = {'recipes_list': [], 'all_ingredients': []}
    else:
        print(f"File {filename} loaded successfully.")
    finally:
        recipes_list = data.get('recipes_list', [])
        all_ingredients = data.get('all_ingredients', [])

    num_recipes = int(input("How many recipes would you like to enter? "))

    for _ in range(num_recipes):
        recipe = take_recipe()
        recipes_list.append(recipe)

        for ingredient in recipe['Ingredients']:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    data = {
        'recipes_list': recipes_list,
        'all_ingredients': all_ingredients
    }

    with open(filename, 'wb') as file:
        pickle.dump(data, file)
        print(f"Data saved to {filename} successfully.")

if __name__ == "__main__":
    main()
