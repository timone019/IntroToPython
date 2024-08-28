# Function to check if the input is a valid number
def is_valid_number(input_str):
    return input_str.lstrip('-').isdigit()

# Function to get a valid number of oranges from the user
def get_valid_number(prompt):
    while True:
        number_str = input(prompt)
        if is_valid_number(number_str):
            return int(number_str)
        else:
            print("Invalid input! Please enter a valid number.")

# Prompt the user to enter the number of oranges
number_of_oranges = get_valid_number("How many oranges do you have?: ")

if number_of_oranges > 0:
    print("You have some oranges.")
    if number_of_oranges > 50:
        print("But you've got way too many!")
elif number_of_oranges < 0:
    if number_of_oranges < -50:
        print("You owe me too many oranges, I'm going to come knocking on your door pal!")
    else:
        print(f"You owe me {abs(number_of_oranges)} oranges buddy.")
else:
    print("You have no oranges.")