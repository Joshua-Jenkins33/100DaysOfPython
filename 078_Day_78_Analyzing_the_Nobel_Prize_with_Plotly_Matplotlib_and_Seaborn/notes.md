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
  - [Challenge 1: Come up with 3 Questions](#challenge-1-come-up-with-3-questions)
  - [Challenge 2](#challenge-2-1)
  - [Challenge 3](#challenge-3-1)
  - [Challenge 4](#challenge-4)
  - [Challenge 5](#challenge-5)
  - [Challenge 6](#challenge-6)
  - [Challenge 7](#challenge-7)
- [Using Matplotlib to Visualize Trends over Time](#using-matplotlib-to-visualize-trends-over-time)
  - [Challenge 1](#challenge-1-1)
    - [Solution 1: Number of Prizes Awarded over Time](#solution-1-number-of-prizes-awarded-over-time)
  - [Challenge 2](#challenge-2-2)
    - [Solution 2: The Prize Share of Laureates over Time](#solution-2-the-prize-share-of-laureates-over-time)
- [A Choropleth Map and the Countries with the Most Prizes](#a-choropleth-map-and-the-countries-with-the-most-prizes)
  - [Challenge 1: Top 20 Country Ranking](#challenge-1-top-20-country-ranking)
    - [Solution 1: Prize ranking by Country](#solution-1-prize-ranking-by-country)
  - [Challenge 2: Choropleth Map](#challenge-2-choropleth-map)
    - [Solution 2: Displaying the Data on a Map](#solution-2-displaying-the-data-on-a-map)
  - [Challenge 3: Country Bar Chart with Prize Category](#challenge-3-country-bar-chart-with-prize-category)
    - [Solution 3: The category breakdown by country](#solution-3-the-category-breakdown-by-country)
  - [Challenge 4: Prizes by Country over Time](#challenge-4-prizes-by-country-over-time)
    - [Solution 4: Country Prizes over Time](#solution-4-country-prizes-over-time)
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

## Challenge 1: Come up with 3 Questions
A big part of data science is coming up with questions that you'd like to explore. This is the most difficult aspect to teach in a tutorial because it's completely open-ended and requires some creativity. Often times you will be asking questions of the data, that it actually cannot answer - and that's ok. That's all part of the process of discovery.

Pause here for a moment and think about the kind of data you saw in the columns. Write down at least 3 questions that you'd like to explore as part of this analysis. For example, your question might go like: "What percentage of the Nobel laureates were women?" or "How many prizes were given out in each category". **Practice coming up with a few of your own questions.**

In the upcoming lessons, you might find that we will write the code to answer some of your questions. And if not, your questions make for a great exercise to take this analysis even further.

The challenges below are all based on questions we're going to ask the data.

**My Questions**
- Which countries most commonly produce Nobel Lauretes?
- Have nobel prizes been awarded more often in certain time periods?
- Do some organizations produce more nobel prize lauretes than tohers?
- Are you more likely to earn a greater prize share in certain categories?
- Do organizations often achieve the nobel prize?


## Challenge 2
Create a [donut chart using plotly](https://plotly.com/python/pie-charts/) which shows how many prizes went to men compared to how many prizes went to women. What percentage of all the prizes went to women?

**My Code**
```py
df_gender_stats = df_data[df_data['sex'].notnull()]

fig = px.pie(df_gender_stats, values='share_pct', names='sex', title='Percentage of Male vs. Female Laureates', hole=.5)
fig.show()
```

**Solution 2: Creating a Donut Chart with Plotly**
To create the chart we use the our `.value_counts()` method together with plotly's `.pie()` function. We see that out of all the Nobel laureates since 1901, only about 6.2% were women.
```py
    biology = df_data.sex.value_counts()
    fig = px.pie(labels=biology.index, 
                 values=biology.values,
                 title="Percentage of Male vs. Female Winners",
                 names=biology.index,
                 hole=0.4,)
     
    fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
     
    fig.show()
```

## Challenge 3
- What are the names of the first 3 female Nobel laureates?
  - Marie Curie
  - Baroness Bertha Sophie
  - Selma Ottilia
- What did the win the prize for?
  - Physica, Peace, Literature
- What do you see in their `birth_country`? Were they part of an organisation?
  - They were standalones and in Russia/Europe

**My Code**
```py
df_females = df_gender_stats[df_gender_stats['sex']=='Female'].sort_values('year')
df_females.head()
```

**Solution 3: The first 3 women to win**
Even without looking at the data, you might have already guessed one of the famous names: Marie Curie.
```py
    df_data[df_data.sex == 'Female'].sort_values('year', ascending=True)[:3]
```

![First Women Winners](https://img-b.udemycdn.com/redactor/raw/2020-10-20_11-59-16-2880c50d998356973cfa975e30bd642c.png)


## Challenge 4
Did some people get a Nobel Prize more than once? If so, who were they?
- The Red Cross
- Frederick Sanger
- Linus Carl Pauling
- John Bardeen
- United Nations High Commissioner for Refugees
- Marie Curie

**My Code**
```py
pd.set_option("display.max_rows", False)
df_data['full_name'].value_counts()
```

**Solution 4: The Repeat Winners**
Winning a Nobel prize is quite an achievement. However, some folks have actually won the prize multiple times. To find them, we can use many different approaches. One approach is to look for duplicates in the full_name column:
```py
    is_winner = df_data.duplicated(subset=['full_name'], keep=False)
    multiple_winners = df_data[is_winner]
    print(f'There are {multiple_winners.full_name.nunique()}' \
          ' winners who were awarded the prize more than once.')
```
There are 6 winners who were awarded the prize more than once.
```py
    col_subset = ['year', 'category', 'laureate_type', 'full_name']
    multiple_winners[col_subset]
```
Only 4 of the repeat laureates were individuals.

We see that Marie Curie actually got the Nobel prize twice - once in physics and once in chemistry. Linus Carl Pauling got it first in chemistry and later for peace given his work in promoting nuclear disarmament. Also, the International Red Cross was awarded the Peace prize a total of 3 times. The first two times were both during the devastating World Wars. 

## Challenge 5
- In how many categories are prizes awarded?
  - 6 categories
- Create a plotly bar chart with the number of prizes awarded by category.
- Use the color scale called `Aggrnyl` to colour the chart, but don't show a color axis.
- Which category has the most number of prizes awarded?
  - Medicine
- Which category has the fewest number of prizes awarded?
  - Economics

**My Code**
```py
len(pd.unique(df_data['category']))

df_category = df_data.groupby(['category'])['prize'].count().reset_index(name='count').sort_values('count', ascending=False)
df_category

fig = px.bar(df_category, x='category', y='share_pct', color="category", color_continuous_scale='Aggrnyl')
fig.update_traces(showlegend=False)
fig.show()
```

**Solution 5: Number of Prizes per Category**
To find the number of unique categories in a column we can use:
```py
    df_data.category.nunique()
```
To generate the vertical plotly bar chart, we again use .value_counts():
```py
    prizes_per_category = df_data.category.value_counts()
    v_bar = px.bar(
            x = prizes_per_category.index,
            y = prizes_per_category.values,
            color = prizes_per_category.values,
            color_continuous_scale='Aggrnyl',
            title='Number of Prizes Awarded per Category')
     
    v_bar.update_layout(xaxis_title='Nobel Prize Category', 
                        coloraxis_showscale=False,
                        yaxis_title='Number of Prizes')
    v_bar.show()
```

![Number of Prizes Awarded per Category](https://img-b.udemycdn.com/redactor/raw/2020-10-20_13-59-47-6fea83b45bae6cda8e421d02b71aa380.png)



## Challenge 6
- When was the first prize in the field of Economics awarded?
  - 1969
- Who did the prize go to?
  - Jan Tinbergen

**My Code**
```py
df_data[df_data['category']=='Economics'].sort_values('year').head()
```

**Solution 6: The Economics Prize**
The chart above begs the question: "Why are there so few prizes in the field of economics?". Looking at the first couple of winners in the economics category, we have our answer:
```py
    df_data[df_data.category == 'Economics'].sort_values('year')[:3]
```
The economics prize is much newer. It was first awarded in 1969, compared to 1901 for physics. 

![Economics](https://img-b.udemycdn.com/redactor/raw/2020-10-20_14-03-25-9b4e50252c31bbc38d8171905a26b9a5.png)

## Challenge 7
Create a [plotly bar chart](https://plotly.com/python/bar-charts/) that shows the split between men and women by category.
- Hover over the bar chart. How many prizes went to women in Literature compared to Physics?
  - 4 in Physics
  - 16 in Literature

**My Code**
```py
df_category_by_sex = df_data.groupby(['category', 'sex'])['prize'].count().reset_index(name='count').sort_values('count', ascending=False)
df_category_by_sex

fig = px.bar(df_category_by_sex, x="category", y="count", color="sex")
fig.show()
```

**Solution 7: Male and Female Winners by Category**
We already saw that overall, only 6.2% of Nobel prize winners were female. Does this vary by category?
```py
    cat_men_women = df_data.groupby(['category', 'sex'], 
                                   as_index=False).agg({'prize': pd.Series.count})
    cat_men_women.sort_values('prize', ascending=False, inplace=True)
```
We can combine `.groupby()` and `.agg()` with the `.count()` function. This way we can count the number of men and women by prize category.

We can then use `.color` the parameter in the `.bar()` function to mark the number of men and women on the chart:

```py
v_bar_split = px.bar(x = cat_men_women.category,
                      y = cat_men_women.prize,
                      color = cat_men_women.sex,
                      title='Number of Prizes Awarded per Category split by Men and Women')
  
v_bar_split.update_layout(xaxis_title='Nobel Prize Category', 
                          yaxis_title='Number of Prizes')
v_bar_split.show()
```

We see that overall the imbalance is pretty large with physics, economics, and chemistry. Women are somewhat more represented in categories of Medicine, Literature and Peace. Splitting bar charts like this is an incredibly powerful way to show a more granular picture. 

# Using Matplotlib to Visualize Trends over Time
Now let's look at how things have changed over time. This will give us a chance to review what we learnt about creating charts with two y-axes in Matplotlib and generating arrays with NumPy. 

## Challenge 1

Are more prizes awarded recently than when the prize was first created? Show the trend in awards visually.
- Count the number of prizes awarded every year.
- Create a 5 year rolling average of the number of prizes (Hint: see previous lessons analysing Google Trends).
- Using Matplotlib superimpose the rolling average on a scatter plot.
- Show a tick mark on the x-axis for every 5 years from 1900 to 2020. (Hint: you'll need to use NumPy).

![Line Chart in Years](https://img-b.udemycdn.com/redactor/raw/2020-10-20_14-15-10-c99698bd9d7749499bb42a4763d446a6.png)

- Use the [named colours](https://matplotlib.org/3.1.0/gallery/color/named_colors.html) to draw the data points in `dodgerblue` while the rolling average is coloured in `crimson`.

![Graph](https://img-b.udemycdn.com/redactor/raw/2020-10-20_14-15-24-c67d3b9baeaa22b2f28b6d3a2202d77a.png)

- Looking at the chart, did the first and second world wars have an impact on the number of prizes being given out?
- What could be the reason for the trend in the chart?

**Count the number of prizes awarded every year.**
```py
df_prize_count_by_year = df_data.groupby('year')['prize'].count().reset_index(name='prize_count')
df_prize_count_by_year
```

**Create a 5 year rolling average of the number of prizes (Hint: see previous lessons analysing Google Trends).**
```py
rolling_df = df_prize_count_by_year['prize_count'].rolling(window=5).mean()
rolling_df
```

**Using Matplotlib superimpose the rolling average on a scatter plot.**
```py
plt.scatter(x=df_prize_count_by_year.year, y=df_prize_count_by_year.prize_count, c='dodgerblue')
plt.plot(df_prize_count_by_year.year, rolling_df.values, c='crimson')

plt.show()
```

**Show a tick mark on the x-axis for every 5 years from 1900 to 2020. (Hint: you'll need to use NumPy).**
I didn't know the answer to this one.

```py
five_year_increments = np.arange(1900, 2021, step=5)
```

- **Using Matplotlib superimpose the rolling average on a scatter plot.**
- **Show a tick mark on the x-axis for every 5 years from 1900 to 2020. (Hint: you'll need to use NumPy).**
- **Use the [named colours](https://matplotlib.org/3.1.0/gallery/color/named_colors.html) to draw the data points in `dodgerblue` while the rolling average is coloured in `crimson`.**
```py
five_year_increments = np.arange(1900, 2021, step=5)
plt.figure(figsize=(16,8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=five_year_increments, 
           fontsize=14, 
           rotation=45)

ax = plt.gca() # get current axis
ax.set_xlim(1900, 2020)


plt.scatter(x=df_prize_count_by_year.index, y=df_prize_count_by_year.values, c='dodgerblue')
plt.plot(df_prize_count_by_year.index, rolling_df.values, c='crimson')

           
plt.show()
```

**Looking at the chart, did the first and second world wars have an impact on the number of prizes being given out?**
- More prizes were awarded as a result of the world wars

**What could be the reason for the trend in the chart?**
- People aiming for peace, discoveries to get an edge in the war

### Solution 1: Number of Prizes Awarded over Time
First, we have to count the number of Nobel prizes that are awarded each year. 

```py
prize_per_year = df_data.groupby(by='year').count().prize 
```

This just involves grouping the data so that we can count the number of entries per year. To calculate the 5-year moving average we use `.rolling()` and `.mean()` like we did with the Google Trend data. 

```py
moving_average = prize_per_year.rolling(window=5).mean()
```

Now we can create a Matplotlib chart that superimposes the two:
```py
plt.scatter(x=prize_per_year.index, 
            y=prize_per_year.values, 
            c='dodgerblue',
            alpha=0.7,
            s=100,)
  
plt.plot(prize_per_year.index, 
        moving_average.values, 
        c='crimson', 
        linewidth=3,)
  
plt.show()
```

![Resulting Graph](https://img-b.udemycdn.com/redactor/raw/2020-10-20_14-23-51-6e82d0a2a593ae5f05b2562d18daed03.png)

With the help of a little styling, this chart could look better. To create 5-year tick marks on the x-axis, we generate an array using NumPy:

```py
np.arange(1900, 2021, step=5)
```

Then we tap into functions like the `.figure()`, the `.title()`, the `.xticks()`, and `.yticks()` to fine-tune the chart.

In addition, we will shortly be adding a second y-axis, so we can use an `Axes` object to draw our scatter and line plots. 

```py
plt.figure(figsize=(16,8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5), 
            fontsize=14, 
            rotation=45)
  
ax = plt.gca() # get current axis
ax.set_xlim(1900, 2020)
  
ax.scatter(x=prize_per_year.index, 
            y=prize_per_year.values, 
            c='dodgerblue',
            alpha=0.7,
            s=100,)
  
ax.plot(prize_per_year.index, 
        moving_average.values, 
        c='crimson', 
        linewidth=3,)
  
plt.show()
```

![Resulting Graph](https://img-b.udemycdn.com/redactor/raw/2020-10-20_14-20-53-0c21b93b7886ff45ea6503747813ff1c.png)

## Challenge 2
Investigate if more prizes are shared than before.
- Calculate the average prize share of the winners on a year by year basis.
- Calculate the 5 year rolling average of the percentage share.
- Copy-paste the cell from the chart you created above.
- Modify the code to add a secondary axis to your Matplotlib chart.
- Plot the rolling average of the prize share on this chart.
- See if you can invert the secondary y-axis to make the relationship even more clear.

```py
# Copy-paste the cell from the chart you created above.
five_year_increments = np.arange(1900, 2021, step=5)
plt.figure(figsize=(16,8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=five_year_increments, 
           fontsize=14, 
           rotation=45)

ax1 = plt.gca() # get current axis
ax1.set_xlim(1900, 2020)

# Modify the code to add a secondary axis to your Matplotlib chart.
ax2 = ax1.twinx()
ax2.set_ylabel('Prize Share Percentage')

# See if you can invert the secondary y-axis to make the relationship even more clear.
ax2.invert_yaxis()


ax1.scatter(x=df_prize_count_by_year.index, y=df_prize_count_by_year.values, c='dodgerblue')

# Plot the rolling average of the prize share on this chart. 
ax1.plot(df_prize_count_by_year.index, rolling_df.values, c='crimson')

# Adding prize share plot on second axis
ax2.plot(avg_prize_share_by_year.index, avg_prize_share_rolling.values, c='grey')
           
plt.show()
```

### Solution 2: The Prize Share of Laureates over Time
Now we can work out the rolling average of the percentage share of the prize. If more prizes are given out, perhaps it is because the prize is split between more people. 

```py
yearly_avg_share = df_data.groupby(by='year').agg({'share_pct': pd.Series.mean})
share_moving_average = yearly_avg_share.rolling(window=5).mean()
```

If more people get the prize, then the average share should go down, right? 

```py
plt.figure(figsize=(16,8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5), 
            fontsize=14, 
            rotation=45)
  
ax1 = plt.gca()
ax2 = ax1.twinx() # create second y-axis
ax1.set_xlim(1900, 2020)
  
ax1.scatter(x=prize_per_year.index, 
            y=prize_per_year.values, 
            c='dodgerblue',
            alpha=0.7,
            s=100,)
  
ax1.plot(prize_per_year.index, 
        moving_average.values, 
        c='crimson', 
        linewidth=3,)
  
# Adding prize share plot on second axis
ax2.plot(prize_per_year.index, 
        share_moving_average.values, 
        c='grey', 
        linewidth=3,)
  
plt.show()
```

![Resulting Graph](https://img-b.udemycdn.com/redactor/raw/2020-10-20_14-31-42-191579962fb7cb3a64f2c97d6f78c438.png)

To see the relationship between the number of prizes and the laureate share even more clearly we can invert the second y-axis. 

```py
plt.figure(figsize=(16,8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5), 
            fontsize=14, 
            rotation=45)
  
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(1900, 2020)
  
# Can invert axis
ax2.invert_yaxis()
  
ax1.scatter(x=prize_per_year.index, 
            y=prize_per_year.values, 
            c='dodgerblue',
            alpha=0.7,
            s=100,)
  
ax1.plot(prize_per_year.index, 
        moving_average.values, 
        c='crimson', 
        linewidth=3,)
  
ax2.plot(prize_per_year.index, 
        share_moving_average.values, 
        c='grey', 
        linewidth=3,)
  
plt.show()
```

What do we see on the chart? Well, there is clearly an upward trend in the number of prizes being given out as more and more prizes are shared. Also, more prizes are being awarded from 1969 onwards because of the addition of the economics category. We also see that very few prizes were awarded during the first and second world wars. Note that instead of there being a zero entry for those years, we instead see the effect of the wards as missing blue dots. 

![Resulting Graph](https://img-b.udemycdn.com/redactor/raw/2020-10-20_14-38-11-076469c853c7b83bc6a9ec20fc1a0aaf.png)


# A Choropleth Map and the Countries with the Most Prizes
For this next bit, we're going to compare which countries actually get the most prizes. And we're also going to look at in which categories those prizes are awarded. This has me feeling a little like I'm at the Olympics 😊. 

## Challenge 1: Top 20 Country Ranking

- Create a Pandas DataFrame called `top20_countries` that has the two columns. The `prize` column should contain the total number of prizes won.

![Expected Results](https://img-b.udemycdn.com/redactor/raw/2020-10-20_14-42-59-9fb704fd63feff9b691697416ea5c722.png)

- Is it best to use `birth_country`, `birth_country_current` or `organization_country`?
- What are some potential problems when using `birth_country` or any of the others? Which column is the least problematic?
- Then use plotly to create a horizontal bar chart showing the number of prizes won by each country. Here's what you're after:

![Bar Chart](https://img-b.udemycdn.com/redactor/raw/2020-10-20_14-43-26-c29a036da3674550eb3e9879a6f1b3a6.png)

- What is the ranking for the top 20 countries in terms of the number of prizes?

### Solution 1: Prize ranking by Country
Looking at our DataFrame there are actually 3 different columns to choose from for creating this ranking: `birth_country`, `birth_country_current` or `organization_country`. However, they each have certain problems and limitations. 

If you look at the entries in the birth country, you'll see that some countries no longer exist! These include the Soviet Union or Czechoslovakia for example. Hence, using `birth_country_current` is better, since it has the country name which controls the city where the laureate was born. Now, notice that this does not determine the laureates' nationality since some globetrotting folks gave birth to their future Nobel laureate children while abroad. Also, people's nationalities can change as they emigrate and acquire different citizenship or get married and change citizenship. What this boils down to is that we will have to be clear about the assumptions that we will make in the upcoming analysis. 

We can create the list of the top 20 countries like this:

```py
top_countries = df_data.groupby(['birth_country_current'], 
                                  as_index=False).agg({'prize': pd.Series.count})
  
top_countries.sort_values(by='prize', inplace=True)
top20_countries = top_countries[-20:]
```

Note that the ranking here determines how our bar chart will be displayed. 

```py
h_bar = px.bar(x=top20_countries.prize,
                y=top20_countries.birth_country_current,
                orientation='h',
                color=top20_countries.prize,
                color_continuous_scale='Viridis',
                title='Top 20 Countries by Number of Prizes')
  
h_bar.update_layout(xaxis_title='Number of Prizes', 
                    yaxis_title='Country',
                    coloraxis_showscale=False)
h_bar.show()
```

![Bar Chart](https://img-b.udemycdn.com/redactor/raw/2020-10-20_15-28-14-d0951596c2e1a822e6b53fd9fc21e3ff.png)

The United States has a massive number of prizes by this measure. The UK and Germany are in second and third place respectively. 

## Challenge 2: Choropleth Map
- Create this choropleth map using [the plotly documentation](https://plotly.com/python/choropleth-maps/):

![Choropleth Map](https://img-b.udemycdn.com/redactor/raw/2020-10-20_14-44-57-c9ec3018035c0e32588e167a8e8b0a00.png)

- Experiment with [plotly's available colors](https://plotly.com/python/builtin-colorscales/). I quite like the sequential color `matter` on this map.

Hint: You'll need to use a 3 letter country code for each country.

### Solution 2: Displaying the Data on a Map
To show the above ranking on a colour coded map, we need to make use of the ISO codes. 

```py
df_countries = df_data.groupby(['birth_country_current', 'ISO'], 
                                as_index=False).agg({'prize': pd.Series.count})
df_countries.sort_values('prize', ascending=False)
```

This means we can use the ISO country codes for the `locations` parameter on the choropleth. 

```py
world_map = px.choropleth(df_countries,
                          locations='ISO',
                          color='prize', 
                          hover_name='birth_country_current', 
                          color_continuous_scale=px.colors.sequential.matter)
  
world_map.update_layout(coloraxis_showscale=True,)
  
world_map.show()
```

I love it how plotly allows you to zoom in and pan on the map it generates.

## Challenge 3: Country Bar Chart with Prize Category
See if you can divide up the plotly bar chart you created above to show which categories made up the total number of prizes. Here's what you're aiming for:

![Bar Chart](https://img-b.udemycdn.com/redactor/raw/2020-10-20_15-11-40-896b68120f5e2daa0e2823f286619336.png)

- In which category are Germany and Japan the weakest compared to the United States?
- In which category does Germany have more prizes than the UK?
- In which categories does France have more prizes than Germany?
- Which category makes up most of Australia's Nobel prizes?
- Which category makes up half of the prizes in the Netherlands?
- Does the United States have more prizes in Economics than all of France? What about in Physics or Medicine?

The hard part is preparing the data for this chart!

*Hint:* Take a two-step approach. The first step is grouping the data by country and category. Then you can create a DataFrame that looks something like this:

![Dataframe](https://img-b.udemycdn.com/redactor/raw/2020-10-20_15-11-54-d06c71c4976b32b66b2bef08144cb67a.png)

### Solution 3: The category breakdown by country
Preparing our data to show the breakdown by category and country is challenging. We'll take a two-step approach here. First we count the prizes by category in each country:

```py
cat_country = df_data.groupby(['birth_country_current', 'category'], 
                                as_index=False).agg({'prize': pd.Series.count})
cat_country.sort_values(by='prize', ascending=False, inplace=True)
```

![Dataframe](https://img-b.udemycdn.com/redactor/raw/2020-10-20_15-39-34-67274118d7ced9c4bf5a8f81c3f667f1.png)

Next, we can merge the DataFrame above with the top20_countries DataFrame that we created previously. That way we get the total number of prizes in a single column too. This is important since we want to control the order for our bar chart. 

```py
merged_df = pd.merge(cat_country, top20_countries, on='birth_country_current')
# change column names
merged_df.columns = ['birth_country_current', 'category', 'cat_prize', 'total_prize'] 
merged_df.sort_values(by='total_prize', inplace=True)
```

![Dataframe Prizes by Category](https://img-b.udemycdn.com/redactor/raw/2020-10-20_15-42-03-e31d94a8366dcf1b7c91618eb9e234f9.png)

Now we can create our bar chart again. This time we use the color parameter based on the category. 

```py
cat_cntry_bar = px.bar(x=merged_df.cat_prize,
                        y=merged_df.birth_country_current,
                        color=merged_df.category,
                        orientation='h',
                        title='Top 20 Countries by Number of Prizes and Category')
  
cat_cntry_bar.update_layout(xaxis_title='Number of Prizes', 
                            yaxis_title='Country')
cat_cntry_bar.show()
```

![Stacked Bar Chart](https://img-b.udemycdn.com/redactor/raw/2020-10-20_15-44-31-1906cb97c5380befcc9d9c09d2880032.png)

Splitting the country bar chart by category allows us to get a very granular look at the data and answer a whole bunch of questions. For example, we see is that the US has won an incredible proportion of the prizes in the field of Economics. In comparison, Japan and Germany have won very few or no economics prize at all. Also, the US has more prizes in physics or medicine alone than all of France's prizes combined. On the chart, we also see that Germany won more prizes in physics than the UK and that France has won more prizes in peace and literature than Germany, even though Germany has been awarded a higher total number of prizes than France. 

When did the United States become so dominant? Was it always this way? Has the prize become more global in scope? 



## Challenge 4: Prizes by Country over Time
Every country's fortunes wax and wane over time. Investigate how the total number of prizes awarded changed over the years.
- When did the United States eclipse every other country in terms of the number of prizes won?
- Which country or countries were leading previously?
- Calculate the cumulative number of prizes won by each country in every year. Again, use the `birth_country_current` of the winner to calculate this.
- Create a [plotly line chart](https://plotly.com/python/line-charts/) where each country is a coloured line.

### Solution 4: Country Prizes over Time
To see how the prize was awarded over time. To do that, we can count the number of prizes by country by year. 

```py
prize_by_year = df_data.groupby(by=['birth_country_current', 'year'], as_index=False).count()
prize_by_year = prize_by_year.sort_values('year')[['year', 'birth_country_current', 'prize']]
```

Then we can create a series that has the cumulative sum for the number of prizes won. 

```py
cumulative_prizes = prize_by_year.groupby(by=['birth_country_current',
                                              'year']).sum().groupby(level=[0]).cumsum()
cumulative_prizes.reset_index(inplace=True) 
```

Using this, we can create a chart, using the current birth country as the `color`:

```py
l_chart = px.line(cumulative_prizes,
                  x='year', 
                  y='prize',
                  color='birth_country_current',
                  hover_name='birth_country_current')
  
l_chart.update_layout(xaxis_title='Year',
                      yaxis_title='Number of Prizes')
  
l_chart.show()
```

![Line Chart](https://img-b.udemycdn.com/redactor/raw/2020-10-20_16-05-40-d768858f0f5ab25eb4082e5b2d0332cf.gif)

What we see is that the United States really started to take off after the Second World War which decimated Europe. Prior to that, the Nobel prize was pretty much a European affair. Very few laureates were chosen from other parts of the world. This has changed dramatically in the last 40 years or so. There are many more countries represented today than in the early days. Interestingly we also see that the UK and Germany traded places in the 70s and 90s on the total number of prizes won. Sweden being 5th place pretty consistently over many decades is quite interesting too. Perhaps this reflects a little bit of home bias? 😊 

All this analysis of different countries makes me curious about where the actual research is happening. Where are the cities and organisations located where people actually make discoveries? 

# Create Sunburst Charts for a Detailed Regional Breakdown of Research Locations

# Unearthing Patterns in the laureate Age at the Time of the Award

# Learning Points & Summary