# Day 57: Templating with Jinja in Flask Applications

We effectively don't want a separate html page for each page. We want to use templates. Jinja will help with that.

## Using Jinja to Produce Dynamic HTML Pages
1. Start off with a basic flask server.py file
```py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return "Hello World!"

if __name__ == "__main__":
  app.run(debug=True)
```

2. Create an `index.html` file

### Challenge 1
Create an `<h1>` that reads "Hello World!" inside the `index.html` file. Then use Flask to render the index.html file.

**HTML**
- In addition to the code below, I had to stick the `.html` file into the `templates` directory.
```html
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>My Website</title>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>
```

**PYTHON**
```py
@app.route('/')
def home():
  return render_template("index.html")
```

### Jinja
With Jinja, we can use html files as templates and execute Python code *inside* of the HTML. This is signified by evaluating Python code between double curly braces `{{ <python code> }}`.

This also doesn't need to be installed; it's built in!

```html
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>My Website</title>
  </head>
  <body>
    <h1>Hello World!</h1>
    <h2>{{ 5 * 6 }}</h2>
  </body>
</html>
```

**How would I generate a random number?**
It's best to assign variable and contain your logic inside your python file; not your html one.

**Server.py**
```py
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
  random_number = random.randint(1, 10)
  return render_template("index.html", num=random_number) #**kwargs usage, **contents; we can create as many as we'd like.

if __name__ == "__main__":
  app.run(debug=True)
```

**HTML**
```html
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>My Website</title>
  </head>
  <body>
    <h1>Hello World!</h1>
    <h2>{{ 5 * 6 }}</h2>
    <h3>Random Number: {{ num }}</h3>
  </body>
</html>
```

### Challenge 2
Copyright Text! We're going to make this dynamic with Python.

Add a paragraph element to the index.html file. The paragraph should read something like "Copyright CURRENT_YEAR. Built by YOUR_NAME". Use the datetime module to get the current year along with what you've learned about templating to display the current year inside the paragraph element.

**Python**
```py
from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route('/')
def home():
  random_number = random.randint(1, 10)
  current_year = datetime.date.today().year
  return render_template("index.html", num=random_number, year=current_year)

if __name__ == "__main__":
  app.run(debug=True)
```

**HTML**
```html
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>My Website</title>
  </head>
  <body>
    <h1>Hello World!</h1>
    <h2>{{ 5 * 6 }}</h2>
    <h3>Random Number: {{ num }}</h3>
  </body>
  <footer>
    <p>Copyright {{ year }}. Built by Joshua Jenkins.</p>
  </footer>
</html>
```

## Challenge: Combining Jinja Templating with APIs
Go to [agify.io](agify.io) to estimate the age of a person based on their name.
You can also to go to [genderize](https://genderize.io/) to estimate gender based on their name.

### Acceptance Criteria

- Set up a route to `/guess/some_name`
- Parse the URL to extract the name at the end of the URL
- Create a template and dynamically insert the name from the URL into the HTML
- Make sure the name is in Title Case
- Make two API calls to `genderize.io` and `agify.io` in order to obtain the "gender" and the "age" for the name at the end of the URL
- Insert the result from the API call into the HTML template

```py
from flask import Flask, render_template
import random
import datetime
import requests

GENDERIZE_URL = 'https://api.genderize.io'
AGIFY_URL = 'https://api.agify.io/'

app = Flask(__name__)

def get_copyright_year():
  return datetime.date.today().year

@app.route('/')
def home():
  random_number = random.randint(1, 10)
  return render_template("index.html", num=random_number, year=get_copyright_year())

@app.route('/guess/<string:name>')
def guess(name):
  print(name)
  parameters = {"name": name}
  genderize_response = requests.get(url=GENDERIZE_URL, params=parameters)
  genderize_response.raise_for_status()
  genderize_data = genderize_response.json()
  estimated_gender = genderize_data['gender']

  parameters['country_id'] = 'US'
  agify_response = requests.get(url=AGIFY_URL, params=parameters)
  agify_response.raise_for_status()
  agify_data = agify_response.json()
  estimated_age = agify_data['age']

  # return render_template("index.html", name=name, age=estimated_age, gender=estimated_gender)
  return render_template("index.html", name=name.title(), age=estimated_age, gender=estimated_gender, year=get_copyright_year())


if __name__ == "__main__":
  app.run(debug=True)
```

```html
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>My Website</title>
  </head>
  <body>
    <h1>Hello {{ name }}!</h1>
    <h2>I think you are {{ gender }}.</h2>
    <h3>And maybe {{ age }} years old.</h3>
  </body>
  <footer>
    <p>Copyright {{ year }}. Built by Joshua Jenkins</p>
  </footer>
</html>
```

## Multiline Statements with Jinja
If statements and for loops! We're going to be using Endpoint which acts as a JSON storage bin. Basically so you can create your own APIs.

Here's how you handle a **for loop**
```html
  <body>
    {% for blog_post in posts: %}
      <h1>{{ blog_post["title"] }}</h1>
      <h2>{{ blog_post["subtitle"] }}</h2>
    {% endfor %}
  </body>
```

An **if statement** would look like this:
```html
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else $}
  <h1>Hello, World!</h1>
{% endif %}
```

### Challenge
Only display the blog post that has the id of 2.

```html
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Blog Posts</title>
  </head>
  <body>
    {% for blog_post in posts: %}
      {% if blog_post["id"] == 2 %}
        <h1>{{ blog_post["title"] }}</h1>
        <h2>{{ blog_post["subtitle"] }}</h2>
      {% endif %}
    {% endfor %}
  </body>
  <footer>
    <p>Copyright {{ year }}. Built by Joshua Jenkins</p>
  </footer>
</html>
```

```py
@app.route('/blog')
def blog():
  blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
  response = requests.get(blog_url)
  all_posts = response.json()
  return render_template("blog.html", posts=all_posts, year=get_copyright_year())
```

## URL Building with Flask
On our main homepage we can have a link to the blog's page.

```py
@app.route('/blog')
def get_blog():
  blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
  response = requests.get(blog_url)
  all_posts = response.json()
  return render_template("blog.html", posts=all_posts, year=get_copyright_year())
```

```html
<a href="{{ url_for('get_blog') }}">Go To Blog</a>
```

We can also add numberless keyword arguments to these:
```html
<a href="{{ url_for('get_blog', num=3) }}">Go To Blog</a>
```



## Blog Capstone Project Part 1 - Templating