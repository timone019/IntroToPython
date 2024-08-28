recipes_list = []
ingredients_list = []

def take_recipe():
    while True:
        name = input("Enter recipe name: ")
        if name.isalpha():
            break
        else:
            print("Invalid input. Please enter a valid name (letters only).")

    while True:
        try:
            cooking_time = int(input("Enter cooking time (in minutes): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for the cooking time.")
    
    while True:
        ingredients = input("Enter ingredients (comma-separated): ").split(',')
        if all(ingredient.strip() for ingredient in ingredients):
            break
        else:
            print("Invalid input. Please enter at least one ingredient.")
    
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": [ingredient.strip() for ingredient in ingredients]
    }
    
    return recipe

def determine_difficulty(recipe):
    cooking_time = recipe["cooking_time"]
    num_ingredients = len(recipe["ingredients"])
    
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"
    
    return difficulty

def print_recipe(recipe):
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time (min): {recipe['cooking_time']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"  - {ingredient}")
    print(f"Difficulty level: {recipe['difficulty']}")
    print()  # Print an empty line for better readability

if __name__ == "__main__":
    while True:
        try:
            n = int(input("How many recipes would you like to enter? "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    for _ in range(n):
        recipe = take_recipe()
        for ingredient in recipe["ingredients"]:
            stripped_ingredient = ingredient.strip()
            if stripped_ingredient not in ingredients_list:
                ingredients_list.append(stripped_ingredient)
        recipe["difficulty"] = determine_difficulty(recipe)
        recipes_list.append(recipe)
    
    for recipe in recipes_list: # Print all recipes
        print_recipe(recipe)

    print("Ingredients Available Across All Recipes:")
    ingredients_list.sort()  # Sort the list alphabetically
    for ingredient in ingredients_list:
        print(f"  - {ingredient}")
    
  
