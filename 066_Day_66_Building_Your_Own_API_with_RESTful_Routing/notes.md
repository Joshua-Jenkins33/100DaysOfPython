# Day 66: Building Your Own APOI with RESTful Routing
On day 33, we learnt about APIs and since then, we've used a number of public APIs. e.g ISS location, Trivia Questions and Twilio. In a lot of cases, the API allows us to tap into a particular website's data or service.

Many companies have collected valuable data e.g. Bitcoin prices, Restaurant reviews and provide an API for developers to access this data for a price. Depending on how valuable the data/service is behind the API, these APIs can charge anywhere from $9 to $99 per month for access. Some even charge per API call.

What if you have access to some information that other people might want to use? E.g. You collected data on all the cafes in a particular city and figured out which ones were suitable for remote-work? Then you could create an API and charge people to access your data.

But how do you create an API?

That's what we'll tackle in today's lessons. Building a full REST API from scratch using Flask.

## What is REST?
**RE**presentational
**S**tate
**T**ransfer

Architecture:
- Client --> Server 

Client makes a request (HTTP hypertext transfer protocol) to the server and the server fulfills the request. HTTP isn't the only language that servers can speak. FTP (File Transfer Protocol). HTTPS (secure requests!). We can use cryptography to encrypt our request. A secret code language. 

The client made a successful request to the server and the server has it, the server will respond with the results of what it was that you requested. 

The server might do one of two things:
1. Work some computations, run some code
2. Communicate with our database to get the resources the client requested

The server will have APIs, services that the clients can tap into, when we're building an API we're building a MENU for what our server can do.

REST is an architectural style for designing APIs (not the only one; SOAP and GraphQL and Falcor are other examples). Standard for Web APIs if REST. Rules web devs could follow when building APIs. 

### REST Rules
1. Use HTTP Request Verbs
2. Use Specific Pattern of Routes/Endopints URLs

Most important parts of making your API RESTful.

VERBS are **GET**, **POST**, **PUT**, **PATCH**, and **DELETE**.
Similar to Create, Read, Update, and Delete with Databases.

PATTERN OF ROUTES AND ENDPOINTS
Compared to a safari map of routes to get camels, elephants, hippos.

| HTTP Verbs | /aritcles | /articles/jack-bauer |
| :--: | :--: | :--: | :--: |
| GET | Fetches **all** the articles | Fetches **the** article on jack-bauer |
| POST | Creates **one** new article | - |
| PUT | - | Updates **the** article on jack-bauer |
| PATCH | - | Updates **the** article on jack-bauer |
| DELETE | Deletes **all** the articles | Deletes **the** article on jack-bauer |

## Download the Starting Project
- [x] Download
- [x] Unzip and Open
- [x] All imports are installed
- [x] Look at the Database

## HTTP GET - a Random Cafe
Given our database consists of a bunch of cafes to remote-work from, one of the likely use cases of our API is a developer who wants to serve up a random cafe for their user to go to. So let's create a /random route that serves up a random cafe.

1. Create a `/random` route in main.py that allows GET requests to be made to it. 

```py
## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random():
    number_of_cafes = Cafe.query.count()
    random_id = randint(1, number_of_cafes) 
    random_cafe = Cafe.query.get(random_id)
    return f'<h1>{random_cafe.name}</h1>'
```

2. When someone makes a `GET` request to the `/random` route, our Flask server should fetch a random cafe from our database.

NOTE: Don't worry about returning anything at the moment.

- [x] Same as above

Normally, we've been returning HTML templates using `render_template()`, but this time, because our server is now acting as an API, we want to return a JSON containing the necessary data. Just like real public APIs.

