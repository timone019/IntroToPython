# Function to check if the input is a valid name
def is_valid_name(name):
    return name.isalpha()

# Function to check if the input is a valid name
def is_valid_name(name):
    return name.isalpha()

# Function to get a valid name from the user
def get_valid_name(prompt):
    while True:
        name = input(prompt)
        if is_valid_name(name):
            return name
        else:
            print("Invalid input! Please enter a valid name containing only alphabetic characters.")

# Prompt the user to enter their first name
first_name = get_valid_name("Enter your first name: ")

# Prompt the user to enter their last name
last_name = get_valid_name("Enter your last name: ")

# Capitalize the first letter of the first and last name
first_name, last_name = first_name.capitalize(), last_name.capitalize()

# Print the capitalized name
print("Your name is", first_name, last_name)