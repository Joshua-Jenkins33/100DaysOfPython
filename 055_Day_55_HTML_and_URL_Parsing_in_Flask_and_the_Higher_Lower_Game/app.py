from flask import Flask
app = Flask(__name__)
print("Hi")
print(app)


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


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World!</h1> \
            <p>This is a paragraph.</p> \
            <img src="https://media.giphy.com/media/vMbC8xqhIf9ny/giphy.gif" width=200px>'

@app.route('/bye')
@make_bold
@make_underlined
@make_emphasis
def say_bye():
    return "Bye"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)