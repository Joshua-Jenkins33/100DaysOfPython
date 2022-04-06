# name of the class should have the first letter in every word capitalized. PascalCase. Or TitleCase.
# camelCase only different because the first word is lowercase; every subsequent word has its first letter capitalized
# snake_case; words separated by underscore
# in python, you won't see a lot of camel casing; Classes use PascalCase, snake_case for pretty much everything else

class User:
  pass # get around indent errors if you don't want to yet add content

def function():
  pass

user_1 = User()
user_1.id = '001'
user_1.username = 'angela'
print(user_1.username)

# attribute is a varaible associated with an object; just like creating a new variable and attached it to an object

user_2 = User()
user_2.id = '002'
user_2.username = 'jack'
# this is prone to error (typos, attribute name whoopsies); gotta be a way to make this simpler.

###
# Constructor
## Part of the blueprint that lets us create from the blueprint; initializing
###

class Car:
  def __init__(self):
  # 2 underscores either side of the name; special method that the python guts knows about
  # used to initialize the attributes
  # init function is going to be called every time you create a new object from this class
    #initialize attributes
    print("new user being created...") # every time we create a new user, this print statement will be triggered
    
  ###
  ## Setting the attributes in the constructor
  ###
class Car:
  def __init__(self, seats): # self = the actual object being created/initialized
      self.seats = seats # setting the object's attribute

my_car = Car(5)
my_car.seats = 5 # these two the same thing; the top is faster and safer.

####################################################################################################################

class User:
  def __init__(self, user_id, username): # name of the parameter is generally the name of the attribute
    self.id = user_id
    self.username = username
    self.followers = 0 # so we can set it equal to 0 so it'll be set an instatiation

user_1 = User("001", "angela") # , follower) We don't want to have to pass this every time just to put in 0. So go to Line 53
user_2 = User("002")


# print(user_1.id)
print(user_1.followers) # prints 0!

# sometimes we might want a default value to start out with; it doesn't make sense for all attributes to be initialized when we create our object

####################################################################################################################

# ADDING METHODS TO A CLASS

####################################################################################################################

# Car class, seats attribute, want a method that changes the seats value

class Car:
  def enter_race_mode(): # class function == method
    self.seats = 2

# my_car.enter_race_mode()

class User:
  def __init__(self, user_id, username):
    self.id = user_id
    self.username = username
    self.followers = 0
    self.following = 0

  def follow(self, user): # "self" needs to be first parameter; when this method is called it *knows* the method that called it. In addition to self paramet, we'll pass in user we're trying to follow.
    user.follwers += 1
    self.folloing += 1

# you'll never see "self" when you're working with objects but you'll see it a lot when you're writing your code inside your class

user_1.follow(user_2) # User 1 Object and follow method from user 1 object; user_2 is the person we're going to follow
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

####################################################################################################################

# Creating the Question Class

####################################################################################################################

class Question:
  def __init__(self, text, answer):
    self.text = text
    self.answer = answer

new_q = Question()