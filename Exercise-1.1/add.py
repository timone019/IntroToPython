# Prompt the user to enter the first number
try:
    a = int(input("Enter the first number: "))
except ValueError:
    print("Invalid input! Please enter a numeric value.")
    exit(1)

# Prompt the user to enter the second number
try:
    b = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input! Please enter a numeric value.")
    exit(1)

# Add the two numbers
c = a + b

# Print the result
print(c)