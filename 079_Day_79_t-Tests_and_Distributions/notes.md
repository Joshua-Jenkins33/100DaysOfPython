# Day 79: The Tragic Discovery of Handwashing: t-Tests & Distributions

- [Day 79: The Tragic Discovery of Handwashing: t-Tests & Distributions](#day-79-the-tragic-discovery-of-handwashing-t-tests--distributions)
- [What You Will Make Today](#what-you-will-make-today)
- [Preliminary Data Exploration and Visualising Births & Deaths at Vienna Hospital](#preliminary-data-exploration-and-visualising-births--deaths-at-vienna-hospital)
  - [Challenge 1: Preliminary Data Exploration](#challenge-1-preliminary-data-exploration)
    - [My Code](#my-code)
    - [Solution to Challenge 1](#solution-to-challenge-1)
  - [Challenge 2: Percentage of Women Dying in Childbirth](#challenge-2-percentage-of-women-dying-in-childbirth)
    - [My Code](#my-code-1)
    - [Solution to Challenge 2](#solution-to-challenge-2)
  - [Challenge 3: Visualise the Total Number of Births 🤱 and Deaths 💀 over Time](#challenge-3-visualise-the-total-number-of-births--and-deaths--over-time)
    - [My Code](#my-code-2)
    - [Solution to Challenge 3](#solution-to-challenge-3)

# What You Will Make Today
**Your Story**
Today you will become a doctor, but not just any doctor. You will become Dr Ignaz Semmelweis, a Hungarian physician born in 1818 who worked in the Vienna General Hospital. 

In the past, people didn't know about bacteria, germs, or viruses. People illness was caused by "bad air" or evil spirits. But in the 1800s Doctors started looking more at anatomy, doing autopsies and making arguments based on data. Dr Semmelweis suspected that something was going wrong with the procedures at Vienna General Hospital. Dr Semmelweis wanted to figure out why so many women in maternity wards were dying from childbed fever (i.e., [puerperal fever](https://en.wikipedia.org/wiki/Postpartum_infections)).

Today you'll learn: 
- How to make a compelling argument using data
- How to superimpose histograms to show differences in distributions
- How to use a Kernel Density Estimate (KDE) to show a graphic estimate of a distribution.
- How to use scipy and test for statistical significance by looking at p-values. 
- How to highlight different parts of a time series chart in Matplotib.
- How to add and configure a Legend in Matplotlib.
- Use NumPy's `.where()` function to process elements depending on a condition.

# Preliminary Data Exploration and Visualising Births & Deaths at Vienna Hospital
You (aka Dr Semmelweis) are working at Vienna General Hospital. Let's take a closer look at the data you've been collecting on the number of births and maternal deaths throughout the 1840s. 

![Old Data](https://img-b.udemycdn.com/redactor/raw/2020-10-23_10-38-09-9527e9a9d46107327b4fa76246c62b81.png)

## Challenge 1: Preliminary Data Exploration
- What is the shape of `df_yearly` and `df_monthly`? How many rows and columns?
  - `df_yearly` has 12 rows and 4 columns
  - `df_monthly` has 98 rows and 3 columns
- What are the column names?
  - year, birthds, deaths, clinic
  - date, births, deaths
- Which years are included in the dataset?
  - `df_yearly` spans 1841 and 1846.
- Are there any NaN values or duplicates?
  - Nope!
- What were the average number of births that took place per month?
  - 267
- What were the average number of deaths that took place per month?
  - 22.5

### My Code
```py
# What is the shape of df_yearly and df_monthly? How many rows and columns?
df_yearly.shape
df_monthly.shape

# What are the column names?
df_yearly.columns
df_monthly.columns

# Which years are included in the dataset?
print(f'df_yearly spans {df_yearly.year.min()} and {df_yearly.year.max()}.')

# Are there any NaN values or duplicates?
print(f'df_yearly has NaN values? {df_yearly.isnull().values.any()}')
print(f'df_yearly has duplicate records?\n{df_yearly.duplicated()}')

print(f'df_monthly has NaN values? {df_monthly.isnull().values.any()}')
print(f'df_monthly has duplicate records?\n{df_monthly.duplicated()}')

# What were the average number of births that took place per month?
print(f"The average number of births per month: {df_monthly['births'].mean()}")

# What were the average number of deaths that took place per month?
print(f"The average number of deaths per month: {df_monthly['deaths'].mean()}")
```

### Solution to Challenge 1
Using `.shape`, `.head()`, `.tail()` we see that the dataset covers the years 1841 to 1849. The two tables report the total number of births and the total number of deaths. Interestingly, the yearly data breaks the number of births and deaths down by clinic. 

![Instructor Code](https://img-b.udemycdn.com/redactor/raw/2020-10-23_10-42-54-fb1af5f4e2bd231b283dabdaca8cc4c3.png)

We see that there are no NaN values in either of the DataFrames. We can verify this either with using `.info()` or using `.isna().values.any()`. 

![Explanation](https://img-b.udemycdn.com/redactor/raw/2020-10-23_10-47-41-c48e37522afaa8f220c19a26a4c7ab73.png)

There are also no duplicate entries. In other words, the dataset appears to be clean.

![Clean dataset](https://img-b.udemycdn.com/redactor/raw/2020-10-23_10-48-41-6018a072a58ca120945dab55dbbdc651.png)

Using `.describe()` allows us to view some interesting statistics at a glance. We see that on average there were about 267 births and 22.47 deaths per month. 

![.describe](https://img-b.udemycdn.com/redactor/raw/2020-10-23_10-52-34-6870fc442c6051d51df38af7904c328b.png)

## Challenge 2: Percentage of Women Dying in Childbirth
How dangerous was childbirth in the 1840s in Vienna?
- Using the annual data, calculate the percentage of women giving birth who died throughout the 1840s at the hospital.

In comparison, the United States recorded 18.5 maternal deaths per 100,000 or 0.018% in 2013 [(source)](https://en.wikipedia.org/wiki/Maternal_death#:~:text=The%20US%20has%20the%20%22highest,17.8%20per%20100%2C000%20in%202009).

### My Code

```py
total_births = df_yearly.births.sum()
print(f'Total births: {total_births}')
total_deaths = df_yearly.deaths.sum()
print(f'Total deaths: {total_deaths}')

death_percentage = total_deaths / total_births
print(f'The percentage of women giving birth who died throughout the 1840s at the hospital: {round(death_percentage*100,2)}%')
```

### Solution to Challenge 2
Childbirth was very risky! About 7.08% of women died 💀 in the 1840s (compared to 0.018% in the US in 2013).
```py
prob = df_yearly.deaths.sum() / df_yearly.births.sum() * 100
print(f'Chances of dying in the 1840s in Vienna: {prob:.3}%')
```
If someone gave me a bag of 100 M&Ms and told me that 7 of them would kill me, I'd (probably) pass on those M&Ms 🤭. Just saying.

## Challenge 3: Visualise the Total Number of Births 🤱 and Deaths 💀 over Time
Create a [Matplotlib chart](https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.pyplot.plot.html) with twin y-axes. It should look something like this:

![Example Chart](https://img-b.udemycdn.com/redactor/raw/2020-10-23_11-06-31-76e4e6fbe90cd4edb47e9dee6eb3da5f.png)

- Format the x-axis using locators for the years and months (Hint: we did this in the Google Trends notebook)
- Set the range on the x-axis so that the chart lines touch the y-axes
- Add gridlines
- Use skyblue and crimson for the line colours
- Use a dashed line style for the number of deaths
- Change the line thickness to 3 and 2 for the births and deaths respectively.
- Do you notice anything in the late 1840s?

### My Code
```py
fig, ax1 = plt.subplots(figsize=(14,8), dpi=200)
ax2 = ax1.twinx()
ax1.grid(color='grey', linestyle='--')

ax1.plot(df_monthly.date, df_monthly.births, color='skyblue', linewidth=3)
ax2.plot(df_monthly.date, df_monthly.deaths, color='crimson', linewidth=2, linestyle='dashed')
```

```py
# Create locators for ticks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y') 

fig, ax1 = plt.subplots(figsize=(14,8), dpi=200)
ax2 = ax1.twinx()
ax1.grid(color='grey', linestyle='--')

ax1.set_ylabel('Births', color='skyblue', fontsize=18)
ax2.set_ylabel('Deaths', color='crimson', fontsize=18)

# Use Locators
ax1.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.plot(df_monthly.date, df_monthly.births, color='skyblue', linewidth=3)
ax2.plot(df_monthly.date, df_monthly.deaths, color='crimson', linewidth=2, linestyle='dashed')
```

### Solution to Challenge 3
Just as in previous notebooks we can use `.twinx()` to create two y-axes. Then it's just a matter of adding a gird with `.grid()` and configuring the look of our plots with the `color`, `linewidth`, and `linestyle` parameters. 

```py
plt.figure(figsize=(14,8), dpi=200)
plt.title('Total Number of Monthly Births and Deaths', fontsize=18)
  
ax1 = plt.gca()
ax2 = ax1.twinx()
  
ax1.grid(color='grey', linestyle='--')
  
ax1.plot(df_monthly.date, 
          df_monthly.births, 
          color='skyblue', 
          linewidth=3)
  
ax2.plot(df_monthly.date, 
          df_monthly.deaths, 
          color='crimson', 
          linewidth=2, 
          linestyle='--')
  
plt.show()
```

![Results](https://img-b.udemycdn.com/redactor/raw/2020-10-23_11-11-50-6276fcca4bbc46fa057415c170ba9189.png)

To get the tickmarks showing up on the x-axis, we need to use `mdates` and Matplotlib's locators.

```py
# Create locators for ticks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y') 
```

We can then use the locators in our chart:

```py
plt.figure(figsize=(14,8), dpi=200)
plt.title('Total Number of Monthly Births and Deaths', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
  
ax1 = plt.gca()
ax2 = ax1.twinx()
  
ax1.set_ylabel('Births', color='skyblue', fontsize=18)
ax2.set_ylabel('Deaths', color='crimson', fontsize=18)
  
# Use Locators
ax1.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
  
ax1.grid(color='grey', linestyle='--')
  
ax1.plot(df_monthly.date, 
          df_monthly.births, 
          color='skyblue', 
          linewidth=3)
  
ax2.plot(df_monthly.date, 
          df_monthly.deaths, 
          color='crimson', 
          linewidth=2, 
          linestyle='--')
  
plt.show()
```

![Final Chart](https://img-b.udemycdn.com/redactor/raw/2020-10-23_11-16-35-039658c53b985fcbb11f9ffa26d074fd.png)

What we see is that something happened after 1847. The total number of deaths seems to have dropped, despite an increasing number of births! 🤔