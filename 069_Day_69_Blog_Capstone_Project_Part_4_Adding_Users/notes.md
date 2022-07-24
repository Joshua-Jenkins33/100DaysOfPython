# Day 69: Blog Capstone Project Part 4 — Adding Users
Wouldn't it be great if we could have some users on our blog? What if we could let anyone sign up and comment on our blog posts? In order for that to work, we would need to add authentication to our blog. This will be the final step in our Blog Capstone Project. Once we're done, it will be a fully-fledged blog website that you can publish and launch. 

## Download the Starting Project
1. Download the starting .zip files from this lesson (Starting Files - blog-with-users-start.zip).
2. Unzip and open the project in PyCharm.
3. Make sure that the required packages (imports) are all installed and there are no red underlines.
   - The starting files consists of an SQLite database called blog.db, I created this in the same way we created databases before.
4. Take a look a the database using DB Viewer and familiarise yourself with the fields in the database.
5. Run the app and navigate around using the buttons and navigation bar. All the HTML pages should already render correctly. The login/register forms won't work of course. Look through all the code and make sure that everything makes sense before you get started.

## Requirement 1 - Register New Users
1. Use what you've learnt yesterday to allow users to go to the `/register` route to sign up to your blog website. You should create a WTForm in **forms.py** called `RegisterForm` and use Flask-Bootstrap to render a wtf quick_form.

The data the user entered should be used to create a new entry in your **blog.db** in a `User` table. 

```py
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
db.create_all()
```

HINT 1: You don't need to change anything in register.html

HINT 2: Don't worry about Flask-Login yet, you are just creating a new user in the database. We'll log them in in the next step.

```py
@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            email = form.email.data,
            password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8),
            name = form.name.data
        )
        db.session.add(new_user)
        db.session.commit()
        print(f"================USER {form.name.data.upper()} REGISTERED================")
        return redirect(url_for('get_all_posts'))

    return render_template("register.html", form=form)
```

## Requirement 2 - Login Registered Users
1. Users who have been successfully registered (added to the user table in the database) should be able to go to the `/login` route to use their credentials to log in. You will need to review the [Flask-Login docs](https://flask-login.readthedocs.io/en/latest/) and the lessons from yesterday to be able to do this.

### forms.py
```py
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")
```

### main.py
```py
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(str(id))

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if user is not None:
            valid_credentials = check_password_hash(user.password, password)
            if valid_credentials:
                login_user(user)
                flash('Logged in successfully.')
                return redirect(url_for('get_all_posts'))
            else:
                flash('Authentication failed; password was incorrect.')
        else:
            flash('Authentication failed, user doesn\'t exist.')
    return render_template("login.html", form=form)
```

2. Add 1 line of code in the `/register` route so that when users successfully register they are taken back to the home page and are logged in with Flask-Login.

```py

```

3. In the in the `/register` route, if a user is trying to register with an email that already exists in the database then they should be redirected to the `/login` route and a flash message used to tell them to log in with that email instead.

```py

```

4. In the `/login` route, if a user's email does not exist in the database or if their password does not match the one stored using `check_password()` then they should be redirected back to `/login` and a flash message should let them know what they issue was and ask them to try again. 

```py

```

5. Figure out how to update the navbar so that when a user is not logged in it shows:
    - Home / Login / Register / About / Contact

But if the user is logged in / authenticated after registering, then the navbar should show:
  - Home / Log Out / About / Contact


HINT: The navbar code is inside header.html
HINT: [https://flask-login.readthedocs.io/en/latest/#login-example](https://flask-login.readthedocs.io/en/latest/#login-example)

```py

```

6. Code up the `/logout` route so that when the user clicks on the LOG OUT button, it logs them out and takes them back to the home page. 

```py

```

## Requirement 3 - Protect Routes

## Creating Relational Databases

## Requirement 4 - Allow Any User to Add Comments to BlogPosts