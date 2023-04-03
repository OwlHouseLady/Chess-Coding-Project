# Import necessary modules
import sqlite3
import hashlib

# Define function to create a database
def create_database():
    # Connect to the database1
    conn = sqlite3.connect('users.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table for users if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")

    # Save the changes to the database
    conn.commit()
    # Close the connection
    conn.close()

# Define function for user login
def login():
    # Prompt user for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Hash the password using SHA-256 
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Connect to the database
    conn = sqlite3.connect('users.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Select user with matching username from the database
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    # Check if user exists and if password is correct
    if user is None:
        print("Invalid username or password!")
    elif user[2] != hashed_password:
        print("Invalid username or password!")
    else:
        print("Login successful!")

    # Close the connection
    conn.close()

# Define function for user registration
def register():
    # Prompt user for desired username and password
    username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")

    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Connect to the database
    conn = sqlite3.connect('users.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Select user with matching username from the database
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    # Check if username is already taken and if not, add user to the database
    if user is not None:
        print("Username already exists!")
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        print("Registration successful!")

    # Save the changes to the database
    conn.commit()
    # Close the connection
    conn.close()

# Call the create_database function to create the database if it doesn't exist
create_database()

# Loop to prompt user for login or registration
while True:
    print("1. Login")
    print("2. Register")
    choice = input("Enter your choice (1 or 2): ")

    # If user chooses login, call the login function and break out of the loop
    if choice == '1':
        login()
        break
    # If user chooses registration, call the register function and break out of the loop
    elif choice == '2':
        register()
        break
    # If user enters an invalid choice, prompt them to try again
    else:
        print("Invalid choice. Please try again.")