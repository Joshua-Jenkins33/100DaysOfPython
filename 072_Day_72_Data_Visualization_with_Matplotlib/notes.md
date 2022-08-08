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

### The [.pivot()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html) Method

Sometimes you want to convert your DataFrame so that each category has its own column. For example, suppose you needed to take the table below and create a separate column for each actor, where each row is the Age of the actor.

| Age   | Actor     | Power |
|-------|-----------|-------|
| Young | Jack      | 100   |
| Young | Arnold    | 80    |
| Young | Keanu     | 25    |
| Young | Sylvester | 50    |
| Old   | Jack      | 99    |
| Old   | Arnold    | 75    |

| Actor | Arnold | Jack  | Keanu | Sylvester |
|-------|--------|-------|-------|-----------|
| Age   |        |       |       |           |
| Old   | 75.0   | 99.0  | 5.0   | NaN       |
| Young | 80.0   | 100.0 | 25.0  | 50.0      |

How would you do this with the DataFrame below? 

```py
test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
test_df
```

The easiest way to accomplish this is by using the `.pivot()` method in Pandas. Try the example for yourself. The thing to understand is how to supply the correct aguments to get the desired outcome. The index are the categories for the rows. The columns are the categories for the columns. And the values are what you want in the new cells.  

```py
pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
pivoted_df
```

However, there's one very important thing to notice. What happens if a value is missing? In the example above there's no value for old Sylvester. In this case, the .pivot() method will insert a NaN value.

### Mini-Challenge
1. Can you pivot the `df` DataFrame so that each row is a date and each column is a programming language? Store the result under a variable called `reshaped_df`. 
2. Examine the dimensions of the reshaped DataFrame. How many rows does it have? How many columns?
3. Examine the head and the tail of the DataFrame. What does it look like?
4. Print out the column names.
5. Count the number of entries per column. 

#### My Solution

```py
# 1
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df

# 2
reshaped_df.shape

# 3
reshaped_df.head()
reshaped_df.tail()

# 4
for col in reshaped_df:
    print(col)

# 5
reshaped_df.count()
```

#### Instructor Solution
Here's how you pivot our existing DataFrame to get the outcome above:
```py
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
```

We have 145 rows and 14 columns in the new DataFrame. Each programming language became a column and our date column became the new index (i.e., the label for the rows). 

When we count the number of entries per column we see that not all languages are the same. The reason is that the .count() method excludes NaN values. When we pivoted the DataFrame the NaN values were inserted when there were no posts for a language in that month (e.g., Swift in July, 2008). 

```py
# 2
resahped_df.shape

# 3
reshaped_df.columns

# 4
reshaped_df.head()

# 5
reshaped_df.count()
```

### Dealing with NaN Values
In this case, we don't want to drop the rows that have a NaN value. Instead, we want to substitute the number 0 for each NaN value in the DataFrame. We can do this with the `.fillna()` method.

```py
reshaped_df.fillna(0, inplace=True) 
```

The `inplace` argument means that we are updating reshaped_df. Without this argument we would have to write something like this:

```py
reshaped_df = reshaped_df.fillna(0) 
reshaped_df.head()
```

Let's check if we successfully replaced all the NaN values in our DataFrame. 

We can also check if there are any NaN values left in the entire DataFrame with this line:

```py
reshaped_df.isna().values.any()
```

Here we are using the `.isna()` method that we've used before, but we're chaining two more things: the `values` attribute and the` any()` method. This means we don't have to search through the entire DataFrame to spot if `.isna()` is True. 

Now we're all set to create some charts and visualise our data. For all of that and more, I'll see you in the next lesson!

## Data Visualization with Matplotlib

### Matplotlib
To create our first charts we're going to use a library called [Matplotlib](https://matplotlib.org/). There are many different libraries in Python to help us create charts and graphs. Matplotlib is an incredibly popular one and it works beautifully in combination with Pandas, so let's check it out.

First, we have to import Matplotlib.

```py
import matplotlib.pyplot as plt
```

Let's do this at the top.

