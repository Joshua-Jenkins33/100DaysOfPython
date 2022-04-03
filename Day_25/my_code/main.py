import pandas

WEATHER_DATA_FILE_PATH = r'C:\repos\100DaysOfPython\Day_25\my_code\weather_data.csv'

data = pandas.read_csv(WEATHER_DATA_FILE_PATH)
# print(type(data))
# print(data["temp"])

# Check out the Pandas Docks

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

def get_average(list_of_numbers):
  average = sum(list_of_numbers)/len(list_of_numbers)
  return average

print(f'The average temperature is: {get_average(temp_list)}.')

print(f'The average temperature is: {data["temp"].mean()}.')

print(f'The highest temperature is: {data["temp"].max()}.')