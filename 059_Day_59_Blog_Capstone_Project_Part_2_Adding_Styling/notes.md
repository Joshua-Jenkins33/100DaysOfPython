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
The reason why Jinja Templates are called templates is because it makes it easier to create HTML pages by templating. Instead of re-writing the same header/navigation bar/footer you can just create a header and footer template which can then be applied to all web pages in your website. 

`{% include "header.html" %}`

Changeable part of your webpage. e.g. the body of the page.

`{% include "footer.html" %}`


Then when the website is rendered, the `header.html` and `footer.html` gets inserted where the `{% include %}` specifies.

Using the documentation from [Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/#include)

1. Remove the `<head>` & `navigation code` from `index.html` and place it in the `header.html` file.

2. Remove the `<footer>` from `index.html` and place it in the `footer.html` file.

3. Using the above documentation, use `include` to make the website still function exactly the same as before. 

## Step 5: Make the About and Contact Pages Work
Now that you've seen how you can replace the repeatable parts of your website (header/footer), we're going to make the rest of the pages work.

1. Delete the navigation bar item that points to the "Sample Post":

2. Update main.py and the about.html and contact.html files so that when you click on the About link in the navigation bar it goes to the About page and likewise with the Contact page
HINT: Make sure that the anchor tags in the header.html are correctly pointing to the relevant routes in your server.


3. See if you can make the static images work on the About and Contact pages.
HINT: Look at the <header> style attribute. Remember that the images are static files located in the img folder.

*note: I wasn't sure how to pass {{ }} parameters into the in-line stylesheet, as css uses {} as special characters.

## Step 6: Fetch and render the blog posts from an API
Just like our last blog website, we're going to save you the hassle of writing all your blog posts. Instead, you're going to get the posts from our API on npoint.


1. Create your own JSON bin with [npoint.io](https://www.npoint.io/).
Use the attached example blog data to create your own endpoint using npoint.io. 
Your endpoint should be formatted something [like this](https://api.npoint.io/c790b4d5cab58020d391)

2. In main.py get hold of the JSON data at the above API endpoint.

3. Use the data from the API to render the home page, replacing the title, subtitle, author and dates of each blog post with the data from the API.

HINT 1: Instead of using a custom class, you can simply use Jinja variables to use the dot notation instead of square brackets. See: https://jinja.palletsprojects.com/en/2.11.x/templates/#variables

HINT 2: You'll need to use a for loop in the Jinja template, which we've done before. See the documentation here:

https://jinja.palletsprojects.com/en/2.11.x/templates/#for


NOTE: The background image behind the header is [this image](https://images.unsplash.com/photo-1470092306007-055b6797ca72?ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80) that I found from Unsplash, feel free to go to the website to find your own.

[https://unsplash.com/](https://unsplash.com/)


## Step 7: Rendering Individual Posts
The final step is to render each individual post in the post.html page. When a user clicks on a particular post title on the home page (index.html), we should take them to the post.html page where the title/subtitle/image/date/author/body of the post is shown.

You've done this in the previous blog website. See if you can remember how to do it. If you can't remember, look back at the code from Day 55 and see if you can adapt it to this project. After all, programming is just tinkering, it's not an exam, you don't have to memorise everything.

This is what you're aiming for, (this is when I clicked on the cactus post on the home page):
