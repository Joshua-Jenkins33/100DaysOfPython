import pandas

SQUIRRELS_FILE_PATH = r'G:\Main\Development\100DaysOfPython\Day_25\my_code\squirrel_analysis\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'

# Primary Fur Color Column; Grey, Cinnamon, Black
#TODO: Figure out how many gray squirrels there are in total, how many cinnamon, how many black ones
#TODO: Take data, build a dataframe, create final CSV using Pandas

data = pandas.read_csv(SQUIRRELS_FILE_PATH)
print(data["Primary Fur Color"].value_counts())

