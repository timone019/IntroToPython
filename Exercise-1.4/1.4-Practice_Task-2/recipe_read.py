import pickle

with open('recipeDetail.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)

print("Recipe details - ")
print("Name:  " + recipe['name'] + " " + recipe['difficulty'])
print("Ingredients:  " + str(recipe['ingredients']))
print("Cooking time (in minutes): " + recipe['color']) 

