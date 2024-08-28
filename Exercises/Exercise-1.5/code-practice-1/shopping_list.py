class ShoppingList:
    def __init__(self, list_name):
        # Initialize the shopping list with a name and an empty list
        self.list_name = list_name
        self.shopping_list = []
        
    def add_item(self, item):
        # Add item to the list only if it is not already in the list
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            # print(f"{item} has been added to the list.")
        else:
            print(f"{item} is already in the list.")

    def remove_item(self, item):
        ## Remove item from the list
        try: 
            self.shopping_list.remove(item)
            # print(f"{item} has been removed from the list.")
        except ValueError:
            print(f"{item} is not in the list.")
            
    def view_list(self):
        # Prints the contents of the shopping list
        if self.shopping_list:
            print("\nItems in ", str(self.list_name), "\n", 30*"-")
            # print(f"Shopping List: {self.list_name}")
            for item in self.shopping_list:
                print(f" - {item}")
        else:
            print(f"Shopping list {self.list_name} is empty.")
            
    def merge_lists(self, obj):
        # Creating a name for our new, merged shopping list
        merged_lists_name = 'Merged List - ' + str(self.list_name) + " + " + str(obj.list_name)

        # Creating an empty ShoppingList object
        merged_lists_obj = ShoppingList(merged_lists_name)

        # Adding the first shopping list's items to our new list
        merged_lists_obj.shopping_list = self.shopping_list.copy()

        # Adding the second shopping list's items to our new list -
        # we're doing this so that there won't be any repeated items
        # in the final list, if both source lists contain common
        # items between each other
        
        for item in obj.shopping_list:
                if not item in merged_lists_obj.shopping_list:
                    merged_lists_obj.shopping_list.append(item)

        # Returning our new, merged object
        return merged_lists_obj
            
# Creating an object of the ShoppingList class
pet_store_list = ShoppingList("Pet Store Shopping List")

# Creating another object of the ShoppingList class
grocery_store_list = ShoppingList('Grocery Store List')

# Adding items to the list
for item in ['dog food', 'frisbee', 'bowl', 'collars', 'flea collars']:
    pet_store_list.add_item(item)

for item in ['fruits' ,'vegetables', 'bowl', 'ice cream']:
    grocery_store_list.add_item(item)


ShoppingList.merge_lists(pet_store_list, grocery_store_list)

merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)

# Viewing the merged list
merged_list.view_list()

# Adding items to the list
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

# Removing 'flea collars' from the list
pet_store_list.remove_item("flea collars")

# try adding 'frisbee' again to trigger already on list else block
pet_store_list.add_item("frisbee")


# Viewing the list to verify the item has been removed
pet_store_list.view_list()


# Viewing the list to verify the items have been added
# pet_store_list.view_list()
