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
On the back of each movie card there is also a Delete button. Make this button work and allow the movie entry to be deleted from the database. 

```py
@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    print(f"================{movie_to_delete.title.upper()} DELETED================")
    return redirect(url_for('home'))
```

```html
<a href="{{ url_for('delete', id=movie.id) }}" class="button delete-button">Delete</a>
```

## Requirement 4 - Be Able to Add New Movies Via the Add Page
Previously, we added a new entry to our database using either a hard-coded piece of code or the DB Viewer. Now, we need to make the add page work for a user who can't do those things. We should be able to add any film and use an API to fetch the poster image, year of release and movie description.

1. Make the add page render when you click on the Add Movie button on the Home page. The Add page should show a WTF quick form that only contains 1 field - the title of the movie. 

```html
<!-- index.html -->
<div class="container text-center add">
<a href="{{ url_for('add') }}" class="button">Add Movie</a>
</div>
```

```html
<!-- add.html -->
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block styles %}
  {{ super() }}
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito+Sans:300,400,700">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
  <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}

{% block title %}Add Movie{% endblock %}

{% block content %}
<div class="content">
    <h1 class="heading">Add a Movie</h1>
    {{ wtf.quick_form(form, novalidate=True) }}
</div>
{% endblock %}
```

```py
@app.route("/add")
def add():
    form = GetMovieForm()
    movie_title = form.title.data
    return render_template('add.html', form=form)
```

2. When the user types a movie title and clicks "Add Movie", your Flask server should receive the movie title. Next, you should use the requests library to make a request and search The Movie Database API for all the movies that match that title. 
  - You will need to sign up for a free account on The Movie Database.
  - Then you will need to go to Settings -> API and get an API Key. Copy that API key into your project. 
  - You will need to read [the documentation](https://developers.themoviedb.org/3/search/search-movies) on The Movie Database to figure out how to request for movie data by making a search query.

HINT 1: The "Try it out" tab on the API docs is particularly useful to see the structure of the request and the data you can expect to get back.

HINT 2: We covered how to make API requests a long time ago on Day 33, it might be worth reviewing the knowledge there if you get stuck.
   - Using the data you get back from the API, you should render the select.html page and add all the movie title and year of release on to the page. This way, the user can choose the movie they want to add. There are usually quite a few movies under similar names. 

**add.html**
```html
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block styles %}
  {{ super() }}
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito+Sans:300,400,700">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
  <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}

{% block title %}Add Movie{% endblock %}

{% block content %}
<div class="content">
    <h1 class="heading">Add a Movie</h1>
    {{ wtf.quick_form(form, novalidate=True) }}
</div>
{% endblock %}
```

**select.html**
```html
    {% for movie in movies %}
      <p>
        <a href="#"> {{ movie.title }} - {{ movie.release_date }}</a>
      </p>
    {% endfor %}
```

**index.html**
```html
<a href="{{ url_for('add') }}" class="button">Add Movie</a>
```

```py
class GetMovieForm(FlaskForm):
    title = StringField(label='Title of the Movie', validators=[DataRequired()])
    submit = SubmitField('Submit')


load_dotenv(r'064_Day_64_My_Top_10_Movies_Website\.env')
API_ACCESS_TOKEN = f"Bearer {os.getenv('API_ACCESS_TOKEN')}"
API_ENDPOINT = 'https://api.themoviedb.org/3/search/movie'


def get_movies(title):
    headers = {
        'Authorization': API_ACCESS_TOKEN,
        'Content-Type': 'application/json;charset=utf-8'
    }
    parameters = {
        'query': title
    }
    response = requests.get(url=API_ENDPOINT, headers=headers, params=parameters)
    response.raise_for_status()
    print(response.json())
    return response.json()['results']


movie_list = []

@app.route("/add", methods=["GET", "POST"])
def add():
    form = GetMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        movie_list = get_movies(movie_title)
        return render_template('select.html', movies=movie_list)
    return render_template('add.html', form=form)
```

3. Once the user selects a particular film from the select.html page, the id of the movie needs to be used to hit up another path in the Movie Database API, which will fetch all the data they have on that movie. e.g Poster image URLs.
   - Use the id of the movie that the user selected to make a request to the get-movie-details path.

https://developers.themoviedb.org/3/movies/get-movie-details

The data you get back from the API should be used to populate the database with the new entry. The properties you will populate are:
- title
- img_url
- year
- description

Once the entry is added, redirect to the home page and it should display the new movie as a card. Some data will be missing, that's ok.

```py
def get_specific_movie(id, headers):
    response = requests.get(url=f"{API_ENDPOINT}/movie/{id}", headers=headers)
    response.raise_for_status()
    print(response.json())

movie_list = []


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
    return redirect(url_for("home"))
```

**select.html**
```html
    {% for movie in movies %}
      <p>
        <a href="{{ url_for('find_movie', id=movie.id) }}"> {{ movie.title }} - {{ movie.release_date }}</a>
      </p>
    {% endfor %}
```

4. Instead of redirecting to the home page after finding the correct film, redirect to the edit.html page. Because the parts of the movie entry that are missing are the rating and review. The form on the edit page will contain these two fields. Update the movie entry in the database with this new data.


## Requirement 5 - Be Able to Sort and Rank the Movies By Rating

At the moment the front of the movie card says None in large letters.

Instead, we want it to display the ranking of the movie according to our rating. e.g.

If we gave The Matrix a rating of **9.2** and Spirited Away was rated **9.5** and those are the only 2 movies we've added then it should display..

If we add another movie and it had the highest rating among the movies, then it should be ranked according to it's rating.

e.g. If Matrix (9.3), Spirited Away (9.5), Parasite (9.9)

But if we edit the rating so that it becomes: Matrix (9.3), Spirited Away (9.5), Parasite (8.9)

Then this is what should happen:

HINT 1: https://docs.sqlalchemy.org/en/13/orm/query.html#sqlalchemy.orm.query.Query.order_by

HINT 2: You don't need to change any code in index.html

HINT 3: You only need to change the code in the home() function.

```py
@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating.desc()).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = i+1
        db.session.commit()  
    return render_template("index.html", movies=all_movies)
```