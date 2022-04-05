# Working with CSV Files and Analyzing Data with Pandas

## Reading CSV Data in Python

Read in a csv line by line. Grab data from a specific column.

```py
import csv
import pandas

WEATHER_DATA_FILE_PATH = r'C:\repos\100DaysOfPython\Day_25\my_code\weather_data.csv'

weather = []
temperature = []
with open(WEATHER_DATA_FILE_PATH) as weather_file:
    data = csv.reader(weather_file)
    for row in data:
      weather.append(row)
      if row[1] != "temp":
        temperature.append(int(row[1]))
print(weather)
print(temperature)

#######################################################################################
# GET PANDAS HELP TO KEEP THIS FROM BEING "FAFFY"
#######################################################################################

data = pandas.read_csv(WEATHER_DATA_FILE_PATH)
print(data["temp"])
```

## DataFrames & Series: Working with Rows & Columns

**The two primary data structures of pandas, *Series* (1-dimensional) and *DataFrame* (2-dimensional), handle the vast majority of typical use cases in finance, statistics, social science, and many areas of engineering.**

**Dataframes** are equivalent to an entire sheet.
**Series** are equivalent to a list; a column.

```py
import pandas

WEATHER_DATA_FILE_PATH = r'C:\repos\100DaysOfPython\Day_25\my_code\weather_data.csv'


data = pandas.read_csv(WEATHER_DATA_FILE_PATH)

data_dict = data.to_dict()

temp_list = data["temp"].to_list()
print(len(temp_list))

data["temp"].mean()
```


Challenges: Get the Averages and the Max numbers

```py
def get_average(list_of_numbers):
  average = sum(list_of_numbers)/len(list_of_numbers)
  return average

print(f'The average temperature is: {get_average(temp_list)}.')

print(f'The average temperature is: {data["temp"].mean()}.')

print(f'The highest temperature is: {data["temp"].max()}.')
```

Working with Data Frames
```py
import pandas

# WEATHER_DATA_FILE_PATH = r'C:\repos\100DaysOfPython\Day_25\my_code\weather_data.csv'
WEATHER_DATA_FILE_PATH = r'G:\Main\Development\100DaysOfPython\Day_25\my_code\weather_data.csv'

data = pandas.read_csv(WEATHER_DATA_FILE_PATH)
data_dict = data.to_dict()

temp_list = data["temp"].to_list()

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])

# Get the Row with the Highest Temperature
print(data[data.temp == data.temp.max()])

# Rows contain lots of data! We want that rows specific value!
monday = data[data.day == "Monday"]
print(monday.condition)

# Convert Monday's temperature to Fahrenheit
def convert_celsius_to_fahrenheit(degrees_in_celsius: int):
  return (degrees_in_celsius * (9/5)) + 32

monday = data[data.day == "Monday"]
monday_degrees = monday.temp
print(monday_degrees)
monday_degrees = convert_celsius_to_fahrenheit(monday_degrees)
print(monday_degrees)

#Create a dataframe from scratch
data_dict = {
  "students": ["Amy", "James", "Angela"],
  "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

#Create a csv file!
data.to_csv("new_data.csv")
```

## The Great Squirrel Census Data Analysis (with Pandas!)

### My Solution
```py
import pandas

# SQUIRRELS_FILE_PATH = r'G:\Main\Development\100DaysOfPython\Day_25\my_code\squirrel_analysis\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
SQUIRRELS_FILE_PATH = r'C:\repos\100DaysOfPython\Day_25\my_code\squirrel_analysis\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'

# Primary Fur Color Column; Grey, Cinnamon, Black
#TODO: Figure out how many gray squirrels there are in total, how many cinnamon, how many black ones
#TODO: Take data, build a dataframe, create final CSV using Pandas

def filter_data_by_color(color, inbound_data, outbound_data):
  df_color_filter = inbound_data[inbound_data["Primary Fur Color"] == color]
  color_count = df_color_filter["Primary Fur Color"].count()
  outbound_data["color"].append(color)
  outbound_data["count"].append(color_count)


data = pandas.read_csv(SQUIRRELS_FILE_PATH)
colors = ["Gray", "Cinnamon", "Black"]
data_dict = {
  "color": [],
  "count": []
}

for color in colors:
  filter_data_by_color(color, data, data_dict)

filtered_data = pandas.DataFrame(data_dict)

filtered_data.to_csv(r'C:\repos\100DaysOfPython\Day_25\my_code\squirrel_analysis\squirrels_fur_color_counts.csv')
```

## U.S. States Game Part 1: Setup

## U.S. States Game Part 2: Challenge with .csv

## U.S. States Game Part 3: Saving Data .csv