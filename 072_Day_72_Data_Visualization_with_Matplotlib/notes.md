# Day 72: Advanced - Data Visualization with Matplotlib: Programming Languages

## What You'll Make
Analyse the Popularity of Different Programming Languages over Time

The oldest programming language still in use today is FORTRAN, which was developed in 1957. Since then many other programming languages have been developed. But which programming language is the most popular? Which programming language is the Kim Kardashian of programming languages; the one people just can't stop talking about? 

StackOverflow will help us answer this burning question. Each post on Stack OverFlow comes with a Tag. And this Tag can be the name of a programming language. 

To figure out which language is the most popular, all we need to do is count the number of posts on Stack Overflow that are tagged with each language. The language with the most posts wins!

Today you will learn:

- How to visualise your data and create charts with Matplotlib
- How to pivot, group and manipulate your data with Pandas to get it into the format you want
- How to work with timestamps and time-series data
- How to style and customise a line chart to your liking


## Download and Open the Starter Notebook

### Open the Template
To help you with your Data Science journey I'll provide you with starter notebook which already has some of the sections and challenges laid out. Download the .zip file from this lesson's resources, unzip it, and upload it to Google Drive. There you can open the file as a Colab Notebook.

### Import the Data
In this lesson, I've also included a QueryResults.csv file with the Stack Overflow data that we'll be using. Download this .csv and add it to your notebook. 

### Challenge
For the next steps, let's review the data exploration that we've done yesterday:

1. Read the .csv file and store it in a Pandas DataFrame called df. Have a look at the `read_csv()` documentation and try to provide these column names: ['DATE', 'TAG', 'POSTS']
2. Look at the first and last 5 rows of the DataFrame.
3. How many rows and how many columns does it have?
4. Count the number of entries in each column.

#### 1
```py
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'])
```

#### 2
```py
df.head()
df.tail()
```

#### 3
```py
df.shape
```

#### 4
```py
df.value_counts()
```


## Solution: Preliminary Data Exploration
I hope the last steps were fairly straightforward. First, we import pandas and then we can call read_csv(), where we can provide some additional arguments, like the names for our columns.

```py
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
```

Setting the header row to 0 allows us to substitute our own column names. 

Next, we use `.head()` and `.tail()` to look at the first and last 5 rows. This allows us to verify that our column naming worked as intended.

To check the dimensions of the DataFrame, we use our old friend `.shape`. This tells us we have 1991 rows and 3 columns. 

To count the number of entries in each column we can use `.count()`. Note that .count() will actually tell us the number of non-NaN values in each column. 

### Next Challenge
The TAG is the name of the programming language. So for example in July 2008, there were 3 posts tagged with the language C#. Given that the TAG serves as our category column, can you figure out how to count the number of posts per language? Which programming language had the most number of posts since the creation of Stack Overflow? (Hint: you may need to review one of yesterday's lessons).

```py
df.groupby("TAG").sum("POSTS").sort_values(by="POSTS", ascending=False).head()
df.groupby("TAG").sum("POSTS").sort_values(by="POSTS", ascending=False).idxmax()
```

Also, some languages are older like C and other languages are newer (like Swift). The dataset starts in July 2008, so some languages will not have any posts for every month. Can you count how many months of posts exist for each programming language? 

```py
df["DATE"] = pd.to_datetime(df["DATE"])
df['TAG'].groupby([df.DATE.dt.month, df.TAG]).agg('count')
```

## Solution: Analysis by Programming Language
In order to look at the number of entries and the number of posts by programming language, we need to make use of the `.groupby()` method. The key is combining `.groupby()` with the TAG column, which holds as our categories (the names of the programming languages).

If we `.sum()` the number of posts then we can see how many posts each programming language had since the creation of Stack Overflow. 

```py
df.groupby("TAG").sum()
```

If we `.count()` the entries in each column, we can see how many months of entries exist per programming language. 

```py
df.groupby("TAG").count()
```

## Data Cleaning: Working with Time Stampes

### Selecting an Individual Cell
Let's take a closer look at the 'DATE' column in our DataFrame. We can use the double square bracket notation to look at the second entry in the column:

```py
df['DATE'][1]
```

Alternatively, for column names no spaces, we can also use the dot notation:

```py
    df.DATE[1]
```

I prefer the square bracket notation for column names since it's more flexible, but with the dot notation, you get to use autocomplete, which is also nice.

### Inspecting the Data Type
When we type check the contents of this cell, we see that we are not dealing with a date object, but rather with a string.

```py
type(df['DATE'][1])
```

This is not very handy. Not only will the string format always show that unnecessary 00:00:00, but we also don't get the benefit of working with Datetime objects, which know hot to handle dates and times. Pandas can help us convert the string to a timestamp using the [to_datetime()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html) method.

Here's how we can convert the entry in our cell and check that it worked:

```py
print(pd.to_datetime(df.DATE[1]))
type(pd.to_datetime(df.DATE[1]))
```

Let's use Pandas' `to_datetime()` to convert the entire `df['DATE']` column.

```py
# Convert Entire Column
df.DATE = pd.to_datetime(df.DATE)
df.head()
```

Now we can start thinking about how to manipulate our data so that we get a one column per programming language. For all of that and more, I'll see you in the next lesson.

## Data Manipulation: Pivoting DataFrames

## Data Visualization with Matplotlib

## Multi-Line Charts with Matplotlib

## Smoothing out Time-Series Data

## Quiz 18: Programming Language Data Analysis

## Learning Points & Summary