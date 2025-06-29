from mysql.connector import Error

def create_database():
    """
    Connects to the MySQL server and creates the 'alx_book_store' database.
    If the database already exists, it will not fail.
    """
    connection = None
    try:
        # Establish the connection to MySQL server
        # You'll need to replace 'your_username' and 'your_password' with your MySQL credentials
        connection = mysql.connector.connect(
            host="localhost",  # Or your MySQL server host
            user="your_username",
            password="your_password"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # SQL to create the database if it doesn't exist
            # Using IF NOT EXISTS to prevent failure if the database already exists
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)
            
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # Specific catch for mysql.connector.Error
        print(f"Error connecting to MySQL or creating database: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()