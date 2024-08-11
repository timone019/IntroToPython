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

# Close cursor and connection
cursor.close()
conn.close()

def create_recipe(conn, cursor):
    # Implement the function to create a new recipe
    print("Creating a new recipe...")
    # Add your code here

def search_recipe(conn, cursor):
    # Implement the function to search for a recipe by ingredient
    print("Searching for a recipe...")
    # Add your code here

def update_recipe(conn, cursor):
    # Implement the function to update an existing recipe
    print("Updating a recipe...")
    # Add your code here

def delete_recipe(conn, cursor):
    # Implement the function to delete a recipe
    print("Deleting a recipe...")
    # Add your code here

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

    conn = mysql.connector.connect(
        host="localhost",
        user="cf-python",
        password="password"
    )
    cursor = conn.cursor()

    # Access the database
    cursor.execute("USE task_database")

    # Call the main menu
    main_menu(conn, cursor)

