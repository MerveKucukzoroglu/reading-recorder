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
    print("Welcome to Reading-Tracker!\n")
    print("Menu:")
    print("1. Log-in a book")
    print("2. About Reading-Tracker\n")

    menu_chosen = input("Enter '1' or '2' from the menu to continue: ")

    validate_menu(menu_chosen)

def validate_menu(value):
    """
    Direct user to option chosen from the menu.
    Let the user enter '1' or '2' else print an error.
    """
    if value == "1":
        print("Call log-in a book function")
    elif value == "2":
        print("This is a tracker to keep a track on the books you read in a time period.")
        print("You will be asked to enter name of the book and name of the author")
        print("You will enter the date you started and completed the book")
        print("You can also use this tracker to enter future dates and make a record of when you want to read this book")
    elif value == "":
        print("Please choose an option from the menu")    
    else:
        print(f"Option chosen is not in the menu, you chose {value}.\nPlease enter '1' or '2'")
              

menu()
