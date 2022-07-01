# Day 60: Make POST Requests with Flask and HTML Forms

## Make the Contact Form Work
Yesterday, we built an upgraded version of our blog website that uses Bootstrap for styling. The only part of the website that doesn't work is the contact form on the Contact Page. This is because we need to learn about submitting HTML forms and catching the submitted data in our Flask server.

So the goal for today is to understand how HTML forms are submitted and how to use the data from the form to actually send an email to ourselves with the data submitted by the user.

## HTML Forms Revision - Creating a Form from Scratch
1. Create a new PyCharm Project called html-forms. It should contain a main.py and index.html. 
2. Create a new Flask application and serve the index.html page. Add an <h1> to the index.html so that you can tell if it's working.
3. CHALLENGE: Create a HTML Form in index.html so that when rendered as a webpage, this is what you see: (image not included)

### `main.py`
```py
from flask import Flask, render_template, url_for
import datetime

app = Flask(__name__)

def get_copyright_year():
  return datetime.date.today().year

@app.route('/')
def home():
    return render_template("index.html", year=get_copyright_year())

if __name__ == "__main__":
    app.run(debug=True)
```

### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Title</title>
  </head>
  <body>
    <h1>It Works!</h1>
    <form>
      <!-- Name name Password password Ok -->
      <label for="name">Name: </label>
      <input type="text" id="name" name="name">
      <label for="password">Password: </label>
      <input type="text" id="password" name="password">
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
```

## Handle POST Requests with Flask Servers
Now that we've created our form, the next step is to get it to work. We need our Flask server to be able to receive the data entered by the user.

At the moment when you fill out the form and press "Ok", nothing happens.

In order for it to send the form data, we have to change our HTML form. It needs to have an `action` and `method`.

1. CHALLENGE: See if you can use the documentation below to figure out how to make our HTML form submit a "POST" request to the path "/login".
https://www.w3schools.com/tags/att_form_method.asp

https://www.w3schools.com/tags/att_form_action.asp

2. Once the form is submitted, we also need to catch this POST request in our server. To do this we first need to give each input in our form a name attribute. 
3. Now we can create a decorator in our **main.py** that will trigger a method when it receives a **POST** request:
Notice that the `methods` parameter accepts a **dictionary**, so you can have **multiple** methods targeted by one route. e.g.

`@app.route("/contact", methods=["GET", "POST"]`

More on this in the documentation here: https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods

4. Flask has a method called `request` (don't confuse this with the requests module) which allows us to tap into the parameters of the request that was made to our server.

💪 DIFFICULT CHALLENGE: See if you can use the Flask documentation below to figure out how to get hold of the name and password that was entered into the form and send it back to the client as a <h1>. e.g.:

Documentation:

https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object

HINT:

https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Title</title>
  </head>
  <body>
    <h1>Your Username Is...</h1>
    <p>{{ username }}</p>

    <h1>Your Password Is...</h1>
    <p>{{ password }}</p>
  </body>
</html>
```

```py
@app.route('/login', methods=["GET", "POST"])
def receive_data():
  username = request.form['name']
  password = request.form['password']
  
  return render_template('login.html', username=username, password=password)
```

## POST Requests in Flask Solution

### The Flask Request Object
To complete the challenge, we had to tap into the `request` object. The [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object) was key in solving this challenge.

NOTE: The action attribute of the form can be set to `"/login"` e.g.

`<form action="/login" method="post">`

or it can be dynamically generated with `url_for` e.g.

`<form action="{‌{ url_for('receive_data') }}" method="post">`

Depending on where your server is hosted, the "/login" path may change. So it's usually a better idea to use url_for to dynamically generate the url for a particular function in your Flask server.

```html
    <form action="{‌{ url_for('receive_data') }}" method="post">
      <!-- Name name Password password Ok -->
      <label for="name">Name: </label>
      <input type="text" id="name" name="name">
      <label for="password">Password: </label>
      <input type="text" id="password" name="password">
      <input type="submit" value="Submit">
    </form>
```

## Getting the Contact Form to Work
Now that we've seen how to get hold of the data entered into a form from our Flask server, it's time to apply this knowledge to our previous blog website.

1. Use your previous day's blog project or get hold of a fresh copy from here:

[replit](https://repl.it/@appbrewery/day-59-end.zip)
[Yesterday's Blog Project](https://github.com/Joshua-Jenkins33/100DaysOfPython/tree/main/059_Day_59_Blog_Capstone_Project_Part_2_Adding_Styling)

2. Add a `"/form-entry"` route in main.py to receive data from the form

3. CHALLENGE: Update the code in `contact.html` and `main.py` so that you print the information the user has entered into the form and return a <h1> that says "Successfully sent your message".

```py
@app.route('/form-entry', methods=["GET", "POST"])
def form_entry():
    print(request.form)
    username = request.form['name']
    phone = request.form['phone']
    email_address = request.form['email']
    message = request.form['message']

    return "<h1>Successfully sent your message!</h1>"
```

```html
<form id="contactForm" action="{{ url_for('form_entry') }}" method="post"> 
    <!-- data-sb-form-api-token="API_TOKEN"  -->
    <div class="form-floating">
        <input class="form-control" id="name" name="name" type="text" placeholder="Enter your name..." data-sb-validations="required" />
        <label for="name">Name</label>
        <div class="invalid-feedback" data-sb-feedback="name:required">A name is required.</div>
    </div>
    <div class="form-floating">
        <input class="form-control" id="email" name="email" type="email" placeholder="Enter your email..." data-sb-validations="required,email" />
        <label for="email">Email address</label>
        <div class="invalid-feedback" data-sb-feedback="email:required">An email is required.</div>
        <div class="invalid-feedback" data-sb-feedback="email:email">Email is not valid.</div>
    </div>
    <div class="form-floating">
        <input class="form-control" id="phone" name="phone" type="tel" placeholder="Enter your phone number..." data-sb-validations="required" />
        <label for="phone">Phone Number</label>
        <div class="invalid-feedback" data-sb-feedback="phone:required">A phone number is required.</div>
    </div>
    <div class="form-floating">
        <textarea class="form-control" id="message" name="message" placeholder="Enter your message here..." style="height: 12rem" data-sb-validations="required"></textarea>
        <label for="message">Message</label>
        <div class="invalid-feedback" data-sb-feedback="message:required">A message is required.</div>
    </div>
    <div class="form-floating">
        <input type="submit" value="Submit">
    </div>
    <!-- <br /> -->
    <!-- Submit success message-->
    <!---->
    <!-- This is what your users will see when the form-->
    <!-- has successfully submitted-->
    <!-- <div class="d-none" id="submitSuccessMessage">
        <div class="text-center mb-3">
            <div class="fw-bolder">Form submission successful!</div>
            To activate this form, sign up at
            <br />
            <a href="https://startbootstrap.com/solution/contact-forms">https://startbootstrap.com/solution/contact-forms</a>
        </div>
    </div> -->
    <!-- Submit error message-->
    <!---->
    <!-- This is what your users will see when there is-->
    <!-- an error submitting the form-->
    <!-- <div class="d-none" id="submitErrorMessage"><div class="text-center text-danger mb-3">Error sending message!</div></div> -->
    <!-- Submit Button-->
    <!-- <button class="btn btn-primary text-uppercase disabled" id="submitButton" type="submit">Send</button> -->
</form>
```

4. CHALLENGE: Combine the `"/contact"` route with `"/form-entry"` so that they are both under the route `"/contact"` but depending on which method (`GET/POST`) that triggered the route, handle it appropriately.

HINT: You can use `request.method` to check which method triggered the route.

[Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods)

```py
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        username = request.form['name']
        phone = request.form['phone']
        email_address = request.form['email']
        message = request.form['message']
        return "<h1>Successfully sent your message!</h1>"
    else:
        return render_template("contact.html", year=get_copyright_year())
```

```html
<form id="contactForm" action="{{ url_for('contact') }}" method="post"> 
```

```css
#contactForm > .form-floating > .btn {
  padding: 0;
}
```

5. CHALLENGE: Instead of returning a `<h1>` that says "Successfully sent message", update the `contact.html` file so that the `<h1>` on the `contact.html` file becomes "Successfully sent message".

HINT: [Jinja Documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/#if)

```html
<header class="masthead" style="background-image: url('../static/assets/img/contact-bg.jpg')">
    <div class="container position-relative px-4 px-lg-5">
        <div class="row gx-4 gx-lg-5 justify-content-center">
            <div class="col-md-10 col-lg-8 col-xl-7">
                <div class="page-heading">
                    {% if form_submitted %}
                        <h1>Successfully sent your message!</h1>
                    {% else %}
                        <h1>Contact Me</h1>
                    {% endif %}
                    <span class="subheading">Have questions? I have answers.</span>
                </div>
            </div>
        </div>
    </div>
</header>
```

```py
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        username = request.form['name']
        phone = request.form['phone']
        email_address = request.form['email']
        message = request.form['message']
        return render_template("contact.html", year=get_copyright_year(), form_submitted = True)
    else:
        return render_template("contact.html", year=get_copyright_year())
```

## Sending Email with smtplib
We've learnt how to send email using smtplib already (e.g. Day 32), let's use this knowledge to make the contact form complete and actually send us (website owner) an email when a user is trying to get in touch.

You might need to review some of the lessons on smtplib from Day 32.

```py
def send_contact_email(form):
    body = f"Username: {form['username']}\nPhone Number: {form['phone']}\nEmail Address: {form['email']}\nMessage:\n{form['message']}"
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=RECEIVER,
            msg=f"Subject:BlogSite Contact Form Submission\n\n{body}"
        )

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        send_contact_email(request.form)
        return render_template("contact.html", year=get_copyright_year(), form_submitted = True)
    else:
        return render_template("contact.html", year=get_copyright_year())
```