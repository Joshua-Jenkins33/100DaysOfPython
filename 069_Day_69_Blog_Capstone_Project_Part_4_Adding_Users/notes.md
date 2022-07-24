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
class User(db.Model):
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

## Requirement 3 - Protect Routes

## Creating Relational Databases

## Requirement 4 - Allow Any User to Add Comments to BlogPosts