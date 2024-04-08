from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

class Director:
    """
    Represents a director with their details such as name, surname, age, number of Oscars, and number of awards.
    
    Attributes:
    - name: A string representing the name of the director.
    - surname: A string representing the surname of the director.
    - age: An integer representing the age of the director.
    - oscar: An integer representing the number of Oscars won by the director.
    - awards: An integer representing the total number of awards won by the director.
    """
    
    def __init__(self, name, surname, age, oscar, awards):
        """
        Initializes a Director object with the provided details.
        
        Parameters:
        - name: A string representing the name of the director.
        - surname: A string representing the surname of the director.
        - age: An integer representing the age of the director.
        - oscar: An integer representing the number of Oscars won by the director.
        - awards: An integer representing the total number of awards won by the director.
        
        Returns:
        None
        """
        
        self.name = name
        self.surname = surname
        self.age = age
        self.oscar = oscar
        self.awards = awards
