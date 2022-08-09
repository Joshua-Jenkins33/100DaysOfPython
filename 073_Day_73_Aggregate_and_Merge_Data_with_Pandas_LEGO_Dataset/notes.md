- [Day 73: Advanced - Aggregate & Merge Data with Pandas: Analyze the LEGO Dataset](#day-73-advanced---aggregate--merge-data-with-pandas-analyze-the-lego-dataset)
  - [Today's Goals](#todays-goals)
  - [Use HTML Markdown to Make Your Notebook Look Pretty](#use-html-markdown-to-make-your-notebook-look-pretty)
    - [Insert a Markdown Cell](#insert-a-markdown-cell)
    - [Adding Images](#adding-images)
    - [Section Headings](#section-headings)
    - [Challenge](#challenge)
  - [Solution: Exploring the LEGO Brick Colors](#solution-exploring-the-lego-brick-colors)
    - [Import Pandas](#import-pandas)
    - [Examine the Structure](#examine-the-structure)
    - [Find the Number of Transparent Colors](#find-the-number-of-transparent-colors)
    - [Challenge](#challenge-1)
  - [Find the Oldest and Largest LEGO Sets](#find-the-oldest-and-largest-lego-sets)
    - [Markdown Challenge Solution](#markdown-challenge-solution)
    - [Exploring the sets.csv](#exploring-the-setscsv)
    - [Solution](#solution)
  - [Visualize the Number of Sets Published over Time](#visualize-the-number-of-sets-published-over-time)
    - [Challenge](#challenge-2)
      - [Solution: Sets Per Year](#solution-sets-per-year)
  - [How to use the Pandas `.agg()` function](#how-to-use-the-pandas-agg-function)
    - [Number of Themes per Calendar Year](#number-of-themes-per-calendar-year)
    - [Challenge](#challenge-3)
  - [Superimposing Line Charts with Separate Axes](#superimposing-line-charts-with-separate-axes)
    - [Two Separate Axes](#two-separate-axes)
  - [Scatter Plots: Average Number of Parts per LEGO Set](#scatter-plots-average-number-of-parts-per-lego-set)
    - [Complexity Over Time](#complexity-over-time)
      - [Challenge](#challenge-4)
      - [Solution](#solution-1)
      - [Challenge](#challenge-5)
      - [Solution](#solution-2)
  - [Relational Database Schemas: Primary and Foreign Keys](#relational-database-schemas-primary-and-foreign-keys)
    - [Number of Sets per LEGO Theme](#number-of-sets-per-lego-theme)
      - [Mini-Challenge](#mini-challenge)
      - [Solution](#solution-3)
    - [Working with a Relational Database](#working-with-a-relational-database)
    - [Understand the theme.csv file](#understand-the-themecsv-file)
      - [Challenge](#challenge-6)
      - [Solution](#solution-4)
  - [How to Merge DataFrames and Create Bar Charts](#how-to-merge-dataframes-and-create-bar-charts)
    - [The Pandas `.merge()` function](#the-pandas-merge-function)
    - [Creating a Bar Chart](#creating-a-bar-chart)
  - [Learning Points and Summary](#learning-points-and-summary)

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
Wouldn't it be nice to have the number of themes and the number sets on the same chart? But what do we get if we just plot both of them the way we have before? 

```py
# This looks terrible
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
```

Well, that's not very informative! 🤦‍♀️ The problem is that the "number of themes" and the "number of sets" have very different scales. The theme number ranges between 0 and 90, while the number of sets ranges between 0 and 900. So what can we do?

### Two Separate Axes
We need to be able to configure and plot our data on two separate axes on the same chart. This involves getting hold of an axis object from Matplotlib. 

```py
ax1 = plt.gca() # get current axes
ax2 = ax1.twinx() 
```

We then create another axis object: `ax2`. The key thing is that by using the `.twinx()` method allows `ax1` and `ax2` to share the same x-axis. When we plot our data on the axes objects we get this:

```py
ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
```

That's very nice! But there's one problem: we can't tell the lines apart because they have the same colour! Let's add some styling. Let's:

- colour in the lines
- colour in the axes and
- add some labels

so that we can see what's going on. Here's what we get:

```py
ax1 = plt.gca() # get current axes
ax2 = ax1.twinx() 

# add styling
ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], 'b')

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='green')
ax2.set_ylabel('Number of Themes', color='blue')
```

## Scatter Plots: Average Number of Parts per LEGO Set

### Complexity Over Time
Have LEGO sets become larger and more complex over time? Let's work out the average number of parts per LEGO set. This is the perfect time to revise how to use the `.agg()` function.

#### Challenge
Create a Pandas Series called parts_per_set that has the year as the index and contains the average number of parts per LEGO set in that year. Here's what you're looking to create:

```py
parts_per_set = sets.groupby("year").agg({'num_parts':'mean'})
```

#### Solution
Once again, we're going to use the `.groupby()` and the `.agg()` function together to work this one out. However, this time we pass a dictionary to the `.agg()` function so that we will target the num_parts column with the `mean()` function. That way, we group our data by year and then we average the number of parts for that year.

```py
parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
```

To visualise our `parts_per_set` data, let's create a scatter plot. A scatter plot simply uses dots to represent the values of each data point.

#### Challenge
See if you can use [the Matplotlib documentation](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.scatter.html) to generate the scatter plot chart. Do you spot a trend in the chart? Again, you'll have to exclude the last two observations.


I'll provide the solution below.

```py
plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
```

#### Solution
We just need to call the `.scatter()` instead of the `.plot()` method to create the chart. For the x-values, we'll use the index of the `parts_per_set` Series (the years) and for the y-values, we'll use the values of the series (the column name happens to be `num_parts`). 

```py
plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
```

From the chart, we can definitely make out an upward trend in the size and complexity of the LEGO sets based on the average number of parts. In the 2010s the average set contained around 200 individual pieces, which is roughly double what average LEGO set used to contain in the 1960s. 

## Relational Database Schemas: Primary and Foreign Keys
LEGO has licensed many hit franchises from Harry Potter to Marvel Super Heros to many others. But which theme has the largest number of individual sets? Is it one of LEGO's own themes like Ninjago or Technic or is it a third party theme? Let's analyse LEGO's product lines in more detail!

### Number of Sets per LEGO Theme
To count the number of sets per Theme we can use the `.value_counts()` method on our `theme_id` column. But there's one problem:

```py
set_theme_count = sets["theme_id"].value_counts()
set_theme_count[:5]
```

We have no idea what our themes are actually called! 🤨 Ok, we can see that the theme with id 158 is the largest theme containing 753 individual sets, but what's that theme called? This is not very helpful. We need to find the names of the themes based on the `theme_id` from the `themes.csv` file. 

#### Mini-Challenge
Display the database schema (link: https://i.imgur.com/Sg4lcjx.png) inside the Notebook.

```md
![Database Schema](https://i.imgur.com/Sg4lcjx.png)
```

#### Solution
To display an image in a Text (aka Markdown) cell, all you need to do is use the HTML `<img>` tag.
```md
<img src="https://i.imgur.com/Sg4lcjx.png">
```

### Working with a Relational Database
What is a database schema? A **schema** is just how the database is organized. Many relational databases, such as our LEGO data, is split into individual tables. We have separate tables for the colours, the sets and the themes. With a relational database, the tables are linked to each other through their **keys**.

### Understand the theme.csv file
The *themes.csv* file has the actual theme names. How is this table linked to the others tables? Well, the *sets.csv* has **theme_ids** which match the id column in the *themes.csv*.

This means that the **theme_id** is the **foreign key** inside the *sets.csv*. Many different sets can be part of the same theme. But inside the themes.csv, each theme_id, which is just called `id` is unique. This uniqueness makes the `id` column the **primary key** inside the *themes.csv*. To see this in action, explore the themes.csv. 

#### Challenge
How is the themes.csv structured?
- id
- name
- parent

Search for the name 'Star Wars'. How many `id`s correspond to the 'Star Wars' name in the themes.csv?
- 18
- 158
- 209
- 261

**4 themes correspond to Star Wars.**

Use the `id`s you just found and look for the corresponding sets in the sets.csv (Hint: you'll need to look for matches in the `theme_id` column).

```py
star_wars_ids = [18, 158, 209, 261]

# sets[sets['theme_id'] == 18]
sets[sets['theme_id'].isin(star_wars_ids)]
```

#### Solution
Looking at the first 5 rows, we see the column names. Each value in the id column is unique (this is the primary key for the themes table). The theme names are not unique. If we search for the name "Star Wars", we see that 4 different ids correspond to that name. 

```py
themes = pd.read_csv('data/themes.csv')
themes.head()

themes[themes.name == 'Star Wars']
```

Why would Star Wars have so many different themes? We can check which products corresponded to those themes in the sets.csv:

```py
sets[sets.theme_id == 18]
```

Star Wars is a really long-running franchise. Theme number 18 was running from 2000 to 2002 and seems to be comprised of several of the show's characters. What about, say theme 209?

```py
sets[sets.theme_id == 209]
```

Here we see that all of the Star Wars Advent Calendars share the same theme_id. That makes sense. 

## How to Merge DataFrames and Create Bar Charts
Wouldn't it be nice if we could combine our data on theme names with the number sets per theme? 

Let's use the [.merge() method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge) to combine two separate DataFrames into one. The merge method works on columns with the same **name** in both DataFrames.

Currently, our theme_ids and our number of sets per theme live inside a Series called `set_theme_count`. 

```py
set_theme_count = sets["theme_id"].value_counts()
set_theme_count[:5]
```

To make sure we have a column with the name `id`, I'll convert this Pandas Series into a Pandas DataFrame. 

```py
set_theme_count = pd.DataFrame({'id':set_theme_count.index,
                                'set_count':set_theme_count.values})

set_theme_count.head()
```

Here I'm providing a dictionary to create the DataFrame. The keys in the dictionary become my column names.


### The Pandas `.merge()` function
To [.merge()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html) two DataFrame along a particular column, we need to provide our two DataFrames and then the **column name** on which to merge. This is why we set `on='id'`. Both our `set_theme_count` and our `themes` DataFrames have a column with this name.

```py
merged_df = pd.merge(set_theme_count, themes, on='id')
```

The first 3 rows in our merged DataFrame look like this:

```py
merged_df = pd.merge(set_theme_count, themes, on='id')
merged_df[:3]
```

Aha! Star Wars is indeed the theme with the most LEGO sets. Let's plot the top 10 themes on a chart.

### Creating a Bar Chart
Matplotlib can create almost any chart imaginable with very few lines of code. Using [.bar()](https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.pyplot.bar.html) we can provide our theme names and the number of sets. This is what we get:

```py
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
```

That worked, but it's almost unreadable. 😩 The good thing for us is that we already know how to customize our charts! Here's what we get when we increase the size of our figure, add some labels, and most importantly, rotate the category names on the x-axis so that they don't overlap.

```py
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
  
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
```

Niiiiice.😌 So what can we see here? Well, a couple of these themes like Star Wars, Town, or Ninjago are what I would think of when I think of LEGO. However, it looks like LEGO also produces a huge number of ... books and key chains?!?! I guess I'm showing my age here, but it's interesting that the LEGO company seems to produce so much more these days than just plastic bricks. The 'Gear' category itself is huge and includes everything from bags to pencil cases apparently. Has LEGO strayed from its core business or is it successfully diversifying? That we can't answer from our dataset. I'll leave that one up to a business school case study to decide. 🤷‍♀️

## Learning Points and Summary
In this lesson we looked at how to:

- use HTML Markdown in Notebooks, such as section headings `#` and how to embed images with the `<img>` tag.
- combine the `groupby()` and `count()` functions to aggregate data
- use the `.value_counts()` function
- slice DataFrames using the square bracket notation e.g., `df[:-2]` or `df[:10]`
- use the `.agg()` function to run an operation on a particular column
- `rename()` columns of DataFrames
- create a line chart with two separate axes to visualise data that have different scales.
- create a scatter plot in Matplotlib
- work with tables in a relational database by using primary and foreign keys
- `.merge()` DataFrames along a particular column
- create a bar chart with Matplotlib


You can download the completed code for today in this lesson.


Today was another super packed day. I hope you found digging into LEGOs product catalogue as fascinating as I have. Have a good rest and I'll see you tomorrow! 💪


