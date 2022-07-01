from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def get_copyright_year():
  return datetime.date.today().year

@app.route('/')
def home():
    return render_template("index.html", year=get_copyright_year())

@app.route('/login', methods=["GET", "POST"])
def receive_data():
  username = request.form['name']
  password = request.form['password']
  
  return render_template('login.html', username=username, password=password)

if __name__ == "__main__":
    app.run(debug=True)