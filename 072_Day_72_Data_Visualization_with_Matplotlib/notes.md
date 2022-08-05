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

## Data Cleaning: Working with Time Stampes

## Data Manipulation: Pivoting DataFrames

## Data Visualization with Matplotlib

## Multi-Line Charts with Matplotlib

## Smoothing out Time-Series Data

## Quiz 18: Programming Language Data Analysis

## Learning Points & Summary