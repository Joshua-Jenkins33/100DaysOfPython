from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(1500))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(1500))
    img_url = db.Column(db.String(500))

    def __repr__(self):
        return '<Movie %r>' % self.title
        
db.create_all()

# new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )

# db.session.add(new_movie)
# db.session.commit()

class RateMovieForm(FlaskForm):
    rating = StringField(label='Your Rating Out of 10 (e.g. 7.5)', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class GetMovieForm(FlaskForm):
    title = StringField(label='Title of the Movie', validators=[DataRequired()])
    submit = SubmitField('Submit')


load_dotenv(r'064_Day_64_My_Top_10_Movies_Website\.env')
API_ACCESS_TOKEN = f"Bearer {os.getenv('API_ACCESS_TOKEN')}"
API_ENDPOINT = 'https://api.themoviedb.org/3'
IMAGE_DB_URL = 'https://image.tmdb.org/t/p/w500'
HEADERS = {
    'Authorization': API_ACCESS_TOKEN,
    'Content-Type': 'application/json;charset=utf-8'
}

def get_movies(title, headers):
    parameters = {
        'query': title
    }
    response = requests.get(url=f"{API_ENDPOINT}/search/movie", headers=headers, params=parameters)
    response.raise_for_status()
    return response.json()['results']


def get_specific_movie(id, headers):
    response = requests.get(url=f"{API_ENDPOINT}/movie/{id}", headers=headers)
    response.raise_for_status()
    print(response.json())

movie_list = []


@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating.desc()).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = i+1
        db.session.commit()  
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        print(f"================{movie.title.upper()} UPDATED WITH NEW RATING OF {movie.rating}================")
        print(f"================{movie.review}================")
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    print(f"================{movie_to_delete.title.upper()} DELETED================")
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = GetMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        movie_list = get_movies(movie_title, HEADERS)
        return render_template('select.html', movies=movie_list)
    return render_template('add.html', form=form)


@app.route("/find")
def find_movie():
    id = request.args.get("id")
    response = requests.get(url=f"{API_ENDPOINT}/movie/{id}", headers=HEADERS)
    response.raise_for_status()
    movie_data = response.json()
    new_movie = Movie(
        title=movie_data["title"],
        year=movie_data["release_date"].split("-")[0],
        img_url=f'{IMAGE_DB_URL+ movie_data["poster_path"]}',
        description=movie_data["overview"]
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)