import gspread
from google.oauth2.service_account import Credentials

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
    while True:
        print("Welcome to Reading-Tracker!\n")
        print("Menu:")
        print("1. Log a book")
        print("2. About Reading-Tracker\n")

        menu_chosen = input("Enter '1' or '2' from the menu to continue: \n")

        if validate_menu(menu_chosen):
            print("menu option is valid!")
            break
    return menu_chosen


def submit_book():
    """
    Initial function to begin collecting data from user
    """
    print("It's great to see you submitting a book.")
    print("Please follow the steps to successfully log-in a book!")


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
            print("Redirecting you to option chosen...")
            break
    return choose_about


def validate_about(option):
    """
    Validates the option chosen in menu - about section
    Redirects user to valid option chosen
    """
    if (option == "y" or option == "Y"):
        print("Going to log a book...\n")
        submit_book()
    elif (option == "n" or option == "N"):
        print("Exiting the menu...")
        print("Clearing the terminal and moving to home page...\n")
    elif option == "":
        print("Please choose a valid option!")
        return False
    else:
        print(f"'{option}' is not valid option.")
        print("Please type 'y' to continue or 'n' to exit\n")
        return False

    return True


def validate_menu(value):
    """
    Direct user to option chosen from the menu.
    Let the user enter '1' or '2' else print an error.
    """
    if value == "1":
        print("Calling submit_book function...")
        submit_book()
    elif value == "2":
        about()
    elif value == "":
        print("Please choose a valid option")
        return False
    else:
        print(f"'{value}' is not valid option in the menu.")
        print("Please enter '1' or '2'\n")
        return False

    return True


user_chose = menu()
