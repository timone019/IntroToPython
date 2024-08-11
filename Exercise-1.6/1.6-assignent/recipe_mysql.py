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
