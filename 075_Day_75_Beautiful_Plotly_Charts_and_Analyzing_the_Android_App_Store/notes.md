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
**Challenge:** Identify which apps are the highest rated. What problem might you encounter if you rely exclusively on ratings alone to determine the quality of an app?

```py
df_apps_clean.sort_values(by=['Rating', 'Reviews', 'Installs'], ascending=False)
```

If you rely *exclusively on ratings alone to determine the quality of an app*, then you could wind up with a dataset that leads you to believe an app is incredibly popular despite only have one or two installs. It only takes one or two ratings to show the app's popularity. Whereas an app with lots more ratings that *maintains* a high rating is in reality the more popular app.

**Challenge:** What's the size in megabytes (MB) of the largest Android apps in the Google Play Store. Based on the data, do you think there could be a limit in place or can developers make apps as large as they please?

```py
df_apps_clean.sort_values(by=['Size_MBs'], ascending=False).head(5)
```

There appears to be a limit for developers to make apps **100 MBs** at most.

**Challenge:** Which apps have the highest number of reviews? Are there any paid apps among the top 50?

```py
df_apps_clean.sort_values(by='Reviews', ascending=False).head(50)
```

**There are no paid apps** among the top 50 most popular applications.

---

**Solution: Preliminary Data Exploration**
This challenge should have been fairly straightforward if you remembered to use the .sort_values() function.


```py
df_apps_clean.sort_values('Rating', ascending=False).head()
```

Only apps with very few reviews (and a low number on installs) have perfect 5 star ratings (most likely by friends and family).

```py
df_apps_clean.sort_values('Size_MBs', ascending=False).head()
```

Here we can clearly see that there seems to be an upper bound of 100 MB for the size of an app. A quick google search would also have revealed that this limit is imposed by the Google Play Store itself. It’s interesting to see that a number of apps actually hit that limit exactly.

```py
df_apps_clean.sort_values('Reviews', ascending=False).head(50)
```

If you look at the number of reviews, you can find the most popular apps on the Android App Store. These include the usual suspects: Facebook, WhatsApp, Instagram etc. What’s also notable is that the list of the top 50 most reviewed apps does not include a single paid app! 🤔


