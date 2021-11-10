# Reading-Tracker

## How to use

## Features
### Existing Features
### Future Features

## Data model

## Testing
### Bugs
* Solved Bugs
* Remaining Bugs

### Validator Testing
* PEP8:
    * test result

## Deployment
This project was deployed to Heroku.
* Steps for deployment:
    * Add requirements.txt to the project for deployment.
    * Type `pip3 freeze > requirements.txt` in the terminal.
    * Create a new Heroku app
    * Name the app to "reading-recorder" and location as Europe.
    * In settings add Config var and buildpacks in order _Python_ and _NodeJS_
    * In Deploy page, connect Github repository
    * Enable automatic deploys until the project is completed 
    * Click on __Deploy__

View the live site [here](https://reading-recorder.herokuapp.com/)

### Local Deployment

In order to make a local copy of this repository, you can type the following into your IDE terminal:

- `git clone hhttps://github.com/MerveKucukzoroglu/reading-tracker.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/MerveKucukzoroglu/reading-tracker)

## Credits

* Clear function credited to [GeekforGeeks](https://www.geeksforgeeks.org/clear-screen-python/):
    * `def clear():`
     `if name == "nt":`
       ` _ = system("cls")`
    `else:`
        `_ = system("clear")`
