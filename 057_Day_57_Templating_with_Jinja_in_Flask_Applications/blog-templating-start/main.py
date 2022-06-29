from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

def get_articles():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_articles = [Post(blog_post) for blog_post in response.json()]
    return all_articles

@app.route('/')
def home():
    
    return render_template("index.html", articles=get_articles())

@app.route('/post/<int:blog_id>')
def full_article(blog_id):
    for article in get_articles():
        if article.id == blog_id:
            return render_template("post.html", article=article)


if __name__ == "__main__":
    app.run(debug=True)
