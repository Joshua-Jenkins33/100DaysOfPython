- [Day 75: Advanced - Beautiful Plotly Charts & Analyzing the Android App Store](#day-75-advanced---beautiful-plotly-charts--analyzing-the-android-app-store)
- [What We'll Make](#what-well-make)
  - [Wrestle the Android App Store Data into Beautiful Looking Charts with Plotly](#wrestle-the-android-app-store-data-into-beautiful-looking-charts-with-plotly)
- [Data Cleaning: Removing NaN Values and Duplicates](#data-cleaning-removing-nan-values-and-duplicates)
  - [Preliminary Data Exploration](#preliminary-data-exploration)
- [Preliminary Exploration: The Highest Ratings, Most Reviews, and Largest Size](#preliminary-exploration-the-highest-ratings-most-reviews-and-largest-size)
- [Data Visualization with Plotly: Create Pie and Donut Charts](#data-visualization-with-plotly-create-pie-and-donut-charts)
- [Numeric Type Conversions for the Installations & Price Data](#numeric-type-conversions-for-the-installations--price-data)
- [Plotly Bar Charts & Scatter Plots: The Most Competitive & Popular App Categories](#plotly-bar-charts--scatter-plots-the-most-competitive--popular-app-categories)
- [Extracting Nested Column Data using `.stack()`](#extracting-nested-column-data-using-stack)
- [Grouped Bar Charts and Box Plots with Plotly](#grouped-bar-charts-and-box-plots-with-plotly)
- [Learning Points & Summary](#learning-points--summary)

# Day 75: Advanced - Beautiful Plotly Charts & Analyzing the Android App Store

# What We'll Make

## Wrestle the Android App Store Data into Beautiful Looking Charts with Plotly
Have you ever thought about building your own an iOS or Android app? If so, then you probably have wondered about how things work in the app stores. Today we'll replicate some of the app store analytics provided by companies like App Annie or Sensor Tower that helps inform development and app marketing strategies for many companies. This stuff is BIG business!

In this module, we will compare thousands of apps in the Google Play Store so that we can gain insight into:
- How competitive different app categories (e.g., Games, Lifestyle, Weather) are
- Which app category offers compelling opportunities based on its popularity
- How many downloads you would give up by making your app paid vs. free
- How much you can reasonably charge for a paid app
- Which paid apps have had the highest revenue 
- How many paid apps will recoup their development costs based on their sales revenue

**Today you'll learn:**
- How to quickly remove duplicates
- How to remove unwanted symbols and convert data into a numeric format
- How to wrangle columns containing nested data with Pandas
- How to create compelling data visualisations with the plotly library
- Create vertical, horizontal and grouped bar charts
- Create pie and donut charts for categorical data
- Use colour scales to make beautiful scatter plots

**Download and add the Notebook to Google Drive**
As usual, download the .zip file from this lesson and extract it. Add the .ipynb file into your Google Drive and open it as a Google Colaboratory notebook.

**Add the Data to the Notebook**
The .zip file also includes a .csv file. This is the data for the project. Add this your notebook.
# Data Cleaning: Removing NaN Values and Duplicates
The first step as always is getting a better idea about what we're dealing with.

## Preliminary Data Exploration
**Challenge.** How many rows and columns does df_apps have? What are the column names? What does the data look like? Look at a random sample of 5 different rows with [.sample()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html).

```py
df_apps.shape
df_apps.columns
df_apps.sample(5)
```

**Solution.** Compared to the previous projects we are working with a fairly large DataFrame this time.

```py
df_apps.shape
```

tells us we have 10841 rows and 12 columns.

We can already see that there are some data issues that we need to fix. In the Ratings and Type columns there are NaN (Not a number values) and in the Price column we have dollar signs that will cause problems.

The `.sample(n)` method will give us n random rows. This is another handy way to inspect our DataFrame.

**Challenge.** Remove the columns called Last_Updated and Android_Version from the DataFrame. We will not use these columns.


How many rows have a NaN value (not-a-number) in the Rating column? Create DataFrame called `df_apps_clean` that does not include these rows.

```py
df_apps_dropped_columns = df_apps.drop(columns=['Last_Updated', 'Android_Ver'])

df_apps_dropped_columns.Rating.isnull().sum().sum()

df_apps_clean = df_apps_dropped_columns.dropna()
df_apps_clean.head()
```

**Solution: Dropping Unused Columns and Removing NaN Values**
To remove the unwanted columns, we simply provide a list of the column names `['Last_Updated', ‘Android_Ver']` to the `.drop()` method. By setting `axis=1` we are specifying that we want to drop certain columns.

To find and remove the rows with the NaN values we can create a subset of the DataFrame based on where `.isna()` evaluates to `True`. We see that NaN values in ratings are associated with no reviews (and no installs). That makes sense.

We can drop the NaN values with `.dropna()`:

```py
df_apps_clean = df_apps.dropna()
df_apps_clean.shape
```

This leaves us with 9,367 entries in our DataFrame. But there may be other problems with the data too:

**Challenge.** Are there any duplicates in data? Check for duplicates using the [.duplicated()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html) function. How many entries can you find for the "Instagram" app? Use [.drop_duplicates()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html) to remove any duplicates from `df_apps_clean`.

```py
df_apps_clean = df_apps_clean.drop_duplicates()
df_apps_clean.duplicated()
```

**Solution: Finding and Removing Duplicates**
There are indeed duplicates in the data. We can show them using the .`duplicated`() method, which brings up 476 rows:

```py
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
print(duplicated_rows.shape)
duplicated_rows.head()
```

We can actually check for an individual app like ‘Instagram’ by looking up all the entries with that name in the App column.

So how do we get rid of duplicates? Can we simply call `.drop_duplicates()`?

```py
df_apps_clean = df_apps_clean.drop_duplicates()
```

Not really. If we do this without specifying how to identify duplicates, we see that 3 copies of Instagram are retained because they have a different number of reviews. We need to provide the column names that should be used in the comparison to identify duplicates.

```py
df_apps_clean[df_apps_clean.App == 'Instagram']
df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])
df_apps_clean[df_apps_clean.App == 'Instagram']
```

This leaves us with 8,199 entries after removing duplicates. Huzzah! 💪

**What Else Should I Know About the Data?**
So we can see that 13 different features were originally scraped from the Google Play Store.
- Obviously, the data is just a sample out of all the Android apps. It doesn't include all Android apps of which there are millions.
- I’ll assume that the sample is representative of the App Store as a whole. This is not necessarily the case as, during the web scraping process, this sample was served up based on geographical location and user behaviour of the person who scraped it - in our case Lavanya Gupta.
- The data was compiled around 2017/2018. The pricing data reflect the price in USD Dollars at the time of scraping. (developers can offer promotions and change their app’s pricing).
- I’ve converted the app’s size to a floating-point number in MBs. If data was missing, it has been replaced by the average size for that category.
- The installs are not the exact number of installs. If an app has 245,239 installs then Google will simply report an order of magnitude like 100,000+. I’ve removed the '+' and we’ll assume the exact number of installs in that column for simplicity.

# Preliminary Exploration: The Highest Ratings, Most Reviews, and Largest Size

# Data Visualization with Plotly: Create Pie and Donut Charts

# Numeric Type Conversions for the Installations & Price Data

# Plotly Bar Charts & Scatter Plots: The Most Competitive & Popular App Categories

# Extracting Nested Column Data using `.stack()`

# Grouped Bar Charts and Box Plots with Plotly

# Learning Points & Summary
