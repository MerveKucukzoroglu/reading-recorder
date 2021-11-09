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
    One for log-in a book
    Second is information on the program.
    """
    while True:
        print("Welcome to Reading-Tracker!\n")
        print("Menu:")
        print("1. Log-in a book")
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
    print("It's great to see you submitting a book. Please follow the steps to successfully log-in a book!")

def about():
    """
    About the program from menu
    Either exits the about section or 
    The user submits a book
    """
    print("This is a tracker to keep a track on the books you read in a time period.")
    print("You will be asked to enter name of the book and name of the author")
    print("You will enter the date you started and completed the book")
    print("You can also use this tracker to enter future dates and make a record of when you want to read this book\n")
    
    choose_about = input("Would you like to submit a book?\nType 'y' to continue or 'n' to exit: ")    

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
        print(f"Option chosen is not in the menu, you chose {value}.\nPlease enter '1' or '2'\n")
        return False

    return True          

user_chose = menu()
