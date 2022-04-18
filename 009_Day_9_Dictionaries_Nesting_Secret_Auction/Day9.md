# Day 9: Dictionaries & Nesting

Going to build a silent auction program.

## Dictionaries

Work kind of like dictionaries in real life.

Code: Program instructions in the computer.

Tag pieces of related information. Kind of like atable.

Key on the left side (word in dictionary) and associated value (definition of the word).

```py
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop":"The action of doing something over and over again."
}

# list[0] retrieves an item in a list

print(programming_dictionary['Bug'])
```

### Adding Values to Dictionaries

And creating an empty dictionary and wiping a dictionary and editing an item ina dictionary.

```py
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary
empty_dictionary = {}

#Wipe an existing empty dictionary
programming_dictionary = {}

#Edit an item in a dictionary
print(programming_dictionary["Bug"])
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])
```

### Looping Through a Dictionary

```py
#Loop through a dictionary
for thing in programming_dictionary:
    print(thing)

    ## --> This code just gives you the keys

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    ## --> Retrieval code in order to get the value
```

## Nesting

Dictionaries and Lists can be like folders!

We can add multiple key value pairs into one dictionary.
I can add a list as a value. I can use a dictionary as a value.

The structure grows more complex but gives us more flexibility.

```py
#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nested Lists; Not as Useful
["A", "B", ["C", "D"]]

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    },
}
```

 ## Nesting a Dictionary Inside a List

 ```py
 #Nesting a Dictionary in a list
 travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    },
]