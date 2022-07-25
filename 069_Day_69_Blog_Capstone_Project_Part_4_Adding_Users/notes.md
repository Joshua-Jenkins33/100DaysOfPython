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
login_user(new_user)
```

3. In the in the `/register` route, if a user is trying to register with an email that already exists in the database then they should be redirected to the `/login` route and a flash message used to tell them to log in with that email instead.

```py
form = RegisterForm()
if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    
    if user is not None:
        flash('You\'ve already registered with this email. Please log in here instead.')
        return redirect(url_for('login'))
```

**login.html**
```html
  {% with messages = get_flashed_messages() %}
    {% if messages %}
        {% for message in messages %}
          <p style="color:red; text-align: center">{{ message }}</p>
        {% endfor %}
    {% endif %}
  {% endwith %}
```

4. In the `/login` route, if a user's email does not exist in the database or if their password does not match the one stored using `check_password()` then they should be redirected back to `/login` and a flash message should let them know what they issue was and ask them to try again. 

```py
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
```

5. Figure out how to update the navbar so that when a user is not logged in it shows:
    - Home / Login / Register / About / Contact

But if the user is logged in / authenticated after registering, then the navbar should show:
  - Home / Log Out / About / Contact


HINT: The navbar code is inside header.html
HINT: [https://flask-login.readthedocs.io/en/latest/#login-example](https://flask-login.readthedocs.io/en/latest/#login-example)

Added `logged_in=current_user.is_authenticated` to most `render_template` returns.

**header.html**
```html
{% if not logged_in: %}
<li class="nav-item">
    <a class="nav-link" href="{{ url_for('login') }}">Login</a>
</li>
<li class="nav-item">
    <a class="nav-link" href="{{ url_for('register') }}">Register</a>
</li>
{% endif %}
{% if logged_in: %}
<li class="nav-item">
    <a class="nav-link" href="{{ url_for('logout') }}">Log Out</a>
</li>
{% endif %}
```

6. Code up the `/logout` route so that when the user clicks on the LOG OUT button, it logs them out and takes them back to the home page. 

```py
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))
```

## Requirement 3 - Protect Routes
In our blog, the first registered user will be the admin. They will be able to create new blog posts, edit posts and delete posts.

1. The first user's `id` is `1`. We can use this in index.html and post.html to make sure that only the admin user can see the "Create New Post" and "Edit Post" and Delete buttons.

**post.html**
```html
{% if current_user.id == 1: %}
    <div class="clearfix">
    <a class="btn btn-primary float-right" href="{{url_for('edit_post', post_id=post.id)}}">Edit Post</a>
    </div>
{% endif %}
```

**index.html**
```html
{% if current_user.id == 1: %}
    <!-- New Post -->
    <div class="clearfix">
    <a class="btn btn-primary float-right" href="{{url_for('add_new_post')}}">Create New Post</a>
    </div>
{% endif %}
```

2. Just because a user can't see the buttons, they can still manually access the /edit-post or /new-post or /delete routes. Protect these routes by creating a Python decorator called `@admin_only`

If the current_user's id is 1 then they can access those routes, otherwise, they should get a 403 error (not authorised).

HINT 1: You might need to review the lessons on Python Decorators on day 54.

HINT 2: See what the @login_required decorator looks like: [https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/#login-required-decorator](https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/#login-required-decorator)

HINT 3: The abort function is quick way to return HTTP errors like 403 or 404: [https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)

```py
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            abort(404, description="You're not supposed to be here.")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/new-post")
@admin_only
def add_new_post():
```

## Creating Relational Databases
Given that the 1st user is the admin and the blog owner. It would make sense if we could link the blog posts they write to their user in the database. In the future, maybe we will want to invite other users to write posts in the blog and grant them the admin privileges.

So we need to create a **relationship** between the `User` table and the `BlogPost` table to link them together. So we can see which BlogPosts a User has written. Or see which User is the author of a particular BlogPost.

If we were just writing Python code, you could imagine creating a `User` object which has a property called `posts` that contains a List of `BlogPost` objects. 

```py
    class User:
        def __init__(self, name, email, password):
             self.name = name
             self.email = email
             self.password = password
             self.posts = []
     
    class BlogPost:
        def __init__(self, title, subtitle, body):
             self.title = title
             self.subtitle = subtitle
             self.body = body
     
    new_user = User(
        name="Angela",
        email="angela@email.com",
        password=123456,
        posts=[
            BlogPost(
                title="Life of Cactus",
                subtitle="So Interesting",
                body="blah blah"
            )
        ]        
    }
