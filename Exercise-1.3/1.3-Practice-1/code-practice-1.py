# Function to check if the input is a valid number
def is_valid_number(input_str):
	return input_str.replace('.', '', 1).isdigit()

# Function to get a valid number from the user
def get_valid_number(prompt):
	while True:
		number_str = input(prompt)
		if is_valid_number(number_str):
			return float(number_str)
		else:
			print("Invalid input! Please enter a valid number.")

# Function to get a valid operator from the user
def get_valid_operator(prompt):
	while True:
		operator = input(prompt)
		if operator in ['+', '-']:
			return operator
		else:
			print("Invalid input! Please enter a valid operator (+ or -).")

# Get the first number from the user
first_value = get_valid_number("Enter the first value: ")

# Get the second number from the user
second_value = get_valid_number("Enter the second value: ")

# Get the operator from the user
operator = get_valid_operator("Enter the operator (+ or -): ")

# Perform the operation based on the operator
if operator == '+':
	result = first_value + second_value
	print(f"The result of {first_value} + {second_value} is {result}.")
elif operator == '-':
	result = first_value - second_value
	print(f"The result of {first_value} - {second_value} is {result}.")
else:
	print("Unknown operator.")