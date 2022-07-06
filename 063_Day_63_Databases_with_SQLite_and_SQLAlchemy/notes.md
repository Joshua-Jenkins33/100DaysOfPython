# Day 63: Advanced - Databases with SQLite and SQLAlchemy

## Day 63: Creating a Virtual Bookshelf
Have you ever wanted to keep track of the books you have read and give each book a rating?

This is not a new concept and there are plenty of [companies](https://www.librarything.com/) that have built something for exactly this purpose.

But in order to do this, we will need to learn how to use a database. By the end of today, you will have learnt how to create an SQLite database and how to create, read, update and delete data in the database.

We'll also be hooking up our database with a Flask application to serve data whenever needed.

So buckle up and head over to the next lesson!

## Download the Starting Project

- [x] Download project and `pip install` requirements.

## Make the Website Work

Code up the main.py `index.html` and `add.html` so that the following requirements are met:

### CHALLENGE 1

- [x] When you head over to http://locahost:5000 (or whatever shows up as your URL when you run main.py), you should have a `<h1>` that says **My Library** and link `<a>` to Add New Book.

```py
@app.route('/')
def home():
    return render_template('index.html')
```

### CHALLENGE 2

- [x] When you head over to the /add path, e.g. http://locahost:5000/add you should see a form like the one below:

```py
@app.route("/add")
def add():
    return render_template('add.html')
```

### CHALLENGE 3
- [x] Make the form on the /add path work so that when you click "Add Book" the book details gets added as a dictionary to the list called `all_books` in `main.py`.
  - The data structure of all_books should be a List of Dictionary objects. e.g 

```py
    all_books = [
         {
            "title": "Harry Potter",
            "author": "J. K. Rowling",
            "rating": 9,
        }
    ]
```

**Challenge Code**
```py
@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        all_books.append({"title": title, "author": author, "rating": rating})
        print(all_books)
        return '<h1>Book Submitted!</h1><br><a href="/">Return Home</a>'
    return render_template('add.html', methods=["GET", "POST"])
```

```html
    <form action="{{ url_for('add') }}" method="POST">
        <label>Book Name</label>
        <input type="text" name="title">
        <label>Book Author</label>
        <input type="text" name="author">
        <label>Rating</label>
        <input type="text" name="rating">
        <button type="submit" value="Submit">Add Book</button>
    </form>
```

### Challenge 4
- [x] Make the home page show each of the books in `all_books` as a list item `<li>` in an unordered list `<ul>`

```py
@app.route('/')
def home():
    return render_template('index.html', books=all_books)
```

```html
    <ul>    
        {% for book in books %}
            <li>{{ book.title }} — {{ book.author }} — {{ book.rating }}/10</li>
        {% endfor %}
    </ul>
```

### Challenge 5
- [x] Make the home page show `<p>Library is empty.</p>` if there are no books. Also, make sure the `"Add New Book"` link works and takes the user to the `/add` page.

Hint: If there are no books then `all_books = []`

```html
<h1>My Library</h1>
{% if books|length == 0 %}
    <p>Library is empty.</p>
{% else %}
    <ul>    
        {% for book in books %}
            <li>{{ book.title }} — {{ book.author }} — {{ book.rating }}/10</li>
        {% endfor %}
    </ul>
{% endif %}
<a href="/add">Add New Book</a>
```

## What Happens When You Refresh the Server?
Add a few books to your website. You should see them listed on the home page. 

Stop your server and run it again.

Go to your website and reload the home page. What do you see? What happened to your books?

This is because our books are currently stored in the List `all_books`, this variable gets re-initialised when we re-run `main.py` and all the data inside is lost.

If this happened to our user's data, they would not have much faith in our website.

In order to fix this, we need to learn about data persistence and how to work with databases in Flask applications.

## SQLite Databases
First, let's create a database. The most used database in the world is SQLite. It's so popular that it's included by default in all Python installations, so if you're creating a Python project, you've already got it installed. We're going to create an SQLite database to store our book data.

1. Create a new project and inside the `main.py` file import the `sqlite3` module. 
2. Now create a connection to a new database (if the database does not exist then it will be created).
   - `db = sqlite3.connect("books-collection.db")`
3. Run `main.py` and you should see a new file appear in PyCharm called `books-collection.db`

NOTE: Don't try to open the `.db` file in PyCharm, it won't work, I'll show you how to download the software to open these files a little later.

4. Next we need to create a **cursor** which will control our database. 
    - `cursor = db.cursor()`

So a cursor is also known as the mouse or pointer. If we were working in Excel or Google Sheet, we would be using the cursor to add rows of data or edit/delete data, we also need a cursor to modify our SQLite database.

### Creating Tables in our Database
Coming back to the Excel analogy, a single Excel file can contain many tables (sheets), each tab is a different table. 

Similarly, our database can contain many tables. 

5. Let's create one. Add this code below all the previous lines.

```py
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
```

Let's break this down.

`cursor` - We created this in step 4 and this is the mouse pointer in our database that is going to do all the work.

`.execute()` - This method will tell the cursor to execute an action. All actions in SQLite databases are expressed as SQL (Structured Query Language) commands. These are almost like English sentences with keywords written in ALL-CAPS. There are [quite a few SQL commands](https://www.codecademy.com/articles/sql-commands). But don't worry, you don't have to memorise them.

`CREATE TABLE` -  This will create a new table in the database. The name of the table comes after this keyword.

[Docs](https://www.w3schools.com/sql/sql_ref_create_table.asp)

`books` - This is the name that we've given the new table we're creating.

`()` - The parts that come inside the parenthesis after CREATE TABLE books ( ) are going to be the fields in this table. Or you can imagine it as the Column headings in an Excel sheet.

`id INTEGER PRIMARY KEY` -  This is the first field, it's a field called "`id`" which is of data type `INTEGER` and it will be the `PRIMARY KEY` for this table. The primary key is the one piece of data that will uniquely identify this record in the table. e.g. The primary key of humans might be their passport number because no two people in the same country has the same passport number.

`title varchar(250) NOT NULL UNIQUE` - This is the second field, it's called "`title`" and it accepts a variable-length string composed of characters. The 250 in brackets is the maximum length of the text. `NOT NULL` means it must have a value and cannot be left empty. `UNIQUE` means no two records in this table can have the same title. 

`author varchar(250) NOT NULL` - A field that accepts variable-length Strings up to 250 characters called `author` that cannot be left empty.

`rating FLOAT NOT NULL` - A field that accepts FLOAT data type numbers, cannot be empty and the field is called `rating`.

6. Run the code from step 5 and there will be no noticeable changes. In order to view our database we need to download some specialised software.

Head over to [this link](https://sqlitebrowser.org/dl/) and download DB Browser for your operating system. (If you are on Windows go for the Standard Installer).

7. Once you've downloaded and installed DB Browser, open it and click on "Open Database".

8. Navigate to your project location (it should in a folder called PyCharm Projects) and open the books-collection.db
  
Now you should see a table called books that contains 4 fields:
- id
- title
- author
- rating

This is our database. 

9. To add data to our table we can head back to main.py and write the following code:

```py    
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
```

This will create a new entry in our books table for the Harry Potter book and commit the changes to our database.

10. Now comment out the previous line of code where you are created the table called books. Otherwise, you'll get `sqlite3.OperationalError: table books already exists.`

11. Then close down the database in DB Browser by clicking Close Database. Otherwise, you'll get a warning about `database locked` when you work with the database in PyCharm.

12. Now run the code in main.py and re-open the database in DB Browser to see the updated books table. it should include the Harry Potter record.

SQL queries are very sensitive to typos. If instead of writing:

```py
    cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
    db.commit()
```

You wrote:

```py
    cursor.execute("INSERT INTO books VALUE(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
    db.commit()
```

Then it won't work at all (can you even spot the difference in the code?) -- **it's missing an *S* in *VALUES***

Luckily, there are much better ways of working with SQLite in Python projects, we can use a tool called SQLAlchemy to write Python code instead of all these error-prone SQL commands. That's what we'll do in the next lesson!


## SQLAlchemy
SQL commands in Python are complicated and error-prone. SQLAlchemy was created to help us just write Python code and get the compiler to help us spot typos and errors. It's defined as an Object Relation Mapping (ORM) library. It's able to map relationships in the database into Objects. Fields become Object properties. Tables can be defined as separate Classes and each row of data is a new Object. 

1. Comment out all the existing code where we create an SQLite database directly using the sqlite3 module.
2. Install the required packages **flask** and **flask_sqlalchemy** and import the `Flask` and `SQLAlchemy` classes from each.
  - `from flask import Flask`
  - `from flask_sqlalchemy import SQLAlchemy`

### CHALLENGE
Use the [SQLAlchemy documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/) to figure out how to do everything we did in the commented out code but this time using SQLAlchemy.

**Requirements**
- Create an SQLite database called **new-books-collection.db**

- Create a table in this database called **books**.

- The **books** table should contain 4 fields: id, title, author and rating. The fields should have the same limitations as before e.g. INTEGER/FLOAT/VARCHAR/UNIQUE/NOT NULL etc.

- Create a new entry in the books table that consists of the following data:
  - id: 1
  - title: 'Harry Potter'
  - author: 'J.K. Rowling'
  - review: 9.3


HINT 1: The URL for your database should be `"sqlite:///new-books-collection.db"`
HINT 2: Don't if you get a deprecation warning in the console that's related to SQL_ALCHEMY_TRACK_MODIFICATIONS

You can silence it with `app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False`

HINT 3: You can always check the database using DB Browser.

## CRUD Operations with SQLAlchemy

### Summary

#### Create a New Database
```py
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///<name of database>.db"
    db = SQLAlchemy(app)
```

#### Create a New Table
```py
    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        author = db.Column(db.String(250), nullable=False)
        rating = db.Column(db.Float, nullable=False)
     
    db.create_all()
```

---

In addition to these things, the most crucial thing to figure out when working with any new database technology is how to **CRUD** data records. 

**C**reate

**R**ead

**U**pdate

**D**elete

### Create a New Record
```py
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
```

NOTE: When creating new records, the primary key fields is optional. The `id` field will be auto-generated. 

### Read All Records
```py
    all_books = session.query(Book).all()
```

### Read a Particular Record by Query
```py
    book = Book.query.filter_by(title="Harry Potter").first()
```

### Update a Particular Record by Query
```py
    book_to_update = Book.query.filter_by(title="Harry Potter").first()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()  
```

### Update a Record by Primary Key
```py
    book_id = 1
    book_to_update = Book.query.get(book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()  
```

### Delete a Particular Record by Primary Key
```py
    book_id = 1
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
```

You can also delete by querying for a particular value e.g. by title or one of the other properties.

## Build a SQLite Database into the Flask Website
You're going to build an SQLite database into the Flask Website we built at the beginning of today. So that any books added are stored in the database and you're also going to build in some extra features to take advantage of the full CRUD features of our database.

### Requirements
- [x] You should be able to add new books via the /add route, once a book is successfully added to the database, it should redirect to the home page.
- [x] The home page should show all the books in the database:
- [x] Add an Edit Rating Anchor Tag to each book `<li>`. When the button is pressed, it should take the user to an Edit Rating page where you can enter a new rating for that book. Then when you click "Change Rating" it should take you back to the home page and the new rating should be displayed next to the book. e.g.
  - HINT: You'll need to think about how to pass the book id as a parameter when you make the GET request to show the edit rating page. There are many ways you can do this. Here are some things that might help:
  - [URL Building](https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building)
  - [Named Parameters from a URL with Flask](https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask)
- [x] Add a Delete Anchor Tag to each book listing `<li>`. When clicked it should delete the book from the database and redirect back to the home page. e.g.

#### Edit Page
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Edit Rating</title>
</head>
<body>
    <form action="{{ url_for('edit') }}" method="POST">
        <p> Book Name: {{ book.title }}</p>
        <p>Book Author: {{ book.author }}</p>
        <input hidden="hidden" name="id" value="{{ book.id }}"
        <label>Rating</label>
        <input type="text" name="rating" placeholder="New Rating">
        <a href="{{ url_for('home') }}">
          <button type="submit" value="Submit">Change Rating</button>
        </a>
    </form>
</body>
</html>
```

```py
@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        book_id = request.form['id']
        book_to_update = books.query.get(book_id)
        new_rating = request.form['rating']
        book_to_update.rating = new_rating
        db.session.commit() 
        print(f"================{book_to_update.title.upper()} UPDATED WITH NEW RATING OF {book_to_update.rating}================")
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = books.query.get(book_id)
    return render_template('edit.html', methods=["GET", "POST"], book=book_selected)

```

### Delete Page
```py
@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit() 
    return redirect(url_for('home'))
```

```html
        {% for book in books %}
            <li>
                {{ book.title }} — {{ book.author }} — {{ book.rating }}/10  
                <a href="{{ url_for('edit', id=book.id) }}">Edit Rating</a>
                <a href="{{ url_for('delete', id=book.id) }}">Delete</a> 
            </li>
        {% endfor %}
```