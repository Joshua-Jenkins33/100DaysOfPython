# Day 64: My Top 10 Movies Website

## What We'll Build

Going to build a website that compiles a list of top favorite movies of all time.

Examples: 

- [British Film Institute](https://www2.bfi.org.uk/greatest-films-all-time)
- [Empire](https://www.empireonline.com/movies/features/best-movies-2/)
- [New York Times](https://www.imdb.com/list/ls058705802/)

Companies exist for the soul purpose of helping build lists of their favorite things. a la [ListChallenges](https://www.listchallenges.com/)

Today, we're going to build a website just like that using Flask/WTForms/SQLite/SQLAlchemy and more. It will allow us to create a beautiful website that lists our top 10 films of all time. As we watch more movies, we can always update our list and keep track of which movies to recommend people.

## Download the Starting Project

Do the download thing.

## Requirement 1 - Be Able to View Movie List Items
1. Create an SQLite database with SQLAlchemy. The database needs to contain a "Movie" Table. This table should contain the following fields:
   - id 
   - title 
   - year 
   - description 
   - rating 
   - ranking
   - review
   - img_url

```py
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(1500))
    rating = db.Column(db.Float(), nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(1500))
    img_url = db.Column(db.String(500))

    def __repr__(self):
        return '<Movie %r>' % self.title
```

2. Using code/DB Viewer, add a new entry to the database with the following values:
```py
new_movie = Movie(
      title="Phone Booth",
      year=2002,
      description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
      rating=7.3,
      ranking=10,
      review="My favourite character was the caller.",
      img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
  )
db.create_all()
```

```py
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
```

HINT: Be sure to remove the add entry code from step 2 after you have run the code once. Otherwise, you'll get a SQLAlchemy Integrity Error.

3. Make the code work so that each entry in the database is displayed correctly on the home page. 

```html
  {% for movie in movies %}
    <div class="card" >
      <div class="front" style="background-image: url('{{ movie.url }}');">
          <p class="large">{{ movie.ranking }}</p>
      </div>
      <div class="back">
        <div>
      <div class="title">{{ movie.title }} <span class="release_date">({{ movie.year }})</span></div>
          <div class="rating">
              <label>{{ movie.rating }}</label>
            <i class="fas fa-star star"></i>
          </div>
            <p class="review">"{{ movie.review}}"</p>
          <p class="overview">
              {{ movie.description }}
          </p>

          <a href="#" class="button">Update</a>
          <a href="#" class="button delete-button">Delete</a>

        </div>
      </div>
    </div>
  {% endfor %}
```

```py
@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)
```

## Requirement 2 - Be Able to Edit a Movie's Rating and Review
There is an edit button on the back of the movie card, you should be able to click on it and change your rating and review.

1. Use what you have learnt about WTForms to create the RateMovieForm. Use this to create a Quick Form to be rendered in edit.html.

NOTE: You don't need to change the code in edit.html, it already has everything you need to render your Quick Form. This is so that students don't just create a simple HTML form.

If you've forgotten how to work with WTForms, you can go back a few lessons and review the content there or just use the documentation:
- [Flask Bootstrap Forms](https://pythonhosted.org/Flask-Bootstrap/forms.html)
- [WTForms](https://wtforms.readthedocs.io/en/2.3.x/)
- [Flask WTF](https://flask-wtf.readthedocs.io/en/stable/)

```html
<a href="{{ url_for('edit', id=movie.id) }}" class="button">Update</a>
```

```py
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
```

2. Once the form is submitted and validated, add the updates to the corresponding movie entry in the database. Here's more documentation on [SQLAchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application)

Accomplished above.

## Requirement 3 - Be Able to Delete Movies from the Database

## Requirement 4 - Be Able to Add New Movies Via the Add Page

## Requirement 5 - Be Able to Sort and Rank the Movies By Rating