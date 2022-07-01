from flask import Flask, render_template, url_for
import datetime
import requests

BLOG_API_ENDPOINT = 'https://api.npoint.io/59dfc431a83b143abbf9'


response = requests.get(url=BLOG_API_ENDPOINT)
response.raise_for_status()
blog_data = response.json()
print(blog_data)

app = Flask(__name__)

def get_copyright_year():
  return datetime.date.today().year

@app.route('/')
def home():
    return render_template("index.html", year=get_copyright_year(), blog_posts=blog_data)

@app.route('/contact')
def contact():
    return render_template("contact.html", year=get_copyright_year())

@app.route('/about')
def about():
    return render_template("about.html", year=get_copyright_year())

@app.route('/blog-post/<int:id>')
def blog_post(id):
    return render_template("post.html", post=blog_data[id-1])


if __name__ == "__main__":
    app.run(debug=True)