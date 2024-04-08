# Movie Management Program

## Overview

The Movie Management Program is a PyQt5-based desktop application designed to manage and organize information about movies, directors, and user accounts to be used by admins. It provides functionalities for adding, editing, deleting, and viewing movie details, director details, and user account information. The program utilizes an SQLite database to store and manage data.

## Features

### Login Page
- Log In
- Sign Up
- Reset Password
- Delete Account
- ![11](https://github.com/anlbora/movieLibrary/assets/100442507/b08e8b91-888f-4d84-93bc-a4040c316d2d)

  Log In page is the starting page which has Log In, Sign Up, Reset Password and Delete Account areas by connecting the SQLite. **create_tables** method creates neccessary database called **MovieDatabase** tables for **USERS, DIRECTORS and MOVIES.** There are various methods attached buttons which have their explanations in the code. All methods have exception handling not to break down the program.

  ![12](https://github.com/anlbora/movieLibrary/assets/100442507/f43b8665-89c9-45d0-aa54-c6d041f23b04)

  ![13](https://github.com/anlbora/movieLibrary/assets/100442507/adb60437-a757-4b5c-a434-edb8e2e265a3)


### AdminPanel
Admin panel lets the admin do various types of actions on Users, Movies and Directors such as **View, Add, Update and Delete.** Admin Panel's methods have their own explanations in the code. All methods have exception handling not to break down the program. 
### User Management

- **View All Users**: Displays a comprehensive list of all registered users.
- **Add Users**: Enables the addition of new user accounts.
- **Update Users**: Allows modification of existing user information.
- **Delete Users**: Facilitates the removal of user accounts after authentication.

### Director Management

- **View All Directors**: Presents a list of all registered directors.
- **Add Directors**: Allows the addition of new director profiles.
- **Update Directors**: Permits updates to existing director details.
- **Delete Directors**: Enables the deletion of director profiles from the database.

### Movie Management

- **View All Movies**: Displays a table containing information on all movies in the database.
- **Add Movies**: Facilitates the addition of new movie entries.
- **Update Movies**: Allows modifications to existing movie details.
- **Delete Movies**: Permits the removal of movies from the database

## Requirements

- Python 3.x
- PyQt5
- SQLite3

## Installation

1. Clone the repository:
  - git clone https://github.com/yourusername/movieLibrary.git
2. Navigate to the project directory:
  - cd movieLibrary
3. Install the required dependencies:
  - pip install -r requirements.txt
4. Run the application:
  - python main.py


## Usage

1. Launch the application by running `main.py`.
2. Sign up for a new account or log in with an existing account.
3. Use the respective buttons in the AdminPanel to manage movies, directors, and user accounts.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
