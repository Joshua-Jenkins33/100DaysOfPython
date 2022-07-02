from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)

app.secret_key = b'O\xd8\xd6\xb7\xdf\xe1jv\xc1Z\xc0G\x1a\x96\xe8R'

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html', form=LoginForm())


if __name__ == '__main__':
    app.run(debug=True)