# Day 78: Advanced - Analzying the Nobel Prize with Plotly, Matplotlib, & Seaborn

- [Day 78: Advanced - Analzying the Nobel Prize with Plotly, Matplotlib, & Seaborn](#day-78-advanced---analzying-the-nobel-prize-with-plotly-matplotlib--seaborn)
- [What You'll Make](#what-youll-make)
- [Updated Packages in Google Colab & Explore and Clean the Dataset](#updated-packages-in-google-colab--explore-and-clean-the-dataset)
  - [Using Google Colab? -> Upgrade plotly](#using-google-colab---upgrade-plotly)
  - [Challenge 1](#challenge-1)
    - [Solution 1: Preliminary Data Exploration](#solution-1-preliminary-data-exploration)
  - [Challenge 2](#challenge-2)
    - [Solution 2: NaN values](#solution-2-nan-values)
  - [Challenge 3](#challenge-3)
    - [Solution 3: Type Conversions](#solution-3-type-conversions)
- [Plotly Bar & Donut Charts: Analyze Prize Categories & Women Winning Prizes](#plotly-bar--donut-charts-analyze-prize-categories--women-winning-prizes)
- [Using Matplotlib to Visualize Trends over Time](#using-matplotlib-to-visualize-trends-over-time)
- [A Choropleth Map and the Countries with the Most Prizes](#a-choropleth-map-and-the-countries-with-the-most-prizes)
- [Create Sunburst Charts for a Detailed Regional Breakdown of Research Locations](#create-sunburst-charts-for-a-detailed-regional-breakdown-of-research-locations)
- [Unearthing Patterns in the laureate Age at the Time of the Award](#unearthing-patterns-in-the-laureate-age-at-the-time-of-the-award)
- [Learning Points & Summary](#learning-points--summary)

# What You'll Make
Today we're going to analyse a dataset on the past winners of the Nobel Prize. Let's see what patterns we can uncover in the past Nobel laureates and what can we learn about the Nobel prize and our world more generally.

![Nobel Prize](https://img-b.udemycdn.com/redactor/raw/2020-10-20_09-43-40-6dd4f59ff9ec129b81ee4c131ef6bf75.jpeg)

On November 27, 1895, Alfred Nobel signed his last will in Paris. When it was opened after his death, the will caused a lot of controversy, as Nobel had left much of his wealth for the establishment of a prize. Alfred Nobel dictates that his entire remaining estate should be used to endow “prizes to those who, during the preceding year, have conferred the greatest benefit to humankind”. Every year the Nobel Prize is given to scientists and scholars in the categories chemistry, literature, physics, physiology or medicine, economics, and peace.

This project will bring a lot of the tools and techniques that we've covered previously together. While we will review many concepts that we've covered in the previous days, you'll also learn a lot of new things. 

**Today you'll learn:**
- Create a Choropleth to display data on a map.
- Create bar charts showing different segments of the data with plotly.
- Create Sunburst charts with plotly.
- Use Seaborn's `.lmplot()` and show best-fit lines across multiple categories using the `row`, `hue`, and `lowess` parameters.
- Understand how a different picture emerges when looking at the same data in different ways (e.g., box plots vs a time series analysis).
- See the distribution of our data and visualise descriptive statistics with the help of a histogram in Seaborn. 

**Download and add the Notebook to Google Drive**
As usual, download the .zip file from this lesson and extract it. Add the .ipynb file into your Google Drive and open it as a Google Colaboratory notebook.

# Updated Packages in Google Colab & Explore and Clean the Dataset

## Using Google Colab? -> Upgrade plotly
Google Colab comes with a lot of Python packages pre-installed and working. However, you can also install new packages as well as upgrade existing packages. In our case, the plotly package is outdated and will cause a problem with our starburst chart. Here's how to updated a package in Google Colab:

Uncomment the cell with the pip install command. Run the cell. And then comment the code out again. 

## Challenge 1

**Preliminary data exploration.**
1. What is the shape of `df_data`? How many rows and columns?
2. What are the column names and what kind of data is inside of them?
3. In which year was the Nobel prize first awarded?
4. Which year is the latest year included in the dataset?

```py
# 1. What is the shape of `df_data`? How many rows and columns?
df_data.shape
# (962, 16)

# 2. What are the column names and what kind of data is inside of them?
df_data.columns

"""
Index(['year', 'category', 'prize', 'motivation', 'prize_share',
       'laureate_type', 'full_name', 'birth_date', 'birth_city',
       'birth_country', 'birth_country_current', 'sex', 'organization_name',
       'organization_city', 'organization_country', 'ISO'],
      dtype='object')
"""

# 3. In which year was the Nobel prize first awarded?
df_data['year'].min()
# 1901


# 4. Which year is the latest year included in the dataset?
df_data['year'].max()
# 2020
```

### Solution 1: Preliminary Data Exploration
When we run `df_data.shape`, `df_data.tail()`, and `df_data.head()`, we see that there are 962 rows and 16 columns. The first Nobel prizes were awarded in 1901 and the data goes up to 2020. 

![Solution 1 Answer](https://img-b.udemycdn.com/redactor/raw/2020-10-20_11-00-28-1798f7e1537c4a5e3a5197eb6411a12b.png)

We notice that the columns contain the following information:

**birth_date:** date in string format
**motivation:** description of what the prize is for
**prize_share:** given as a fraction
**laureate_type:** individual or organisation
**birth_country:** has countries that no longer exist
**birth_country_current:** current name of the country where the birth city is located
**ISO:** three-letter international country code
**organization_name:** research institution where the discovery was made
**organization_city:** location of the institution

## Challenge 2
1. Are there any duplicate values in the dataset?
2. Are there NaN values in the dataset?
3. Which columns tend to have NaN values?
4. How many NaN values are there per column?
5. Why do these columns have NaN values?

```py
# 1. Are there any duplicate values in the dataset?
df_data.duplicated().sum()
# Negative

# 2. Are there NaN values in the dataset?
df_data.isnull().values.any()
# Yes


# 3. Which columns tend to have NaN values?
df_data.isna()
# motivation, birth_date, birth_city, birth_country


# 4. How many NaN values are there per column?
all_columns = df_data.columns

results = {}

for column in all_columns:
    count = df_data[column].isna().sum()
    if count > 0:
        results[column] = count
    
print(results)
# {'motivation': 88, 'birth_date': 28, 'birth_city': 31, 'birth_country': 28, 'birth_country_current': 28, 'sex': 28, 'organization_name': 255, 'organization_city': 255, 'organization_country': 254, 'ISO': 28}

# 5. Why do these columns have NaN values?

# They're missing a value. Likely, these fields were not required and no data was entered.
```

### Solution 2: NaN values
There are no duplicates in the dataset:
```py
print(f'Any duplicates? {df_data.duplicated().values.any()}')
```

However, there are a number of NaN values
```py
print(f'Any NaN values among the data? {df_data.isna().values.any()}')
```

We can get a count of the NaN values per column using
```py
df_data.isna().sum()
```

![Solution 2 Answer 1](https://img-b.udemycdn.com/redactor/raw/2020-10-20_11-10-39-9f5107ed7f79742d98c60af382a4a4e7.png)

Why are there so many NaN values for the birth date? And why are there so many missing values among the organisation columns?

Filtering on the NaN values in the birth date column we see that we get back a bunch of organisations, like the UN or the Red Cross. 

```py
col_subset = ['year','category', 'laureate_type',
              'birth_date','full_name', 'organization_name']
df_data.loc[df_data.birth_date.isna()][col_subset]
```

![Solution 2 Answer 2](https://img-b.udemycdn.com/redactor/raw/2020-10-20_11-24-58-ca4ff85fc797f3662c8ed33c9ac7b481.png)

That makes sense. We also see that since the organisation's name is in the `full_name` column, the `organisation_name` column contains `NaN`.

In addition, when we look at for rows where the `organization_name` column has no value, we also see that many prizes went to people who were not affiliated with a university or research institute. This includes many of the Literature and Peace prize winners.

```py
col_subset = ['year','category', 'laureate_type','full_name', 'organization_name']
df_data.loc[df_data.organization_name.isna()][col_subset]
```

![Solution 2 Answer 3](https://img-b.udemycdn.com/redactor/raw/2020-10-20_11-26-52-390f5c9ddbfce24588ff4f6a59ad1028.png)

## Challenge 3
1. Convert the `birth_date` column to Pandas `Datetime` objects
2. Add a Column called `share_pct` which has the laureates' share as a percentage in the form of a floating-point number.

```py
# 1. Convert the `birth_date` column to Pandas `Datetime` objects
df_data['birth_date'] = pd.to_datetime(df_data['birth_date'], format='%Y-%m-%d')
df_data['year'] = pd.to_datetime(df_data['year'], format='%Y')

df_data.dtypes

# 2. Add a Column called `share_pct` which has the laureates' share as a percentage in the form of a floating-point number.
def convert_prize_share(row):
    prize_share = float(row.prize_share.split('/'))
    numerator, denominator = prize_share[0], prize_share[1]
    share_percentage = numerator/denominator
    return share_percentage

df_data['share_pct'] = df_data.apply(convert_prize_share, axis=1)

df_data
```

### Solution 3: Type Conversions
We can use pandas to convert the birth_date to a Datetime object with a single line:

```py
df_data.birth_date = pd.to_datetime(df_data.birth_date)
```

Adding a column that contains the percentage share as first requires that we split the string on the forward slash. Then we can convert to a number. And finally, we can do the division.

```py
separated_values = df_data.prize_share.str.split('/', expand=True)
numerator = pd.to_numeric(separated_values[0])
denomenator = pd.to_numeric(separated_values[1])
df_data['share_pct'] = numerator / denomenator
```
Now we can check if our type conversions were successful:

![Solution 3 Answer 1](https://img-b.udemycdn.com/redactor/raw/2020-10-20_11-32-10-f5d62149b40ac16398ffdbdf516c5530.png)



# Plotly Bar & Donut Charts: Analyze Prize Categories & Women Winning Prizes

# Using Matplotlib to Visualize Trends over Time

# A Choropleth Map and the Countries with the Most Prizes

# Create Sunburst Charts for a Detailed Regional Breakdown of Research Locations

# Unearthing Patterns in the laureate Age at the Time of the Award

# Learning Points & Summary