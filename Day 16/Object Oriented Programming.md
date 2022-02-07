# Object Oriented Programing (OOM)

## Procedural Programming

One leads to another; top-to-bottom and jumping to a function as needed.

Increase in complexity, # of relationships that we need to remember and manage makes it get very very confusing. 

## Object Oriented Programming

Object Oriented Paradigm comes in really handy.

Modularizing chunks of code; resusable; Modularized

Split larger task into smaller pieces and each of those pieces can be worked on separate teams and spearate people and also each pieces can be reusable if we need that functionality in the future.

### Managed with the task of running a restaurant

Doing all the things if you're one person. Can't have a large restaurant with only person running the show.

Same thing with size of software projects. You can't do it as one person. Very complex, very hard to manage very quickly if it was all procedural.

If you had a Chef, a Waiter, a Cleaner... Then you can be the manager. They're trained for what they need to do; you just need to tell them what to do without knowing the nitty gritty details with exactly how they accomplish what you told them to do. Chef doesn't need to be told how to cook an egg.

Same concept to simplify relationships in our code and make it more scaleable for larger and more complex projects.

# How to use OOP: Classes and Objects

Virtual Restaurant. Model a virtual chef, waiter, cleaner and manager.
Think about:
- What is **has**
- What it **does**


## Waiter Object/Class

### What it Has

```py
is_holding_plate = True
tables_responsible = [4, 5, 6]
```

### What it does
```py
def take_order(table, order):
    # takes order to chef

def take_payment(amount):
    #add money to restaurant
```

It's a variable attached to a particular object.

**Attributes** and **methods** belong to an object. 

**Attribute.** A variable that is associated with a modeled object. Not just a floating variable; it's attached to a particular object. Things they can have.

**Method.** These are functions. We call it a method because it's a function because it's something a particular modeled object can do. Not just free-floating functions. Things they can do.

### Inheritance

When we model a particular job, like the waiter's job, we can generate multiple versions of the same object. We could have Henry and Betty, the waiters. We call this blueprint/type a **Class**. **Objects** are generated from these blueprints.

# Constructing Objects and Accessing their Attributes and Methods

Blueprint, models the real life car. Object is like the car created from a blueprint. 

`car = CarBlueprint()`

car is the object created from the CarBlueprint class/blueprint.

The `()` trigger the construction of the class just like they define a function call.

## Object Attributes

As we saw before with out car object it **has certain attributes, like speed and fuel, data we can keep track of**.

Syntax: `car.speed`. It identifies the object and, from this object, get this attribute!

## Object Methods

In addition to the things that *an object has*, the data, like fuel and speed, which we've already seen, it also has things **that it can do**, functions associated with particular objects. We use it the same way!

Syntax: `car.stop()`. Get a hold of an object and then we're calling a function associated with that object. And it's called a method.

# Python Packages

Modules of code by others!

**Package.** A whole bunch of code; lots of files to achieve some sort of goal or purpose.
**Module.** Where each file we create is essentially a module in itself.

We want to create a table of pokemon and their type.

```py
print("| Pokemon Name | Type |")
print("______________________")
# just to create the table; not fun to create ASCII
```

1. Search for a package! Go to pypi.org!
2. Search for prettytable (displays table in ASCII format)
3. Click on Project Link. Google Code Archive (where documentation is hosted). Tutorial will show you what need.
4. Install module into your package!
5. PyCharm (preferences --> Click on Your Project --> Interpreter --> "+" button to install it --> Search for the package.

# Steve Jobs on OOP

Go to Japan. Long flight. Soil T-Shirt. Bummed. Don't have local currency, don't speak language, don't know where the nearest laundromat is. Go to hotel. Hotel probably speaks english. Ask them to take care of it for you. They take your shirt away and do the messy work of cleaning it and present it to you with, now all clean.

```py
# Hotel
hotel.dry_clean()
```

## Coffee Machine (OOP)

1. Print report
2. Check resources sufficient?
3. Process coins
4. Check transaction succesful?
5. Make coffee