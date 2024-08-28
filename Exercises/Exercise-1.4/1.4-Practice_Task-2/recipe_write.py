import pickle

# Create the recipe dictionary
recipe = {
    'Name': "Tea",
    'Ingredients': [ "Tea leaves", "Water", "Sugar" ],
    'Cooking Time (in minutes)': 5,  
    'Difficulty': "Easy"
}
# Store the dictionary in a binary file
# Using the with statement to ensure the file is properly closed
with open('recipeDetail.bin', 'wb') as my_file:
    pickle.dump(recipe, my_file)

# Load the dictionary back and display it
with open("recipe_binary.bin", "rb") as file:
    loaded_recipe = pickle.load(file)

# Display the loaded recipe with readable formatting
print("Recipe:")
print(f"Ingredient Name: {loaded_recipe['Ingredient Name']}")
print(f"Ingredients: {', '.join(loaded_recipe['Ingredients'])}")
print(f"Cooking Time: {loaded_recipe['Cooking Time']}")
print(f"Difficulty: {loaded_recipe['Difficulty']}")