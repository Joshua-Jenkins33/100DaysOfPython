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

df = pandas.DataFrame(data_dict)

df.to_csv(r'C:\repos\100DaysOfPython\Day_25\my_code\squirrel_analysis\squirrels_fur_color_counts.csv')
