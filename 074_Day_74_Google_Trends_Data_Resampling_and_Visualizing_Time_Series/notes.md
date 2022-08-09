- [Day 74: Google Trends Data: Resapmling and Visualizing Time Series](#day-74-google-trends-data-resapmling-and-visualizing-time-series)
  - [What We'll Make Today](#what-well-make-today)
    - [Combine Google Trends with other Time Series Data](#combine-google-trends-with-other-time-series-data)
    - [What You'll Learn Today](#what-youll-learn-today)
    - [Downlad and add the Notebook to Google Drive](#downlad-and-add-the-notebook-to-google-drive)
    - [Add the Data to the Notebook](#add-the-data-to-the-notebook)
  - [Data Exploration: Making Sense of Google Search Data](#data-exploration-making-sense-of-google-search-data)
    - [What do the Search Numbers Mean?](#what-do-the-search-numbers-mean)
  - [Data Cleaning: Resampling Time Series Data](#data-cleaning-resampling-time-series-data)
  - [Data Visualization: Tesla Line Charts in Matplotlib](#data-visualization-tesla-line-charts-in-matplotlib)
  - [Using Locators and DateFormatters to generate Tick Marks on a Time Line](#using-locators-and-dateformatters-to-generate-tick-marks-on-a-time-line)
  - [Data Visualization - Bitcoin: Line Style and Markers](#data-visualization---bitcoin-line-style-and-markers)
  - [Data Visualization - Unemployment: How to use Grids](#data-visualization---unemployment-how-to-use-grids)
  - [Data Visualization - Unemployment: The Effect of New Data](#data-visualization---unemployment-the-effect-of-new-data)
  - [Learning Points & Summary](#learning-points--summary)

# Day 74: Google Trends Data: Resapmling and Visualizing Time Series

## What We'll Make Today

### Combine Google Trends with other Time Series Data
![Header Image](https://img-b.udemycdn.com/redactor/raw/2020-10-10_10-30-21-9b8bd58ba8815919292f5bc49591dbd3.png)

What can the popularity of search terms tell us about the world? Google Trends gives us access to the popularity of Google Search terms. Let's investigate:
- How search volume for "Bitcoin" relates to the price of Bitcoin
- How search volume for a hot stock like Telsa relates to that stock's price and
- How searches for "Unemployment Benefits" vary with the actual unemployment rate in the United States

### What You'll Learn Today
- How to make time-series data comparable by resampling and converting to the same periodicity (e.g., from daily data to monthly data). 
- Fine-tuning the styling of Matplotlib charts by using limits, labels, linestyles, markers, colours, and the chart's resolution.
- Using grids to help visually identify seasonality in a time series.
- Finding the number of missing and NaN values and how to locate NaN values in a DataFrame. 
- How to work with Locators to better style the time axis on a chart 
- Review the concepts learned in the previous three days and apply them to new datasets

### Downlad and add the Notebook to Google Drive
Download the .zip file from this lesson and extract it. Add the .ipynb file into your Google Drive and open it as a Google Colaboratory notebook.

### Add the Data to the Notebook
The .zip file also includes 5 .csv files. This is the data for the project. Add these to the notebook. 

## Data Exploration: Making Sense of Google Search Data
I've gone ahead and already added the import statements and created the four different DataFrames in this notebook. Your first step is to explore the data, by getting an understanding of what's actually in those .csv files for this project.

Start with `df_tesla`, then have a look at `df_unemployment` and finally, check out the two bitcoin DataFrames. 

**Challenge**
Try to answer these questions about the DataFrames:
- What are the shapes of the DataFrames? 
- How many rows & columns do they have? 
- What are the column names? 
- What is the largest number in the search data column? Try using the `.describe()` function. 
- What is the periodicity of the time series data (daily, weekly, monthly)?

---

**Tesla**

```py
df_tesla.shape
df_tesla.columns

print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')
print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')

df_tesla.describe()
```

---

**Unemployment**

```py
print(df_unemployment.shape)
df_unemployment.head()

print('Largest value for "Unemployment Benefits"  '
  f'in Web Search: {df_unemployement.UE_BENEFITS_WEB_SEARCH.max()}')
```

---

**Bitcoin**

```py
print(df_btc_search.shape)
df_btc_search.head()

print(df_btc_price.shape)
df_btc_price.head()

print(f'largest BTC News Search: {df_btc_search.BTC_NEWS_SEARCH.max()}')

```

**Solution for Tesla**
The `df_tesla` DataFrame has 124 rows and 3 columns: for the Month, the search popularity and the closing price of the Tesla stock.

```py
print(df_tesla.shape)
df_tesla.head()
```

You can use the max() and min() functions to see that the largest value in the search column is 31 and the smallest value is 2.

```py
print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')
print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')
```

One of my favourite functions to run on DataFrames is `.describe()`. If you use `df_tesla.describe()`, you get a whole bunch of descriptive statistics. Right off the bat. 

**Solution for Unemployment**
The unemployment DataFrame has 181 rows and 3 columns. As with Tesla, we have monthly data from 2004 onwards, organised in rows. Interestingly here, the largest value in the search column is 100. 

**Solution for Bitcoin**
With the Bitcoin data we see that we have two different .csv files. One of them has the day-by-day closing price and the trade volume of Bitcoin across 2204 rows. The other has the monthly search volume from Google Trends. 

### What do the Search Numbers Mean?
We can see from our DataFrames that Google's search interest ranges between 0 and 100. But what does that mean? Google defines the values of search interest as: 

> Numbers represent search interest relative to the highest point on the chart for the given region and time. A value of 100 is the peak popularity for the term. A value of 50 means that the term is half as popular. A score of 0 means there was not enough data for this term. 

Basically, the actual search volume of a term is not publicly available. Google only offers a scaled number. Each data point is divided by the total searches of the geography and time range it represents to compare relative popularity. 

For each word in your search, Google finds how much search volume in each region and time period your term had relative to all the searches in that region and time period. It then combines all of these measures into a single measure of popularity, and then it scales the values across your topics, so the largest measure is set to 100. In short: Google Trends doesn’t exactly tell you how many searches occurred for your topic, but it does give you a nice proxy.

Here are the Google Trends Search Parameters that I used to generate the .csv data:
- "Tesla", Worldwide, Web Search
- "Bitcoin", Worldwide, News Search
- "Unemployment Benefits", United States, Web Search

## Data Cleaning: Resampling Time Series Data

## Data Visualization: Tesla Line Charts in Matplotlib

## Using Locators and DateFormatters to generate Tick Marks on a Time Line

## Data Visualization - Bitcoin: Line Style and Markers

## Data Visualization - Unemployment: How to use Grids

## Data Visualization - Unemployment: The Effect of New Data

## Learning Points & Summary