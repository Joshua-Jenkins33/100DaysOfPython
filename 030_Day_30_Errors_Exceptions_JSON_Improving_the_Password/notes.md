# Day 30: Errors, Exceptions, JSON Data, Improving the Password

## Catching Exceptions: The `try catch except finally` pattern

What happens if we try to read from a file that doesn't exist?

```py
with open("a_file.txt") as file:
  file.read()
```

The above code will result in the following error:
> FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'

**KeyError**
```py
a_dictionary = {"key": "value"}
value = a_dictionary["non-existent-key"] # key doesn't exist in this dictionary!
```

**IndexError**
```py
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruits_list[3] # index 3 doesn't exist!
```

**TypeError**
```py
txt = 'abc'
print(text+5) # trying to do something with a piece of data but can't do it with a certain data type
```
**Catching Errors When They Aren't So Easy...**
```py
try: # something that might cause an exception

except: # do this if there **was** an exception

else: # do this if there were no exceptions

finally: # do this no matter what happens; usually used for cleaning/tidying things up after a code execution
```

**FileNotFound**
```py
file = open("a_file.txt") # this line of code will fail because we don't have this file 

#########################################################################################

try:
  file = open("a_file.txt")
except:
  # once we tried running the above line of code and it failed... we're going to do something different
  print("There was an error") # kind of like an if statement; if something failed, then do this!
  # Need a better message than the above!
  file = open("a_file.txt", "w") # the except block created the file!
  file.write("Something!")
  #pep8 says you should never use a bare except clause

#########################################################################################
try:
  file = open("a_file.txt")
  a_dictionary = {"key": "value"}
  print(a_dictionary{'sdfsdf'}) # this fails but is just sent to the below except block; not what we want!
except FileNotFoundError: # we can specify the type of exception
  file = open("a_file.txt", "w")
  file.write("Something")
except KeyError: # you can have more than one except block!
  print("That key does not exist")

# Alternatively to the above, we can just catch the regular error message
except KeyError as error_message:
  print(f'The key {error_message} does not exist.')

# ELSE BLOCK
else:
    content = file.read()
    print(content) # this only works if the above exceptions aren't raised

# FINALLY BLOCK
finally:
  file.close()
  print("File was closed.") # Will run no matter what; sometimes useful
```

## Raising your own Exceptions

### The Final Key Word: `raise`
```py
try:
except:
else:
finally:
  raise TypeError("This is an error that I made up.") # you can set your own errors
```

When do you want to raise your own errors?
- You may raise exceptions when your code is perfectly valid but there is a human portion of it that doesn't make sense; this is a way to tell your computer to worry about those scenarios.
```py
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
  raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

'''
H: 45 # this is godzilla height
W: 67 
BMI: 0.0330865
'''
```
## IndexError Handling (Coding Exercise)
```py
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError:
    print("Fruit Pie")
  else:
    print(f"{fruit} pie")

make_pie(4)
```

## KeyError Handling (Coding Exercise)
```py
facebook_posts = [
  {'Likes': 21, 'Comments': 2},
  {'Likes': 13, 'Comments': 2, 'Shares': 1},
  {'Likes': 33, 'Comments': 8, 'Shares': 3},
  {'Comments': 4, 'Shares': 2},
  {'Comments': 1, 'Shares': 1},
  {'Likes': 19, 'Comments': 3},
]

total_likes = 0

for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    pass
```

## Exception Handling in the NATO Phonetic Alphabet Project (Coding Exercise)
Real life example of using `try..except` blocks to handle erroneous user input! See the NATO project in today's directory.

## Write, Read, and Update JSON data in the Password Manager
Leveling up our data storage from a text file to a JSON (JavaScriptObjectNotation). Most popular way of transferring data across the internet.

It's very similar to dictionaries. It's composed of nested lists and dictionaries with the key:value pair setup.

### The JSON Library

**Important Commands.**
1. `json.dump()` -- Write
2. `json.load()` -- Read
3. `json.update()` -- Update

See `Password_Manager` in today's directory.

```py
json.dump(new_data, data_file, indent=4) # most important parameters: Data you want to dump and file you want to dump it to
                ## indent makes it human-readable!

data = json.load(data_file) #takes json data and converts it into python dictionary; serialize and deserialize from storage to not storage
print(data)
```

You can't append to a json object. `json.update()` will handle this.

Snippet from Password Manager updates
```py
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        with open("data.json", "r") as data_file: # switched to writing to json from csv; modified from append to write
            #json.dump(new_data, data_file, indent=4) # most important parameters: Data you want to dump and file you want to dump it to
                ## indent makes it human-readable!

            # THREE STEP APPROACH
            ## Reading old data
            data = json.load(data_file) #takes json data and converts it into python dictionary; serialize and deserialize from storage to not storage
            #print(data)
            
            #data_file.write(f"{website} | {email} | {password}\n")

            ##Updating old data with enw data
            data.update(new_data)

        with open('data.json', 'w') as data_file:
            ##Saving updated data
            json.dump(data, data_file, indent=4)
```


## Challenge 1 - Handling Exceptions in the Password Manager
Modify the code to handle the `FileNotFoundError`. Create a new `data.json` file if it does not exist.
If the file already exists, then simply add the new entry.
```py
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
      try:
        with open("data.json", "r") as data_file:
            ## Reading old data
            data = json.load(data_file)
      except FileNotFoundError:
        with open("data.json", "w") as data_file:
          json.dump(new_data, data_file, indent=4)

            ##Updating old data with enw data
      else:
            data.update(new_data)

        with open('data.json', 'w') as data_file:
            ##Saving updated data
            json.dump(data, data_file, indent=4)
      finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
```

## Challenge 2 - Search for a Website in the Password Manager
Add the search functionality! We don't want to dig through a json file to find out username and passwords. We want to search through the JSON to find the key that matches the one the user typed in.

Should be an exception if you don't find the object.

1. Add a "Search" button next to the website entry field.
2. Adjust the layout and the other widgets as needed to get the desired look.
3. Create a function called `find_password()` that get triggered when the "Search" button is pressed.
4. Check if the user's text entry matches an item in the `data.json`
5. If yes, show a `messagebox` with the website's name and password
6. Catch an exception that might occur trying to access the `data.json` showing a `messagebox` with the text: "No Data File Found"
7. If the user's website does not exist inside the `data.json`, show a `messagebox` that reads "No details for the website exists".

```py
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found.")
    else:
        if website in data: # handle if this returns false
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Emails: {email}\nPassword: {password}")
        else:
            messagebox.showing(title="Error", message=f"No details for {website} exists.")


#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2,row=1)

```

Why don't we catch the following with an exception?

```py
if website in data: # handle if this returns false
    email = data[website]['email']
    password = data[website]['password']
    messagebox.showinfo(title=website, message=f"Emails: {email}\nPassword: {password}")
else:
    messagebox.showing(title="Error", message=f"No details for {website} exists.")
```
If you can do something with `if` and `else` keywords very easily, then you should do so. If you can't do it easily and it's an error that's going to be thrown that and you don't have any other way of dealing with it, then you should use a `try...except`. 

Try is something that's supposed to be `exceptional`. It happens rarely.