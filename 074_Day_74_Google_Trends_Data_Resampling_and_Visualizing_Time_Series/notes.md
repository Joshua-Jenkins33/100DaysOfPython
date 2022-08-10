- [Day 74: Google Trends Data: Resapmling and Visualizing Time Series](#day-74-google-trends-data-resapmling-and-visualizing-time-series)
  - [What We'll Make Today](#what-well-make-today)
    - [Combine Google Trends with other Time Series Data](#combine-google-trends-with-other-time-series-data)
    - [What You'll Learn Today](#what-youll-learn-today)
    - [Downlad and add the Notebook to Google Drive](#downlad-and-add-the-notebook-to-google-drive)
    - [Add the Data to the Notebook](#add-the-data-to-the-notebook)
  - [Data Exploration: Making Sense of Google Search Data](#data-exploration-making-sense-of-google-search-data)
    - [What do the Search Numbers Mean?](#what-do-the-search-numbers-mean)
  - [Data Cleaning: Resampling Time Series Data](#data-cleaning-resampling-time-series-data)
    - [Resampling Time Series Data](#resampling-time-series-data)
  - [Data Visualization: Tesla Line Charts in Matplotlib](#data-visualization-tesla-line-charts-in-matplotlib)
  - [Using Locators and DateFormatters to generate Tick Marks on a Time Line](#using-locators-and-dateformatters-to-generate-tick-marks-on-a-time-line)
    - [Adding Locator Tick Marks](#adding-locator-tick-marks)
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
First, we have to identify if there are any missing or junk values in our DataFrames. 

**Challenge**
Can you investigate all 4 DataFrames and find if there are any missing values? 

If yes, find how many missing or NaN values there are. Then, find the row where the missing values occur.

Finally, remove any rows that contain missing values. 

```py
def check_if_missing_values(df):
    missing_values = False
    if df.isnull().sum().sum() > 0:
        missing_values = True
    return missing_values

def number_of_df_missing_values(df):
    return df.isnull().sum().sum()

print(f'Missing values for Tesla?: {check_if_missing_values(df_tesla)}')
print(f'\nMissing values for U/E?: {check_if_missing_values(df_unemployment)}')
print(f'\nMissing values for BTC Search?: {check_if_missing_values(df_btc_search)}')

print(f'Missing values for BTC price?: {check_if_missing_values(df_btc_price)}')

print(f'Number of missing values: {number_of_df_missing_values(df_btc_price)}')

df_btc_price.dropna()
```

**Solution: Finding the missing values**
For 3 of the DataFrames there are no missing values. We can verify this using the `.isna()` method. This will return a whole series of booleans, but we can chain `.values.any()` to see if any value in the series is `True`.

```py
    print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
    print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')
    print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}')
```

However, for the Bitcoin price data, there seems to be a problem. There's a missing value somewhere.

The number of missing values can be found by using `.sum()` to add up the number of occurrences of `True` in the series. This shows that there are 2 missing values.

To find the row where the missing values occur, we can create a subset of the DataFrame using `.isna()` once again (If you've arrived at this answer using a different approach, that's fine too. There are a number of ways to solve this challenge.) 

To remove a missing value we can use `.dropna()`. The `inplace` argument allows to overwrite our DataFrame and means we don't have to write:

```py
# don't need to do this
df_btc_price = df_btc_price.dropna()

# can do this
df_btc_price.dropna(inplace=True)
```

**Challenge**
Our DataFrames contain time-series data. Do you remember how to check the data type of the entries in the DataFrame? Have a look at the data types of the MONTH or DATE columns. Convert any strings you find into `Datetime` objects. Do this for all 4 DataFrames. Double-check if your type conversion was successful.

```py
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH, format='%Y/%m/%d')
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH, format='%Y/%m/%d')
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE, format='%Y/%m/%d')
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH, format='%Y/%m/%d')

print(f'Data Types:\nTesla: {df_tesla.dtypes}\n\nBitcoin Search: {df_btc_search.dtypes}\n\nBitcoin Price: {df_btc_price.dtypes}\n\nUnemployment: {df_unemployment.dtypes}')
```

**Solution: Converting Strings to DateTime Objects**
All the date data in our columns are in the form of strings. To convert this into a Datetime object we're going to use the Pandas `.to_datetime()` function.

```py
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)
```

### Resampling Time Series Data
Next, we have to think about how to make our Bitcoin price and our Bitcoin search volume comparable. Our Bitcoin price is daily data, but our Bitcoin Search Popularity is monthly data. 

To convert our daily data into monthly data, we're going to use the [.resample()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html) function. The only things we need to specify is which column to use (i.e., our DATE column) and what kind of sample frequency we want (i.e., the "rule"). We want a monthly frequency, so we use `'M'`.  If you ever need to resample a time series to a different frequency, you can find a list of different options [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects) (for example `'Y'` for yearly or `'T'` for minute).

After resampling, we need to figure out how the data should be treated. In our case, we want the last available price of the month - the price at month-end.

```py
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
```

If we wanted the average price over the course of the month, we could use something like:

```py
df_btc_monthly = df_btc_price.resample('M', on='DATE').mean()
```

We have 73 rows in our price data - the same as our search data. Nice! 😎

## Data Visualization: Tesla Line Charts in Matplotlib
Let's create a basic line chart of the Tesla stock price and the search popularity and then gradually add more and more styling to our chart. 

**Challenge.**
Plot the Tesla stock price against the Tesla search volume using a line chart and two different axes. 

```py
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE)

ax1.set_xlabel('Month')
ax1.set_ylabel('Search Trend')
ax2.set_ylabel('TSLA Stock Price')
```

**Solution: Creating a basic chart**
This bit should pretty much be review from the previous days' lessons. To create a line plot with two different y-axes we first have to get the current axis and make a copy of it using `.twinx()`. Then we can configure each axis separately and call `.plot()`.

```py
    ax1 = plt.gca() # get current axis
    ax2 = ax1.twinx()
     
    ax1.set_ylabel('TSLA Stock Price')
    ax2.set_ylabel('Search Trend')
     
    ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE)
    ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH)
```

**Challenge.**
Now let's style the chart a bit more. In particular, let's check out the different colours you can use with Matplotlib.

For our updated chart, let's differentiate the two lines and the axis labels using different colours. Try using one of the blue [colour names](https://matplotlib.org/3.1.1/gallery/color/named_colors.html) for the search volume and a [HEX code](https://htmlcolorcodes.com/color-picker/) for a red colour for the stock price. 

```py
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, 'tab:purple')
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, '#ae2d2d')

ax1.set_xlabel('Month')
ax1.set_ylabel('Search Trend', color='tab:purple')
ax2.set_ylabel('TSLA Stock Price', color='#ae2d2d')
```

**Solution: Adding Colors**
Your code should now look something like this (with your own choice of colours of course):
```py
    ax1 = plt.gca()
    ax2 = ax1.twinx()
     
    ax1.set_ylabel('TSLA Stock Price', color='#E6232E') # can use a HEX code
    ax2.set_ylabel('Search Trend', color='skyblue') # or a named colour
     
    ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E')
    ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue')
```

**Challenge.**
There are still some ways to improve the look of this chart. First off, let's make it larger. Can you make the following changes:

1. Increase the figure size (e.g., to 14 by 8).
2. Increase the font sizes for the labels and the ticks on the x-axis to 14.
3. Rotate the text on the x-axis by 45 degrees.
4. Add a title that reads 'Tesla Web Search vs Price'
5. Make the lines on the chart thicker.
6. Keep the chart looking sharp by changing the dots-per-inch or [DPI value](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.figure.html).
7. Set minimum and maximum values for the y and x-axis. Hint: check out methods like [set_xlim()](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.set_xlim.html).
8. Finally use [plt.show()](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.show.html) to display the chart below the cell instead of relying on the automatic notebook output.

```py
plt.figure(figsize=(14,8), dpi=120)
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.title('Tesla Web Search vs Price', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_xlabel('Month')
ax1.set_ylabel('Search Trend', color='tab:purple', fontsize=14)
ax2.set_ylabel('TSLA Stock Price', color='#ae2d2d', fontsize=14)
# ax1.set_xlim(2011, 2021)
# ax1.set_ylim(0, 35)
# ax2.set_ylim(25, 550)

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, 'tab:purple', linewidth=2)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, '#ae2d2d', linewidth=2)

plt.show()
```

**Solution: Additional Styling, Icnreasing Size & Resolution**
There's a couple of tweaks to the code going on here. First, we use `.figure()` to increase the size and resolution of our chart. Since we now have a bigger chart, we should also increase the font size of our labels and the thickness of our lines.

Finally, we are calling `.show()` to explicitly display the chart below the cell. This `.show()` method is important to be aware of if you're ever trying to generate charts in PyCharm or elsewhere outside of an interactive notebook like Google Colab or Jupyter. Also, it gives our notebook a very clean look.

```py
# increases size and resolution
plt.figure(figsize=(14,8), dpi=120) 
plt.title('Tesla Web Search vs Price', fontsize=18)
  
ax1 = plt.gca()
ax2 = ax1.twinx()
  
# Also, increase fontsize and linewidth for larger charts
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
  
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)
  
# Displays chart explicitly
plt.show()
```

Here's the code with rotation added to the x-ticks. With `.set_ylim()` and `.set_xlim()` you have precise control over which data you want to show on the chart. You can either choose hard values like displaying the Tesla stock price between $0 and $600. Or you could use the `.min()` and `.max()` functions to help you work out the bounds for the chart as well. 

```py
plt.figure(figsize=(14,8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)
  
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
  
ax1 = plt.gca()
ax2 = ax1.twinx()
  
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
  
# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])
  
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)
  
plt.show()
```

**Fix the Matplotlib Warning (if you see it)**
At this point, you might have seen a warning from Matplotlib.

This is not an error, but an FYI to be explicit about which datetime converter to use. We have a timeline on our x-axis after all. To address this simply follow the instructions in the warning message and add the following code:

```py
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
```

## Using Locators and DateFormatters to generate Tick Marks on a Time Line

### Adding Locator Tick Marks
When working with time series, it's often quite difficult to get the tick marks on charts looking the way you want to. This is why we have Locator helpers. 

The first step is importing `matplotlib.dates`.  This is where all the date plotting capabilities live. 

```py
import matplotlib.dates as mdates
```

Next, we need a `YearLocator()` and a `MonthLocator()` objects, which will help Matplotlib find the years and the months. Then we also need a `DateFormatter()`, which will help us specify how we want to display the dates. 

```py
# Create locators for ticks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

# format the ticks
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
```

When we take a look at our chart, we can see the tick marks nicely. The tick marks also allow us to visually date that spike of interest in the middle of the chart - March 2016. This was when the Tesla Model 3 was unveiled. Also, we can clearly see that the most recent spikes in search coincide, not with the release of a new car, but the roaring stock price for the company!


## Data Visualization - Bitcoin: Line Style and Markers
Now that we've got Tesla looking the way we want it to, let's do the same for Bitcoin. We've already matched the sample frequency and we can re-use our chart! Simply copy-paste the entire cell and make some modifications to the code as per the challenge. 

**Challenge.**
1. Modify the chart title to read 'Bitcoin News Search vs Resampled Price'
2. Change the y-axis label to 'BTC Price'
3. Change the y- and x-axis limits to improve the appearance
4. Investigate the [linestyles](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html) to make the BTC closing price a dashed line
5. Investigate the [marker types](https://matplotlib.org/3.2.1/api/markers_api.html) to make the search datapoints little circles
6. Were big increases in searches for Bitcoin accompanied by big increases in the price?

```py
plt.figure(figsize=(14,8), dpi=120)
plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
  
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
  
ax1 = plt.gca()
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
ax1.set_ylabel('BTC Price', color='#E6232E', fontsize=14)
ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])
# Set the minimum and maximum values on the axes
ax1.set_ylim(bottom=0, top=15000)
ax1.plot(df_btc_monthly.DATE, df_btc_monthly.CLOSE, color='#E6232E', linewidth=3, linestyle='--')

ax2 = ax1.twinx()
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
ax2.plot(df_btc_search.MONTH, df_btc_search.BTC_NEWS_SEARCH, color='skyblue', linewidth=3, marker='o')

plt.show()
```

**Solution: Charting Bitcoin**
I hope you had a good go at generating the chart.

Updating the title and the axis labels just involved changing the strings. To set the axis limits, I've chosen $0 to $15,000 on the left y-axis. I've also used a HEX code for orange to colour the line.

To change the line style or the markers, you just have to look at the documentation (e.g., try `'--'` or `'-.'` for the `linestyle`). Similarly for the markers, you also have loads of different options.

I think the main trick with this challenge involved substituting a different set of dates. The months of the time series are found in the index of the monthly bitcoin prices: `df_btc_monthly.index`. 

```py
plt.figure(figsize=(14,8), dpi=120)
  
plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)
  
ax1 = plt.gca()
ax2 = ax1.twinx()
  
ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
  
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
  
ax1.set_ylim(bottom=0, top=15000)
ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])
  
# Experiment with the linestyle and markers
ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE, 
          color='#F08F2E', linewidth=3, linestyle='--')
ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH, 
          color='skyblue', linewidth=3, marker='o')
  
plt.show()
```

What we see in the chart is that similar to Tesla, the crazy price movements in the beginning of 2018 are associated with very high search volumes. Everyone was talking about (and buying) Bitcoin in late 2017/early 2018 so search volumes were at a record high!  Interestingly, there was quite a huge spike in bitcoin prices in Q1 of 2019, but this time the increase in search volume was much less pronounced (perhaps because at this point everyone knew what Bitcoin was). 

## Data Visualization - Unemployment: How to use Grids
For the next challenge, carry over your existing code once again (by copy-pasting the entire cell) and make some modifications. 

**Challenge.**
Plot the search for "unemployment benefits" against the official unemployment rate.

1. Change the title to: Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate
2. Change the y-axis label to: FRED U/E Rate
3. Change the axis limits
4. Add a grey [grid](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.grid.html) to the chart to better see the years and the U/E rate values. Use dashed lines for the line style. 
5. Can you discern any seasonality in the searches? Is there a pattern?

```py
plt.figure(figsize=(14,8), dpi=120)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
  
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
  
plt.grid(visible=True, which='major', axis='both', color='#c2c2c2', linestyle='--', linewidth=2)
    
ax1 = plt.gca()
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
ax1.set_ylabel('FRED U/E Rate', color='#6c186e', fontsize=14)
ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
# Set the minimum and maximum values on the axes
ax1.set_ylim(bottom=0, top=11)
ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, color='#6c186e', linewidth=3, linestyle='--')

ax2 = ax1.twinx()
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH, color='skyblue', linewidth=3)

plt.show()
```

**Solution: Adding a Grid to Spot Seasonality**
Ok, so there are relatively few changes you had to make here. Just the labels and the dataset we're using. The line of code I wanted you to figure out from the documentation was this one:

```py
    ax1.grid(color='grey', linestyle='--')
```

This overlays a grid of dashed lines.

Notice how we can now clearly see the vertical dashed lines line up with spikes in searches for "Unemployment benefits". Many of the spikes are at year-end - in December. This clearly shows that there is seasonality in the job market. What else do we see? We see that the financial crisis in 2007/2008 caused a massive spike in unemployment. It took around 10 years (2007-2017) for the unemployment to reach the same level it had before the crisis. 

Interestingly the big spike in searches for Unemployment benefits at the end of 2013 was not accompanied by a big increase in the unemployment rate. Something else must have been going on around that time. 

Here's the full code for the cell:

```py
    plt.figure(figsize=(14,8), dpi=120)
    plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14, rotation=45)
     
    ax1 = plt.gca()
    ax2 = ax1.twinx()
     
    ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
    ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
     
    ax1.xaxis.set_major_locator(years)
    ax1.xaxis.set_major_formatter(years_fmt)
    ax1.xaxis.set_minor_locator(months)
     
    ax1.set_ylim(bottom=3, top=10.5)
    ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
     
    # Show the grid lines as dark grey lines
    ax1.grid(color='grey', linestyle='--')
     
    # Change the dataset used
    ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, 
             color='purple', linewidth=3, linestyle='--')
    ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH, 
             color='skyblue', linewidth=3)
     
    plt.show()
```

The search volume moves around quite a bit - month on month. Perhaps we can smooth out the search volumes to get a slightly different picture (pun intended!).

**Challenge.**
Calculate the 3-month or 6-month rolling average for the web searches. Plot the 6-month rolling average search data against the actual unemployment. What do you see? Which line moves first?


Hint: Take a look at our prior lesson on Programming Languages where we smoothed out time-series data. 

```py
roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=3).mean()

plt.figure(figsize=(14,8), dpi=120)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
  
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
  
# ax1.grid(visible=True, which='major', axis='both', color='#c2c2c2', linestyle='--')
plt.grid(visible=True, which='major', axis='both', color='#c2c2c2', linestyle='--')
    
ax1 = plt.gca()
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
ax1.set_ylabel('FRED U/E Rate', color='#6c186e', fontsize=14)
ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
# Set the minimum and maximum values on the axes
ax1.set_ylim(bottom=3, top=11)
ax1.plot(df_unemployment.MONTH, roll_df.UNRATE, color='#6c186e', linewidth=3, linestyle='--')

ax2 = ax1.twinx()
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, color='skyblue', linewidth=3)

plt.show()
```

**Solution: Rolling Average**
You can create a rolling average using .rolling() and .mean() functions together.
```py
    roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
```

What is this telling us? We see that searches for "Unemployment Benefits" happen before the actual official unemployment rate goes up. Similarly, the search popularity for the term goes down before the unemployment rate decreases. In other words, these searches seem to act as a leading economic indicator for the unemployment rate (which is a lagging indicator). 

Full Code for the Cell:
```py
plt.figure(figsize=(14,8), dpi=120)
plt.title('Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
  
ax1 = plt.gca()
ax2 = ax1.twinx()
  
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
  
ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)
  
ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([df_unemployment.MONTH[0], df_unemployment.MONTH.max()])
  
# Calculate the rolling average over a 6 month window
roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
  
ax1.plot(df_unemployment.MONTH, roll_df.UNRATE, 'purple', linewidth=3, linestyle='-.')
ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)
  
plt.show()
```

## Data Visualization - Unemployment: The Effect of New Data
The financial crisis in 2008 was pretty bad. We saw how it took around 10 years for the unemployment rate to go back to where it was prior to the crisis.

Let's see how 2020 affects our analysis.

**Challenge**
Read the data in the 'UE Benefits Search vs UE Rate 2004-20.csv' into a DataFrame. Convert the MONTH column to Pandas Datetime objects and then plot the chart. What do you see?

```py
df_unemployment_new = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
df_unemployment_new.head()

df_unemployment_new.MONTH = pd.to_datetime(df_unemployment.MONTH, format='%Y/%m')
df_unemployment_new.head()

plt.figure(figsize=(14,8), dpi=120)
plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)
  
# Increase the size and rotate the labels on the x-axis
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
  
# ax1.grid(visible=True, which='major', axis='both', color='#c2c2c2', linestyle='--')
plt.grid(visible=True, which='major', axis='both', color='#c2c2c2', linestyle='--')
    
ax1 = plt.gca()
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
ax1.set_ylabel('FRED U/E Rate', color='#6c186e', fontsize=14)
ax1.set_xlim([df_unemployment_new.MONTH.min(), df_unemployment_new.MONTH.max()])
# Set the minimum and maximum values on the axes
ax1.set_ylim(bottom=3, top=11)
ax1.plot(df_unemployment_new.MONTH, df_unemployment_new.UNRATE, color='#6c186e', linewidth=3, linestyle='--')

ax2 = ax1.twinx()
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
ax2.plot(df_unemployment_new.MONTH, df_unemployment_new.UE_BENEFITS_WEB_SEARCH, color='skyblue', linewidth=3)

plt.show()
```

**Solution: Included 2020**
Here's how you read the data and make a DataFrame:

```py
    df_ue_2020 = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
    df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)
```
And here's the chart:
```py
    plt.figure(figsize=(14,8), dpi=120)
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14, rotation=45)
    plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)
     
    ax1 = plt.gca()
    ax2 = ax1.twinx()
     
    ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
    ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)
     
    ax1.set_xlim([df_ue_2020.MONTH.min(), df_ue_2020.MONTH.max()])
     
    ax1.plot(df_ue_2020.MONTH, df_ue_2020.UNRATE, 'purple', linewidth=3)
    ax2.plot(df_ue_2020.MONTH, df_ue_2020.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)
     
    plt.show()
```
What we see is not pretty. The US unemployment rate spiked to unprecedented levels during the COVID pandemic, dwarfing the levels seen during the financial crisis. Let's hope the recovery will be swifter this time. 

## Learning Points & Summary
In this lesson we looked at how to:
- How to use `.describe()` to quickly see some descriptive statistics at a glance.
- How to use `.resample()` to make a time-series data comparable to another by changing the periodicity.
- How to work with `matplotlib.dates` Locators to better style a timeline (e.g., an axis on a chart).
- How to find the number of NaN values with `.isna().values.sum()`
- How to change the resolution of a chart using the figure's `dpi`
- How to create dashed `'--'` and dotted `'-.'` lines using `linestyles`
- How to use different kinds of markers (e.g., `'o'` or `'^'`) on charts.
- Fine-tuning the styling of Matplotlib charts by using limits, labels, `linewidth` and colours (both in the form of named colours and HEX codes).
- Using `.grid()` to help visually identify seasonality in a time series.

Well done for completing another challenging data science day! I hope working with Pandas is starting to feel more and more second nature at this point. 