```

This would make it easy to find all the BlogPosts a particular user has written. But what about the other way around? How can you find the author of a particular BlogPost object? This is why we're using a database instead of just simple Python data structures.

In relational databases such as SQLite, MySQL or Postgresql we're able to define a relationship between tables using a `ForeignKey` and a `relationship()` method.

e.g. If we wanted to create a One to Many relationship between the User Table and the BlogPost table, where One User can create Many BlogPost objects, we can use the [SQLAlchemy docs](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html) to achieve this. 

**CHALLENGE 1:** See if you can modify the User (Parent) and BlogPost (Child) class code to create a bidirectional One-to-Many relationship between the two tables. You should be able to easily locate the BlogPosts a User has written and also the User of any BlogPost object.

```py
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
db.create_all()

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author = relationship("User", back_populates="posts")
db.create_all()
```

### Re-creating the Database after changes to the Schema
If you re-run your blog at this point you'll get an error:

`OperationalError: (sqlite3.OperationalError) no such column: blog_posts.author_id`

The reason is that our new code in the main.py modifies our database model by adding a new column into our database that was not present in the original `blog.db`  from the starter code:

`author_id = db.Column(db.Integer, db.ForeignKey("users.id"))`

We don't have any valuable data at this point that we'd like to preserve, so the easiest way to simply **delete** the existing blog.db entirely and to use the line `db.create_all()` to re-create all the tables from scratch. Remember, this means you also have to register your user again and create a post since we've just wiped our database. 

Now if you refresh your Blog website, you'll see the author name disappear from the index.html and page.html pages. 

**CHALLENGE 2:** Modify the index.html and post.html pages so that the author name is still displayed in the right places.

HINT: the author property of `BlogPost` is now a `User` object.

```py
@app.route("/new-post", methods=["POST", "GET"]) # had to add the methods
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url, # had to remove author from here as it's not in the form builder at forms.py
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user # had to change to the current user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
```

**index.thml and post.html**
```html
<a href="#">{{post.author.name}}</a> 
```

## Requirement 4 - Allow Any User to Add Comments to BlogPosts
1. Create a `CommentForm` in the form.py file it will only contain a single `CKEditorField` for users to write their comments.

Hint: You might need to check the [documentation](https://flask-ckeditor.readthedocs.io/en/latest/basic.html) or day 67 to see how we implement the CKEditor. 

**main.py**
```py
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        author = current_user
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post, logged_in=current_user.is_authenticated, form=form)
```

**forms.py**
```py
class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
```

**post.html**
```html
{% import "bootstrap/wtf.html" as wtf %}

<!--           Comments Area -->
          <div class="col-lg-8 col-md-10 mx-auto comment">
              <ul class="commentList">
                <li>
                    <div class="commenterImage">
                      <img src="https://pbs.twimg.com/profile_images/744849215675838464/IH0FNIXk.jpg"/>
                    </div>
                    <div class="commentText">
                      <p>Some comment</p>
                      <span class="date sub-text">comment author name</span>
                    </div>
                </li>
              </ul>
            </div>

            {{ ckeditor.load() }}
            {{ ckeditor.config(name='body') }}
            {{ wtf.quick_form(form, novalidate=True, button_map={"submit": "primary"}) }}
```

The next step is to allow users to leave a comment and save the comment. Now that we've seen how relationships can be established between tables in our database. Let's step up our relationships to create a new Table where any user can write comments to our blog posts.

2. Create a Table called `Comment` where the `tablename` is `"comments"`. It should contain an `id` and a `text` property which will be the primary key and the text entered into the CKEditor.

**main.py** -- Adding the comments table.
```py
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
```

3. Establish a One to Many relationship Between the `User` Table (Parent) and the `Comment` table (Child). Where One `User` is linked to Many `Comment` objects. 

```py
# class User(UserMixin, db.Model):
#     __tablename__ = "user"
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(250), nullable=False)
#     password = db.Column(db.String(250), nullable=False)
#     name = db.Column(db.String(250), nullable=False)
#     posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")
# db.create_all()

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.Text, nullable=False)
    comment_author = relationship("User", back_populates="comments")
db.create_all()
```

4. Establish a One to Many relationship between each `BlogPost` object (Parent) and `Comment` object (Child). Where each `BlogPost` can have many associated `Comment` objects.

```py
# class BlogPost(db.Model):
#     __tablename__ = "blog_post"
#     id = db.Column(db.Integer, primary_key=True)
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     subtitle = db.Column(db.String(250), nullable=False)
#     date = db.Column(db.String(250), nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     img_url = db.Column(db.String(250), nullable=False)
#     author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post_comment")
# db.create_all()

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('blog_post.id'))
    text = db.Column(db.Text, nullable=False)
    comment_author = relationship("User", back_populates="comments")
    post_comment = relationship("BlogPost", back_populates="comments")
db.create_all()
```