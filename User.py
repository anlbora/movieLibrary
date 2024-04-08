from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

class User:
    """
    Represents a user with their details such as name, surname, age, username, password, and email.
    
    Attributes:
    - name: A string representing the first name of the user.
    - surname: A string representing the last name of the user.
    - age: An integer representing the age of the user.
    - username: A string representing the username of the user.
    - password: A string representing the password of the user.
    - email: A string representing the email address of the user.
    """
    
    def __init__(self, name, surname, age, username, password, email):
        """
        Initializes a User object with the provided details.
        
        Parameters:
        - name: A string representing the first name of the user.
        - surname: A string representing the last name of the user.
        - age: An integer representing the age of the user.
        - username: A string representing the username of the user.
        - password: A string representing the password of the user.
        - email: A string representing the email address of the user.
        
        Returns:
        None
        """
        
        self.name = name
        self.surname = surname
        self.age = age
        self.username = username
        self.password = password
        self.email = email
