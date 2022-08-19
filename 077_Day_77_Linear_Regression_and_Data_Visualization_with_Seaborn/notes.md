# Day 77: Advanced - Linear Regression and Data Visualization with Seaborn

- [Day 77: Advanced - Linear Regression and Data Visualization with Seaborn](#day-77-advanced---linear-regression-and-data-visualization-with-seaborn)
- [What You Will Make](#what-you-will-make)
- [Explore and Clean the Data](#explore-and-clean-the-data)
  - [Challenge 1](#challenge-1)
  - [Challenge 2](#challenge-2)
  - [Challenge 3](#challenge-3)
- [Investigate the Films that had Zero Revenue](#investigate-the-films-that-had-zero-revenue)
  - [Challenge 1](#challenge-1-1)
  - [Challenge 2](#challenge-2-1)
  - [Challenge 3](#challenge-3-1)
- [Filter on Multiple Conditions: International Films](#filter-on-multiple-conditions-international-films)
  - [Challenge](#challenge)
  - [Unreleased Films](#unreleased-films)
    - [Challenge](#challenge-1)
    - [Bonus Challenge: Films that Lost Money](#bonus-challenge-films-that-lost-money)
- [Seaborn Data Visualization: Bubble Charts](#seaborn-data-visualization-bubble-charts)
  - [Import Seaborn](#import-seaborn)
  - [Seaborn Scatter Plots](#seaborn-scatter-plots)
  - [From Scatter Plot to Bubble Chart](#from-scatter-plot-to-bubble-chart)
  - [Challenge](#challenge-2)
- [Floor Division: A Trick to Convert Years to Decades](#floor-division-a-trick-to-convert-years-to-decades)
  - [Challenge](#challenge-3)
  - [Challenge](#challenge-4)
- [Plotting Linear Regressions with Seaborn](#plotting-linear-regressions-with-seaborn)
  - [Challenge](#challenge-5)
- [Use scikit-learn to Run Your Own Regression](#use-scikit-learn-to-run-your-own-regression)
- [Learning Points & Summary](#learning-points--summary)

# What You Will Make
In this lesson, we're going to be looking at movie budget and revenue data. This dataset is perfect for trying out some new tools like scikit-learn to run a linear regression and seaborn, a popular data visualisation library built on top of Matplotlib.  

![Movies](https://img-b.udemycdn.com/redactor/raw/2020-10-14_11-55-48-2c83542d09cb8d7e8c8dfc03616734f7.png)

The question we want to answer today is: Do higher film budgets lead to more revenue in the box office? In other words, should a movie studio spend more on a film to make more?  

**Today you'll learn:**
- How to use a popular data visualisation library called Seaborn
- How to run and interpret a linear regression with scikit-learn
- How to plot a regression a scatter plot to visualise relationships in the data
- How to add a third dimension to a scatter plot to create a bubble chart
- How to cleverly use floor division `//` to convert your data

![Seaborn Image](https://img-b.udemycdn.com/redactor/raw/2020-10-14_11-48-35-4f37a708b04a864a3fe1ab0b2138dd05.png)

**Download and add the Notebook to Google Drive**
As usual, download the .zip file from this lesson and extract it. Add the .ipynb file into your Google Drive and open it as a Google Colaboratory notebook.

**Add the Data to the Notebook**
The .zip file also includes a .csv file called cost_revenue_dirty. This is the data for the project. Add this file to your notebook.

![SciKit Learn Image](https://img-b.udemycdn.com/redactor/raw/2020-10-14_11-57-57-f2a45422e3025ee7021afa483d10ade8.png)

# Explore and Clean the Data
As with any dataset, the first steps are going to be data exploration and data cleaning. We need to get a better understanding of what we're dealing with. Since you've gone through this process a number of times before on previous days, can you tackle the following challenges on your own? 

## Challenge 1
Answer these questions about how the data is structured:
1. How many rows and columns does the dataset contain?
    - 5391 rows, 6 columns
2. Are there any NaN values present?
    - Negative
3. Are there any duplicate rows?
    - Negative
4. What are the data types of the columns?


| Column Name | Data Type |
| :--- | :--- |
| Rank | int64 |
| Release_Date | object |
| Movie_Title | object |
| USD_Production_Budget | object |
| USD_Worldwide_Gross | object | 
| USD_Domestic_Gross | object |

```py
data.shape
data.isna().any(axis=None)
data.duplicated().any(axis=None)
data.dtypes
```

**Instructor Solution**
With any new dataset, it's a good idea to do some standard checks and conversions. I typically always first look at `.shape`, `.head()`, `.tail()`, `.info()` and `.sample()`.  Here's what I'm spotting already:

![Soluion Image](https://img-b.udemycdn.com/redactor/raw/2020-10-14_14-46-28-63dd3d1025bbcd51f2effa33132c48f0.png)

There are thousands of entries in the DataFrame - one entry for each movie. We'll have some challenges formatting the data before we can do more analysis because we have non-numeric characters in our budget and revenue columns. 

We can check for NaN values with this line:
```py
    data.isna().values.any()
```
And check for duplicates with this line:
```py
    data.duplicated().values.any()
```
We can see the total number of duplicates by creating a subset and looking at the length of that subset:
```py
    duplicated_rows = data[data.duplicated()]
    len(duplicated_rows)
```

![Query Results](https://img-b.udemycdn.com/redactor/raw/2020-10-14_14-51-20-7ae3dea5e27c5d9ea9d7e26b9bdddc36.png)

The fact that there are no duplicates or NaN (not-a-number) values in the dataset will make our job easier. We can also see if there are null values in `.info()`, which also shows us that we need to do some type conversion.

![Info Results](https://img-b.udemycdn.com/redactor/raw/2020-10-14_14-54-47-6c35659efd0a6ebd03bde9de6851e72c.png)


## Challenge 2
Convert the `USD_Production_Budget`, `USD_Worldwide_Gross`, and `USD_Domestic_Gross` columns to a numeric format by removing `$` signs and `,`.

Note that *domestic* in this context refers to the United States.

```py
data[data.columns[3:]] = data[data.columns[3:]].replace('[\$,]','', regex=True).astype(float)
data[data.columns[3:]].dtypes
```

**Instructor Solution**
In order to convert the data in the budget and revenue columns and remove all the non-numeric characters, we can use a nested for loop. We create two Python lists: the characters to remove and the column names. Inside the nested loop we can combine `.replace()` and `.to_numeric()` to achieve our goal.
```py
    chars_to_remove = [',', '$']
    columns_to_clean = ['USD_Production_Budget', 
                        'USD_Worldwide_Gross',
                        'USD_Domestic_Gross']
     
    for col in columns_to_clean:
        for char in chars_to_remove:
            # Replace each character with an empty string
            data[col] = data[col].astype(str).str.replace(char, "")
        # Convert column to a numeric data type
        data[col] = pd.to_numeric(data[col])
```
![Results](https://img-b.udemycdn.com/redactor/raw/2020-10-14_15-01-32-a70628a70ce1a0f946a2a760132323ba.png)

## Challenge 3
Convert the Release_Date column to a Pandas Datetime type.
```py
data['Release_Date'] = pd.to_datetime(data['Release_Date'])
data.dtypes
```

**Instructor Solution**
To convert the Release_Date column to a DateTime object, all we need to do is call the `to_datetime()` function.
```py
    data.Release_Date = pd.to_datetime(data.Release_Date)
```
When we check `.info()` again we see that the columns now have the desired data type. This allows us to proceed with the next parts of our analysis. 

![Results](https://img-b.udemycdn.com/redactor/raw/2020-10-14_15-06-08-862b621b9dfc92e9110a1619e0da56ee.png)


# Investigate the Films that had Zero Revenue
Now that we've done some legwork on cleaning our data, we can investigate our data set more thoroughly. 

## Challenge 1
1. What is the average production budget of the films in the data set?
  - $31,113,737.58
2. What is the average worldwide gross revenue of films?
  - $88,855,421.96
4. What were the minimums for worldwide and domestic revenue?
  - Worldwide: $2,358,918,982.00
  - Domestic: $630,662,225.00
5. Are the bottom 25% of films actually profitable or do they lose money?
  - The bottom 25% of films lose money by about $60 and $17.6 million respectively
7. What are the highest production budget and highest worldwide gross revenue of any film?
  - Highest Production Budget: $425,000,000
  - Highest Worldwide Gross Revenue: $2.78 billion
8. How much revenue did the lowest and highest budget films make?
  - Highest Budget Revenue: $2.3 billion
  - Lowest Budget Revenue: $179,941.00

**My Code**
```py
# 1. What is the average production budget of the films in the data set?
data['USD_Production_Budget'].mean()

# 2. What is the average worldwide gross revenue of films?
data['USD_Worldwide_Gross'].mean()

# 3. What were the minimums for worldwide and domestic revenue?
data.describe()

def calc_ww_revenue(row):
    revenue = row.USD_Production_Budget-row.USD_Worldwide_Gross
    return revenue

def calc_dom_revenue(row):
    revenue = row.USD_Production_Budget-row.USD_Domestic_Gross
    return revenue

data['Worldwide_Revenue'] = data.apply(calc_ww_revenue, axis=1)
data['Domestic_Revenue'] = data.apply(calc_dom_revenue, axis=1)
data

data.describe()

# 6. How much revenue did the lowest and highest budget films make?
             
data.agg(Lowest_Film=('USD_Production_Budget', min), Highest_Film=('USD_Production_Budget', max))

data.sort_values('USD_Production_Budget', ascending=False)[:1]
```

**Solution for Challenge 1**
We can answer many of the questions with a single command: `.describe()`. 

![Describe Image](https://img-b.udemycdn.com/redactor/raw/2020-10-14_17-25-22-50638b2907fc1a16098f440072858223.png)

The average film costs about $31m to make and makes around 3x that (or ~$89m) in worldwide revenue. So that's encouraging.

But quite a lot of films lose money too. In fact, all the films in the bottom quartile lose money, since the average cost is $5 million and they only bring in $3.8m in worldwide revenue!

The minimum domestic and worldwide revenue is $0. That makes sense. If a film never gets screened or is cancelled, then this is the number we would expect to see here.

On the other hand, the highest production budget was $425,000,000 and the highest worldwide revenue was $2,783,918,982. $2.7 Billion revenue! Holy smokes.

So which film was the lowest budget film in the dataset?

![Lowest Budget Film](https://img-b.udemycdn.com/redactor/raw/2020-10-14_17-28-28-0e643636fa2dfc616b2624c049e3be3e.png)

I've ... never heard of this film. But it looks like a real money maker. It grossed $181,041 with a measly $1,100 budget. 😮 Wow. Talk about return on investment! 

![My Date With Drew](https://img-b.udemycdn.com/redactor/raw/2020-10-14_17-31-29-814c8fa514cdd86e226534cd68167830.png)

And the highest budget film in the dataset is:

![Highest Budget Film](https://img-b.udemycdn.com/redactor/raw/2020-10-14_17-29-16-1e10adb271c1211de0b264b1c35ecbd7.png)

![Avatar](https://img-b.udemycdn.com/redactor/raw/2020-10-14_17-35-51-45a833f04cef1a441bdc004a84391593.png)

Sigh, I remember watching this film in the cinema with 3D glasses 🤓 and not wanting the film to ever end! I would have been quite content living with those blue people. 😊

## Challenge 2
How many films grossed $0 domestically (i.e., in the United States)? What were the highest budget films that grossed nothing?
- 512 films grossed $0 domestically
- Singularity, Aquaman, A Wrinkle in Time, Amusement Park, Don Gato el inicio de la pandilla

**My Code**

```py
print(len(data[data['USD_Domestic_Gross'] == 0]))
zero_domestic = data[data['USD_Domestic_Gross'] == 0]
zero_domestic.sort_values('USD_Production_Budget', ascending=False).head()
```

**Solution to Challenge 2: No domestic revenue**
We see that there are 512 films in the dataset that had no revenue in the United States. However, the highest budget films with no revenue have a release date AFTER the date on which the dataset was compiled (May 1st, 2018).
```py
    zero_domestic = data[data.USD_Domestic_Gross == 0]
    print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
    zero_domestic.sort_values('USD_Production_Budget', ascending=False)
```

![Movies weren't out yet](https://img-b.udemycdn.com/redactor/raw/2020-10-14_17-45-10-325d5e70022e4c7919caf7e6713d14ce.png)

## Challenge 3
How many films grossed $0 worldwide? What are the highest budget films that had no revenue internationally (i.e., the biggest flops)?
- 357 films grossed $0 internationally
- Singularity, Aquaman, A Wrinkle in Tim, Amusement Park, The Ridiculous 6

**My Code**
```py
print(len(data[data['USD_Worldwide_Gross'] == 0]))
zero_worldwide = data[data['USD_Worldwide_Gross'] == 0]
zero_worldwide.sort_values('USD_Production_Budget', ascending=False).head()
```

**Solution to Challenge 3: No worldwide revenue**
When we check worldwide revenue instead, we see that there are 357 films that made no money internationally. Once again, some of the films have not been released yet at the time the data was compiled. However, 512 versus 357. Why is there a difference? 

The reason some international films were never screened in the United States.  In fact, we can see an example of this in our previous screenshot. "Don Gato, el inicio de la pandilla" made about $4.5 million dollars in the box office, but nothing in the United States. Perhaps they should have screened it there too, considering it cost $80 million to make!
```py
    zero_worldwide = data[data.USD_Worldwide_Gross == 0]
    print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
    zero_worldwide.sort_values('USD_Production_Budget', ascending=False)
```

![International Grossing Films not in US](https://img-b.udemycdn.com/redactor/raw/2020-10-14_17-49-17-c0c42e8a463d6d79a09dadfe670a1b07.png)


# Filter on Multiple Conditions: International Films
So far, we've created subsets for our DataFrames based on a single condition. But what if we want to select our data based on more than one condition? For example, which films made money internationally (i.e., `data.USD_Worldwide_Gross != 0`), but had zero box office revenue in the United States (i.e., `data.USD_Domestic_Gross == 0`)? 

How would we create a filter for these two conditions? One approach is to use the `.loc[]` property combined with the [bitwise and](https://docs.python.org/3.4/library/operator.html#mapping-operators-to-functions) `&` operator.
```py
    international_releases = data.loc[(data.USD_Domestic_Gross == 0) & 
                                      (data.USD_Worldwide_Gross != 0)]
```
Why does this work? Pandas is built on top of NumPy, which uses Python's bitwise operators. And these bitwise operators allow us to do comparisons on an element by element basis in both NumPy and Pandas! Here's an example: 

![Example](https://img-b.udemycdn.com/redactor/raw/2020-10-14_18-25-38-1acab27e5b6c677db5828de681d34cbe.png)

However, we're also checking if the domestic revenue was zero and the worldwide revenue was not zero. Because the bitwise operator takes precedence, we need to include parentheses `()` around the comparisons we'd like to prioritise. 

```py
# Filtering on Multiple Conditions
international_releases = data.loc[(data.USD_Domestic_Gross == 0) &
                                  (data.USD_Worldwide_Gross != 0)]

print(f'Number of International Releases: {len(international_releases)}')
international_releases.head()
```

However, this is not the only technique we can use to make multiple comparisons. 

## Challenge
Use the Pandas [`.query()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) to accomplish the same thing. Create a subset for international releases that had some worldwide gross revenue, but made zero revenue in the United States.

Hint: This time you'll have to use the `and` keyword.

```py
international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
international_releases.head()
```

**Solution: Using the .query() function to filter on multiple conditions**
In this case, we enclose the entire query inside a string.

    international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
    print(f'Number of international releases: {len(international_releases)}')
    international_releases.tail()

The column names are recognised and we see the following:

![Results of .query](https://img-b.udemycdn.com/redactor/raw/2020-10-14_18-34-38-3cdecd04820328d2020a3300f5bab57c.png)

## Unreleased Films
Now we can turn our attention to films in the dataset that were not released at the time the data was collected. This is why films like Singularity and Aquaman had zero revenue. 

### Challenge
- Identify which films were not released yet as of the time of data collection (May 1st, 2018).
- How many films are included in the dataset that have not yet had a chance to be screened in the box office? 
- Create another DataFrame called `data_clean` that does not include these films. 

**My Code**
```py
films_not_released = data[data['Release_Date'] >= scrape_date]
films_not_released.head()

# How many films are included in the dataset that have not yet had a chance to be screened in the box office? 
films_not_released.describe() # 7

# Create another DataFrame called `data_clean` that does not include these films.
cond = data['Movie_Title'].isin(films_not_released['Movie_Title'])
data.drop(data[cond].index, inplace = True)

data
```

**Solution: Removing the unreleased films**
There are a total of 7 unreleased films at the time of data collection included in the dataset. 

![Identify Future Releases](https://img-b.udemycdn.com/redactor/raw/2020-10-14_18-46-19-04127ebc60d12d2a5eb14800bbfd7a7a.png)

From this point on, we'll work with another DataFrame called `data_clean` that does not include these films. 

```py
    data_clean = data.drop(future_releases.index)
```

### Bonus Challenge: Films that Lost Money
Having removed the unreleased films entirely can you calculate the percentage of films that did not break even at the box office? We already saw that more than the bottom quartile of movies appears to lose money when we ran `.describe()`. However, what is the true percentage of films where the costs exceed the worldwide gross revenue? 
- 37.2%

**My Code**

```py
total_film_count = len(data_clean)
costly_film_count = len(data_clean.query('USD_Production_Budget > USD_Worldwide_Gross'))

print(float(costly_film_count)/float(total_film_count))
```

**Solution: Budget greater than revenue**
Again, there are different ways you could have calculated this. For example, using the .loc[] property,
```py
    money_losing = data_clean.loc[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
    len(money_losing)/len(data_clean)
```
or the .query() function
```py
    money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
    money_losing.shape[0]/data_clean.shape[0]
```
In both cases, we see that a whopping 37.2% 😮 of films do not recoup their production budget at the box office. 💸💸💸 Who knew that film finance could be so risky! 😬

# Seaborn Data Visualization: Bubble Charts
We're now ready to visualise our data. Today I want to introduce you to another popular data visualisation tool that you can use alongside plotly and Matplotlib: [Seaborn](https://seaborn.pydata.org/). Seaborn is built on top of Matplotlib and it makes creating certain visualisations very convenient. 

![Seaborn Example](https://img-b.udemycdn.com/redactor/raw/2020-10-15_09-09-20-72497b72e13443b2cebd18af668ac37e.png)

## Import Seaborn

The first step is adding Seaborn to our notebook. By convention we'll use the name `sns`.

![Import Image](https://img-b.udemycdn.com/redactor/raw/2020-10-15_09-10-22-4722ef6ffbcef591bc19aa7b71133683.png)

## Seaborn Scatter Plots
To create a [.scatterplot()](https://seaborn.pydata.org/generated/seaborn.scatterplot.html?highlight=scatterplot#seaborn.scatterplot), all we need to do is supply our DataFrame and the column names that we'd like to see on our axes.
```py
    sns.scatterplot(data=data_clean,
                    x='USD_Production_Budget', 
                    y='USD_Worldwide_Gross')
```

That should look familiar. 😊 Because Seaborn is built on top of Matplotlib, we can dive into the Matplotlib layer anytime to configure our chart. For example, we can increase the size of our figure:

```py
plt.figure(figsize=(8,4), dpi=200)

sns.scatterplot(data=data_clean,
                x='USD_Production_Budget', 
                y='USD_Worldwide_Gross')

plt.show()
```

And to style our chart we can simply configure the `Axes` object that is returned from `sns.scatterplot()`.

![Returns Axes](https://img-b.udemycdn.com/redactor/raw/2020-10-15_09-19-14-d55c7a6c5b664184458469f081502617.png)

Here's how:
```py
plt.figure(figsize=(8,4), dpi=200)
  
ax = sns.scatterplot(data=data_clean,
                      x='USD_Production_Budget', 
                      y='USD_Worldwide_Gross')
  
ax.set(ylim=(0, 3000000000),
        xlim=(0, 450000000),
        ylabel='Revenue in $ billions',
        xlabel='Budget in $100 millions')
  
plt.show()
```

Here we're diving into the Matplotb layer to set the limits on the axes and change the labels. 

![Scatter Plot](https://img-b.udemycdn.com/redactor/raw/2020-10-15_09-21-28-2f57d90c5f1f97686b5c48b765b21051.png)

## From Scatter Plot to Bubble Chart
But the reason we're using Seaborn is because of the `hue` and `size` parameters that make it very easy to create a bubble chart. These parameters allow us to colour the data and change their size according to one of the columns in our DataFrame. 

```py
    plt.figure(figsize=(8,4), dpi=200)
    ax = sns.scatterplot(data=data_clean,
                         x='USD_Production_Budget', 
                         y='USD_Worldwide_Gross',
                         hue='USD_Worldwide_Gross', # colour
                         size='USD_Worldwide_Gross',) # dot size
     
    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions',)
     
    plt.show()
```

![Shmancy Bubble Chart](https://img-b.udemycdn.com/redactor/raw/2020-10-15_09-28-08-831897dbfc869643665e710decb79e5f.png)

Now our higher grossing movies are bigger and darker on our chart. That's super handy. But Seaborn offers a number of convenient styling options as well.

To set the styling on a single chart (as opposed to all the charts in the entire notebook) we can use Python's `with` keyword. We've seen `with` used already when it comes to opening files in previous lessons. 

```py
    plt.figure(figsize=(8,4), dpi=200)
     
    # set styling on a single chart
    with sns.axes_style('darkgrid'):
      ax = sns.scatterplot(data=data_clean,
                           x='USD_Production_Budget', 
                           y='USD_Worldwide_Gross',
                           hue='USD_Worldwide_Gross',
                           size='USD_Worldwide_Gross')
     
      ax.set(ylim=(0, 3000000000),
            xlim=(0, 450000000),
            ylabel='Revenue in $ billions',
            xlabel='Budget in $100 millions')
```

![Chart from Above Code](https://img-b.udemycdn.com/redactor/raw/2020-10-15_09-33-57-2840113022769b3f9be9fe8dc4667693.png)

In addition to `'darkgrid'`, Seaborn has a number of [built-in themes](https://python-graph-gallery.com/104-seaborn-themes/). so you can style your chart very quickly. Try out `'whitegrid'`, `'dark'`,  or `'ticks'` for example. 

## Challenge
Now that you've seen how to create a beautiful bubble chart in Seaborn, it's time to create your own. Can you write the code to replicate this chart? Notice how we are actually representing THREE dimensions in this chart: the budget, the release date, and the worldwide revenue. This is what makes bubble charts so awesomely informative. 

**My Code**
```py
plt.figure(figsize=(8,4), dpi=200)
  
# set styling on a single chart
with sns.axes_style('darkgrid'):
  ax = sns.scatterplot(data=data_clean,
                        x='Release_Date', 
                        y='USD_Worldwide_Gross',
                        hue='USD_Worldwide_Gross',
                        size='USD_Worldwide_Gross')
  
  ax.set(ylim=(0, 3000000000),
        xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
        ylabel='Budget in $100 millions',
        xlabel='Year')
```

**Solution: Movie Budgets over Time**
Alright, I hope that was fairly straightforward. All you needed to do is change a few arguments:
```py
    plt.figure(figsize=(8,4), dpi=200)
     
    with sns.axes_style("darkgrid"):
        ax = sns.scatterplot(data=data_clean, 
                        x='Release_Date', 
                        y='USD_Production_Budget',
                        hue='USD_Worldwide_Gross',
                        size='USD_Worldwide_Gross',)
     
        ax.set(ylim=(0, 450000000),
               xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
               xlabel='Year',
               ylabel='Budget in $100 millions')
```

**Analysis**
What do we see here? What is this chart telling us? Well, first off, movie budgets have just exploded in the last 40 years or so. Up until the 1970s, the film industry appears to have been in an entirely different era. Budgets started growing fast from the 1980s onwards and continued to grow through the 2000s. Also, the industry has grown massively, producing many more films than before. The number of data points is so dense from 2000 onwards that they are overlapping. 

![Graph Explanation](https://img-b.udemycdn.com/redactor/raw/2020-10-15_10-00-28-26cc75fe26fee70f2445c638aa490791.png)

# Floor Division: A Trick to Convert Years to Decades
In our bubble charts, we've seen how massively the industry has changed over time, especially from the 1970s onwards. This makes me think it makes sense to separate our films out by decade. Here's what I'm after:

![Goal Image](https://img-b.udemycdn.com/redactor/raw/2020-10-15_10-07-36-6a3655edec46115548a0f09bbd8b1173.png)

## Challenge

Can you create a column in `data_clean` that has the decade of the movie release. For example, a film released in 1992 or 1999 should have 1990 in the Decade column.

Here is one approach that you can follow:

1. Create a [`DatetimeIndex` object](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html) from the Release_Date column.
![Release Date Column](https://img-b.udemycdn.com/redactor/raw/2020-10-16_10-59-13-2ca82264854d799c5ea7a9aac7246b85.png)
2. Grab all the years from the `DatetimeIndex` object using the `.year` property.
3. Use floor division `//` to convert the year data to the decades of the films.
4. Add the decades as a `Decade` column to the `data_clean` DataFrame.

**My Code**
```py
test = data_clean
test["Decade"] = (pd.DatetimeIndex(test.Release_Date).year // 10) * 10
test
```

**Solution: Using Floor Division to Convert Years to Decades**
To create a DatetimeIndex, we just call the constructor and provide our release date column as an argument to initialise the DatetimeIndex object. Then we can extract all the years from the DatetimeIndex.
```py
dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year
```
Now, all we need to do is convert the years to decades. For that, we will use floor division (aka integer division). The difference to regular division is that the result is effectively rounded down.
```py
    5.0 / 2
    # output: 2.5
    5.0 // 2
    # output: 2.0
```
In our case, we will use the floor division by 10 and then multiplication by 10 to convert the release year to the release decade:

![Solution Image](https://img-b.udemycdn.com/redactor/raw/2020-10-16_11-13-38-ea1ff36ff1f36d1b44616077685626e5.png)

We can do this for all the years and then add the decades back as a column.
```py
    decades = years//10*10
    data_clean['Decade'] = decades
```

## Challenge
Create two new DataFrames: `old_films` and `new_films`
- `old_films` should include all the films before 1970 (up to and including 1969)
- `new_films` should include all the films from 1970 onwards
- How many of our films were released prior to 1970?
  - 153
- What was the most expensive film made prior to 1970?
  - $42 million

**My Code**
```py
data_clean.query('Decade < 1970')

new_films = data_clean.drop(data_clean.query('Decade <= 1960').index)
old_films = data_clean.drop(data_clean.query('Decade > 1960').index)

old_films.head()
new_films.head()

# How many films were released prior to 1970?
old_films.describe() # 153

# What was the most expensive film made prior to 1970?
# $42,000,000.00 for Cleopatra
```

**Solution: Separate the films made before and after 1970**
Now that we have our Decades column we can use it to create subsets of our data.
```py
old_films = data_clean[data_clean.Decade <= 1960]
new_films = data_clean[data_clean.Decade > 1960]
```
The cut-off for our calculation is 1960 in the Decade column because this will still include 1969. When we inspect our old_films DataFrame we see that it only includes 153 films. As we saw in the bubble chart, the bulk of films in the dataset have been released in the last 30 years.

![Old Films](https://img-b.udemycdn.com/redactor/raw/2020-10-16_11-29-47-b6944d0cec5baa62d332a7bcde19d8be.png)

The most expensive film prior to 1970 was Cleopatra, with a production budget of $42 million. That's some serious 1960s money, and judging by the trailer, a lot of it went into extravagant costumes, set design, and plenty of extras. Impressive. 

![Cleopatra](https://img-b.udemycdn.com/redactor/raw/2020-10-16_11-40-07-75393a74422b12f0ccc714e15e3eafbe.png)

# Plotting Linear Regressions with Seaborn
Let's visualise the relationship between the movie budget and the worldwide revenue using linear regression. Seaborn makes this incredibly easy with the [.regplot()](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot) function.
```py
sns.regplot(data=old_films, 
            x='USD_Production_Budget',
            y='USD_Worldwide_Gross')
```
This creates a scatter plot and draws a linear regression line together with the confidence interval at the same time.

To style the chart further, we can once again, drop into the Matplotlib layer and supply keyword arguments as dictionaries. We can customise the scatter plot (e.g., by changing the transparency of the dots) and the regression line itself (e.g., by changing the colour).

```py
plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("whitegrid"):
  sns.regplot(data=old_films, 
            x='USD_Production_Budget', 
            y='USD_Worldwide_Gross',
            scatter_kws = {'alpha': 0.4},
            line_kws = {'color': 'black'})
```

![RegPlot](https://img-b.udemycdn.com/redactor/raw/2020-10-16_11-54-26-bf6d69797f23a0d34875a64c59e36720.png)

What do we see here? Well, first off we can spot Cleopatra on the far right. But also, we see that many lower budget films made much more money! The relationship between the production budget and movie revenue is not very strong. Many points on the left are very far away for the line, so the line appears not to capture the relationship between budget and revenue very well at all!

But does the same hold true for the newer films?

## Challenge
Use Seaborn's `.regplot()` to show the scatter plot and linear regression line against the `new_films`.

**Style the chart**
- Put the chart on a `'darkgrid'`.
- Set limits on the axes so that they don't show negative values.
- Label the axes on the plot "Revenue in $ billions" and "Budget in $ millions".
- Provide HEX colour codes for the plot and the regression line. Make the dots dark blue (#2f4b7c) and the line orange (#ff7c43).

**My Code**
```py
plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("darkgrid"):
    ax = sns.regplot(data=new_films, 
            x='USD_Production_Budget', 
            y='USD_Worldwide_Gross',
            scatter_kws = {'alpha': 0.4, 'color': '#2f4b7c'},
            line_kws = {'color': 'black', 'color': '#ff7c43'})

    ax.set(ylim=(0, new_films.USD_Worldwide_Gross.max()),
           xlim=(0, new_films.USD_Production_Budget.max()),
           ylabel='Revenue in billions',
           xlabel='Budget in millions')
```

**Interpret the chart**
- Do our data points for the new films align better or worse with the linear regression than for our older films?
  - Better!
- Roughly how much would a film with a budget of $150 million make according to the regression line?
  - $500 million

**Solution: Plotting a regression against the newer films**
To style the chart we can use the same techniques as before: providing values for the `.regplot()` function, as well as making use of the Matplotlib Axes object to fine-tune the limits, labels, and general style.
```py
plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style('darkgrid'):
  ax = sns.regplot(data=new_films,
                    x='USD_Production_Budget',
                    y='USD_Worldwide_Gross',
                    color='#2f4b7c',
                    scatter_kws = {'alpha': 0.3},
                    line_kws = {'color': '#ff7c43'})
  
  ax.set(ylim=(0, 3000000000),
          xlim=(0, 450000000),
          ylabel='Revenue in $ billions',
          xlabel='Budget in $100 millions') 
```

![Answer Plot](https://img-b.udemycdn.com/redactor/raw/2020-10-16_14-53-50-e2314fcbccd1782b326fc9ea05367883.png)

How do we interpret our chart? This time we are getting a much better fit, compared to the old films. We can see this visually from the fact that our data points line up much better with our regression line (pun intended). Also, the confidence interval is much narrower. We also see that a film with a $150 million budget is predicted to make slightly under $500 million by our regression line. 

![$150 Million Budget Film](https://img-b.udemycdn.com/redactor/raw/2020-10-16_14-57-10-7c88b2c9af63e82477610c41a9fe6a4d.png)

All in all, we can be pretty confident that there does indeed seem to be a relationship between a film's budget and that film's worldwide revenue.

But how much of the variation in revenue does the budget actually explain? And how much extra revenue can we expect for an additional $1 increase in the budget? To find out, we need to dive into the numbers underlying our regression model.

# Use scikit-learn to Run Your Own Regression

# Learning Points & Summary