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

### Markdown Challenge Solution
Here's how you'd organise the markdown cells with the section headings and image tags. You might have also spotted that enclosing text in the double-asterisk ** symbol will make it bold. 

### Exploring the sets.csv
The sets.csv contains a list of LEGO sets. It shows in which year the set was released and the number of parts in the set.

Can you take the first steps in exploring this dataset? Read the .csv and take a look at the columns.

Then try and answer the following questions:

- In which year were the first LEGO sets released and what were these sets called?
- How many different products did the LEGO company sell in their first year of operation?
- What are the top 5 LEGO sets with the most number of parts? 

```py
year = sets.year.min()

sets[sets['year'] == year]

sets[sets['year'] == year]['year'].count()

sets.sort_values('num_parts', ascending=False).head(5)

```

Scroll down to see the solution below...

### Solution
The first step as always is reading the .csv file and looking what's in it. We see that there's some sort of id for each set (the set_num), the name of the set, the year in which it was released, the theme_id (the code for the theme name) and the number of parts.

So it looks like we have everything we here to answer our two questions.

```py
sets = pd.read_csv('data/sets.csv')
sets.head()

sets.tail()
```

To find the year when the FIrst LEGO sets were released we have to sort by the year column. The [.sort_values()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html?highlight=sort_values#pandas.DataFrame.sort_values) method will b ydefault sort in ascending order.

```py
sets.sort_values('year').head()
```

Looks like LEGO started all the way back in 1949! 😮 The names for these sets are nothing to write home about, but let's find out how many different products the company was selling in their first year since launch:

```py
sets[sets['year'] == 1949]
```

Back in 1949, LEGO got started selling only 5 different sets! Note that here we are filtering our DataFrame on a **condition**. We are retrieving the rows where the year column has the value 1949: `sets['year'] == 1949`. 

Now let's find the LEGO set with the largest number of parts. If we want to find the largest number of parts, then we have to set the `ascending` argument to `False` when we sort by the num_parts column. 

```py
sets.sort_values('num_parts', ascending=False).head()
```

The largest LEGO set ever produced has around 10,000 pieces! Apparently, only two of these boxes were ever produced, so if you wanted to get your hands on a ridiculously large LEGO set, you'll have to settle for the 7,541 piece Millennium Falcon. 

## Visualize the Number of Sets Published over Time
Now let's take a look at how many sets the LEGO company has published year-on-year. This might tell us something about how LEGO's product offering has changed over time.

First, let's import Matplotlib so we can visualise our findings up top:

### Challenge
Now, let's create a new Series called `sets_by_year` which has the years as the index and the number of sets as the value. 

```py
sets_by_year = sets.groupby('year').count()
sets_by_year.set_num.head()
```

Having summed the number of LEGO sets per year, visualise this data using a line chart with Matplotlib. 

```py
plt.figure(figsize=(16,10))
sets_by_year.plot.line()
plt.xlabel('Year', fontsize=14)
plt.ylabel('LEGO Set Count', fontsize=14)
```

Because the .csv file is from late 2020, to plot the full calendar years, you will have to exclude some data from your chart. Use the slicing techniques covered in Day 21 to avoid plotting the last two years? The same syntax will work on Pandas DataFrames. 

```py
sets_by_year[0,-2].plot.line()
```

#### Solution: Sets Per Year
The trick is grouping the data by the year and counting the number of entries for that year. 

```py
sets_by_year = sets.groupby('year').count()
sets_by_year['set_num'].head()
sets_by_year['set_num'].tail()
```

From this, we can see that LEGO published less than 10 different sets per year during its first few years of operation. But by 2019 the company had grown spectacularly, releasing 840 sets in that year alone!

You also notice that there is an entry for 2021. The .csv file is from late 2020, so it appears that it already includes some sets on a forward-looking basis. We'll have to take this into account for our charts:
```py
    plt.plot(sets_by_year.index, sets_by_year.set_num)
```
If we don't exclude the last two years we get a dramatic drop at the end of the chart. This is quite misleading as it suggests LEGO is in big trouble! Given the dataset does not include a full calendar year for 2020, it's best to exclude the last two rows to get a better picture:
```py
    plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
```
The Python List slicing syntax covered in Day 21 comes in quite handy here! 

We also see that while the first 45 years or so, LEGO had some steady growth in its product offering, but it was really in the mid-1990s that the number of sets produced by the company increased dramatically! We also see a brief decline in the early 2000s and a strong recovery around 2005 in the chart. 

## How to use the Pandas `.agg()` function
Often you find yourself needing to summarise data. This is where the .groupby() function comes in really handy. However, sometimes you want to run even more operations based on a particular DataFrame column. This is where the [.agg()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html) method comes in.

In our case, we want to calculate the number of different themes by calendar year. This means we have to group the data by year and then count the number of unique theme_ids for that year. 

### Number of Themes per Calendar Year
We can accomplish this by chaining the `.groupby()` and the `.agg()` functions together:
```py
themes_by_year = sets.groupby("year").agg({"theme_id": pd.Series.nunique})
```
Note, the `.agg()` method takes a dictionary as an argument. In this dictionary, we specify which operation we'd like to apply to each column. In our case, we just want to calculate the number of unique entries in the theme_id column by using our old friend, the `.nunique()` method.

Let's give our column in `themes_by_year` a more appropriate name and let's take a look at what we've got:

```py
themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns = {'theme_id':'nr_themes'}, inplace=True)
themes_by_year.head() 
themes_by_year.tail()
```

Here we can see that LEGO only had 2 themes during the first few years, but just like the number of sets the number of themes expanded manifold over the years. Let's plot this on a chart again. 

### Challenge
Create a line plot of the number of themes released year-on-year. Only include the full calendar years in the dataset (1949 to 2019). 

```py
themes_by_year[0:-2].plot.line()
### or
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
```

Again, we're using the same slicing technique as before. In the chart, we can see that LEGO has pretty consistently added more and more themes until the mid-1990s. From then the number of themes has stagnated for around 10 years or so until the early 2010s. 

## Superimposing Line Charts with Separate Axes

## Scatter Plots: Average Number of Parts per LEGO Set

## Relational Database Schemas: Primary and Foreign Keys

## How to Merge DataFrames and Create Bar Charts

## Learning Points and Summary