#### Mini Challenge
You can actually show a line chart for the popularity of a programming language using only a single line of code. Can you use the [.plot() documentation](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) to figure out how to do this? Try and plot the popularity of the Java programming language. 

```py
java_df = reshaped_df.filter(items=['java', 'python'], axis=1)
java_df.plot.line()
```
##### Solution
All you need to do is supply the values for the horizontal axis (the x-values) and the vertical axis (the y-values) for the chart. The x-values are our dates and the y-values are the number of posts. We can supply these values to the .plot() function by position like so:

```py
plt.plot(reshaped_df.index, reshaped_df.java)
```

or like so if you prefer the square bracket notation.

```py
plt.plot(reshaped_df.index, reshaped_df['java'])
```

### Styling the Chart
Let's look at a couple of methods that will help us style our chart:

`.figure()` - allows us to resize our chart

`.xticks()` - configures our x-axis

`.yticks()` - configures our y-axis

`.xlabel()` - add text to the x-axis

`.ylabel()` - add text to the y-axis

`.ylim()` - allows us to set a lower and upper bound 

To make our chart larger we can provide a width (16) and a height (10) as the figsize of the figure. 

```py
plt.figure(figsize=(16,10)) 
plt.plot(reshaped_df.index, reshaped_df.java)
```

This will make our chart easier to see. But when we increase the size of the chart, we should also increase the fontsize of the ticks on our axes so that they remain easy to read.

Now we can add labels. Also, we're never going to get less than 0 posts, so let's set a lower limit of 0 for the y-axis with `.ylim()`.

```py
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
```

### Challenge
Now that you've successfully created and styled your chart, can you figure out how to plot both Java and Python next to each other?

```py
plt.figure(figsize=(16,10)) 
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
```


## Multi-Line Charts with Matplotlib

### Solution: Two Line Charts Next to Each Other
The trick is simply calling the .plot() method twice. That's all there is to it! =)

```py
plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python) # Tadah!
```

But what if we wanted to plot all the programming languages on the same chart? We don't want to type out .plot() a million times, right? We can actually just use a for-loop:

```py
    for column in reshaped_df.columns:
        plt.plot(reshaped_df.index, reshaped_df[column])
```

This will allow us to iterate over each column in the DataFrame and plot it on our chart.

But wait, which language is which? It's really hard to make out without a legend that tells us which colour corresponds to each language. Let's modify the plotting code to add a label for each line based on the column name (and make the lines thicker at the same time using linewidth). Then let's add a legend to our chart: 

```py
    plt.figure(figsize=(16,10))
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Number of Posts', fontsize=14)
    plt.ylim(0, 35000)
     
    for column in reshaped_df.columns:
        plt.plot(reshaped_df.index, reshaped_df[column], 
                 linewidth=3, label=reshaped_df[column].name)
     
    plt.legend(fontsize=16) 
```

Looks like Python is the most popular programming language judging by the number of posts on Stack Overflow! Python for the win! =) 

## Smoothing out Time-Series Data
Looking at our chart we see that time-series data can be quite noisy, with a lot of up and down spikes. This can sometimes make it difficult to see what's going on.

A useful technique to make a trend apparent is to smooth out the observations by taking an average. By averaging say, 6 or 12 observations we can construct something called the rolling mean. Essentially we calculate the average in a window of time and move it forward by one observation at a time.

Since this is such a common technique, Pandas actually two handy methods already built-in: `rolling()` and `mean()`. We can chain these two methods up to create a DataFrame made up of the averaged observations. 

```py
    # The window is number of observations that are averaged
    roll_df = reshaped_df.rolling(window=6).mean()
     
    plt.figure(figsize=(16,10))
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Number of Posts', fontsize=14)
    plt.ylim(0, 35000)
     
    # plot the roll_df instead
    for column in roll_df.columns:
        plt.plot(roll_df.index, roll_df[column], 
                 linewidth=3, label=roll_df[column].name)
     
    plt.legend(fontsize=16)
```

Play with the `window` argument (use `3` or `12`) and see how the chart changes!


## Quiz 18: Programming Language Data Analysis

## Learning Points & Summary