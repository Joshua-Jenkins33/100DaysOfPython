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

  return render_template("guess.html", name=name.title(), age=estimated_age, gender=estimated_gender, year=get_copyright_year())

@app.route('/blog/<int:id>')
def get_blog(id):
  print(id)
  blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
  response = requests.get(blog_url)
  blog_post = response.json()[id]
  return render_template("blog.html", post=blog_post, year=get_copyright_year())

if __name__ == "__main__":
  app.run(debug=True)
