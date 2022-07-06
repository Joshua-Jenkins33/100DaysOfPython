from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

all_books = []

@app.route('/')
def home():
    return render_template('index.html', books=all_books)


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

if __name__ == "__main__":
    app.run(debug=True)

