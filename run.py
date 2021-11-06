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

    menu_chosen = int(input("Enter '1' or '2' from the menu to continue:"))
    print(f"You chose {menu_chosen}")

menu()
