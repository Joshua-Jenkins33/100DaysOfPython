from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)

app.secret_key = b'O\xd8\xd6\xb7\xdf\xe1jv\xc1Z\xc0G\x1a\x96\xe8R'

class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email(message="Invalid email address.", check_deliverability=True)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Password must be at least 8 characters long.")])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(f"Email: {login_form.email.data}")
        print(f"Password: {login_form.password.data}")
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)