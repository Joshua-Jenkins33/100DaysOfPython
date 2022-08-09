# Day 73: Advanced - Aggregate & Merge Data with Pandas: Analyze the LEGO Dataset

## Today's Goals
- Learn to Aggregate and Merge Data in Pandas while Analysing a Dataset of LEGO Pieces

Today we're going to be diving deep into a dataset all about LEGO, which will help us answer a whole bunch of interesting questions about the history of the company, their product offering, and which LEGO set rules them all:
- What is the most enormous LEGO set ever created and how many parts did it have?
- In which year were the first LEGO sets released and how many sets did the company sell when it first launched?
- Which LEGO theme has the most sets? Is it Harry Potter, Ninjago, Friends or something else?
- When did the LEGO company really take-off based on its product offering? How many themes and sets did it release every year?
- Did LEGO sets grow in size and complexity over time? Do older LEGO sets tend to have more or fewer parts than newer sets? 

**What You'll Learn Today**
- How to combine a Notebook with HTML Markup.
- Apply Python List slicing techniques to Pandas DataFrames.
- How to aggregate data using the `.agg()` function.
- How to create scatter plots, bar charts, and line charts with two axes in Matplotlib.
- Understand database schemas that are organised by primary and foreign keys.
- How to merge DataFrames that share a common key

**Download and Open the Template Notebook**
Download the .zip file from this lesson. This contains the starter Notebook, some images, and the data. Unzip the file and add the Notebook to your Google Drive. 

**Add the Data to your Project**
Right-click to create a new folder called `data` and add the .csv files to the data folder (sadly dragging and dropping entire folders won't work).

If you are running the Notebook locally using Jupyter, I've supplied the image assets for you as well. If you're using Google Colab, then you won't need the assets folder. 

## Use HTML Markdown to Make Your Notebook Look Pretty
The cells inside the notebook can either be code cells for your Python code or Text (Markdown) cells. The starter notebook includes a few of these Text cells with section headings and challenge text. However, we can style these cells even more by using HTML (see Days 43 and 44). 

### Insert a Markdown Cell

Add a new Text cell below the Introduction. 

### Adding Images

Display an image in a Text cell, use an HTML `<img>` tag with the URL of the image. For example:
```html
    <img src="https://i.imgur.com/49FNOHj.jpg">
```
If you are using Jupyter Notebook instead of Google Colab, you can also link to one of the files provided in the .zip like so:
```html
    <img src="assets/bricks.jpg">
```

### Section Headings

You can add section headings using tags like `<h1>` or `<h2>`. However, the Notebook also has its own shorthand for common HTML tags. For example, you can use the `#` symbol as a shortcut. Here's how the headings change their size up to a minimum of `<h5>`

### Challenge
Now, let's get warmed up and write some Python code. Let's find out how many different colour LEGO bricks are actually in production!

Read the colors.csv file from the data folder and find the total number of unique colours.

There's a number of different ways you can accomplish this. Maybe try using the [.nunique()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nunique.html?highlight=nunique#pandas.DataFrame.nunique) from Pandas this time.

Also, figure out how many of the LEGO colours are transparent compared to how many colours are opaque. See if you can Google your way to finding at least two different ways of arriving at the answer. 

## Solution: Exploring the LEGO Brick Colors
### Import Pandas
As always, the first step is importing the module that we'll use: Pandas

```py
    import pandas as pd
```

### Examine the Structure
From there we can read the .csv file and take a look at the first 5 rows.
```py
    colors = pd.read_csv('data/colors.csv')
    colors.head()
```
We see that there are 5 columns, which include the name of the colour and its corresponding RGB value. To find the number of unique colours, all we need to do is check if every entry in the `name` column is unique: 
```py
    colors['name'].nunique()
```
This shows us that there are 135 unique colours for LEGO blocks.

### Find the Number of Transparent Colors
One way you can do this is through combining our old friend, the .groupby() method, with the .count() method.
```py
    colors.groupby('is_trans').count() 
```
Here we just group by the is_trans column and count the entries.

But you might have also come across the very handy [.value_counts()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html) method in your research.
```py
    colors.is_trans.value_counts()
```
Once again, we select the column (here with the .dot notation) and call the method. The .value_counts() method is a very quick way of finding the number of members of each category. 

### Challenge
Do you remember how to work with section headings and images? See if you can tackle the next couple of challenges to make your notebook look like this:

```md
![Image 1](https://i.imgur.com/aKcwkSx.png)
```

## Find the Oldest and Largest LEGO Sets

## Visualize the Number of Sets Published over Time

## How to use the Pandas `.agg()` function

## Superimposing Line Charts with Separate Axes

## Scatter Plots: Average Number of Parts per LEGO Set

## Relational Database Schemas: Primary and Foreign Keys

## How to Merge DataFrames and Create Bar Charts

## Learning Points and Summary