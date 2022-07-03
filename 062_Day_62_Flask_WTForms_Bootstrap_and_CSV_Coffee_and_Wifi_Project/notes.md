# Day 62: Flask, WTForms, Bootstrap and CSV: Coffee and Wifi Project

- [x] Download and unzip the starting project from the lesson resources (Starting Files - coffee-and-wifi.zip).

- [x] Open the project in PyCharm and make sure that all required packages are installed.

(If you are downloading from Repl.it all packages should be pre-installed, but you can always check in the Project Preferences.

## Look at the Desired Final Product

Gif of finished product.

## Check Off Each Requirement

Now it's time to write some code. Look at the list of requirements below for this project. Just like a real client project, the front-end has already been built for you (If you have more time/want more practice with HTML/Bootstrap you can build the entire project from scratch, just create a new empty PyCharm project). But the main goal of today is to ensure that you are fully comfortable with Flask-WTF, Flask-Bootstrap, Bootstrap classes and do a bit of revision on csv manipulation.

### Requirements
- [x] The home page should use the **css/styles.css** file to look like this:

HINT: Think about **bootstrap blocks** and **super blocks**

**index.html**
```html
{% block styles %}
{{super()}}
<link rel="stylesheet"
      href="{{url_for('static', filename='css/styles.css')}}">
{% endblock %}
```

---

- [x] The /cafes route should render the cafes.html file. This file should contain a [Bootstrap table](https://getbootstrap.com/docs/4.5/content/tables/) which displays all the data from the cafe-data.csv

HINT: A object called `cafes` is passed to cafes.html from the /cafes route. try putting it in a <p> to see what the data in cafes look like.

**cafes.html**
```html
	  <table class="table">
          <!-- This is where you will write the code to render a Bootstrap 
          Table that contains all the information from the 
          cafe-data.csv file. -->
          <!-- <p>{{ cafes }}</p> -->
          <thead>
            <tr>
              <th scope="col">{{ cafes[0][0] }}</th>
              <th scope="col">{{ cafes[0][1] }}</th>
              <th scope="col">{{ cafes[0][2] }}</th>
              <th scope="col">{{ cafes[0][3] }}</th>
              <th scope="col">{{ cafes[0][4] }}</th>
              <th scope="col">{{ cafes[0][5] }}</th>
              <th scope="col">{{ cafes[0][6] }}</th>
            </tr>
          </thead>
          <tbody>
            {% for cafe in cafes %}
              <tr>
                <th scope="row">{{ cafe[0] }}</th>
                <td>{{ cafe[1] }}</td>
                <td>{{ cafe[2] }}</td>
                <td>{{ cafe[3] }}</td>
                <td>{{ cafe[4] }}</td>
                <td>{{ cafe[5] }}</td>
                <td>{{ cafe[6] }}</td>
              </tr>
            {% endfor %}
          </tbody>
  	  </table>
```

---

- [x] The location URL should be rendered as an anchor tag `<a>` in the table instead of the full link. It should have the link text `"Maps Link"` and the href should be the actual link.

HINT: All location links have the first 4 characters as "`http`".

**cafes.html**
```html
	  <table class="table">
          <!-- This is where you will write the code to render a Bootstrap 
          Table that contains all the information from the 
          cafe-data.csv file. -->
          <!-- <p>{{ cafes }}</p> -->
          <thead>
            <tr>
              <th scope="col">{{ headers[0] }}</th> <!-- Cafe Name -->
              <th scope="col">{{ headers[1] }}</th> <!-- Location -->
              <th scope="col">{{ headers[2] }}</th> <!-- Open -->
              <th scope="col">{{ headers[3] }}</th> <!-- Close -->
              <th scope="col">{{ headers[4] }}</th> <!-- Coffee -->
              <th scope="col">{{ headers[5] }}</th> <!-- Wifi -->
              <th scope="col">{{ headers[6] }}</th> <!-- Power -->
            </tr>
          </thead>
          <tbody>
            {% for cafe in cafes %}
              <tr>
                <th scope="row">{{ cafe[0] }}</th> <!-- Cafe Name -->
                <td><a href="{{ cafe[1] }}">Maps Link</a></td> <!-- Location -->
                <td>{{ cafe[2] }}</td> <!-- Open -->
                <td>{{ cafe[3] }}</td> <!-- Close -->
                <td>{{ cafe[4] }}</td> <!-- Coffee -->
                <td>{{ cafe[5] }}</td> <!-- Wifi -->
                <td>{{ cafe[6] }}</td> <!-- Power -->
              </tr>
            {% endfor %}
          </tbody>
  	  </table>
```

---

- [x] Clicking on the "Show Me!" button on the home page should take you to the cafes.html page.

```html
<a class="btn btn-warning btn-lg" href="/cafes" role="button">Show Me!</a>
```

- [x] There should be a secret route "/add" which doesn't have a button, but those in the know should be able to access it and it should take you to the add.html file. 
- [x] Use what you have learnt about WTForms to create a quick_form in the add.html page that contains all the fields you can see in the demo below:
  - [HINT](https://flask-wtf.readthedocs.io/en/stable/quickstart.html)
  - [Form Help](https://pythonhosted.org/Flask-Bootstrap/forms.html)

```py
from wtforms.validators import DataRequired, URL

class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name')
    location = StringField(label='Cafe Location on Google Maps (URL)')
    opening_time = StringField(label='Opening Time e.g. 8AM')
    closing_time = StringField(label='Closing Time e.g. 5:30PM')
    coffee_rating = SelectField(label='Coffee Rating', choices=['☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️'])
    wifi_rating = SelectField(label='Wifi Strength Rating', choices=['✘','💪','💪💪','💪💪💪','💪💪💪💪'])
    power_socket_rating = SelectField(label='Power Socket Rating', choices=['✘','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌'])
    submit = SubmitField('Submit')

@app.route('/add', methods=["GET", "POST"])
```

---

- [x] Make sure that the location URL field has validation that checks the data entered is a valid URL:

[HINT](https://wtforms.readthedocs.io/en/2.3.x/validators/)

[How to switch off client-side (browser) validation with quick_forms](https://stackoverflow.com/a/61166621/10557313)

```py
from wtforms.validators import DataRequired, URL

 cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL(message="Must be a valid URL (beginning in http)")])
    opening_time = StringField(label='Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField(label='Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=['☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️'], validators=[DataRequired()])
    wifi_rating = SelectField(label='Wifi Strength Rating', choices=['✘','💪','💪💪','💪💪💪','💪💪💪💪'], validators=[DataRequired()])
    power_socket_rating = SelectField(label='Power Socket Rating', choices=['✘','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField('Submit')
```

---

- [x] When the user successfully submits the form on `add.html`, make sure the data gets added to the `cafe-data.csv`. It needs to be appended to the end of the csv file. The data from each field need to be comma-separated like all the other lines of data in cafe-data.csv

[HINT](https://www.w3schools.com/python/python_file_write.asp)

```py
    if form.validate_on_submit():
        with open(r'062_Day_62_Flask_WTForms_Bootstrap_and_CSV_Coffee_and_Wifi_Project/cafe-data.csv', 'a+', newline='', encoding='utf-8') as csv_file:
            writer_object = writer(csv_file)
            form_submission = [form.cafe.data,form.location.data,form.opening_time.data,form.closing_time.data,form.coffee_rating.data,form.wifi_rating.data,form.power_socket_rating.data]
            print(form_submission)
            writer_object.writerow(form_submission)  
    return render_template('add.html', form=form)
```

---

- [x] Make sure all the navigation links in the website work. 