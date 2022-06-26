# Day 54: Introduction to Web Development with Flask

## Understanding Backend Web Development with Python

Three Components:
1. Client
    - User going onto a browser
2. Server
    - Powerful computer hooked up to the internet and on 24/7
3. Database
    - Souped up spreadsheet where you store information related to your program

Analogy of a Restaurant:
1. Front of House (Customers sit)
2. Kitchen (Server)
3. Larder (Database of ingredients)

The server fetches relevenat ingredients from the database (fetches information about your spotify playlist) and the server ships it to the client-side so you see what you see.

## Create your First Web Server with Flask

For Windows, you need to set the Flask environment variable to your file:
`set FLASK_APP=hello.py`

(in bash it is `export FLASK_APP=app.py` and you can verify it's there by doing `printenv FLASK_APP`)

Followed by `flask run` in the terminal.

Click on the link and it'll launch your site in the browser. 

Flask converts the string into full html (inspect element and see your string in a tag!)

### Flask
> "One of the most popular web development frameworks." 

#### Library vs. Framework

Biggest difference:
**Libraries:** You are in full control when you call a method from a library and the control is then returned
**Frameworks:** The code never calls into a framework; instead the framework calls you

## Understand the Command Line on Windows and Mac

The terminal is a powerful tool! Type in commands in the terminal/command line/shell to control your computer.

The Kernal is the core of your operating system. The shell of your operating system refers to your user interface to allow you to interact with the kernal. There are GUI and CLI (command line interface). 

**Why Use the Command Line?** 
- Greater control.
- Easier and faster to do common things

`pwd` = Print Working Directory
`ls`= List (Display contents of directory)
`cd` = Change Directory

Creating a new folder:
`mkdir <name>`

Creating a new file:
`touch <name of file>`

deletes file:
`rm <name of file>` 

Remove Directory:
`rm -rf <name of folder>`; recursively and forcibly removes it. Deletes all subfolders in the folder
The terminal is *very* powerful.
Double check you're in the right folder.


## `__name__` and `__main__`: Special Attributes built into Python

## Python Functions as First Class Objects: Passing & Nesting Functions

## Understanding Python Decorator Functions and the `@` Syntax

## Create Your Own Python Decorator