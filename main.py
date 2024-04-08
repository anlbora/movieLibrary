import sys
import sqlite3
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from LoginPage import Ui_logInPage
from AdminPage import Ui_MainWindow
from User import *

class Main(QMainWindow):
    def __init__(self):    
        """
        Initializes the main application window and sets up the UI and database connections.
        
        This method initializes the main application window, sets up the UI using the Ui_logInPage class,
        establishes a connection to the SQLite database 'MovieDatabase.db', creates the required tables,
        and connects the UI buttons to their respective methods.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        # Initialize the main application window and set up the UI
        super().__init__()
        self.ui = Ui_logInPage()
        self.ui.setupUi(self)

        # Establish a connection to the SQLite database
        self.connect = sqlite3.connect('MovieDatabase.db')
        self.cursor = self.connect.cursor()

        # Create the required database tables
        self.create_tables()
    
        # Connect UI buttons to their respective methods
        self.ui.signup_btn.clicked.connect(self.sign_up)
        self.ui.login_btn.clicked.connect(self.log_in)
        self.ui.reset_btn.clicked.connect(self.reset_password)
        self.ui.delete_btn.clicked.connect(self.delete_account)

    def create_tables(self):
        """
        Creates database tables for Users, Directors, and Movies if they do not already exist.
        
        This method executes SQL queries to create the Users, Directors, and Movies tables in the database,
        with the specified column names and data types. It also establishes foreign key constraints
        to maintain referential integrity between the Movies and Directors tables.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        # Create the Users table if it does not exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100),
                surname VARCHAR(100),
                age INTEGER,
                username VARCHAR(100),
                password VARCHAR(100),
                email VARCHAR(100)
            )
        ''')

        # Create the Directors table if it does not exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Directors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                director_name_surname VARCHAR(200),
                age INTEGER,
                oscar INTEGER,
                awards INTEGER
            )
        ''')

        # Create the Movies table if it does not exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                director_name_surname VARCHAR(200),
                release_date DATETIME,
                genre VARCHAR(100),
                rating INTEGER,
                url VARCHAR(200),
                FOREIGN KEY (director_name_surname) REFERENCES Directors(director_name_surname)
            )
        ''')

        # Commit the changes to the database
        self.connect.commit()

    def sign_up(self):
        """
        Registers a new user by validating the provided user details and inserting them into the database.
        
        This method retrieves the user details entered by the user from the UI,
        validates the provided details,
        creates a new User object with the validated details,
        inserts the new user's details into the database,
        and displays an appropriate message based on the result of the sign-up operation.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        # Retrieve user details entered by the user from the UI
        name = self.ui.signup_name.text()
        surname = self.ui.signup_surname.text()
        age = self.ui.signup_age.text()
        email = self.ui.signup_email.text()
        username = self.ui.signup_username.text()
        password = self.ui.signup_password.text()

        # Validate if all fields are filled
        if not name or not surname or not age or not email or not username or not password:
            QMessageBox.warning(self, "Warning", "Please fill in all fields.")
            return

        # Validate the email format
        elif not email.endswith("@gmail.com") and not email.endswith("@hotmail.com") and not email.endswith("@outlook.com"):
            QMessageBox.warning(self, "Warning", "Not a valid email")
            return

        # Create a User object with the validated details
        user = User(name, surname, age, username, password, email)

        # Insert the new user's details into the database
        self.cursor.execute('''
                INSERT INTO Users (name, surname, age, username, password, email)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (user.name, user.surname, user.age, user.username, user.password, user.email))
        
        # Commit the changes to the database
        self.connect.commit()
        
        # Display a success message
        QMessageBox.information(self, "Success", "Sign-up successful.")

        # Clear the sign-up fields
        self.ui.signup_name.setText("")
        self.ui.signup_surname.setText("")
        self.ui.signup_age.setText("")
        self.ui.signup_password.setText("")
        self.ui.signup_email.setText("")
        self.ui.signup_username.setText("")

    def log_in(self):
        """
        Authenticates the user by checking the provided username and password against the database.
        
        This method retrieves the username and password entered by the user from the UI,
        executes an SQL query to find a matching user in the database,
        and displays an appropriate message based on the authentication result.
        If authentication is successful, it closes the current window and opens the admin page.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        # Retrieve username and password entered by the user from the UI
        username = self.ui.login_username.text()
        password = self.ui.login_password.text()

        # Execute the SQL query to find a matching user in the database
        self.cursor.execute('SELECT * FROM Users WHERE username = ? AND password = ?', (username, password))
        
        # Fetch the first matching row from the executed query
        row = self.cursor.fetchone()

        # Check if a matching user was found
        if row:
            # Display a success message
            QMessageBox.information(self, "Success", "Logged in successfully.")
            
            # Close the current window
            self.close()

            # Instantiate the admin page
            self.adminPage = QMainWindow()

            # Setup and initialize the admin page
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.adminPage)  # Assuming QMainWindow is the parent widget for adminPage

            # Show the admin page
            self.adminPage.show()

        else:
            # Display an error message
            QMessageBox.warning(self, "Error", "User not found or incorrect password.")

    def reset_password(self):
        """
        Resets the user's password by verifying the provided username and email and updating the password in the database.
        
        This method retrieves the email, username, and new password entered by the user from the UI,
        executes an SQL query to find a matching user in the database,
        updates the user's password in the database if a matching user is found,
        and displays an appropriate message based on the result of the password reset operation.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        # Retrieve email, username, and new password entered by the user from the UI
        email = self.ui.reset_email.text()
        username = self.ui.reset_username.text()
        password = self.ui.reset_newpassword.text()

        # Execute the SQL query to find a matching user in the database
        self.cursor.execute('SELECT * FROM Users WHERE username = ? AND email = ?', (username, email))
        
        # Fetch the first matching row from the executed query
        row = self.cursor.fetchone()

        # Check if a matching user was found
        if row:
            # Update the user's password in the database
            self.cursor.execute('UPDATE Users SET password = ? WHERE username = ? AND email = ?', (password, username, email))
            
            # Commit the changes to the database
            self.connect.commit()
            
            # Display a success message
            QMessageBox.information(self, "Success", "Password changed successfully.")

        else:
            # Display an error message
            QMessageBox.warning(self, "Error", "User not found or incorrect username/email.")

    def delete_account(self):
        """
        Deletes the user's account by verifying the provided username, email, and password and removing the account from the database.
        
        This method retrieves the email, username, and password entered by the user from the UI,
        executes an SQL query to find a matching user in the database,
        deletes the user's account from the database if a matching user is found,
        and displays an appropriate message based on the result of the account deletion operation.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        # Retrieve email, username, and password entered by the user from the UI
        email = self.ui.delete_email.text()
        username = self.ui.delete_username.text()
        password = self.ui.delete_password.text()

        # Execute the SQL query to find a matching user in the database
        self.cursor.execute('SELECT * FROM Users WHERE username = ? AND password = ?', (username, password))
        
        # Fetch the first matching row from the executed query
        row = self.cursor.fetchone()

        # Check if a matching user was found
        if row:
            # Delete the user's account from the database
            self.cursor.execute('DELETE FROM Users WHERE username = ? AND email = ? AND password = ?', (username, email, password))
            
            # Commit the changes to the database
            self.connect.commit()
            
            # Display a success message
            QMessageBox.information(self, "Success", "Account deleted successfully.")

        else:
            # Display an error message
            QMessageBox.warning(self, "Error", "User not found or incorrect username/password.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec_())
