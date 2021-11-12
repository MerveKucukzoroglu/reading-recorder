from os import system, name
import gspread
from google.oauth2.service_account import Credentials
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('reading_tracker')


def menu():
    """
    Provide two options in the menu for user,
    One for log a book
    Second is information on the program.
    """
    print("Welcome to Reading-Tracker!\n")
    while True:
        print("Menu:")
        print("1. Log a book")
        print("2. About Reading-Tracker\n")

        menu_chosen = input("Enter '1' or '2' from the menu to continue: \n")

        if validate_menu(menu_chosen):
            break
    return menu_chosen


def validate_menu(value):
    """
    Direct user to option chosen from the menu.
    Let the user enter '1' or '2' else print an error.
    """
    if value == "1":
        clear()
        submit_book()
    elif value == "2":
        clear()
        about()
    elif value == "":
        clear()
        print("Please choose a valid option\n")
        return False
    else:
        clear()
        print(f"'{value}' is not valid option in the menu.")
        print("Please enter '1' or '2'\n")
        return False

    return True


def submit_book():
    """
    Call email, username, and book_info functions one by one
    """
    email()
    username()
    book_info()


def book_info():
    """
    This function will collect
    Title and author information from the user.
    """
    print("Hello there bookworm! Lets see which book you have read!")
    print("It's okay if you enter the book you wish to read later..\n")
    while True:
        book_title = input("You can now enter the title of the book: \n")
        if validate_book(book_title.title()):
            break
        
    while True:
        author = input(f"Who is the author of {book_title.title()}? \n")
        if validate_book(author):
            break
    print("You have submitted the following book: \n") 
    book_data = print(f"{book_title.title()} by {author.title()}\n")
    return book_data


def validate_book(value):
    """
    Validate input submitted by user is not empty
    """
    if value == "":
        print("You have forgotten to type here..\n")
        return False
    else:
        return True
    return True


def about():
    """
    About the program from menu
    Either exits the about section or
    The user submits a book
    """
    print("This is a recorder to keep a track on your reading.")
    print("You will be asked to enter your name and email address")
    print("You will enter title of the book and author")
    print("You will enter the date you started and completed the book")
    print("You can also use this tracker to enter future dates.")
    print("It will help you keep a track of when you want to read the book\n")

    while True:
        print("Would you like to submit a book?")
        choose_about = input("Type 'y' to continue or 'n' to exit: \n")
        if validate_about(choose_about):
            break
    return choose_about


def validate_about(option):
    """
    Validates the option chosen in menu - about section
    Redirects user to valid option chosen
    """
    if (option == "y" or option == "Y"):
        clear()
        print("Going to log a book...\n")
        submit_book()
    elif (option == "n" or option == "N"):
        clear()
        menu()
    elif option == "":
        clear()
        print("Please choose a valid option!\n")
        return False
    else:
        clear()
        print(f"'{option}' is not valid option.")
        print("Please type 'y' to continue or 'n' to exit\n")
        return False

    return True


def username():
    """
    Collect username by input
    Place it to the name field in Google Sheet
    """
    while True:
        first_name = input("Please enter your First name: \n")
        if validate_name(first_name):
            break
    while True:
        last_name = input("Please enter your Last name: \n")
        if validate_name(last_name):
            break
    clear()
    full_name = print(f"{first_name.capitalize()} {last_name.capitalize()},\n")
    return full_name


def validate_name(name_input):
    """
    Validates user-input for username
    Passes only when the user has submitted a name
    """
    if name_input == "":
        clear()
        print("Oh..uh I'm afraid you have left the name blank.\n")
        return False
    elif (name_input.isnumeric()):
        clear()
        print(f"Have you just entered number '{name_input}' as your name?")
        return False
    elif (not name_input.isalpha()):
        clear()
        print(f"You entered '{name_input}', enter your name in alphabets!\n")
        return False
    else:
        return True
    return True


def email():
    """
    Collects and passes only valid email of the user
    Email validation credits are described in README.md
    """
    while True:
        user_email = input("Please enter your email: \n")
        regex = r"^[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]{3,252}\.[a-zA-Z]{2,}$"
    
        if(not re.fullmatch(regex, user_email)):
            clear()
            print(f"'{user_email}' is Invalid, enter a real email address!\n")
        else:
            clear()
            print("Thank you for entering your email!\n")
            break
    return user_email


def clear():
    """
    Clears the terminal whenever called.
    Credentials for this code is mentioned in README.md
    """
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def main():
    user_start = menu()

main()
