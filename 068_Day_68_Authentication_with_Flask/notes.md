# Day 68: Authentication with Flask

## Login and Registering Users with Authentication
In order to have users and associate data to user accounts, we need a way to register them and allow them to sign back into their accounts at a later date. 

This means they will be giving us some information that we have to keep secure. This is what authentication is all about, how to figure out if a user really is who they say they are. And that is the goal of today; Figure out how to register, login and logout users with email and password. So they can access their own private profile pages.

Also, we're going to allow users to download a top-secret Flask Programming Cheat Sheet. But only when they have registered and signed up to our website. 

## What is Authentication?
Often thought of as incredibly complicated; doesn't have to be!

### Why Authenticate?
Users start generating data. In order to associate pieces of data with users, they need an account (kind of like an ID card). It enables them to return and login and access their private information.

**Restrict Access**. Paying customers get to access whatever it is they're now entitled to.

The difficult part of authentication comes from how secure you make your website.

Our structure of our site will be simple with 4 pages. It'll have a **Home** page with two buttons that allows you to either go to the **Register** or **Log In** page. After they've registered or logged in, then they are able to gain access to the **Secrets** page.

## Download the Starting Project
- [x] Download the starting .zip files from this lesson (Starting Files - flask-auth-start.zip).
- [x] Unzip and open the project in PyCharm.
- [x] Make sure that the required packages (imports) are all installed and there are no red underlines.
* The starting files consists of an SQLite database called users.db, I created this in the same way we created databases before. 
- [x] Take a look at the database using DB Viewer and familiarise yourself with the fields in the database.
  - id, email (varchar100), password (varchar100), name (varchar1000)
- [x] Run the app and navigate around using the buttons and navigation bar. All the HTML pages should already render correctly. The login/register forms won't work of course. Look through all the code and make sure that everything makes sense before you get started.
## Register New Users
In order to register new users, you will need to take the information they have inputted in register.html and create a new `User` object with `email`, `name` and `password` to save into the **users.db**.

Once they are registered, we will take them straight to the **secrets.html** page.

The secrets.html page should say "Hello `<insert name>`". Where the name they typed in the registration form is displayed.

At this point, you should see a new entry in the database that corresponds to the data entered in the form.

Don't worry about download the file just yet, we'll do that in the next lesson!

```py
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(
            email = email,
            password = password,
            name = name
        )

        db.session.add(new_user)
        db.session.commit()
        return render_template("secrets.html", name=name)
    else:
        return render_template("register.html")
```

```html
{% extends "base.html" %}
{% block content %}

<div class="container">
  <h1 class="title">Welcome, {{ name }}!</h1>
  <a href="#">Download Your File</a>
</div>
{% endblock %}
```

## Downloading Files
When the user accesses the **secrets.html** page, they should be able to download a secret file. The file is located in the starting project:

static > files > cheat_sheet.pdf

In order to do this, we need to use a method from Flask called `send_from_directory()`.

1. First go into the secrets.html page and make the anchor tag make a GET request to your server at the path `/download`

2. In the download route, use the documentation for `send_from_directory()` to download the cheat_sheet.pdf file when the user clicks on the "Download Your File" button.

