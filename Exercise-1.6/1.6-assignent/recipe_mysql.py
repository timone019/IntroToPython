# Create & Connect Database

import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="cf-python",
    password="password"
)

# Initialize cursor
cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Access the database
cursor.execute("USE task_database")

# Create Recipes table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)
""")

# Setting up a function to calculate difficulty
def calculate_difficulty(cooking_time, ingredients):
    # Calculate difficulty based on cooking_time and number of ingredients
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"
    
    return difficulty

# Creating a Recipe with create_recipe()    
def create_recipe(conn, cursor):
    # Collect recipe details
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))

    ingredients = []
    while True:
        ingredient = input("Enter an ingredient (or 'done' to finish): ")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)

    # Calling the function to calculate difficulty
    difficulty = calculate_difficulty(cooking_time, ingredients)

    # Convert ingredients list to a comma-separated string
    ingredients_str = ", ".join(ingredients)

    # Prepare SQL query
    query = """
    INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
    VALUES (%s, %s, %s, %s)
    """
    values = (name, ingredients_str, cooking_time, difficulty)

    # Execute query and commit changes
    cursor.execute(query, values)
    conn.commit()

    print("Recipe added successfully!")

# Searching for a Recipe with search_recipe()
def search_recipe(conn, cursor):
    # Step 1: Retrieve all ingredients from the Recipes table
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    # Step 2: Extract all unique ingredients into a list
    all_ingredients = set()
    for row in results:
        ingredients = row[0].split(", ")
        for ingredient in ingredients:
            all_ingredients.add(ingredient)

    # Convert the set to a sorted list for display
    all_ingredients = sorted(list(all_ingredients))

    # Step 3: Display ingredients to the user
    print("Available ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")

    # Step 4: Get user's choice
    choice = int(input("Enter the number corresponding to the ingredient you want to search for: "))
    search_ingredient = all_ingredients[choice - 1]

    # Step 5: Search for recipes containing the selected ingredient
    query = """
    SELECT name, ingredients, cooking_time, difficulty
    FROM Recipes
    WHERE ingredients LIKE %s
    """
    cursor.execute(query, ('%' + search_ingredient + '%',))
    search_results = cursor.fetchall()

    # Step 6: Display the search results
    if search_results:
        print("\nRecipes containing", search_ingredient + ":")
        for recipe in search_results:
            print(f"\nName: {recipe[0]}")
            print(f"Ingredients: {recipe[1]}")
            print(f"Cooking Time: {recipe[2]} minutes")
            print(f"Difficulty: {recipe[3]}")
    else:
        print(f"\nNo recipes found containing {search_ingredient}.")

# Updating a Recipe with update_recipe()
def update_recipe(conn, cursor):
    # Step 1: Fetch all recipes
    cursor.execute("SELECT id, name, cooking_time, ingredients, difficulty FROM Recipes")
    recipes = cursor.fetchall()

    # Step 2: Display all recipes
    print("\nRecipes:")
    for recipe in recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}, Cooking Time: {recipe[2]} minutes, Ingredients: {recipe[3]}, Difficulty: {recipe[4]}")
    
    # Step 3: Get the recipe ID to update
    recipe_id = int(input("\nEnter the ID of the recipe you want to update: "))

    # Step 4: Select the column to update
    print("\nWhich column do you want to update?")
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")
    column_choice = int(input("Enter the number corresponding to your choice: "))

    # Map the user's choice to the column name
    if column_choice == 1:
        column_name = "name"
    elif column_choice == 2:
        column_name = "cooking_time"
    elif column_choice == 3:
        column_name = "ingredients"
    else:
        print("Invalid choice. Exiting update function.")
        return

    # Step 5: Get the new value for the selected column
    new_value = input(f"Enter the new value for {column_name}: ")

    # Step 6: Build and execute the SQL update query
    if column_name == "name":
        query = "UPDATE Recipes SET name = %s WHERE id = %s"
        cursor.execute(query, (new_value, recipe_id))
    elif column_name == "cooking_time":
        query = "UPDATE Recipes SET cooking_time = %s WHERE id = %s"
        cursor.execute(query, (new_value, recipe_id))
        
        # Recalculate difficulty since cooking_time was updated
        cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        ingredients = cursor.fetchone()[0].split(", ")
        difficulty = calculate_difficulty(int(new_value), ingredients)
        
        # Update difficulty in the table
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (difficulty, recipe_id))
    elif column_name == "ingredients":
        # Convert ingredients list to a comma-separated string
        ingredients_list = new_value.split(", ")
        
        # Update the ingredients column
        query = "UPDATE Recipes SET ingredients = %s WHERE id = %s"
        cursor.execute(query, (", ".join(ingredients_list), recipe_id))
        
        # Recalculate difficulty since ingredients were updated
        cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
        cooking_time = cursor.fetchone()[0]
        difficulty = calculate_difficulty(cooking_time, ingredients_list)
        
        # Update difficulty in the table
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (difficulty, recipe_id))

    # Step 7: Commit the changes
    conn.commit()
    print("Recipe updated successfully!")
    
# Deleting a Recipe with delete_recipe()
def delete_recipe(conn, cursor):
    # Step 1: Fetch all recipes
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()

    # Step 2: Display all recipes
    print("\nRecipes:")
    for recipe in recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")
    
    # Step 3: Get the recipe ID to delete
    recipe_id = int(input("\nEnter the ID of the recipe you want to delete: "))

    # Step 4: Build and execute the SQL delete query
    query = "DELETE FROM Recipes WHERE id = %s"
    cursor.execute(query, (recipe_id,))

    # Step 5: Commit the changes
    conn.commit()
    print("Recipe deleted successfully!")

# The Main Menu
def main_menu(conn, cursor):
    while True:
        print("\nMain Menu:")
        print("1. Add a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")

        choice = input("Please enter your choice (1-5): ")

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            print("Exiting the program...")
            conn.commit()  # Commit any changes to the database
            cursor.close()  # Close the cursor
            conn.close()  # Close the connection
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")

# Main code
if __name__ == "__main__":
    # Call the main menu
    main_menu(conn, cursor)

    # Close cursor and connection
    cursor.close()
    conn.close()


