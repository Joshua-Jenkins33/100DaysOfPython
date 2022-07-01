# Day 59: Blog Capstone Project: Part 2 - Adding Styling

## What We're Making
Previously we've built a simple blog with simple CSS styling. It had no fancy animations and was not mobile responsive. Now that we've learnt all about Bootstrap and how much time it can save us, we're going to upgrade our blog with the power of Bootstrap.

The best part? We don't even have to write the Bootstrap code.

### Bootstrap Templates

On the internet, there are hundreds of thousands of free Bootstrap templates. Beautifully designed websites using Bootstrap that are ready to go. All we need is to understand how Bootstrap works (Day 58) and then we can simply customise these beautiful websites for our own purposes.

e.g.
- [bootstrapmade](https://bootstrapmade.com/)
- [getbootstrap](https://getbootstrap.com/docs/4.0/examples/)
- [creative-tim](https://www.creative-tim.com/bootstrap-themes/free)

### What You Will Build
By the end of today, you will build a blog website with these features:
- multi-page website with an interactive navigation bar
- dynamically generated blog post pages with full screen titles
- Fully mobile-responsive with an adaptive navigation bar

## Step 1: Download the Starting Project
1. Head over to Start Bootstrap's website and download the [Clean Blog Template](https://startbootstrap.com/previews/clean-blog/)
2. Unzip the downloaded file and rename the folder to "upgraded blog"
3. Open the project folder and:
  - Create the static and template folders
  - Move the files in the project to the correct folders (HTML files to templates and all folders to static)
  - Delete the mail folder. We're going to be coding up the functionality from scratch
  - Create a header.html and footer.html file and the all important main.py
  - Check that your file structure looks like the image included in the course

## Step 2: Get the Home Page to Work
Use what you have learnt about Flask, get the home page to render when you go to

http://localhost:5000

in your browser.

Don't worry about styling yet.

```py
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

## Step 3: Fix the Header and Footer
Notice that at the moment the styling is completely missing. This is because the static files (CSS/JS/images etc.) are served up by our server and they are no longer at the locations specified in the header.

1. Fix the header in index.html so that the styling and bootstrap all appear. 

Note: it's usually a good idea to build a dynamic url for the static resources instead of just pointing to the static folder. See the documentation [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files).

2. Fix the footer resources so that the Javascript works. You can verify this by checking that when you scroll the navigation bar becomes sticky at the top and changes background color

## Step 4: Using Jinja Include to Render Templates

## Step 5: Make the About and Contact Pages Work

## Step 6: Fetch and render the blog posts from an API

## Step 7: Rendering Individual Posts