from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from csv import writer

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL(message="Must be a valid URL (beginning in http)")])
    opening_time = StringField(label='Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField(label='Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=['☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️'], validators=[DataRequired()])
    wifi_rating = SelectField(label='Wifi Strength Rating', choices=['✘','💪','💪💪','💪💪💪','💪💪💪💪'], validators=[DataRequired()])
    power_socket_rating = SelectField(label='Power Socket Rating', choices=['✘','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField('Submit')

# ---------------------------------------------------------------------------

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open(r'062_Day_62_Flask_WTForms_Bootstrap_and_CSV_Coffee_and_Wifi_Project/cafe-data.csv', 'a+', newline='', encoding='utf-8') as csv_file:
            writer_object = writer(csv_file)
            form_submission = [form.cafe.data,form.location.data,form.opening_time.data,form.closing_time.data,form.coffee_rating.data,form.wifi_rating.data,form.power_socket_rating.data]
            print(form_submission)
            writer_object.writerow(form_submission)  
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(r'062_Day_62_Flask_WTForms_Bootstrap_and_CSV_Coffee_and_Wifi_Project/cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        column_headers = list_of_rows[0]
        list_of_rows.pop(0)
    return render_template('cafes.html', headers=column_headers, cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
