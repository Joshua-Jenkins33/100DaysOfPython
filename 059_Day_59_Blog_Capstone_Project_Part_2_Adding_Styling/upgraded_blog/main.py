from flask import Flask, render_template, request
import datetime
import requests
import smtplib
from dotenv import load_dotenv
from os import getenv

load_dotenv(r'059_Day_59_Blog_Capstone_Project_Part_2_Adding_Styling\upgraded_blog\.env')
EMAIL = getenv('EMAIL')
PASSWORD = getenv('PASSWORD')
RECEIVER = getenv('RECEIVER')

BLOG_API_ENDPOINT = 'https://api.npoint.io/59dfc431a83b143abbf9'


response = requests.get(url=BLOG_API_ENDPOINT)
response.raise_for_status()
blog_data = response.json()

app = Flask(__name__)

def get_copyright_year():
  return datetime.date.today().year

def send_contact_email(form):
    body = f"Username: {form['username']}\nPhone Number: {form['phone']}\nEmail Address: {form['email']}\nMessage:\n{form['message']}"
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=RECEIVER,
            msg=f"Subject:BlogSite Contact Form Submission\n\n{body}"
        )

@app.route('/')
def home():
    return render_template("index.html", year=get_copyright_year(), blog_posts=blog_data)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        send_contact_email(request.form)
        return render_template("contact.html", year=get_copyright_year(), form_submitted = True)
    else:
        return render_template("contact.html", year=get_copyright_year())

@app.route('/about')
def about():
    return render_template("about.html", year=get_copyright_year())

@app.route('/blog-post/<int:id>')
def blog_post(id):
    return render_template("post.html", post=blog_data[id-1])


if __name__ == "__main__":
    app.run(debug=True)