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
The above was pretty easy because we weren't taking in any other conditions or passing parameters. We were just calling the function inside the decorator.

We want to simulate a case where we have user objects:
```py
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")
```

Certain methods on the website can only be achieved for users that are logged in. 

```py
new_user = User("Angela")
create_blog_post(new_user)
```

I want a decorator method that will require `self.is_logged_in` attribute to be equal to `True`.

```py
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        # if user.is_logged_in == True:
        if args[0].is_logged_in == True: # look at the first position input to see if is_logged_in property = True
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Angela")
new_user.is_logged_in = True
create_blog_post(new_user)
```

This idea of adding in parameters is one step higher in terms of understanding Python decorator functions.

## Interactive Coding Exercise: Advanced Decorators

### Instructions

Create a `logging_decorator()` which is going to log the name of the function that was called, the arguments it was given and finally the returned output.

### Expected Output

https://cdn.fs.teachablecdn.com/jA2ypes2RfuB0cuC41yd

HINT 1: You can use `function.__name__` to get the name of the function.

HINT 2: You'll need to use `*args`

[SOLUTION](https://repl.it/@appbrewery/day-55-1-solution)

```py
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        function_arguments = [arg for arg in args]
        function_name = function.__name__
        function_output = function(*args)
        print(f"Function {function_name.upper()}{args}")
        print(f"And returned: {function_output}")
    return wrapper

@logging_decorator
def a_function(a, b, c):
    return a * b * c
    
a_function(1, 2, 3)
```

## Final Project -- Higher or Lower URLs
Now it's time to complete the final project of the day, the higher lower game that we created in Day 14, but now with a real website.

1. Create a new project in PyCharm called higher-lower, add a server.py file.

2. Create a new Flask application where the home route displays an <h1> that says "Guess a number between 0 and 9" and display a gif of your choice from giphy.com.

Alternatively use the one I found on Giphy: https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif

3. Generate a random number between 0 and 9 or any range of numbers of your choice.

4. Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9" and checks that number against the generated random number. If the number is too low, tell the user it's too low, same with too high or if they found the correct number. try to make the <h1> text a different colour for each page.  e.g. If the random number was 5:

Here are the GIF URLs I used, but it's way more fun finding your own on giphy.com

High: https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif

Low: https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif

Correct: https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif

[Solution](https://gist.github.com/angelabauer/26eb9190a094761a9f49b22e8ee4c0fb)