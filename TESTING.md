# Testing
## Bugs
### Solved Bugs
* Menu - About:
    * When user choses option '2. About' from Menu, to read about the application, a bug appeared. 
    * The about section in menu does not do anything when user chooses to read about it.
    * Add a function to direct the user to submit a book or else exit to the home page(Welcome and menu).
    Added the submit a book or exit functionality at this stage. Resolved the issue.
    * To follow the progress of this issue from Github issues, [click here](https://github.com/MerveKucukzoroglu/reading-tracker/issues/1).

* White lines and extra spaces warning in run.py:
    * Remove the warnings by running the code in PEP8 and resolve the issue.
    * Removed extra white trailing spaces.
    * Added 2 lines between functions.
    * Shortened or separated long sentences.
    * PEP8 validation resolved the issues.
    * To follow the progress of this issue from Github issues, [click here](https://github.com/MerveKucukzoroglu/reading-tracker/issues/2).

* Submit section clear() incorrect user input:
    * When the user enters wrong names in submit a book stage, the terminal gets full. clear the wrong input by clear function.

         ![name-input-bug](documentation/name-input-bug.png)

    * The above error is resolved by adding clear() function in validate username function.
    * To follow the progress of this issue from Github issues, [click here](https://github.com/MerveKucukzoroglu/reading-tracker/issues/3).

* Email input bug:
    * The terminal gets busy with invalid email inputs and must be cleared with clear function.

        ![email-input-bug](documentation/email-input-bug.png)

    * Terminal is cleared by clear function when an email input is invalid.   

        ![invalid-mail](documentation/invalid-mail.png) 
        ![mail-error](documentation/mail-error.png) 

    * When email is valid:    
       
       ![correct-mail](documentation/correct-mail.png) 

    * To follow the progress of this issue from Github issues, [click here](https://github.com/MerveKucukzoroglu/reading-tracker/issues/4).

* End-date >= Start-date bug:
    * The start date of the book must be either on the same day or before the end date.
    * The bug is that the user can enter end date that is before start date.

    example:
    start_date = 2021-10-10
    end_date = 2010-11-11

    * Contacted Code Institute Tutor Assistance for identifying the issue.

    * Solution: Naming global variables END_DATE and START_DATE within another function with "global" keyword was the bug.

    * SOLVED: Created another function `validate_date(date)` to call it inside `end_book_date` function to proceed.

        ![invalid-date](documentation/invalid-date.png)

        ![valid-date](documentation/valid-date.png)

    * To follow the progress of this issue from Github issues, [click here](https://github.com/MerveKucukzoroglu/reading-tracker/issues/5).

### Remaining Bugs
* There are no remaining bugs.

## Validator Testing
* [PEP8](http://pep8online.com):
    * No Errors
    * White lines and extra spaces warnings found.
    * Remove the warnings by running the code in PEP8 and resolve the issue.
    * Removed extra white trailing spaces.
    * Added 2 lines between each function.
    * Shortened or separated long sentences.