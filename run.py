import os
from os import system, name
import re
import datetime
import time
import gspread
from google.oauth2.service_account import Credentials


# ----- EMAIL SETTINGS ----- #
import smtplib  # SMTP protocol client (sending emails)
from email.mime.multipart import MIMEMultipart  # MIME (sending emails)
from email.mime.text import MIMEText  # Multipurpose Internet Mail Extensions
if os.path.exists("env.py"):
    import env  # noqa
MY_ADDRESS = os.environ.get("MY_ADDRESS")
PASSWORD = os.environ.get("PASSWORD")

FULL_NAME = ""
BOOK_DATA = ""
USER_EMAIL = ""
START_DATE = ""
END_DATE = ""
READER_INFO = []

# SCOPE code credits to CI, mentioned in README.md
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
    print("Welcome to Reading-Recorder!\n")
    while True:
        print("Menu:")
        print("1. Log a book")
        print("2. About Reading-Recorder\n")

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
    This function handles the automated python email sent to user
    The email is sent from Reading-Recorder to the user email given.
    As it is an automatic email, it is the user's responsibility
    to enter valid information.
    The credits of raw-python email code is mentioned in README.md
    """
    global USER_EMAIL
    global FULL_NAME
    global BOOK_DATA
    global START_DATE
    global END_DATE
    USER_EMAIL = email()
    FULL_NAME = username()
    print(FULL_NAME)
    BOOK_DATA = book_info()
    print(BOOK_DATA)
    START_DATE = start_book_date()
    END_DATE = end_book_date()

    # send the user an email with the book details they've entered
    msg = MIMEMultipart()
    msg["From"] = MY_ADDRESS
    msg["To"] = USER_EMAIL
    msg["Subject"] = "Reading Recorder"
    format_email = (
        f"Hi Bookworm, {FULL_NAME}<br>"
        "You have added the following book to your reading-recorder:"
        f"<br>{BOOK_DATA}<br>"
        f"Start Date: {START_DATE}<br>End Date: {END_DATE}<br>"
        "<p><em>Note: This is an automated email."
        f"You recieve this email as '{USER_EMAIL}'"
        "is entered to Reading-Recorder"
        " application to submit a book. Ignore this email,"
        " if it's not you.</em></p><br>"
        "<p>* Reading Recorder is a reading recorder to keep"
        " a track on your readings."
        " This program aims to target the bookworms."
        "It is a handy program to store details of the book you read."
        "You can use this tracker both when you complete a book "
        "or when you wish to read the book.<br>"
        "<a href = 'https://reading-recorder.herokuapp.com/'>"
        "Click here to view the application</a></p>"
        )
    msg.attach(MIMEText(str(format_email), "html"))  # must convert to str()
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)  # access server
    smtpserver.ehlo()  # identify ourselves to smtp gmail client
    smtpserver.starttls()  # secure our email with tls encryption
    smtpserver.ehlo()  # re-identify ourselves as an encrypted connection
    smtpserver.login(MY_ADDRESS, PASSWORD)  # login to the server
    smtpserver.send_message(msg)  # send the message
    smtpserver.quit()  # quit the server


def book_info():
    """
    This function will collect
    Title and author information from the user.
    """
    global BOOK_DATA
    print("Hello there bookworm! Lets see which book you have read!")
    print("It's okay if you enter the book you wish to read later..\n")
    while True:
        book_title = input("You can now enter the title of the book: \n")
        if validate_book(book_title.title()):
            READER_INFO.append(book_title.title())
            break
    while True:
        author = input(f"Who is the author of {book_title.title()}? \n")
        if validate_book(author):
            READER_INFO.append(author.title())
            break
    print("You have submitted the following book: \n")
    BOOK_DATA = f"{book_title.title()} by {author.title()}\n"
    return BOOK_DATA


def validate_book(value):
    """
    Validate input submitted by user is not empty
    """
    if value == "":
        clear()
        print("Oops.. You have forgotten to type..\n")
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
    if option.lower() == "y":
        clear()
        print("Going to log a book...\n")
        submit_book()
    elif option.lower() == "n":
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
    global FULL_NAME
    while True:
        first_name = input("Please enter your First name: \n")
        if validate_name(first_name):
            READER_INFO.append(first_name.capitalize())
            break
    while True:
        last_name = input("Please enter your Last name: \n")
        if validate_name(last_name):
            READER_INFO.append(last_name.capitalize())
            break
    clear()
    FULL_NAME = f"{first_name.capitalize()} {last_name.capitalize()},\n"
    return FULL_NAME


def validate_name(name_input):
    """
    Validates user-input for username
    Passes only when the user has submitted a name
    """
    if name_input == "":
        clear()
        print("Oh..uh I'm afraid you have left the name blank.\n")
        return False
    elif name_input.isnumeric():
        clear()
        print(f"Have you just entered number '{name_input}' as your name?")
        return False
    elif not name_input.isalpha():
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
    global USER_EMAIL
    while True:
        print("ATTENTION! At this stage you must enter your real email!")
        print("After successfully submitting a book to Reading-Recorder,")
        print("your inputs will be saved and you will recieve")
        print("an automatic email of your submission.\n")

        USER_EMAIL = input("Please enter your email: \n")
        regex = r"^[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]{3,252}\.[a-zA-Z]{2,}$"

        if not re.fullmatch(regex, USER_EMAIL):
            clear()
            print(f"'{USER_EMAIL}' is Invalid, enter a real email address!\n")
        else:
            clear()
            print("Thank you for entering your email!\n")
            READER_INFO.append(USER_EMAIL)
            break
    return USER_EMAIL


def start_book_date():
    """
    User will be asked to enter start date
    Date that user started or wish to start the book
    """
    clear()
    global START_DATE
    print("You can either enter the date you have started")
    print("or wish to start reading book you submitted.")
    print("You must enter the date in correct format!")
    print("i.e 'yyyy/mm/dd'\n")
    while True:
        START_DATE = input("Please enter Start-date in (YYYY-MM-DD): \n")
        date_format = "%Y-%m-%d"

        try:
            datetime.datetime.strptime(START_DATE, date_format)
            clear()
            READER_INFO.append(START_DATE)
            break
        except ValueError:
            clear()
            print("You must enter correct date format in YYYY-MM-DD..\n")
    return START_DATE


def end_book_date():
    """
    User will be asked to enter end date
    Date that user completed or wish to complete the book
    Validate-date code credentials in README.md
    """
    global START_DATE
    global END_DATE
    print("START-DATE: ", START_DATE)

    print("\nNow, you can either enter the date you have completed")
    print("or wish to complete reading book you submitted.")
    print("You must enter the date in correct format!")
    print("i.e 'yyyy/mm/dd'\n")
    while True:
        END_DATE = input("Please enter date completed in (YYYY-MM-DD): \n")
        date_format = "%Y-%m-%d"

        if validate_date(END_DATE):
            try:
                datetime.datetime.strptime(END_DATE, date_format)
                clear()
                print("START: ", START_DATE)
                print(f"END: {END_DATE}\n")

                READER_INFO.append(END_DATE)
                update_worksheet()
                time.sleep(3)
                clear()
                menu()
                break
            except ValueError:
                clear()
                print("You must enter correct date format in YYYY-MM-DD..\n")
    return END_DATE


def validate_date(date):
    """
    Validates end date is same or after start date
    """
    global START_DATE
    global END_DATE

    if date >= START_DATE:
        return True
    else:
        clear()
        print(f"Your Start date is {START_DATE}\n")
        print(f"You entered {END_DATE}\n")
        print(f"Please enter a date that is on or after {START_DATE}\n")
        return False
    return True


def clear():
    """
    Clears the terminal whenever called.
    Credentials for this code is mentioned in README.md
    """
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def update_worksheet():
    """
    Update reader worksheet by the input given by user
    """

    print("Updating reader worksheet..\n")
    reader_worksheet = SHEET.worksheet("read")

    worksheet_headings = reader_worksheet.row_values(1)
    print(worksheet_headings)

    reader_worksheet.append_row(READER_INFO)

    print(READER_INFO)

    print("\nWorksheet updated successfully.\n")


menu()
