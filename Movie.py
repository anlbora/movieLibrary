from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

class Movie:
    """
    Represents a movie with its details such as name, director, release date, genre, rating, and URL.
    
    Attributes:
    - name: A string representing the name of the movie.
    - director: A string representing the name of the director of the movie.
    - release_date: A string representing the release date of the movie.
    - genre: A string representing the genre of the movie.
    - rating: An integer representing the rating of the movie.
    - url: A string representing the URL of the movie.
    """
    
    def __init__(self, name, director, release_date, genre, rating, url):
        """
        Initializes a Movie object with the provided details.
        
        Parameters:
        - name: A string representing the name of the movie.
        - director: A string representing the name of the director of the movie.
        - release_date: A string representing the release date of the movie.
        - genre: A string representing the genre of the movie.
        - rating: An integer representing the rating of the movie.
        - url: A string representing the URL of the movie.
        
        Returns:
        None
        """
        
        self.name = name
        self.director = director
        self.release_date = release_date
        self.genre = genre
        self.rating = rating
        self.url = url
