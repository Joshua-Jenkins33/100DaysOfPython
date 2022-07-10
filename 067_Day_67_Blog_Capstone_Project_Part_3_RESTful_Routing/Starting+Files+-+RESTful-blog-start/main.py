from venv import create
from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)



@app.route("/post/<int:index>")
def show_post(index):
    exists = db.session.query(BlogPost.id).filter_by(id=index).first() is not None
    if exists:
        requested_post = BlogPost.query.get(index)
        return render_template("post.html", post=requested_post)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a blog with that index."}), 404


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    create_post_form = CreatePostForm()
    if create_post_form.validate_on_submit():
        new_post = BlogPost(
            title=create_post_form.title.data,
            subtitle=create_post_form.subtitle.data,
            date=str(datetime.date.today().strftime("%B %d, %Y")),
            body=create_post_form.body.data,
            author=create_post_form.author.data,
            img_url=create_post_form.img_url.data
        )
        db.session.add(new_post)
        db.session.commit()
        print(f"================BlogPost Added================")
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=create_post_form, post_type="new")


@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    form = CreatePostForm()
    if form.validate_on_submit():
        post_to_edit = BlogPost.query.get(post_id)
        print(post_to_edit)
        post_to_edit.title = form.title.data
        post_to_edit.subtitle = form.subtitle.data
        post_to_edit.author = form.author.data
        post_to_edit.img_url = form.img_url.data
        post_to_edit.body = form.body.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form, post_type="edit")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)


