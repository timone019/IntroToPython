# Function to check if the input is a valid number
def is_valid_number(input_str):
	return input_str.isdigit()

# Function to get a valid age from the user
def get_valid_age(prompt):
	while True:
		age_str = input(prompt)
		if is_valid_number(age_str):
			return int(age_str)
		else:
			print("Invalid input! Please enter a valid number.")

# Prompt the user to enter their age
age = get_valid_age("Enter your age: ")

# Check if age is between 18 and 35
print("Age between 18 and 35: " + str(18 < age < 35))