e.g. [ISS API](http://api.open-notify.org/iss-now.json)


In order to do this, we have to turn our random_cafe SQLAlchemy Object into a JSON. This process is called **serialization**.

Flask has a **serialisation helper method** built-in called `jsonify()`. But we have to provide the structure of the JSON to return. 


3. See if you can use the documentation on `jsonify()` to figure out how to get the `/random` route to work. If successful, this is what you should see when you run main.py and go to localhost:5000/random

```py
## HTTP GET - Read Record
@app.route("/random")
def random():
    number_of_cafes = Cafe.query.count()
    random_id = randint(1, number_of_cafes)
    r = Cafe.query.get(random_id)
    return jsonify(
            cafe={
                'can_take_calls':r.can_take_calls,
                'coffee_price':r.coffee_price,
                'has_sockets':r.has_sockets,
                'has_toilet':r.has_toilet,
                'has_wifi':r.has_wifi,
                'id':r.id,
                'img_url':r.img_url,
                'location':r.location,
                'map_url':r.map_url,
                'name':r.name,
                'seats':r.seats
            }   
    )
```

The method described in the docs has maximum flexibility. It allows you to have perfect control over the JSON response. e.g. You could also structure the response by omitting some properties like id. You could also group the Boolean properties into a subsection called amenities.

```py
cafe={
  'amenities': {
    'can_take_calls':r.can_take_calls,
    'has_sockets':r.has_sockets,
    'has_toilet':r.has_toilet,
    'has_wifi':r.has_wifi
  },
  'coffee_price':r.coffee_price,
  'id':r.id,
  'img_url':r.img_url,
  'location':r.location,
  'map_url':r.map_url,
  'name':r.name,
  'seats':r.seats
}  
```

But in most cases, you might just want to return all the data you have on a particular record and it would drive you crazy if you had to write out all that code for every route.

So another method of serialising our database row Object to JSON is by first converting it to a dictionary and then using jsonify() to convert the dictionary (which is very similar in structure to JSON) to a JSON. 

```py
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
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    #Simply convert the random_cafe data record to a dictionary of key-value pairs. 
    return jsonify(cafe=random_cafe.to_dict())
```

## HTTP GET - All the Cafes
If someone was creating a website that lists all the cafes, then they would need to fetch all the cafes in our database.

e.g. [https://laptopfriendly.co/london](https://laptopfriendly.co/london)

**CHALLENGE:**

1. Create another GET route that's called `/all`

2. When a GET request is made to this `/all` route, your server should return all the cafes in your database as a JSON.

e.g.

https://gist.github.com/angelabauer/889a0e57359ede23e7b09a7902a45a6e

```py
@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    return jsonify([cafe.to_dict() for cafe in cafes])
```

## HTTP GET - Find a Cafe
1. Create a `/search` route to search for cafes at a particular location.

e.g. If you look in the **cafes.db**, you can see the field location, this is the rough area where the cafe is located.

Make our API return all the cafes in a particular area.

The user will make a `GET` request to your `/search` route and pass the location as a parameter.

HINT: Parameters are passed in the URL with a ?

e.g. Passing a lat and lon parameter to the ISS Tracking API:

[http://api.open-notify.org/iss-pass.json?lat=50&lon=-0.1](http://api.open-notify.org/iss-pass.json?lat=50&lon=-0.1)

If successful, this is what you should be able to do:

```py
@app.route("/search")
def search_by_location():
    query_location = request.args.get("location")
    cafes_by_location = Cafe.query.filter(Cafe.location==query_location).all()
    if len(cafes_by_location > 0):
        return jsonify([cafe.to_dict() for cafe in cafes_by_location])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
```

## Postman - The all in one API Testing Tool
As you can imagine, if you need to test your API with a bunch of parameters, it can quickly get tiring typing them all out in the URL bar of your browser. It's also super error-prone.

So how do developers test their APIs? One of the best tools is Postman.

It allows you to add key-value pairs for your request parameters and it will automatically format your URL.

It will also allow you to automatically [create documentation for your API](https://learning.postman.com/docs/publishing-your-api/documenting-your-api/)

(We'll do this a bit later).

After you have successfully tested your API route, try creating a new collection called Cafe & Wifi and adding all the existing routes to the collection.

You should end up with all 3 routes saved in your collection. This is important if you want to generate documentation for your API later.

## HTTP POST - A New Cafe
What if we wanted to add a new cafe to the database? e.g. There is a website where users can contribute cafes they have discovered?

e.g. [https://laptopfriendly.co/suggest](https://laptopfriendly.co/suggest)

How would you test your API without building out a WTForm or HTML Form? Because that's likely where the `POST` request is going to come from.

Luckily Postman makes this easy. 

The Key-Value pairs you enter into the Body tab in Postman is equivalent to `<input>` elements.

```html
    <label>Name of Cafe</label>
    <input name="name">
    <label>Google Map URL Link</label>
    <input name="map_url">
```

It's so good at making POST requests that some call it the "POSTman". 😜

This is what you're aiming to get in Postman:

e.g.

## HTTP PUT vs. PATCH
Analogy: Amazon Bicycle, clicked on "Buy Now". Bike showed up and it was busted. 2 options to make things better:
1. Send a whole new bike (`PUT`)
2. Send a new tire (rest of the bike was fine) (`PATCH`)
  
## HTTP PATCH - A Cafe's Coffee Price
One of the fields in our cafe database is the price of a single black coffee. It's a good way for users to gauge how expensive is the coffee shop. But cafes often change their prices. What if a user wanted to submit a change in price at one of the cafes?

If they knew the `id` of the cafe (which they can get by making a GET request to fetch data on all the cafes), then they can update the `coffee_price` field of the cafe. 

In this situation, a `PATCH` request is probably more efficient, as we don't need to change any of the rest of the cafe's data. 

1. Create a `PATCH` request route in main.py to handle PATCH requests to our API. In order for our API to be RESTful, ideally, the route should be something like this:

`/update-price/<cafe_id>`

[HINT 1](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules)

So the user might go to `localhost:5000/update-price/22` and that would update the cafe with an id of 22.

HINT 2: The user will also need to provide the updated price of a single black coffee by passing it with the request as a parameter.

This is what should happen if you've done this correctly, you should be able to test the API in Postman and get a successful response:

```json
{
  "success": "Successfully updated the price."
}
```

NOTE: There might be a chance that the id in the route doesn't exist. In this case, make sure you give the user the correct feedback:
```json
{
  "error": {
    "Not Found": "Sorry a cafe with that id was not found in the database."
  }
}
```

NOTE: Notice that even when the resource is not found and we get an error the correct HTTP code is not being returned. It should be 404 for "resource not found" but instead we're getting 200 for "a ok".

This is how you can pass an HTTP code with your response:
```py
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        ## Just add the code after the jsonify method. 200 = Ok
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        #404 = Resource not found
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
```

## HTTP DELETE - A Cafe that's Closed
One of the saddest things is when your favourite cafe/workplace closes. But we have to just accept and move on. Also, make a DELETE request to our server and update the database.

But we can't let just anyone delete things in our database. We might soon end up with someone accidentally deleting everything.

We can add a security feature by requiring an `api-key`. If they have the api-key `"TopSecretAPIKey"` then they're allowed to make the delete request, otherwise, we tell them they are not authorized to make that request. A 403 in HTTP speak.

Check out all the [HTTP Codes](https://httpstatuses.com/)

1. Complete this challenge by adding the DELETE route to `/report-closed/<cafe_id>`

e.g. The request via Postman might look like this:

`localhost:5000/report-closed/22?api-key=TopSecretAPIKey`

If they have the wrong api-key, say that it's not allowed and to ensure you have the right api key.

If the cafe doesn't exist with that id, state it.

```py
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
```

## Build Documentation for Your API
If we want other people to use our API, then we have to document how to use it. People can't see the code on our servers, so we have to tell them how to interact with our servers via the API constraints.

e.g. What are the routes, what are the required parameters etc.

Luckily for us, if you made all your requests in Postman and you gave each request a name and description then Postman will generate the documentation automatically for you.

1. Make sure that you've made each of the requests and they work as you expect.
2. Make sure all the requests are saved in the same collection e.g. My collection is called Cafe & Wifi
3. Click on the three dots next to your collection name and go to "Publish Docs"
4. Go through the steps to publish your documentation and this is what you should end up with:

e.g. Here's [mine](https://documenter.getpostman.com/view/2568017/TVRhd9qR)

5. We can now edit out index.html to include an anchor tag to our API's documentation.

```html
<body>
    <h1>Welcome to the Cafe & Wifi API</h1>
    <a href="https://documenter.getpostman.com/view/13962454/UzJPMb3V">Cafe API Documentation</a>
</body>
```