# Day 61: Building Advanced Forms with Flask WTForms
Yesterday we saw how we could make HTML forms work with our Flask server and get hold of the data that a user enters into the form. Today, we're going to improve on that, we're going to build forms using a Flask extension called **Flask-WTF**. It has a number of benefits over the simple HTML Form. e.g.

- **Easy Form Validation** - Makes sure the user is entering data in the required format in all the required fields. e.g. checking that the user's email entry has a "@" and a "." at the end. All without having to write your own validation code.
- **Less Code** - If you have a number of forms in your website, using WTForm can dramatically reduce the amount of code you have to write (or copy & paste).
- **Built in CSRF Protection** - CSRF stands for [Cross Site Request Forgery](https://owasp.org/www-community/attacks/csrf), it's an attack that can be made on website forms which forces your users to do unintended actions (e.g. transfer money to a stranger) or compromise your website's security if it's an admin. 

Flask developers will usually choose Flask-WTF to create forms in their websites. However, in the wild, you might also see projects that are built with HTML Forms. So it's important to understand how both of them work.

**Secrets**
By the end of today, we will build a website that holds some secrets. Only with the right username and password can you access the page with our secrets.


## Installing Flask-WTF
[WTForms](https://wtforms.readthedocs.io/en/2.3.x/)

- Unzip the starting folder
- Install Flask
- [x] Create the login route which renders the `login.html` file
- [x] Run the app to make sure it works
- [x] Install Flask-WTF Extension
- [x] Use the terminal to install Flask-WTF ([install guide](https://flask-wtf.readthedocs.io/en/1.0.x/install/))
### requirements.txt
This is a file where you can specify all the dependencies (the installed packages that your project depends on) and their versions. This means that you can share your project without all the installed packages, making it a lot more lightweight. When someone downloads your project (like you've done here), the requirements.txt file tells their code editor which packages need to be installed. [More here](https://docs.google.com/document/d/e/2PACX-1vRIW_TuZ6z0ASjAoxgJgmzjGYLCDx019tKvphaTwK_Za7fnMKywUuXI0-s5wr0nQI_gprm6J6y7L9rL/pub).

## Creating Forms with Flask-WTF
**Challenge.** Read the [documentation](https://flask-wtf.readthedocs.io/en/1.0.x/form/) to create a simple login form.

**Specifications.**
- Must have `email` and `password`
- Can be `StringFields`
- Don't worry about validators
- Inputs should be size 30
- No need to create `labels` or `inputs` manually with HTML

HINT: csrf protection comes via adding `{{ form.csrf_token }}` to `login.html`. A [secret key]() will need to be created and applied to `main.py` to generate the csrf_token

NOTE: Uses Python Classes and Object Inheritance (from Day 16)

Had to change the button to a link in order to renavigate from index.html to login.html.
```html
<!DOCTYPE HTML>
<html>
<head>
	<title>Secrets</title>
</head>
<body>
<div class="jumbotron">
	<div class="container">
		<h1>Welcome</h1>
		<p>Are you ready to discover my secret?</p>
		<a href="{{ url_for('login') }}"><button class="btn btn-primary btn-lg">Login</button></a>
	</div>
</div>
</body>
</html>
```

```html
<!DOCTYPE HTML>

<html>
	<head>
		<title>Login</title>
		{{ form.csrf_token }}
	</head>
	<body>
        <div class="container">
		<h1>Login</h1>
        <!-- This is where our form will go. -->
				<form method="POST" action="/">
					{{ form.csrf_token }}
					{{ form.username.label }} {{ form.username(size=30) }}
					{{ form.password.label }} {{ form.password(size=30) }}
					<input type="submit" value="Go">
				</form>
        </div>
	</body>
</html>
```

```py
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)

app.secret_key = b'xxxxxxxxxxxxxxxxxxxxxxx'

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')

@app.route("/login")
def login():
    return render_template('login.html', form=LoginForm())
```

## Code Improvements for Our WTForms

## Adding Validation to Forms with Flask-WTF

## Receiving Form Data with WTForms

## Inheriting Templates Using Jinja2

## Using FLask-Bootstrap as an Inherited Template

## Flask-BootStrap Supports WTForms