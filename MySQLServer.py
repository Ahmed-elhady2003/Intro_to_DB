import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server (without specifying a database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",  # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Define the SQL query to create the database
        db_name = "alx_book_store"
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {db_name}"

        # Execute the query
        cursor.execute(create_db_query)

        # Commit the changes (not necessary for CREATE DATABASE but good practice)
        connection.commit()

        # Print success message
        print(f"Database '{db_name}' created successfully!")

    except mysql.connector.Error as err:
        # Handle specific error codes
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied (check your username or password)")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: The database does not exist and cannot be created")
        else:
            print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if _name_ == "_main_":
    create_database()