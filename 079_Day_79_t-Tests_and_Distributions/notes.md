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
- [Analysing the Yearly Data Split By Clinic](#analysing-the-yearly-data-split-by-clinic)
  - [Challenge 1: The Yearly Data Split by Clinic](#challenge-1-the-yearly-data-split-by-clinic)
    - [My Code](#my-code-3)
    - [Solution to Challenge 1](#solution-to-challenge-1-1)
  - [Challenge 2: Calculate the Proportion of Deaths at Each Clinic](#challenge-2-calculate-the-proportion-of-deaths-at-each-clinic)
    - [My Code](#my-code-4)
    - [Solution to Challenge 2](#solution-to-challenge-2-1)
- [The Effect of Handwashing](#the-effect-of-handwashing)
  - [Challenge 1: The Effect of Handwashing](#challenge-1-the-effect-of-handwashing)
    - [My Code](#my-code-5)
    - [Solution to Challenge 1](#solution-to-challenge-1-2)
  - [Challenge 2: Calculate a Rolling Average of the Death Rate](#challenge-2-calculate-a-rolling-average-of-the-death-rate)
    - [My Code](#my-code-6)
    - [Solution to Challenge 2](#solution-to-challenge-2-2)
  - [Challenge 3: Highlighting Subsections of a Line Chart](#challenge-3-highlighting-subsections-of-a-line-chart)
    - [Solution to Challenge 3](#solution-to-challenge-3-1)
- [Visualizing Distributions and Testing for Statistical Significance](#visualizing-distributions-and-testing-for-statistical-significance)
  - [Challenge 1: Calculate the Difference in the Average Monthly Death Rate](#challenge-1-calculate-the-difference-in-the-average-monthly-death-rate)
    - [My Code](#my-code-7)
    - [Solution to Challenge 1](#solution-to-challenge-1-3)
  - [Challenge 2: Using Box Plots to Show How the Death Rate Changed Before and After Handwashing](#challenge-2-using-box-plots-to-show-how-the-death-rate-changed-before-and-after-handwashing)
    - [My Code](#my-code-8)
    - [Solution to Challenge 2](#solution-to-challenge-2-3)
  - [Challenge 3: Use Histograms to Visualise the Monthly Distribution of Outcomes](#challenge-3-use-histograms-to-visualise-the-monthly-distribution-of-outcomes)
    - [My Code](#my-code-9)
    - [Solution to Challenge 3](#solution-to-challenge-3-2)
  - [Challenge 4: Use a Kernel Density Estimate (KDE) to visualise a smooth distribution](#challenge-4-use-a-kernel-density-estimate-kde-to-visualise-a-smooth-distribution)
    - [My Code](#my-code-10)
    - [Solution to Challenge 4](#solution-to-challenge-4)
  - [Challenge 5: Use a T-Test to Show Statistical Significance](#challenge-5-use-a-t-test-to-show-statistical-significance)
    - [My Code](#my-code-11)
    - [Solution to Challenge 5](#solution-to-challenge-5)

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

# Analysing the Yearly Data Split By Clinic
**Welcome to your workplace...**

There are two maternity wards at the Vienna General Hospital: clinic 1 and clinic 2. Clinic 1 was staffed by all-male doctors and medical students, and clinic 2 was staffed by female midwives.

## Challenge 1: The Yearly Data Split by Clinic
Let's turn our attention to the annual data. Use plotly to create line charts of the births and deaths of the two different clinics at the Vienna General Hospital.
- Which clinic is bigger or more busy judging by the number of births?
- Has the hospital had more patients over time?
- What was the highest number of deaths recorded in clinic 1 and clinic 2?

### My Code
This didn't work.

```py
# Which clinic is bigger or more busy judging by the number of births?
df_yearly[['clinic', 'births']].groupby(['clinic']).mean('births')

# Has the hospital had more patients over time? 
df_yearly[['clinic', 'births']].groupby(['clinic']).sum('births')

# What was the highest number of deaths recorded in clinic 1 and clinic 2?
df_yearly[['clinic', 'deaths']].groupby(['clinic']).max('deaths')

fig, ax1 = plt.subplots(figsize=(14,8), dpi=200)
#ax2 = ax1.twinx()
ax1.grid(color='grey', linestyle='--')

ax1.plot(df_yearly.year, df_yearly.births, color='skyblue', linewidth=3)
#ax2.plot(df_yearly.year, df_yearly.deaths, color='crimson', linewidth=2, linestyle='dashed')
```

### Solution to Challenge 1
To show two line charts side by side we can use plotly and provide the clinic column as the `color`. 

```py
line = px.line(df_yearly, 
                x='year', 
                y='births',
                color='clinic',
                title='Total Yearly Births by Clinic')
  
line.show()
```

We see that more and more women gave birth at the hospital over the years. Clinic 1, which was staffed by male doctors and medical students was also the busier or simply the larger ward. More births took place in clinic 1 than in clinic 2. 

![Results](https://img-b.udemycdn.com/redactor/raw/2020-10-23_11-31-13-b5897c5011eadac9f54e6956b30d4f97.png)

We also see that, not only were more people born in clinic 1, more people also died in clinic 1. 

```py
line = px.line(df_yearly, 
                x='year', 
                y='deaths',
                color='clinic',
                title='Total Yearly Deaths by Clinic')
  
line.show()
```

![Results](https://img-b.udemycdn.com/redactor/raw/2020-10-23_11-32-45-1f1c814dd89d9e8102ff7642a53a3ecd.png)

To compare apples and apples, we need to look at the proportion of deaths per clinic. 

## Challenge 2: Calculate the Proportion of Deaths at Each Clinic
Calculate the proportion of maternal deaths per clinic. That way we can compare like with like.

- Work out the percentage of deaths for each row in the `df_yearly` DataFrame by adding a column called "pct_deaths".
- Calculate the average maternal death rate for clinic 1 and clinic 2 (i.e., the total number of deaths per the total number of births).
- Create another plotly line chart to see how the percentage varies year over year with the two different clinics.
- Which clinic has a higher proportion of deaths?
- What is the highest monthly death rate in clinic 1 compared to clinic 2?

### My Code
```py
df_yearly['pct_deaths'] = df_yearly.deaths / df_yearly.births
df_yearly

clinic_1_avg_maternal_death_rate = df_yearly.groupby('clinic').mean('pct_deaths')
clinic_1_avg_maternal_death_rate

# Clinic 1 has higher proportion
# Clinic 1 has a high of 16% compared to Clinic 2's almost 8%
```

### Solution to Challenge 2
We can add a new column that has the percentage of deaths for each row like this: 
```py
df_yearly['pct_deaths'] = df_yearly.deaths / df_yearly.births
```
The average death rate for the entire time period for clinic 1 is:
```py
clinic_1 = df_yearly[df_yearly.clinic == 'clinic 1']
avg_c1 = clinic_1.deaths.sum() / clinic_1.births.sum() * 100
print(f'Average death rate in clinic 1 is {avg_c1:.3}%.')
```
9.92%. In comparison, clinic 2 which was staffed by midwives had a much lower death rate of 3.88% over the course of the entire period. Hmm... 🤔
```py
clinic_2 = df_yearly[df_yearly.clinic == 'clinic 2']
avg_c2 = clinic_2.deaths.sum() / clinic_2.births.sum() * 100
print(f'Average death rate in clinic 2 is {avg_c2:.3}%.')
```
Once again, let's see this on a chart
```py
line = px.line(df_yearly, 
                x='year', 
                y='pct_deaths',
                color='clinic',
                title='Proportion of Yearly Deaths by Clinic')
  
line.show()
```

1842 was a rough year. About 16% of women died in clinic 1 and about 7.6% of women died in clinic 2. 

![Results](https://img-b.udemycdn.com/redactor/raw/2020-10-23_11-48-48-f1ea588ddc802796ce504f8cae08a844.png)

Still, clinic 2 had a consistently lower death rate than clinic 1! This is what puzzled and frustrated Dr Semmelweis. 

**The story continues...**

At first, Dr Semmelweis thought that the position of the women giving birth was the issue. In clinic 2, the midwives' clinic, women gave birth on their sides. In the doctors' clinic, women gave birth on their backs. So, Dr. Semmelweis, had women in the doctors' clinic give birth on their sides. However, this had no effect on the death rate.

Next, Dr Semmelweis noticed that whenever someone on the ward died, a priest would walk through clinic 1, past the women's beds ringing a bell 🔔. Perhaps the priest and the bell ringing terrified the women so much after birth that they developed a fever, got sick and died. Dr Semmelweis had the priest change his route and stop ringing the bell 🔕. Again, this had no effect.

At this point, Dr Semmelweis was so frustrated he went on holiday to Venice. Perhaps a short break would clear his head. When Semmelweis returned from his vacation, he was told that one of his colleagues, a pathologist, had fallen ill and died. His friend had pricked his finger while doing an autopsy on a woman who had died from childbed fever and subsequently got very sick himself and died. 😮

Looking at the pathologist's symptoms, Semmelweis realised the pathologist died from the same thing as the women he had autopsied.  This was his breakthrough: anyone could get sick from childbed fever, not just women giving birth!

This is what led to Semmelweis' new theory. Perhaps there were little pieces or particles of a corpse that the doctors and medical students were getting on their hands while dissecting the cadavers during an autopsy. And when the doctors delivered the babies in clinic 1, these particles would get inside the women giving birth who would then develop the disease and die.

# The Effect of Handwashing
In June 1846, Dr Semmelweis ordered everyone on his medical staff to start cleaning their hands and instruments not just with soap and water but with a chlorine solution (he didn't know it at the time, but chlorine is an amazing disinfectant). The reason Dr Semmelweis actually chose the chlorine was that he wanted to get rid of any smell on doctors' hands after an autopsy. No one knew anything about bacteria, germs or viruses at the time. 

## Challenge 1: The Effect of Handwashing
- Add a column called "pct_deaths" to `df_monthly` that has the percentage of deaths per birth for each row.
- Create two subsets from the `df_monthly` data: before and after Dr Semmelweis ordered washing hand.
- Calculate the average death rate prior to June 1846.
- Calculate the average death rate after June 1846.

### My Code
```py
# Add a column called "pct_deaths" to df_monthly that has the percentage of deaths per birth for each row. 
df_monthly['pct_deaths'] = df_monthly.deaths / df_monthly.births
df_monthly

# Create two subsets from the df_monthly data: before and after Dr Semmelweis ordered washing hand.
df_pre_handwashing = df_monthly[df_monthly.date < handwashing_start]
df_pre_handwashing

df_post_handwashing = df_monthly[df_monthly.date > handwashing_start]
df_post_handwashing

# Calculate the average death rate prior to June 1846.
print(f'Average Death Rate prior to June 1846: {df_pre_handwashing.pct_deaths.mean()}')

# Calculate the average death rate after June 1846.
print(f'Average Death Rate after June 1846: {df_post_handwashing.pct_deaths.mean()}')
```

### Solution to Challenge 1
We can add a column with the proportion of deaths per birth like so:
```py
df_monthly['pct_deaths'] = df_monthly.deaths/df_monthly.births
```
Then we can create two subsets based on the `handwashing_start` date. 
```py
before_washing = df_monthly[df_monthly.date < handwashing_start]
after_washing = df_monthly[df_monthly.date >= handwashing_start]
```
The death rate per birth dropped dramatically after handwashing started - from close to 10.53% to 2.15%. We can use the colon and dot inside a print statement to determine the number of digits we'd like to print out from a number. 
```py
bw_rate = before_washing.deaths.sum() / before_washing.births.sum() * 100
aw_rate = after_washing.deaths.sum() / after_washing.births.sum() * 100
print(f'Average death rate before 1847 was {bw_rate:.4}%')
print(f'Average death rate AFTER 1847 was {aw_rate:.3}%')
```

## Challenge 2: Calculate a Rolling Average of the Death Rate
Create a DataFrame that has the 6-month rolling average death rate prior to mandatory handwashing.

*Hint:* You'll need to set the dates as the index in order to avoid the date column being dropped during the calculation

### My Code
```py
df_roll_death = df_pre_handwashing.set_index('date')

df_roll_death = df_roll_death.rolling(window=6).mean()
df_roll_death
```

### Solution to Challenge 2
To work out the moving 6-month average we first set the date column as the index. Then we can use the same Pandas functions as in the Google Trends notebook. 
```py
roll_df = before_washing.set_index('date')
roll_df = roll_df.rolling(window=6).mean()
```

## Challenge 3: Highlighting Subsections of a Line Chart
Copy-paste and then modify the Matplotlib chart from before to plot the monthly death rates (instead of the total number of births and deaths). The chart should look something like this:

![Desired Outcome](https://img-b.udemycdn.com/redactor/raw/2020-10-23_12-27-28-063144e4acbc37b96bfd66f6f25f75f3.png)

- Add 3 separate lines to the plot: the death rate before handwashing, after handwashing, and the 6-month moving average before handwashing.
- Show the monthly death rate before handwashing as a thin dashed black line.
- Show the moving average as a thicker, crimson line.
- Show the rate after handwashing as a skyblue line with round markers.
- Look at the [code snippet in the documentation to see how you can add a legend](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html) to the chart.

Blegh. Hate these types of graphs. My efforts weren't even close.

### Solution to Challenge 3
After copy-pasting the previous code for the Matplotlib chart, we just need to change a few things. First, we remove the twin axes. And instead, we plot the three different lines on the same axis. To create the legend, we supply a label to the `.plot()` function and capture return value in a variable. It's important to notice that `.plot()` returns more than one thing, so we need to use a comma (`,`) since we're only grabbing the first item. We can then feed these handles into `plt.legend()`.

```py
# handle overall size and axis
plt.figure(figsize=(14,8), dpi=200)
plt.title('Percentage of Monthly Deaths over Time', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
 
plt.ylabel('Percentage of Deaths', color='crimson', fontsize=18)

# deal with dates on the x-axis to display nicely
ax = plt.gca()
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
ax.set_xlim([df_monthly.date.min(), df_monthly.date.max()])

plt.grid(color='grey', linestyle='--')

# never seen this comma thing before...
ma_line, = plt.plot(roll_df.index, 
                    roll_df.pct_deaths, 
                    color='crimson', 
                    linewidth=3, 
                    linestyle='--',
                    label='6m Moving Average')

bw_line, = plt.plot(before_washing.date, 
                    before_washing.pct_deaths,
                    color='black', 
                    linewidth=1, 
                    linestyle='--', 
                    label='Before Handwashing')

aw_line, = plt.plot(after_washing.date, 
                    after_washing.pct_deaths, 
                    color='skyblue', 
                    linewidth=3, 
                    marker='o',
                    label='After Handwashing')

plt.legend(handles=[ma_line, bw_line, aw_line],
           fontsize=18)
 
plt.show()
```

# Visualizing Distributions and Testing for Statistical Significance
There are even more powerful arguments we can make to convince our fellow doctors in clinic 1 of the virtues of handwashing. The first are statistics regarding the mean monthly death rate. The second are compelling visualisations to accompany the statistics.

## Challenge 1: Calculate the Difference in the Average Monthly Death Rate
- What was the average percentage of monthly deaths before handwashing (i.e., before June 1847)?
- What was the average percentage of monthly deaths after handwashing was made obligatory?
- By how much did handwashing reduce the average chance of dying in childbirth in percentage terms?
- How do these numbers compare to the average for all the 1840s that we calculated earlier?
- How many times lower are the chances of dying after handwashing compared to before?

### My Code
```py
# What was the average percentage of monthly deaths before handwashing? 
before_handwashing = df_pre_handwashing.pct_deaths.mean()*100
print(f'Average Death Rate prior to Handwashing: {round(before_handwashing, 3)}%')

# What was the average percentage of monthly deaths after handwashing was made obligatory?
after_handwashing = df_post_handwashing.pct_deaths.mean()*100
print(f'Average Death Rate after Handwashing: {round(after_handwashing, 3)}%')

# By how much did handwashing reduce the average chance of dying in childbirth in percentage terms?
print(f'Handwashing reduced the average chance of dying in childbirth by: {round(before_handwashing - after_handwashing, 3)}%.')

# How do these numbers compare to the average for all the 1840s that we calculated earlier? 
print('I don\'t know what this is asking.')

# How many times lower are the chances of dying after handwashing compared to before?
print(f'You are {round(before_handwashing/after_handwashing,2)} times less likely to die after handwashing compared to before.')
```

### Solution to Challenge 1
A lot of statistical tests rely on comparing features of distributions, like the mean. We see that the average death rate before handwashing was 10.5%. After handwashing was made obligatory, the average death rate was 2.11%. The difference is massive. Handwashing decreased the average death rate by 8.4%, a 5x improvement. 😮
```py
avg_prob_before = before_washing.pct_deaths.mean() * 100
print(f'Chance of death during childbirth before handwashing: {avg_prob_before:.3}%.')
  
avg_prob_after = after_washing.pct_deaths.mean() * 100
print(f'Chance of death during childbirth AFTER handwashing: {avg_prob_after:.3}%.')
  
mean_diff = avg_prob_before - avg_prob_after
print(f'Handwashing reduced the monthly proportion of deaths by {mean_diff:.3}%!')
  
times = avg_prob_before / avg_prob_after
print(f'This is a {times:.2}x improvement!')
```

## Challenge 2: Using Box Plots to Show How the Death Rate Changed Before and After Handwashing
The statistic above is impressive, but how do we show it graphically? With a box plot we can show how the quartiles, minimum, and maximum values changed in addition to the mean. 

- Use [NumPy's `.where()` function](https://numpy.org/doc/stable/reference/generated/numpy.where.html) to add a column to `df_monthly` that shows if a particular date was before or after the start of handwashing.
- Then use plotly to create box plot of the data before and after handwashing.
- How did key statistics like the mean, max, min, 1st and 3rd quartile changed as a result of the new policy

### My Code
```py
# Add a column to df_monthly that shows if a particular date was before or after the start of handwashing
df_monthly['Handwashing'] = np.where(df_monthly.date < handwashing_start, False, True)
df_monthly

# Then use plotly to create box plot of the data before and after handwashing. 

fig = px.box(df_monthly, x='Handwashing', y="pct_deaths", color='Handwashing', title='Impact of Handwashing')

fig.update_layout(xaxis_title='Handwashing', yaxis_title='Monthly Death Rate')

fig.show()

#  How did key statistics like the mean, max, min, 1st and 3rd quartile changed as a result of the new policy?
print('Everything got better! D\'oh!')
```

### Solution to Challenge 2
The easiest way to create a box plot is to have a column in our DataFrame that shows the rows' "category" (i.e., was it before or after obligatory handwashing). NumPy allows us to easily test for a condition and add a column of data.
```py
df_monthly['washing_hands'] = np.where(df_monthly.date < handwashing_start, 'No', 'Yes')
```
Now we can use plotly:
```py
box = px.box(df_monthly, 
              x='washing_hands', 
              y='pct_deaths',
              color='washing_hands',
              title='How Have the Stats Changed with Handwashing?')
  
box.update_layout(xaxis_title='Washing Hands?',
                  yaxis_title='Percentage of Monthly Deaths',)
  
box.show()
```
![Results](https://img-b.udemycdn.com/redactor/raw/2020-10-23_14-39-42-eb859925d7e636d7244c6b410bad919b.png)

The plot shows us the same data as our Matplotlib chart, but from a different perspective. Here we also see the massive spike in deaths in late 1842. Over 30% of women who gave birth that month died in hospital. What we also see in the box plot is how not only did the average death rate come down, but so did the overall range - we have a lower max and 3rd quartile too. Let's take a look at a histogram to get a better sense of the distribution.

## Challenge 3: Use Histograms to Visualise the Monthly Distribution of Outcomes
Create a [plotly histogram](https://plotly.com/python/histograms/) to show the monthly percentage of deaths.
- Use docs to check out the available parameters. Use the [`color` parameter](https://plotly.github.io/plotly.py-docs/generated/plotly.express.histogram.html) to display two overlapping histograms.
- The time period of handwashing is shorter than not handwashing. Change `histnorm` to `percent` to make the time periods comparable.
- Make the histograms slightly transparent
- Experiment with the number of bins on the histogram. Which number works well in communicating the range of outcomes?
- Just for fun, display your box plot on the top of the histogram using the `marginal` parameter

### My Code
```py
fig = px.histogram(df_monthly, x="pct_deaths", color="Handwashing", histnorm="percent", marginal="box", nbins=20)
fig.update_layout(barmode='overlay')
fig.update_traces(opacity=0.75)
fig.update_layout(xaxis_title='Proportion of Monthly Deaths',yaxis_title='Count')
fig.show()
```

### Solution to Challenge 3
To create our histogram, we once again make use of the color parameter. This creates two separate histograms for us. When we set the opacity to 0.6 or so we can clearly see how the histograms overlap. The trick to getting a sensible-looking histogram when you have a very different number of observations is to set the `histnorm` to 'percent'. That way the histogram with more observations won't completely overshadow the shorter series.
```py
hist = px.histogram(df_monthly, 
                    x='pct_deaths', 
                    color='washing_hands',
                    nbins=30,
                    opacity=0.6,
                    barmode='overlay',
                    histnorm='percent',
                    marginal='box',)
  
hist.update_layout(xaxis_title='Proportion of Monthly Deaths',
                    yaxis_title='Count',)
  
hist.show()
```
I quite like how in plotly we can display our box plot from earlier at the top. 
![Results](https://img-b.udemycdn.com/redactor/raw/2020-10-23_14-49-58-3961b13cff88b2866bba7da183716a04.png)

Now, we have only about 98 data points or so, so our histogram looks a bit jagged. It's not a smooth bell-shaped curve. However, we can estimate what the distribution would look like with a Kernel Density Estimate (KDE).

## Challenge 4: Use a Kernel Density Estimate (KDE) to visualise a smooth distribution
Use [Seaborn's `.kdeplot()`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) to create two kernel density estimates of the pct_deaths, one for before handwashing and one for after.
- Use the `shade` parameter to give your two distributions different colours.
- What weakness in the chart do you see when you just use the default parameters?
- Use the `clip` parameter to address the problem.

### My Code
```py
sns.kdeplot(data=df_monthly, x='pct_deaths', hue='Handwashing', clip=[0,.45], shade=True)
```

### Solution to Challenge 4
To create two bell-shaped curves of the estimated distributions of the death rates we just call `.kdeplot()` twice. 
```py
plt.figure(dpi=200)
# By default the distribution estimate includes a negative death rate!
sns.kdeplot(before_washing.pct_deaths, shade=True)
sns.kdeplot(after_washing.pct_deaths, shade=True)
plt.title('Est. Distribution of Monthly Death Rate Before and After Handwashing')
plt.show()
```
However, the problem is that we end up with a negative monthly death rate on the left tail. The doctors would be very surprised indeed if a corpse came back to life after an autopsy! 🧟‍♀️ 

![Results](https://img-b.udemycdn.com/redactor/raw/2020-10-23_14-59-53-0b2eb0809a34c6eb94983086e631800c.png)

The solution is to specify a lower bound of 0 for the death rate. 

```py
plt.figure(dpi=200)
sns.kdeplot(before_washing.pct_deaths, 
            shade=True,
            clip=(0,1))
sns.kdeplot(after_washing.pct_deaths, 
            shade=True,
            clip=(0,1))
plt.title('Est. Distribution of Monthly Death Rate Before and After Handwashing')
plt.xlim(0, 0.40)
plt.show()
```

![Results](https://img-b.udemycdn.com/redactor/raw/2020-10-23_15-00-50-d951f463f0f6b86e096672a3d6a05e77.png)

Now that we have an idea of what the two distributions look like, we can further strengthen our argument for handwashing by using a statistical test. We can test whether our distributions ended up looking so different purely by chance (i.e., the lower death rate is just an accident) or if the 8.4% difference in the average death rate is **statistically significant**. 

## Challenge 5: Use a T-Test to Show Statistical Significance
Use a t-test to determine if the differences in the means are statistically significant or purely due to chance.

If the p-value is less than 1% then we can be 99% certain that handwashing has made a difference to the average monthly death rate.
- Import `stats` from scipy
- Use the [`.ttest_ind()` function](https://docs.scipy.org/%5Ddoc/scipy/reference/generated/scipy.stats.ttest_ind.html) to calculate the t-statistic and the p-value
- Is the difference in the average proportion of monthly deaths statistically significant at the 99% level?

### My Code
```py
import scipy.stats as stats

statistic, pvalue = stats.ttest_ind(a=df_pre_handwashing.pct_deaths, b=df_post_handwashing.pct_deaths)
print(f'Statistic: {statistic}\nP-Value: {pvalue}')
```

### Solution to Challenge 5
The first step is to import stats from scipy
```py
import scipy.stats as stats
```
When we calculate the p_value we see that it is 0.0000002985 or .00002985% which is far below even 1%. In other words, the difference in means is highly statistically significant and we can go ahead on publish our research paper 😊 

```py
t_stat, p_value = stats.ttest_ind(a=before_washing.pct_deaths, 
                                  b=after_washing.pct_deaths)
print(f'p-palue is {p_value:.10f}')
print(f't-statstic is {t_stat:.4}')
```