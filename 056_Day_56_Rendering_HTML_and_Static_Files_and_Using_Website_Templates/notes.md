# Day 56: Rendering HTML/Static Files and Using Website Templates
Web development with Flask. Going to static files (local images and videos) and render HTML and CSS files.

## Rendering HTML Files with Flask

### Challenge 1
Write the starter code for a Flask application that shows the text "Hello World" for the home route.

```py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello there'

if __name__ == "__main__":
    app.run()
```

The next step is how we can render and HTML page rather than returning strings or small bits of html elements.

1. Make a new html file.
2. Place file in `templates` directory
- Checkout the **Rendering Templates** section on the Flask documentation. It is a *Framework* not a *library* so it will place certain restrictiosn and requirements on your code so that it will actually work. It requires the templates to exist in a `templates` directory.
3. Import `from flask import Flask, render_templates`
4. `return render_template()`

### Challenge 2
Use Flask to render the html file from your own cv website from days 41 & 42 as a template (If you don't have it, download the sample from the course resources). Ignore any images for now. We'll tackle rendering images in the next lesson.

```py
from flask import Flask, render_template
app = Flask(__name__)
print("Hi")
print(app)


@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

## Serving Static Files using FLask
Why aren't images loading? Back to the documentation.

Flask will look for all your static files (CSS, images, etc) in a folder called `static`.

### Challenge 3
Create a `styles.css` file. Use the stylesheet to change the background-color of the `<body>` to purple. Remember to link your html and css files.

#### HTML
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Site Title</title>
    <link rel="stylesheet" href="../static\styles.css">
  </head>
  <body>
    <h1>I'm NAME</h1>
  </body>
</html>
```

#### CSS
```css
body {
  background-color: purple;
}
```

#### Python
```py
from flask import Flask, render_template
app = Flask(__name__)
print("Hi")
print(app)


@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

## How to Use Website Templates to Speed Up Web Development

### Challenge 4
Use your personal site project from the end of day 44 and render it using Flask, complete with images and styling. If you don't have the files, download the sample from the course resources.

- [x] Moved images to `static` folder
- [x] Updated templates `index.html`
- [x] Changed image paths

Transition was pretty easy!

We can also get templates of HTML and CSS from the website like from [html5up.net](html5up.net).

How do we make this work with Python? Download the template. We need to attribute the designer who created the design (you can pay to not have to attribute it). Squarspace costs $10+ per month if you don't know how to make your own website.

We're going to transfer these files to our files to our website. We're going to delete all the files from `static` and `templates` folders.

We want to get this HTML to work when it's being served up by our server.

...It's got all of the HTML but no images / styling. Probably because we're not referencing the `static` folder. Replace `assets` and `images` with `static`.

**How would you edit this?** Easiest way -- edit the raw HTML.

We can go to the `console` tab in the debugger and type `document.body.contentEditable=true` I can close down the pane. I can now edit anything on the website in the web browser. I can select any part of the html elements that I didn't like and delete it.

Refreshing removes all of your changes. That's because it's reloaded with the code contained in your server project.

## Final Project - Name Card Website Template
We're going to be using one of the templates on HTML 5 Up to create a web-based name card. Like the old-school paper ones, but better.

1. Download html5up's "Identity" template from this lesson's resources (PS: you can also browse the live demo sites on https://html5up.net/ and use a different template like "Astral" or "Ethereal"...)
- [x] Donezo

2. Create a new PyCharm project called name-card and create a new Flask Application from scratch.
- [x] Oops. Overwrote my previous stuff. 
- [x] Recreate my old website with Flask

3. Create the necessary folders and move the relevant files from the download in step1.
- [x] Donezo

4. Get the website to work when you access the root route ("/")
- [x] Yep

5. Personalise the website, change the background image, change the text, change the links, make it your own.
- [x] Change the Background Image
- [x] Change the text
- [ ] Change the links
- [ ] Make it Your Own

## Solution and Walkthrough for the Name Card Final Project

You can use [unsplash.com](unsplash.com) for beautiful pictures for commercial use.