[https://flask.palletsprojects.com/en/1.1.x/api/#flask.send_from_directory](https://flask.palletsprojects.com/en/1.1.x/api/#flask.send_from_directory)

```html
{% extends "base.html" %}
{% block content %}

<div class="container">
  <h1 class="title">Welcome, {{ name }}!</h1>
  <a href="{{ url_for('download') }}" method="GET">Download Your File</a>
</div>
{% endblock %}
```

```py
@app.route('/download')
def download():
    return send_from_directory('static', filename="files/cheat_sheet.pdf")
```

## Encryption and Hashing
Level 1 Encryption -- Storing data in plain text in our databse (server level)
Level 2 Authentication -- Involves the use of Encryption

**Encryption.** Scrambling something so they can't tell what the original was *unless* they knew the secret to decode the message.

Level 3 Authentication -- Hashing

Easy to convert a password into a hash but not back into a password. Find the factors of 377 besides 1 and 377. 13 and 29. Not easy to find them. Like 2 years to go backwards. Make it not worth the hacker's time. What we do instead is HASH their password when they create it and store the hash in our database.

Then we hash it again when they next login and compare the hash values. If the hash's match then initial and current passwords matched. The only person who knows the password is the user themself. As long as we knew the encryption key we're able to encode and decode. Decoding step is not defined for hash functions; that's the whole point of hash functions and making things secure!

## How to Hack Passwords 101
We've reached the level of security that most websites are at. And better than others! Go to [plaintextoffenders.com](plaintextoffenders.com). 

How are big companies getting hacked? They are hashing their passwords. Three of the hashes in a list of four are completely identical. A hacker can look at this table and realized that the hashes were the same. You search by the hash value and match it to the password. Hackers can make hash tables. Create hashes from all possible words. 

- All words from a dictionary (about 150,000)
- All numbers form a telephone book (5mil)
- All combinations of characters up to 6 places (19,770,609,664)

With parallel processing GPUs, you can calculate about 30billion MD5 hashes/second. 

Large hash tables have been built for most common passwords.

Long passwords are the solution! Computation time increases exponentially for longer passwords. 

## Salting Passwords
Hashing and Salting to prevent dictionary attacks or hash table attacks.

**Salting** takes hashing a step further. We take the password, salt it (add some characters to it) and then hash it. The salt isn't something the user has to remember. It's stored in the database along with the hash. We only store the salt and the hash.

We can use another hashing algorithm. `bcrypt` comes into play. Latest and greatest gpus can only calculate 17,000 bcrypt hashes per second (as opposed to 20bil). 

bcrypt has **salt rounds**. We add the same salt form before and hash the hash. The number of times you do this is the number of salt rounds. Every year you can get more computing power for less money. We'll store their hash after a set number of salting rounds.

## Hashing Passwords using Werkzeug
At the moment, the user's password is stored in our database as plaintext.

1. Delete the previous unhashed entry in the database.

Let's secure their password by hashing it before we store it. To do this, we'll use the **Werkzeug** helper function: `generate_password_hash()`.

2. Use the documentation [here](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#module-werkzeug.security) and see if you can figure out how to hash and salt the user's password.

Aim to hash the password using ***pbkdf2:sha256***

And add a salt lenght of **8**.

```py
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)
```

## Authenticating Users with Flask-Login
At the moment, if you simply navigate to `/secrets` you can see the secret page and the download link. There are no authentication barriers. How can we make sure that only registered/logged in users can see that page and download the file?

We'll need to secure certain routes in our server and make them only accessible if a user is authenticated.

To do this, most Flask developers will use the Flask_Login package.

HARD CHALLENGE:

Use the [Flask_Login documentation](https://flask-login.readthedocs.io/en/latest/) to implement the `/login` route. The `/secrets` route should be secured so that it requires the user to be logged in. 

HINT 1: [You will need to configure your Flask app to use Flask_Login](https://flask-login.readthedocs.io/en/latest/#configuring-your-application).

HINT 2: [You will need to create a user_loader function](https://flask-login.readthedocs.io/en/latest/#how-it-works).

HINT 3: Make sure you [implement the UserMixin](https://flask-login.readthedocs.io/en/latest/#your-user-class) in your User class.

Note: A Mixin is simply a way to provide multiple inheritance to Python. This is how you add a Mixin:

`class MyClass(MixinClassB, MixinClassA, BaseClass):`

[Further Reading on Mixins](https://www.thedigitalcatonline.com/blog/2020/03/27/mixin-classes-in-python/)

HINT 4: [You can check the user's password using the check_password_hash function](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#werkzeug.security.check_password_hash).

HINT 5: You need to find the user by the email they entered in the login form.

HINT 6: If the user has successfully logged in or registered, you need to use the login_user() function to authenticate them.

HINT 7: Both the /secrets and /download route need to be [secured](https://flask-login.readthedocs.io/en/latest/#flask_login.login_required) so that only authenticated users can access them.

## Flask Flash Messages

## Passing Authentication Status to Templates