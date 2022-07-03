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
We can improve the code we wrote in the previous section, which was written mostly the standard expectation that students and those with 60 days of Python under their belts should be able to manage.

1. Change the `password` input to use a `PasswordField` from WTForms to obscure the text typed in the input
  - [Documentation for Other Field Types](https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields)
2. Arugments given when creating a `String` or `PasswordField` is for the `label` property of the form field. Add the keyword argument for this so it is clear what this parameter is associated with. See `login.html` to see how this parameter attribute relates to the field attribute.
3. The Quickstart set the form action to the hardcoded path of `"/"`. It's a good idea to use dynamically built urls; swap it for `url_for()`.
4. We can also better format the layout of the labels and inputs in our WTForms generated form by using normal HTML elements
5. `SubmitField`s are a thing; no button necessary!

## Adding Validation to Forms with Flask-WTF
One of the major reasons to use WTForms over HTML Forms is validation. These validation rules come straight out of the WTForms box.

1. Add validator objects when we create each field in our form (`, validators=[DataRequired()])`) remember to import from `from wtforms.validators import DataRequired`
  - [Documentation](https://wtforms.readthedocs.io/en/2.3.x/crash_course/#validators)
  - `validators` accepts a **List** of validator **Objects**. DataRequired makes the two fields required fields, so the user must type something, otherwise an error will be generated.
  - When a form is submitted, there may be a number of erros, so a List of `errors` can be generated and passed over to our form HTML as a property on the field which generated the error (`form.<field>.errors`)
2. Utilize these errors and loop through them to show some text when an error appears
  - [Documentation](https://wtforms.readthedocs.io/en/2.3.x/crash_course/#displaying-errors)

```html
  {% for err in form.email.errors %}
    <span style="color:red">{{ err }}</span>
  {% endfor %}
```

3. The final step is to tell our form to validate the user's entry when they hit submit. Edit our route and make sure it is able to respond to `POST` requests and then to `validate_on_submit()`.
  - Some browsers have built form detection things that supply validation pop-ups; this isn't coming from our code and will vary accross browsers
4. To switch it off, we give the `form` tag an attribute of `novalidate` and now our validation efforts should work.

### Challenge: Email Validation
Using the [documentation](https://wtforms.readthedocs.io/en/2.3.x/validators/#module-wtforms.validators) on WTForm validators, add `Email` validation to the email field so that you must type a **valid email** (with `"@"` and `"."`) otherwise you get an error. Also add `Length` validation to the password so you must type at least **8 characters**.

*Hint:* Pay close attention if the documentation mentions anything about installing an additional package to get email validation to work. If so, you may want to pip isntall the package through the terminal.

```py
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email(message="You must enter a valid email address.", check_deliverability=True)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Password must be at least 8 characters long.")])
```

## Receiving Form Data with WTForms
With basic HTML we could use the `request` object from Flask to access the key-value pairs that were entered into the form when the `POST` request was made.

It's easier with WTForms; tap into the `<form_object>.<form_field>.data`.
- [Documentation](https://wtforms.readthedocs.io/en/2.3.x/crash_course/#how-forms-get-data)
- `print(login_form.email.data)`

One thing to check before printing is whether the form has been submitted (POST request) or if it's a GET request when the form is being rendered.

Previously, we used `if request.method == "POST"`

No we're going to check the return value of `validate_on_submit()` which will be `True` if validation was successful **after the user submitted the form**, or `False` if it failed.

```py
if login_form.validate_on_submit():
  print(login_form.email.data)
```

### Challenge
Update the `/login` route in **main.py** so that if the form was **submitted** and **validated** and their **credentials** matched the following:
- email: **admin@email.com**
- password: **12345678**

Then show them the **success.html** page, otherwise show them the **denied.html** page.

```py
@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(f"Email: {login_form.email.data}")
        print(f"Password: {login_form.password.data}")
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)
```

## Inheriting Templates Using Jinja2
We've injected `header.html` and `footer.html` code using Jinja like this:
```html
{% include "header.html" %}
Web Page Content
{% include "footer.html" %}
```

Which makes for a flexible way of using Jinja to Template a website. It means that your header and footer can stay the same and you can easily insert them into all of your webpages.

### Template Inheritance
You might find that you want to use the same design template for your entire website, but you might need to change some code in your header or footer. In these cases, it's better to use **Template Inheritance**.

It's similar to Class Inheritance in that you can take parent templates and extend its styling to your child web pages.

i.e. **base.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```
This has predefined areas (or blocks) where new content can be inserted by a child webpage inheriting from this template.

1. Rewrite the `success.html` page to inherit from this `base.html` template
```html
#1.
{% extends "base.html" %}
#2.
{% block title %}Success{% endblock %}
#3.
{% block content %}
    <div class="container">
      <h1>Top Secret </h1>
      <iframe src="https://giphy.com/embed/Ju7l5y9osyymQ" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
      <p><a href="https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ">via GIPHY</a></p>
    </div>
{% endblock %}
```
- #1: This line of code tells the templating engine (Jinja) to use **base.thml** as the template for this page
- #2: This block inserts a custom title into the header of the template
- #3: This block provides the content of the website. The part that is going to vary between webpages

### Challenge
Try doing the same thing for `denied.html`, making sure that it uses the `base.html` as the template and it has a custom title and content.

```html
{% extends "base.html" %}
{% block title %}Denied{% endblock %}
{% block content %}
	<div class="container">
		<h1>Access Denied </h1>
		<iframe src="https://giphy.com/embed/1xeVd1vr43nHO" width="480" height="271" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
		<p><a href="https://giphy.com/gifs/cheezburger-funny-dog-fails-1xeVd1vr43nHO">via GIPHY</a></p>
	</div>
{% endblock %}
```

## Using FLask-Bootstrap as an Inherited Template
We'll be using inheritance to improve the look-and-feel of the site.

### Flask Bootstrap
The Flask-Bootstrap Python extension makes stylizing this incredibly easy.

1. Install Flask-Bootstrap to your project using pip:
  - `pip install FLask-Bootstrap`
2. Challenge: Delete the super block in your `denied.html` file and use the [Flask-Bootstrap documentation](https://pythonhosted.org/Flask-Bootstrap/basic-usage.html) to convert our `denied.html`, `success.html`, and `index.html` to use Bootstrap as the template.

```py
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = b'blahblahblah'
Bootstrap(app)
```

```html
{% extends "bootstrap/base.html" %}
{% block title %}Secrets{% endblock %}
{% block navbar %}
<div class="navbar navbar-fixed-top">
  <!-- ... -->
</div>
{% endblock %}
{% block content %}
	<div class="jumbotron">
		<div class="container">
			<h1>Welcome</h1>
			<p>Are you ready to discover my secret?</p>
			<a href="{{ url_for('login') }}"><button class="btn btn-primary btn-lg">Login</button></a>
		</div>
	</div>
{% endblock %}
```

## Flask-BootStrap Supports WTForms
Super convenient method for generating forms with WTForms.

1 line of code == form. `{{ wtf.quick_form(form) }}`

This line generates all the labels, inputs, buttons, styling for your form just by taking the WTForm object that was passed to the template (`form`).
You can delete the entire element and add a line to inherit the wtf support from bootstrap and use the `quick_form()` to generate your `form`.
`{% import "bootstrap/wtf.html" as wtf %}`


[Documentation](https://pythonhosted.org/Flask-Bootstrap/forms.html)

**Login.html**
```html
{% extends "bootstrap/base.html" %}
{% import "bootstrap/wtf.html" as wtf %}
{% block title %}Login{% endblock %}
{% block navbar %}
<div class="navbar navbar-fixed-top">
  <!-- ... -->
</div>
{% endblock %}
{% block content %}
		<div class="container" style="width: 25%;">
		<h1>Login</h1>
		{{ wtf.quick_form(form, novalidate=True) }}
		</div>
{% endblock %}
```