# Data Visualization with Plotly: Create Pie and Donut Charts
All Android apps have a content rating like “Everyone” or “Teen” or “Mature 17+”. Let’s take a look at the distribution of the content ratings in our dataset and see how to visualise it with [plotly](https://plotly.com/python/) - a popular data visualisation library that you can use alongside or instead of Matplotlib.

First, we’ll count the number of occurrences of each rating with .value_counts()

```py
ratings = df_apps_clean.Content_Rating.value_counts()
```

![Image 1](https://img-b.udemycdn.com/redactor/raw/2020-10-10_11-59-55-d92168b181149464c7edad65547e7859.png)

The first step in creating charts with plotly is to `import` plotly.express. This is the fastest way to create a beautiful graphic with a minimal amount of code in plotly.

![Import Plotly](https://img-b.udemycdn.com/redactor/raw/2020-10-10_12-00-08-bbf5ed815dadf9c64cf82f064bdd7ad2.png)

To create a pie chart we simply call `px.pie()` and then `.show()` the resulting figure. Plotly refers to all their figures, be they line charts, bar charts, or pie charts as graph_objects.+

```py
fig = px.pie(labels=ratings.index, values=ratings.values)

fig.show()
```

![Pie Chart](https://img-b.udemycdn.com/redactor/raw/2020-10-10_12-00-31-31b7402c83df9ab64a30eca64147d286.png)

Let’s customise our pie chart. Looking at the [.pie() documentation](https://plotly.com/python-api-reference/generated/plotly.express.pie.html) we see a number of parameters that we can set, like title or names.

![PLOTLY.EXPRESS.PI](https://img-b.udemycdn.com/redactor/raw/2020-10-10_12-00-52-8e188db47a2c59e78c59597ac9f58130.png)

If you’d like to configure other aspects of the chart, that you can’t see in the list of parameters, you can call a method called `.update_traces()`. In plotly lingo, “traces” refer to graphical marks on a figure. Think of “traces” as collections of attributes. Here we update the traces to change how the text is displayed.

```py
fig = px.pie(labels=ratings.index,
  values=ratings.values,
  title="Content Rating",
  names=ratings.index,
)
fig.update_traces(textposition='outside', textinfo='percent+label')
  
fig.show()
```

![Pie Chart 2](https://img-b.udemycdn.com/redactor/raw/2020-10-10_12-01-14-05cf469b8bad01ae65343706f70f3feb.png)

To create a donut 🍩 chart, we can simply add a value for the `hole` argument:

```py
fig = px.pie(labels=ratings.index,
  values=ratings.values,
  title="Content Rating",
  names=ratings.index,
  hole=0.6,
)
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
  
fig.show()
```

![Donut Chart](https://img-b.udemycdn.com/redactor/raw/2020-10-10_12-01-52-9743066db238bd044fd095783c3261e1.png)

Yum! 😋

# Numeric Type Conversions for the Installations & Price Data
**Challenge:** How many apps had over 1 billion (that's right - BILLION) installations? How many apps just had a single install?
1. Check the datatype of the Installs column
2. Count the number of apps at each level of installations
3. Convert the number of installations (the Installs column) to a numeric data type. Hint: this is a 2-step process. You'll have to make sure you remove non-numeric characters first.

```py
df_apps_clean.dtypes # shows object type

#Needed help with 2 and 3
```

**Solution: Data Cleaning & Converting Data to Numeric Types**
To check the data types you can either use `.describe()` on the column or `.info()` on the DataFrame.

`df_apps_clean.Installs.describe()`

`df_apps_clean.info()`

Both of these show that we are dealing with a non-numeric data type. In this case, the type is "object".

If we take two of the columns, say Installs and the App name, we can count the number of entries per level of installations with `.groupby()` and `.count()`. However, because we are dealing with a non-numeric data type, the ordering is not helpful. The reason Python is not recognising our installs as numbers is because of the comma (`,`) characters.

`df_apps_clean[['App', 'Installs']].groupby('Installs').count()`

![Query Return](https://img-b.udemycdn.com/redactor/raw/2020-10-11_12-25-56-6e1796e77c7c62d86add95c5bb702d61.png)

We can remove the comma (`,`) character - or any character for that matter - from a DataFrame using the string’s [.replace()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html) method. Here we’re saying: “replace the `,` with an empty string”. This completely removes all the commas in the Installs column. We can then convert our data to a number using `.to_numeric()`.

```py
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[['App', 'Installs']].groupby('Installs').count()
```

![Query Return 2](https://img-b.udemycdn.com/redactor/raw/2020-10-11_12-27-06-b8d1d316afdae7047bd4c37d3c1bd0ab.png)

Let's examine the Price column more closely.

**Challenge:** Convert the price column to numeric data. Then investigate the top 20 most expensive apps in the dataset.

Remove all apps that cost more than $250 from the df_apps_clean DataFrame.

Add a column called 'Revenue_Estimate' to the DataFrame. This column should hold the price of the app times the number of installs. What are the top 10 highest-grossing paid apps according to this estimate? Out of the top 10, how many are games?

```py
df_apps_clean.info() # price is an object
df_apps_clean.Price # we want to replace $ 

df_apps_clean_sub250 = df_apps_clean.drop(df_apps_clean[df_apps_clean.Price >= 250].index)
df_apps_clean_sub250

df_apps_clean_sub250['Revenue_Estimate'] = df_apps_clean_sub250.Price * df_apps_clean_sub250.Installs
df_apps_clean_sub250.sort_values('Revenue_Estimate', ascending=False)

df_apps_clean_sub250['Revenue_Estimate'] = df_apps_clean_sub250.Price * df_apps_clean_sub250.Installs
df_highest_grossing_paid_apps = df_apps_clean_sub250.sort_values('Revenue_Estimate', ascending=False).head(10)

df_highest_grossing_paid_apps.loc[df_apps_clean_sub250.Category == 'GAME'].count()
```

**Solution: Finding the most Expensive Apps and Filtering out the Junk**
If you look at the data type of the price column:
```py
    df_apps_clean.Price.describe()
```
You also see that is of type object. The reason is the dollar $ signs that we’ve spotted before. To convert the price column to numeric data we use the .replace() method once again, but this time we filter out the dollar sign.
```py
    df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
    df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
     
    df_apps_clean.sort_values('Price', ascending=False).head(20)
```
Here’s what we see:

![I am rich](https://img-b.udemycdn.com/redactor/raw/2020-10-11_12-29-17-bc5f0a4ad2e83b4d4fcf62a84f7f3511.png)

What’s going on here? There are 15 I am Rich Apps in the Google Play Store apparently. They all cost $300 or more, which is the main point of the app. The story goes that in 2008, Armin Heinrich released the very first I am Rich app in the iOS App Store for $999.90. The app does absolutely nothing. It just displays the picture of a gemstone and can be used to prove to your friends how rich you are. Armin actually made a total of 7 sales before the app was hastily removed by Apple. Nonetheless, it inspired a bunch of copycats on the Android App Store, but if you search today, you’ll find all of these apps have disappeared as well. The high installation numbers are likely gamed by making the app available for free at some point to get reviews and appear more legitimate.

Leaving this bad data in our dataset will misrepresent our analysis of the most expensive 'real' apps. Here’s how we can remove these rows:
```py
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
df_apps_clean.sort_values('Price', ascending=False).head(5)
```
When we look at the top 5 apps now, we see that 4 out of 5 are medical apps.

![Still Rich](https://img-b.udemycdn.com/redactor/raw/2020-10-11_12-30-28-ab771a555e152a1f12150951f5cb06b4.png)

We can work out the highest grossing paid apps now. All we need to do is multiply the values in the price and the installs column to get the number:
```py
df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10]
```
This generously assumes of course that all the installs would have been made at the listed price, which is unlikely, as there are always promotions and free give-aways on the App Stores.

# Plotly Bar Charts & Scatter Plots: The Most Competitive & Popular App Categories
If you were to release an app, would you choose to go after a competitive category with many other apps? Or would you target a popular category with a high number of downloads? Or perhaps you can target a category which is both popular but also one where the downloads are spread out among many different apps. That way, even if it’s more difficult to discover among all the other apps, your app has a better chance of getting installed, right? Let’s analyse this with bar charts and scatter plots and figure out which categories are dominating the market.

We can find the number of different categories like so:

```py
    df_apps_clean.Category.nunique()
```

Which shows us that we there are 33 unique categories.

To calculate the number of apps per category we can use our old friend `.value_counts()`

```py
top10_category = df_apps_clean.Category.value_counts()[:10]
```

To visualise this data in a bar chart we can use the plotly express (our px) [bar()](https://plotly.com/python-api-reference/generated/plotly.express.bar.html#plotly.express.bar) function:

```py
    bar = px.bar(x = top10_category.index, # index = category name
                 y = top10_category.values)
     
    bar.show()
```

![Bar Chart](https://img-b.udemycdn.com/redactor/raw/2020-10-11_12-50-27-18f0bf39f584e83d11de5a269b080336.png)

Based on the number of apps, the Family and Game categories are the most competitive. Releasing yet another app into these categories will make it hard to get noticed.


But what if we look at it from a different perspective? What matters is not just the total number of apps in the category but how often apps are downloaded in that category. This will give us an idea of how popular a category is. First, we have to group all our apps by category and sum the number of installations:

```py
category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)
```

Then we can create a horizontal bar chart, simply by adding the orientation parameter:
```py
h_bar = px.bar(x = category_installs.Installs,
                y = category_installs.index,
                orientation='h')
  
h_bar.show()
```

We can also add a custom title and axis labels like so:
```py
h_bar = px.bar(x = category_installs.Installs,
                y = category_installs.index,
                orientation='h',
                title='Category Popularity')
  
h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
h_bar.show()
```

![Horizontal Bar Chart](https://img-b.udemycdn.com/redactor/raw/2020-10-11_12-51-08-abc65eebc2434504dd6457da4618a9ac.png)

Now we see that Games and Tools are actually the most popular categories. If we plot the popularity of a category next to the number of apps in that category we can get an idea of how concentrated a category is. Do few apps have most of the downloads or are the downloads spread out over many apps?

**Challenge.** As a challenge, let’s use plotly to create a scatter plot that looks like this:
![Scatter Chart](https://img-b.udemycdn.com/redactor/raw/2020-10-11_12-51-37-3937d6162a4800714f6fdcbdf2b12870.png)
- Create a DataFrame that has the number of apps in one column and the number of installs in another
- Then use the [plotly express examples from the documentation](https://plotly.com/python/line-and-scatter/) alongside the [.scatter() API reference](https://plotly.com/python-api-reference/generated/plotly.express.scatter.html) to create scatter plot that looks like the chart above.

*Hint:* Use the `size`, `hover_name` and `color` parameters in `.scatter()`. To scale the y-axis, call `.update_layout()` and specify that the y-axis should be on a log-scale like so: `yaxis=dict(type='log')`

```py
category_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})

df_categories_and_installs = category_installs.merge(category_number, on='Category')
df_categories_and_installs

fig = px.scatter(
    x=df_categories_and_installs.App, 
    y=df_categories_and_installs.Installs,
    size=df_categories_and_installs.App,
    #hover_name=,
    color=df_categories_and_installs.Installs
).update_layout(yaxis=dict(type='log'))
fig.show()
```

**Solution: Create a scatter plot with Plotly**
First, we need to work out the number of apps in each category (similar to what we did previously).

```py
cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})
```

Then we can use `.merge()` and combine the two DataFrames.

```py
cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how="inner")
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
cat_merged_df.sort_values('Installs', ascending=False)
```

Now we can create the chart. Note that we can pass in an entire DataFrame and specify which columns should be used for the x and y by column name.

```py
scatter = px.scatter(cat_merged_df, # data
                    x='App', # column name
                    y='Installs',
                    title='Category Concentration',
                    size='App',
                    hover_name=cat_merged_df.index,
                    color='Installs')
  
scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))
  
scatter.show()
```

What we see is that the categories like Family, Tools, and Game have many different apps sharing a high number of downloads. But for the categories like video players and entertainment, all the downloads are concentrated in very few apps.

![Scatter Plot Results](https://img-b.udemycdn.com/redactor/raw/2020-10-11_13-16-11-a310e773b06e1efc0ad4114a12a51e01.png)

# Extracting Nested Column Data using `.stack()`
Let's turn our attention to the Genres column. This is quite similar to the categories column but more granular.

**Challenge.**
How many different types of genres are there? Can an app belong to more than one genre? Check what happens when you use `.value_counts()` on a column with nested values? See if you can work around this problem by using the `.split()` function and the DataFrame's [.stack()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html) method.

```py
len(df_apps_clean.Genres.unique())

df_apps_clean.Genres.value_counts()

# had to cheat on this one
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()

genres = stack.value_counts()
len(genres)
```

**Solution: Working with Nested Column Data**

If we look at the number of unique values in the Genres column we get 114. But this is not accurate if we have nested data like we do here. We can see this using `.value_counts()` and looking at the values that just have a single entry. There we see that the semi-colon (`;`) separates the genre names.

```py
# Number of Genres?
len(df_apps_clean.Genres.unique())

# Problem: Have multiple categories separated by ;
df_apps_clean.Genres.value_counts().sort_values(ascending=-Ture)[:5]
```

We somehow need to separate the genre names to get a clear picture. This is where the string’s `.split()` method comes in handy. After we’ve separated our genre names based on the semi-colon, we can add them all into a single column with `.stack()` and then use `.value_counts()`.

```py
# Split the strings on the semi-colon and then .stack them.
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')
```

This shows us we actually have 53 different genres.

**Challenge.**
Can you create this chart with the Series containing the genre data?
![Chart to Replicate](https://img-b.udemycdn.com/redactor/raw/2020-10-11_13-20-25-275a5904eaf5ce179f8fc10d1cdb4f2b.png)

Try experimenting with the built-in colour scales in Plotly. You can find a full list [here](https://plotly.com/python/builtin-colorscales/).
- Find a way to set the colour scale using the `color_continuous_scale` parameter.
- Find a way to make the colour axis disappear by using `coloraxis_showscale`.

```py
genres = genres.to_frame(name='App_Count')[:15]

bar = px.bar(genres, x = genres.index,
             y = 'App_Count',
             color_continuous_scale="Algae",
             labels={'index':'Genre','App_Count':'Number of Apps'},
             color='App_Count')
  
bar.update_layout(coloraxis_showscale=False)

bar.show()
```

**Solution: Working with Colour Scales in Plotly**

```py
bar = px.bar(x = num_genres.index[:15], # index = category name
              y = num_genres.values[:15], # count
              title='Top Genres',
              hover_name=num_genres.index[:15],
              color=num_genres.values[:15],
              color_continuous_scale='Agsunset')
  
bar.update_layout(xaxis_title='Genre',
yaxis_title='Number of Apps',
coloraxis_showscale=False)
  
bar.show()
```

# Grouped Bar Charts and Box Plots with Plotly

# Learning Points & Summary
