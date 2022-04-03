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

## The Great Squirrel Census Data Analysis (with Pandas!)

## U.S. States Game Part 1: Setup

## U.S. Sstates Game Part 2: Challenge with .csv

## U.S. States Game Part 3: Saving Data .csv