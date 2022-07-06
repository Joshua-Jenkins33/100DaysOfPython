from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title

db.create_all()

all_books = []


@app.route('/')
def home():
    all_books = db.session.query(books).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        new_book = books(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        db.session.add(new_book)
        db.session.commit()
        print(f"================{request.form['title'].upper()} ADDED================")
        return redirect(url_for('home'))
    return render_template('add.html', methods=["GET", "POST"])

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

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit() 
    print(f"================{book_to_delete.title.upper()} DELETED================")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

