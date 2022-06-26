# Day 55: HTML & URL Parsing in Flask and the Higher Lower Game

Diving deeper into web dev with flask and new concepts: how to render HTML for websites using flask and get a hold of parse and the url the user typed in. We'll also look at decorators that take in inputs. 

## Working Flask URL Paths and the Flask Debugger
**Parsing the URL**

### Variable Rules
You can add vairable sections to a URL by marking sections with `<variable name>`. Your function then receives the `<variable_name>` as a keyword argument. Optionally, you can use a converter to specify the type of the argument like `<converter:variable_name>`.

Example: 
```py
@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"
```

\*Note that you need to stop and restart your server to see your updates.

You can set Debug mode **on**. It allows us to activate the debugger, the automatic reloader, and enables debug mode on the Flask application.

`app.run(debug=True)`

Other ways of parsing URLs:
```py
@app.route("/username/<name>/<int:number>")
def greet(name)
    return f"Hello there {name}, you are {number} years old!"

@app.route("/username/<name>/<path:name>")
def greet(name)
    return f"Hello there {name}" # this would print out Angela/1 if you had path username/Angela/1
```

## Rendering HTML Elements with Flask
Right now, we're just returning a string and getting flask to do whatever it wants to with it. Flask accepts html in the return!

```py
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World!</h1>'
```

**Rendering more than 1 html element**
```py
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World!</h1> \
            <p>This is a paragraph.</p> \
            <img src="https://media.giphy.com/media/vMbC8xqhIf9ny/giphy.gif" width=200px>'
```

## Challenge: Use Python Decorators to Style HTML Tags
Create the following decorators to modify the HTML
1. `@make_bold`
2. `@make_emphasis`
3. `@make_underlined`

```py
def make_bold(function):
    def add_b_tags():
        bold_html = f"<b>{function()}</b>"
        return bold_html
    return add_b_tags


def make_emphasis(function):
    def add_em_tags():
        emphasis_html = f"<em>{function()}</em>"
        return emphasis_html
    return add_em_tags


def make_underlined(function):
    def add_u_tags():
        underline_html = f"<u>{function()}</u>"
        return underline_html
    return add_u_tags

@app.route('/bye')
@make_bold
@make_underlined
@make_emphasis
def say_bye():
    return "Bye"
```

## Advanced Decorators with `*args` and `**kwargs`

## Interactive Coding Exercise: Advanced Decorators

## Final Project -- Higher or Lower URLs