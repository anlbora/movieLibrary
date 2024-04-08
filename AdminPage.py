from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from User import *
from Director import *
from Movie import *
import pandas as pd
from PyQt5.QtWidgets import QMessageBox
import plotly.graph_objects as go


class Ui_MainWindow(object):

    def __init__(self):
        """
        Initialize the DatabaseManager class.

        Establishes a connection to the SQLite database 'MovieDatabase.db' and creates a cursor 
        object to execute SQL queries.

        Attributes:
            connect (sqlite3.Connection): SQLite database connection object.
            cursor (sqlite3.Cursor): Cursor object to execute SQL queries.

        Raises:
            None

        Returns:
            None
        """
        self.connect = sqlite3.connect('MovieDatabase.db')
        self.cursor = self.connect.cursor()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 850)
        MainWindow.setMinimumSize(QtCore.QSize(600, 850))
        MainWindow.setMaximumSize(QtCore.QSize(600, 850))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 200, 801))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.show_AllUsers_btn = QtWidgets.QPushButton(self.groupBox)
        self.show_AllUsers_btn.setObjectName("show_AllUsers_btn")
        self.verticalLayout.addWidget(self.show_AllUsers_btn)
        self.show_AddUser_btn = QtWidgets.QPushButton(self.groupBox)
        self.show_AddUser_btn.setObjectName("show_AddUser_btn")
        self.verticalLayout.addWidget(self.show_AddUser_btn)
        self.show_DeleteUser_btn = QtWidgets.QPushButton(self.groupBox)
        self.show_DeleteUser_btn.setObjectName("show_DeleteUser_btn")
        self.verticalLayout.addWidget(self.show_DeleteUser_btn)
        self.show_UpdateUser_btn = QtWidgets.QPushButton(self.groupBox)
        self.show_UpdateUser_btn.setObjectName("show_UpdateUser_btn")
        self.verticalLayout.addWidget(self.show_UpdateUser_btn)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Show_AllDirectors_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.Show_AllDirectors_btn.setObjectName("Show_AllDirectors_btn")
        self.verticalLayout_4.addWidget(self.Show_AllDirectors_btn)
        self.Add_Director_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.Add_Director_btn.setObjectName("Add_Director_btn")
        self.verticalLayout_4.addWidget(self.Add_Director_btn)
        self.Delete_Director_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.Delete_Director_btn.setObjectName("Delete_Director_btn")
        self.verticalLayout_4.addWidget(self.Delete_Director_btn)
        self.Update_Director_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.Update_Director_btn.setObjectName("Update_Director_btn")
        self.verticalLayout_4.addWidget(self.Update_Director_btn)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Show_AllMovies_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.Show_AllMovies_btn.setObjectName("Show_AllMovies_btn")
        self.verticalLayout_5.addWidget(self.Show_AllMovies_btn)
        self.AddMovie_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.AddMovie_btn.setObjectName("AddMovie_btn")
        self.verticalLayout_5.addWidget(self.AddMovie_btn)
        self.DeleteMovie_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.DeleteMovie_btn.setObjectName("DeleteMovie_btn")
        self.verticalLayout_5.addWidget(self.DeleteMovie_btn)
        self.UpdateMovie_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.UpdateMovie_btn.setObjectName("UpdateMovie_btn")
        self.verticalLayout_5.addWidget(self.UpdateMovie_btn)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(220, 10, 361, 265))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.User_name = QtWidgets.QLineEdit(self.groupBox_4)
        self.User_name.setEnabled(True)
        self.User_name.setFrame(False)
        self.User_name.setObjectName("User_name")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.User_name)
        self.User_surname = QtWidgets.QLineEdit(self.groupBox_4)
        self.User_surname.setEnabled(True)
        self.User_surname.setFrame(False)
        self.User_surname.setObjectName("User_surname")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.User_surname)
        self.User_age = QtWidgets.QLineEdit(self.groupBox_4)
        self.User_age.setEnabled(True)
        self.User_age.setFrame(False)
        self.User_age.setObjectName("User_age")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.User_age)
        self.User_username = QtWidgets.QLineEdit(self.groupBox_4)
        self.User_username.setEnabled(True)
        self.User_username.setFrame(False)
        self.User_username.setObjectName("User_username")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.User_username)
        self.User_password = QtWidgets.QLineEdit(self.groupBox_4)
        self.User_password.setEnabled(True)
        self.User_password.setFrame(False)
        self.User_password.setObjectName("User_password")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.User_password)
        self.User_email = QtWidgets.QLineEdit(self.groupBox_4)
        self.User_email.setEnabled(True)
        self.User_email.setFrame(False)
        self.User_email.setObjectName("User_email")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.User_email)
        self.horizontalLayout_3.addLayout(self.formLayout_3)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(220, 280, 361, 240))
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.Director_name = QtWidgets.QLineEdit(self.groupBox_5)
        self.Director_name.setEnabled(True)
        self.Director_name.setFrame(False)
        self.Director_name.setObjectName("Director_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Director_name)
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.Director_surname = QtWidgets.QLineEdit(self.groupBox_5)
        self.Director_surname.setEnabled(True)
        self.Director_surname.setFrame(False)
        self.Director_surname.setObjectName("Director_surname")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Director_surname)
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.Director_Age = QtWidgets.QLineEdit(self.groupBox_5)
        self.Director_Age.setEnabled(True)
        self.Director_Age.setFrame(False)
        self.Director_Age.setObjectName("Director_Age")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Director_Age)
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.Director_Oscar = QtWidgets.QLineEdit(self.groupBox_5)
        self.Director_Oscar.setEnabled(True)
        self.Director_Oscar.setFrame(False)
        self.Director_Oscar.setObjectName("Director_Oscar")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Director_Oscar)
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.Director_Awards = QtWidgets.QLineEdit(self.groupBox_5)
        self.Director_Awards.setEnabled(True)
        self.Director_Awards.setFrame(False)
        self.Director_Awards.setObjectName("Director_Awards")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Director_Awards)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(220, 550, 361, 265))
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Movie_name = QtWidgets.QLineEdit(self.groupBox_6)
        self.Movie_name.setEnabled(True)
        self.Movie_name.setFrame(False)
        self.Movie_name.setObjectName("Movie_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Movie_name)
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Movie_releaseDate = QtWidgets.QLineEdit(self.groupBox_6)
        self.Movie_releaseDate.setEnabled(True)
        self.Movie_releaseDate.setFrame(False)
        self.Movie_releaseDate.setObjectName("Movie_releaseDate")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Movie_releaseDate)
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.Movie_director = QtWidgets.QLineEdit(self.groupBox_6)
        self.Movie_director.setEnabled(True)
        self.Movie_director.setFrame(False)
        self.Movie_director.setObjectName("Movie_director")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Movie_director)
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Movie_genre = QtWidgets.QLineEdit(self.groupBox_6)
        self.Movie_genre.setEnabled(True)
        self.Movie_genre.setFrame(False)
        self.Movie_genre.setObjectName("Movie_genre")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Movie_genre)
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.Movie_rating = QtWidgets.QLineEdit(self.groupBox_6)
        self.Movie_rating.setEnabled(True)
        self.Movie_rating.setFrame(False)
        self.Movie_rating.setObjectName("Movie_rating")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Movie_rating)
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.Movie_url = QtWidgets.QLineEdit(self.groupBox_6)
        self.Movie_url.setEnabled(True)
        self.Movie_url.setFrame(False)
        self.Movie_url.setObjectName("Movie_url")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Movie_url)
        self.horizontalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.show_AllUsers_btn.clicked.connect(self.show_AllUser)
        self.show_AddUser_btn.clicked.connect(self.addUser)
        self.show_DeleteUser_btn.clicked.connect(self.deleteUser)
        self.show_UpdateUser_btn.clicked.connect(self.updateUser)

        self.Show_AllDirectors_btn.clicked.connect(self.show_AllDirectors)
        self.Add_Director_btn.clicked.connect(self.addDirector)
        self.Delete_Director_btn.clicked.connect(self.deleteDirector)
        self.Update_Director_btn.clicked.connect(self.updateDirector)

        self.Show_AllMovies_btn.clicked.connect(self.show_AllMovies)
        self.AddMovie_btn.clicked.connect(self.addMovie)
        self.DeleteMovie_btn.clicked.connect(self.deleteMovie)
        self.UpdateMovie_btn.clicked.connect(self.updateMovie)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "User Operations"))
        self.show_AllUsers_btn.setText(_translate("MainWindow", "All Users"))
        self.show_AddUser_btn.setText(_translate("MainWindow", "Add User"))
        self.show_DeleteUser_btn.setText(_translate("MainWindow", "Delete User"))
        self.show_UpdateUser_btn.setText(_translate("MainWindow", "Update User"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Director Operations"))
        self.Show_AllDirectors_btn.setText(_translate("MainWindow", "All Directors"))
        self.Add_Director_btn.setText(_translate("MainWindow", "Add Director"))
        self.Delete_Director_btn.setText(_translate("MainWindow", "Delete Director"))
        self.Update_Director_btn.setText(_translate("MainWindow", "Update Director"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Movie Operations"))
        self.Show_AllMovies_btn.setText(_translate("MainWindow", "All Movies"))
        self.AddMovie_btn.setText(_translate("MainWindow", "Add Movie"))
        self.DeleteMovie_btn.setText(_translate("MainWindow", "Delete Movie"))
        self.UpdateMovie_btn.setText(_translate("MainWindow", "Update Movie"))
        self.groupBox_4.setTitle(_translate("MainWindow", "User Informations"))
        self.label_12.setText(_translate("MainWindow", "Name:"))
        self.label_13.setText(_translate("MainWindow", "Surname:"))
        self.label_14.setText(_translate("MainWindow", "Age:"))
        self.label_15.setText(_translate("MainWindow", "Username:"))
        self.label_16.setText(_translate("MainWindow", "Password:"))
        self.label_17.setText(_translate("MainWindow", "Email:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Director Informations"))
        self.label_7.setText(_translate("MainWindow", "Name:"))
        self.label_8.setText(_translate("MainWindow", "Surname:"))
        self.label_9.setText(_translate("MainWindow", "Age:"))
        self.label_10.setText(_translate("MainWindow", "Oscar Nominated:"))
        self.label_11.setText(_translate("MainWindow", "Total Awards:"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Movie Informations"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "Release Date:"))
        self.label_3.setText(_translate("MainWindow", "Director:"))
        self.label_4.setText(_translate("MainWindow", "Genre:"))
        self.label_5.setText(_translate("MainWindow", "Rating:"))
        self.label_6.setText(_translate("MainWindow", "Movie URL:"))

    def show_AllUser(self):
        """
        Retrieve and display all user data from the database.

        Executes an SQL query to fetch all user data from the database, converts it into 
        a DataFrame, and visualizes the data using a table.

        Raises:
            None

        Returns:
            None
        """
        self.cursor.execute('SELECT * FROM Users')
        rows = self.cursor.fetchall()

        # Convert the fetched data to a DataFrame
        df = pd.DataFrame(rows, columns=[desc[0] for desc in self.cursor.description])

        # Visualize the data using a table
        fig = go.Figure(data=[go.Table(
            header=dict(values=list(df.columns),
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[df[col] for col in df.columns],
                    fill_color='lavender',
                    align='left'))
        ])

        fig.update_layout(title='Users Data')
        fig.show()

    def addUser(self):
        """
        Add a new user to the database based on the provided input from the UI fields.

        Retrieves user details from UI fields, validates them, and adds the new user to the database.
        Displays appropriate warning or success messages based on the operation's outcome.

        Raises:
            None

        Returns:
            None
        """
        # Retrieve user input from UI fields
        name = self.User_name.text()
        surname = self.User_surname.text()
        age = self.User_age.text()
        email = self.User_email.text()
        username = self.User_username.text()
        password = self.User_password.text()

        # Validate user input
        if not all([name, surname, age, email, username, password]):
            QMessageBox.warning(None, "Warning", "Please fill in all fields.")
            return

        # Validate email format
        if not email.endswith("@gmail.com") and not email.endswith("@hotmail.com") and not email.endswith("@outlook.com"):
            QMessageBox.warning(None, "Warning", "Not a valid email")
            return

        try:
            # Check if username or email already exists in the database
            self.cursor.execute("SELECT COUNT(*) FROM Users WHERE username = ? OR email = ?", (username, email))
            count = self.cursor.fetchone()[0]

            if count > 0:
                QMessageBox.warning(None, "Warning", "Username or email already taken")
                return

            # Create User object
            user = User(name, surname, age, username, password, email)

            # Insert new user into the database
            self.cursor.execute('''
                INSERT INTO Users (name, surname, age, username, password, email)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (user.name, user.surname, user.age, user.username, user.password, user.email))
            self.connect.commit()

            QMessageBox.information(None, "Success", "User added successfully")
            
            # Clear UI fields after successful addition
            self.clearUserFields()
        except Exception as e:
            # Display error message if an exception occurs
            QMessageBox.warning(None, "Error", f"An error occurred: {str(e)}")

    def clearUserFields(self):
        """
        Clear all user input fields in the UI.

        Resets all the user input fields in the UI to empty strings.

        Raises:
            None

        Returns:
            None
        """
        self.User_name.setText("")
        self.User_surname.setText("")
        self.User_age.setText("")
        self.User_email.setText("")
        self.User_username.setText("")
        self.User_password.setText("")

    def clearDirectorFields(self):
        """
        Clear all director input fields in the UI.

        Resets all the director input fields in the UI to empty strings.

        Raises:
            None

        Returns:
            None
        """
        self.Director_name.setText("")
        self.Director_surname.setText("")
        self.Director_Age.setText("")
        self.Director_Oscar.setText("")
        self.Director_Awards.setText("")

    def clearMovieFields(self):
        """
        Clear all movie input fields in the UI.

        Resets all the movie input fields in the UI to empty strings.

        Raises:
            None

        Returns:
            None
        """
        self.Movie_name.setText("")
        self.Movie_director.setText("")
        self.Movie_releaseDate.setText("")
        self.Movie_genre.setText("")
        self.Movie_rating.setText("")
        self.Movie_url.setText("")

    def deleteUser(self):
        """
        Delete a user from the database based on the provided input from the UI fields.

        Retrieves user details from UI fields, validates them, and deletes the corresponding 
        user from the database. Displays appropriate warning or success messages based on the operation's outcome.

        Raises:
            None

        Returns:
            None
        """
        # Retrieve user details from UI fields
        username = self.User_username.text()
        password = self.User_password.text()
        email = self.User_email.text()

        # Validate user details
        if not username or not password or not email:
            QMessageBox.warning(None, "Warning", "Please fill in username, password, and email.")
            return

        try:
            # Validate the user credentials before deletion
            self.cursor.execute("SELECT COUNT(*) FROM Users WHERE username = ? AND password = ?", (username, password))
            count = self.cursor.fetchone()[0]

            if count == 0:
                QMessageBox.warning(None, "Warning", "Invalid username or password.")
                return

            # Delete user from the database
            self.cursor.execute("DELETE FROM Users WHERE username = ?", (username,))
            self.connect.commit()
            
            QMessageBox.information(None, "Success", "User deleted successfully")
            
            # Clear UI fields after successful deletion
            self.clearUserFields()
        except Exception as e:
            # Display error message if an exception occurs
            QMessageBox.warning(None, "Error", f"An error occurred: {str(e)}")

    def updateUser(self):
        """
        Update user details in the database based on the provided input from the UI fields.

        Retrieves user details from UI fields, validates them, and updates the corresponding 
        user details in the database. Displays appropriate warning or success messages based on the operation's outcome.

        Raises:
            None

        Returns:
            None
        """
        # Retrieve user details from UI fields
        name = self.User_name.text()
        surname = self.User_surname.text()
        age = self.User_age.text()
        username = self.User_username.text()
        password = self.User_password.text()
        new_email = self.User_email.text()

        # Validate user details
        if not all([username, password, new_email, surname, name, age]):
            QMessageBox.warning(None, "Warning", "Please fill in all fields.")
            return

        try:
            # Validate the user credentials before updating
            self.cursor.execute("SELECT COUNT(*) FROM Users WHERE username = ? AND password = ?", (username, password))
            count = self.cursor.fetchone()[0]

            if count == 0:
                QMessageBox.warning(None, "Warning", "Invalid username or password.")
                return

            # Update user details in the database
            self.cursor.execute("UPDATE Users SET name = ?, surname = ?, age = ?, email = ? WHERE username = ? AND password = ?", 
                                (name, surname, age, new_email, username, password))
            self.connect.commit()
            
            QMessageBox.information(None, "Success", "User updated successfully")
            
            # Clear UI fields after successful update
            self.clearUserFields()
        except Exception as e:
            # Display error message if an exception occurs
            QMessageBox.warning(None, "Error", f"An error occurred: {str(e)}")

    def show_AllDirectors(self):
        """
        Retrieve and display all director data from the database.

        Executes an SQL query to fetch all director data from the database, converts it into 
        a DataFrame, and visualizes the data using a table.

        Raises:
            None

        Returns:
            None
        """
        self.cursor.execute('SELECT * FROM Directors')
        rows = self.cursor.fetchall()

        # Convert the fetched data to a DataFrame
        df = pd.DataFrame(rows, columns=[desc[0] for desc in self.cursor.description])

        # Visualize the data using a table
        fig = go.Figure(data=[go.Table(
            header=dict(values=list(df.columns),
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[df[col] for col in df.columns],
                    fill_color='lavender',
                    align='left'))
        ])

        fig.update_layout(title='Directors Data')
        fig.show()

    def addDirector(self):
        """
        Add a new director to the database based on the provided input from the UI fields.

        Retrieves director details from UI fields, validates them, and inserts the new director 
        into the database. Displays appropriate warning or success messages based on the operation's outcome.

        Raises:
            None

        Returns:
            None
        """
        # Retrieve director details from UI fields
        name = self.Director_name.text()
        surname = self.Director_surname.text()
        age = self.Director_Age.text()
        oscar = self.Director_Oscar.text()
        awards = self.Director_Awards.text()

        director_name_surname = name + " " + surname

        # Validate director details
        if not all([name, surname, age, oscar, awards]):
            QMessageBox.warning(None, "Warning", "Please fill in all fields.")
            return

        try:
            # Check if the director already exists in the database
            self.cursor.execute("SELECT COUNT(*) FROM Directors WHERE director_name_surname = ? ", (director_name_surname,))
            count = self.cursor.fetchone()[0]

            if count > 0:
                QMessageBox.warning(None, "Warning", "Director already exists")
                return

            # Create Director object
            director = Director(name, surname, age, oscar, awards)

            # Insert new director into the database
            self.cursor.execute('''
                INSERT INTO Directors (director_name_surname, age, oscar, awards)
                VALUES (?, ?, ?, ?)
            ''', (director_name_surname, director.age, director.oscar, director.awards))
            self.connect.commit()
            
            QMessageBox.information(None, "Success", "Director added successfully")
            
            # Clear UI fields after successful addition
            self.clearDirectorFields()
        except Exception as e:
            # Display error message if an exception occurs
            QMessageBox.warning(None, "Error", f"An error occurred: {str(e)}")

    def deleteDirector(self):
        """
        Delete a director from the database based on the provided input from the UI fields.

        Retrieves director details from UI fields, validates them, and deletes the corresponding 
        director from the database. Displays appropriate warning or success messages based on the operation's outcome.

        Raises:
            None

        Returns:
            None
        """
        # Retrieve director details from UI fields
        name = self.Director_name.text()
        surname = self.Director_surname.text()
        director_name_surname = name + " " + surname

        # Validate director details
        if not name or not surname:
            QMessageBox.warning(None, "Warning", "Please fill in name and surname.")
            return

        try:
            # Validate the director exists in the database before deletion
            self.cursor.execute("SELECT COUNT(*) FROM Directors WHERE director_name_surname = ?", (director_name_surname,))
            count = self.cursor.fetchone()[0]

            if count == 0:
                QMessageBox.warning(None, "Warning", "Invalid Director")
                return

            # Delete director from the database
            self.cursor.execute("DELETE FROM Directors WHERE director_name_surname = ?", (director_name_surname,))
            self.connect.commit()
            
            QMessageBox.information(None, "Success", "Director deleted successfully")
            
            # Clear UI fields after successful deletion
            self.clearDirectorFields()
        except Exception as e:
            # Display error message if an exception occurs
            QMessageBox.warning(None, "Error", f"An error occurred: {str(e)}")

    def updateDirector(self):
        """
        Update director details in the database based on the provided input from the UI fields.

        Retrieves director details from UI fields, validates them, and updates the corresponding 
        director details in the database. Displays appropriate warning or success messages based on the operation's outcome.

        Raises:
            None

        Returns:
            None
        """
        # Retrieve director details from UI fields
        name = self.Director_name.text()
        surname = self.Director_surname.text()
        age = self.Director_Age.text()
        oscar = self.Director_Oscar.text()
        awards = self.Director_Awards.text()

        director_name_surname = name + " " + surname

        # Validate director details
        if not all([name, surname, age, oscar, awards]):
            QMessageBox.warning(None, "Warning", "Please fill in all fields.")
            return

        try:
            # Validate the director exists in the database before updating
            self.cursor.execute("SELECT COUNT(*) FROM Directors WHERE director_name_surname = ?", (director_name_surname,))
            count = self.cursor.fetchone()[0]

            if count == 0:
                QMessageBox.warning(None, "Warning", "Invalid Director.")
                return

            # Update director details in the database
            self.cursor.execute("UPDATE Directors SET director_name_surname = ?, age = ?, oscar = ?, awards = ? WHERE director_name_surname = ?", 
                                (director_name_surname, age, oscar, awards, director_name_surname))
            self.connect.commit()
            
            QMessageBox.information(None, "Success", "Director updated successfully")
            
            # Clear UI fields after successful update
            self.clearDirectorFields()
        except Exception as e:
            # Display error message if an exception occurs
            QMessageBox.warning(None, "Error", f"An error occurred: {str(e)}")

        def show_AllMovies(self):
            """
            Retrieve all movies from the database and visualize the data in a table format.

            Executes an SQL query to fetch all movies from the database, converts the fetched data 
            into a DataFrame using pandas, and visualizes the data using a table from plotly.

            Raises:
                None

            Returns:
                None
            """
            # Execute SQL query to fetch all movies
            self.cursor.execute('SELECT * FROM Movies')
            rows = self.cursor.fetchall()

            # Convert the fetched data to a DataFrame
            df = pd.DataFrame(rows, columns=[desc[0] for desc in self.cursor.description])

            # Visualize the data using a table from plotly
            fig = go.Figure(data=[go.Table(
                header=dict(values=list(df.columns),
                            fill_color='paleturquoise',
                            align='left'),
                cells=dict(values=[df[col] for col in df.columns],
                        fill_color='lavender',
                        align='left'))
            ])

            # Set the title for the visualization
            fig.update_layout(title='Movies Data')

            # Display the plotly figure
            fig.show()

    def show_AllMovies(self):
        """
        Fetches all movie records from the database and visualizes them using a table.
        
        This method executes an SQL query to retrieve all movie data, 
        converts the fetched data into a DataFrame, and visualizes it 
        using Plotly's table visualization feature.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
        
        Returns:
        None
        """
        
        # Execute SQL query to fetch all movie records
        self.cursor.execute('SELECT * FROM Movies')
        
        # Fetch all rows from the executed query
        rows = self.cursor.fetchall()

        # Convert the fetched data to a DataFrame
        df = pd.DataFrame(rows, columns=[desc[0] for desc in self.cursor.description])

        # Create a Plotly figure to visualize the data as a table
        fig = go.Figure(data=[go.Table(
            header=dict(values=list(df.columns),
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[df[col] for col in df.columns],
                    fill_color='lavender',
                    align='left'))
        ])

        # Set the title for the visualization
        fig.update_layout(title='Movies Data')
        
        # Display the Plotly figure
        fig.show()

    def addMovie(self):
        """
        Add a new movie to the database based on the provided input from the UI fields.

        Retrieves movie details from UI fields, validates them, and inserts the new movie into the database.
        Displays appropriate warning or success messages based on the operation's outcome.

        Raises:
            None

        Returns:
            None
        """
        # Retrieve movie details from UI fields
        name = self.Movie_name.text()
        director = self.Movie_director.text()
        release_Date = self.Movie_releaseDate.text()
        genre = self.Movie_genre.text()
        rating = self.Movie_rating.text()
        url = self.Movie_url.text()

        # Validate movie details
        if not all([name, director, release_Date, genre, rating, url]):
            QMessageBox.warning(None, "Warning", "Please fill in all fields.")
            return

        try:
            # Check if the movie already exists in the database
            self.cursor.execute("SELECT COUNT(*) FROM Movies WHERE name = ?", (name,))
            count = self.cursor.fetchone()[0]

            if count > 0:
                QMessageBox.warning(None, "Warning", "Movie already exists")
                return

            # Create Movie object
            movie = Movie(name, director, release_Date, genre, rating, url)

            # Insert new movie into the database
            self.cursor.execute('''
                INSERT INTO Movies (name, director_name_surname, release_Date, genre, rating, url)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (movie.name, movie.director, movie.release_date, movie.genre, movie.rating, movie.url))
            
            # Commit the changes to the database
            self.connect.commit()
            
            QMessageBox.information(None, "Success", "Movie added successfully")
            
            # Clear UI fields after successful addition
            self.clearMovieFields()
        except Exception as e:
            # Display error message if an exception occurs
            QMessageBox.warning(None, "Error", f"An error occurred: {str(e)}")

    def deleteMovie(self):
        """
        Delete a movie from the database based on the provided input from the UI fields.

        Retrieves movie details from UI fields, validates them, and deletes the corresponding movie from the database.
        Displays appropriate warning or success messages based on the operation's outcome.

        Raises:
            None

        Returns:
            None
        """
        # Retrieve movie details from UI fields
        name = self.Movie_name.text()
        director = self.Movie_director.text()

        # Validate movie details
        if not all([name, director]):
            QMessageBox.warning(None, "Warning", "Please fill in name and director areas.")
            return

        try:
            # Check if the movie exists in the database
            self.cursor.execute("SELECT COUNT(*) FROM Movies WHERE name = ? AND director_name_surname = ?", (name, director))
            count = self.cursor.fetchone()[0]

            if count == 0:
                QMessageBox.warning(None, "Warning", "Invalid Movie")
                return

            # Delete movie from the database
            self.cursor.execute("DELETE FROM Movies WHERE name = ?", (name,))
            
            # Commit the changes to the database
            self.connect.commit()
            
            QMessageBox.information(None, "Success", "Movie deleted successfully")
            
            # Clear UI fields after successful deletion
            self.clearMovieFields()
        except Exception as e:
            # Display error message if an exception occurs
            QMessageBox.warning(None, "Error", f"An error occurred: {str(e)}")

    def updateMovie(self):
        """
        Update movie details in the database based on the provided input from the UI fields.

        Retrieves movie details from UI fields, validates them, and updates the movie details in the database.
        Displays appropriate warning or success messages based on the operation's outcome.

        Raises:
            None

        Returns:
            None
        """
        # Retrieve movie details from UI fields
        name = self.Movie_name.text()
        director = self.Movie_director.text()
        release_Date = self.Movie_releaseDate.text()
        genre = self.Movie_genre.text()
        rating = self.Movie_rating.text()
        url = self.Movie_url.text()

        # Validate movie details
        if not all([name, director, release_Date, genre, rating, url]):
            QMessageBox.warning(None, "Warning", "Please fill in all fields.")
            return

        try:
            # Check if the movie exists in the database
            self.cursor.execute("SELECT COUNT(*) FROM Movies WHERE name = ?", (name,))
            count = self.cursor.fetchone()[0]

            if count == 0:
                QMessageBox.warning(None, "Warning", "Invalid Movie.")
                return

            # Update movie details in the database
            self.cursor.execute("""
                UPDATE Movies 
                SET director_name_surname = ?, release_date = ?, genre = ?, rating = ?, url = ? 
                WHERE name = ?""", 
                (director, release_Date, genre, rating, url, name))
            
            # Commit the changes to the database
            self.connect.commit()
            
            QMessageBox.information(None, "Success", "Movie updated successfully")
            
            # Clear UI fields after successful update
            self.clearDirectorFields()
        except Exception as e:
            # Display error message if an exception occurs
            QMessageBox.warning(None, "Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

