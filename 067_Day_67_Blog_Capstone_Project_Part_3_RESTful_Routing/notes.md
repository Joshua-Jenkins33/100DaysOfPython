# Day 67: Advanced—Blog Capstone Project Part 3 -- RESTful Routing

## Goals: Building a RESTful Blog with Editing!
Using the knowledge we've gained, we're going to take our blog even further. We'll add more HTTP routes so that you can create new blog posts, edit posts and delete posts. All inside your blog website. 

## Download the Starting Project

- [x] Do the things; downloads, library installs, etc

## Requirement 1 - Be Able to GET Blog Post Items
Instead of getting hold of blog posts from the npoint JSON bin, grab the posts from the posts.db SQLite database that's included in the starting project.

NOTE: In the starting files, the `requests.get()` method call is commented out. This means that the home page (index.html) will not load when you run the app. It will crash because `posts` doesn't exist.

This is what you should see when you are reading the blog posts from the posts.db: (all three posts)

And this is what you should see when you click on one of the individual posts: (should take you to the post's individual page)

```py
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
```

I also had to cut out the following:
```html
<a class="btn btn-primary float-right" href="{{url_for('edit_post', post_id=post.id)}}">Edit Post</a>
```

## Requirement 2 - Be Able to POST a New Blog Post
Create a new POST route called `/new-post` in your Flask server.

1. It should render the make-post.html page when you click on the "Create New Post" button.

You will need to figure out how to use the Flask CKEditor package to make the Blog Content (`body`) input in the WTForm into a full CKEditor.

Useful Docs:

[https://flask-ckeditor.readthedocs.io/en/latest/basic.html](https://flask-ckeditor.readthedocs.io/en/latest/basic.html)

[https://pythonhosted.org/Flask-Bootstrap/forms.html](https://pythonhosted.org/Flask-Bootstrap/forms.html)

[https://flask-wtf.readthedocs.io/en/stable/](https://flask-wtf.readthedocs.io/en/stable/)

Hint 1: Every time you make changes in the Jinja2 Templating of an HTML file, you will need to stop and re-run your server for the changes to happen.

```py
@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    create_post_form = CreatePostForm()
    return render_template("make-post.html", form=create_post_form)
```

```html
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block content %}
{% include "header.html" %}
  <!-- Page Header -->
  <header class="masthead" style="background-image: url('{{ url_for('static', filename='img/edit-bg.jpg')}}')">
    <div class="overlay"></div>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <div class="page-heading">
            <h1>New Post</h1>
            <span class="subheading">You're going to make a great blog post!</span>
          </div>
        </div>
      </div>
    </div>
    {{ ckeditor.load() }}
  </header>

  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        
          <!-- This is where the form will go -->
          {{ wtf.quick_form(form, novalidate=True, button_map={"submit": "primary"}) }}
      </div>
    </div>
  </div>

{% include "footer.html" %}
{% endblock %}
```

Note: If you want the Submit Post button to be blue instead of white, simply add a button_map parameter to the wtf quickform and make the submit field a Bootstrap "primary" button.

[Docs](https://pythonhosted.org/Flask-Bootstrap/forms.html#form-macro-reference)
[Bootstrap Primary Button](https://getbootstrap.com/docs/4.0/components/buttons/)

```html
{{ wtf.quick_form(form, novalidate=True, button_map={"submit": "primary"}) }}
```

2. When the user is done typing out entries to all the fields, the data in the form should be saved as a `BlogPost` Object into the posts.db

Once the post is saved, the user should be redirected to the home page and the new post should show up if the saving process was successful.

Note: the date field is not in the WTForm, because the date should be automatically calculated using the datetime module in the server. The date needs to be formatted like this:

August 31, 2019

`<full month name> <date number>, <full year>`

[Docs](https://www.w3schools.com/python/python_datetime.asp)

NOTE: The data from the CKEditorField is saved as HTML. It contains all the structure and styling of the blog post. In order for this structure to be reflected when you go to the post.html page for the blog post, you need to add a [Jinja safe() filter](https://jinja.palletsprojects.com/en/2.11.x/templates/#safe).

This makes sure that when Jinja renders the post.html template, it doesn't treat the HTML as text.

To apply a Jinja filter, you need the pipe symbol "|" and this goes between the Jinja expression and Jinja filter.

e.g. `{‌{ Jinja expression | Jinja filter }}`

## Requirement 3 - Be Able to Edit Existing Blog Posts


























## Requirement 4 - Be Able to DELETE Blog Posts