from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_articles = [Post(blog_post) for blog_post in response.json()]
    return render_template("index.html", articles=all_articles)

if __name__ == "__main__":
    app.run(debug=True)
