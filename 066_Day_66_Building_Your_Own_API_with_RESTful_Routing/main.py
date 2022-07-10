from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):      
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def random():
    number_of_cafes = Cafe.query.count()
    random_id = randint(1, number_of_cafes)
    random_cafe = Cafe.query.get(random_id)
    return jsonify(
            cafe={
                'amenities': {
                    'can_take_calls': random_cafe.can_take_calls,
                    'has_sockets': random_cafe.has_sockets,
                    'has_toilet': random_cafe.has_toilet,
                    'has_wifi': random_cafe.has_wifi
                },
                'coffee_price': random_cafe.coffee_price,
                'id': random_cafe.id,
                'img_url': random_cafe.img_url,
                'location': random_cafe.location,
                'map_url': random_cafe.map_url,
                'name': random_cafe.name,
                'seats': random_cafe.seats
            }   
    )


@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    return jsonify([cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search_by_location():
    query_location = request.args.get("location")
    cafes_by_location = Cafe.query.filter(Cafe.location==query_location).all()
    if len(cafes_by_location > 0):
        return jsonify([cafe.to_dict() for cafe in cafes_by_location])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    name = request.form['name']
    return jsonify(response={"success": "Successfully added the new cafe (but not really because it wasn't actually added to the database)."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    exists = db.session.query(Cafe.id).filter_by(id=cafe_id).first() is not None
    if exists:
        new_price = request.args.get("new_price")
        cafe_to_patch = Cafe.query.get(cafe_id)
        cafe_to_patch.price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    exists = db.session.query(Cafe.id).filter_by(id=cafe_id).first() is not None
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        if exists:
            Cafe.query.filter_by(id=cafe_id).delete()
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the record."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key."), 403


if __name__ == '__main__':
    app.run(debug=True)
