# import pandas

# WEATHER_DATA_FILE_PATH = r'C:\repos\100DaysOfPython\Day_25\my_code\weather_data.csv'

# data = pandas.read_csv(WEATHER_DATA_FILE_PATH)
# # print(type(data))
# # print(data["temp"])

# # Check out the Pandas Docks

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# def get_average(list_of_numbers):
#   average = sum(list_of_numbers)/len(list_of_numbers)
#   return average

# print(f'The average temperature is: {get_average(temp_list)}.')

# print(f'The average temperature is: {data["temp"].mean()}.')

# print(f'The highest temperature is: {data["temp"].max()}.')

import pandas

# WEATHER_DATA_FILE_PATH = r'C:\repos\100DaysOfPython\Day_25\my_code\weather_data.csv'
WEATHER_DATA_FILE_PATH = r'G:\Main\Development\100DaysOfPython\Day_25\my_code\weather_data.csv'

data = pandas.read_csv(WEATHER_DATA_FILE_PATH)

data_dict = data.to_dict()

temp_list = data["temp"].to_list()
# print(len(temp_list))

# data["temp"].mean()

# print(data["temp"].max())

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])

# Get the Row with the Highest Temperature
# print(data[data.temp == data.temp.max()])

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

data.to_csv("new_data.csv")
