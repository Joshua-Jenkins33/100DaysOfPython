- [Day 71: Data Exploration with Pandas: College Major v.s. Your Salary](#day-71-data-exploration-with-pandas-college-major-vs-your-salary)
  - [Getting Set Up for Data Science](#getting-set-up-for-data-science)
  - [Upload the Data and Read the .csv File](#upload-the-data-and-read-the-csv-file)
  - [Preliminary Data Exploration and Data Cleaning with Pandas](#preliminary-data-exploration-and-data-cleaning-with-pandas)
    - [Missing Values and Junk Data](#missing-values-and-junk-data)
      - [Delete the Last Row](#delete-the-last-row)
  - [Accessing Columns and Individual Cells in a Dataframe](#accessing-columns-and-individual-cells-in-a-dataframe)
    - [Find College Major with Highest Starting Salaries](#find-college-major-with-highest-starting-salaries)
    - [Challenge](#challenge)
  - [Solution: Highest and Lowest Earning Degrees](#solution-highest-and-lowest-earning-degrees)
    - [The Highest Mid-Career Salary](#the-highest-mid-career-salary)
    - [The Lowest Starting and Mid-Career Salary](#the-lowest-starting-and-mid-career-salary)
  - [Sorting Values & Adding Columns: Majors with the Most Potential vs Lowest Risk](#sorting-values--adding-columns-majors-with-the-most-potential-vs-lowest-risk)
    - [Lowest Risk Majors](#lowest-risk-majors)
      - [Sorting by the Lowest Spread](#sorting-by-the-lowest-spread)
    - [Challenge](#challenge-1)
  - [Solution: Degress with the Highest Potential](#solution-degress-with-the-highest-potential)
    - [Majors with the Highest Potential](#majors-with-the-highest-potential)
    - [Majors with the Greatest Spread in Salaries](#majors-with-the-greatest-spread-in-salaries)
  - [Grouping and Pivoting Data with Pandas](#grouping-and-pivoting-data-with-pandas)
    - [Mini Challenge](#mini-challenge)
    - [Number formats in the Output](#number-formats-in-the-output)
    - [Extra Credit](#extra-credit)
  - [Learning Points & Summary](#learning-points--summary)

# Day 71: Data Exploration with Pandas: College Major v.s. Your Salary
Learn Data Exploration with Pandas by Analysing the Post-University Salaries of Graduates by Major 

College degrees are *very* expensive. But, do they pay you back? Choosing Philosophy or International Relations as a major may have worried your parents, but does the data back up their fears? PayScale Inc. did a year-long survey of 1.2 million Americans with only a bachelor's degree. We'll be digging into this data and use Pandas to answer these questions: 
- Which degrees have the highest starting salaries? 
- Which majors have the lowest earnings after college?
- Which degrees have the highest earning potential?
- What are the lowest risk college majors from an earnings standpoint?
- Do business, STEM (Science, Technology, Engineering, Mathematics) or HASS (Humanities, Arts, Social Science) degrees earn more on average? 

Today you'll learn 
- How to explore a Pandas DataFrame
- How to detect NaN (not a number) values and clean your data
- How to select particular columns, rows, and individual cells
- How to sort your data
- How to group data by category

and so much more! Let's get started!

## Getting Set Up for Data Science
**Introducing the Google Colab Notebook**

PyCharm is a fantastic IDE, but when we're exploring and visualising a dataset, you'll find the Python notebook format better suited.

Open your first Google Colab Notebook in through your [Google Drive](https://drive.google.com/). You can find the Python Notebook under New → More → Google Colaboratory

If you cannot access the Google Colab Notebooks or would like to run everything locally on your computer, then I recommend [installing Anaconda](https://www.anaconda.com/products/individual) and using the bundled Jypyter Notebook instead. Either way works. Google Colab is essentially just an online version of Jupyter. 

**How to use a Python Notebook**
The notebook is divided into cells. Each cell can be executed individually and the result is automatically printed out below. To execute a cell use the shortcut **Shift + Enter**. 

*Note:* The Google Colab Notebook will to connect to a Runtime in order to execute any code.


That's pretty much it. Let's get started!

## Upload the Data and Read the .csv File
Download the salaries_by_college_major.csv file from the course resources and add this file to the notebook by dropping it into the sidebar with the little folder icon.

Then import pandas into your notebook and read the .csv file. 

```py
import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')
```

You can save yourself some typing by bringing up the autocompletion by using the keyboard shortcuts `ctrl` + `Space` (windows) or `⌘` + `Space` (Mac). 

Now take a look at the Pandas dataframe we've just created with .head(). This will show us the first 5 rows of our dataframe.

```py
df.head() 
```

Once you hit shift + enter on your keyboard the cell will be evaluated and you should see the output automatically printed below the cell. This feature of automatically printing the output below in a pretty format is what makes the notebook format so lovely to work with. 

## Preliminary Data Exploration and Data Cleaning with Pandas
Now that we've got our data loaded into our dataframe, we need to take a closer look at it to help us understand what it is we are working with. This is always the first step with any data science project. Let's see if we can answer the following questions: 

- How many rows does our dataframe have? 
- How many columns does it have?
- What are the labels for the columns? Do the columns have names?
- Are there any missing values in our dataframe? Does our dataframe contain any bad data? 

We've already used the `.head()` method to peek at the top 5 rows of our dataframe. To see the number of rows and columns we can use the `shape` attribute: 

```py
df.shape
```

Do you see 51 rows and 6 columns printed out below the cell? 

We saw that each column had a name. We can access the column names directly with the `columns` attribute. 

```py
df.columns
```

### Missing Values and Junk Data
Before we can proceed with our analysis we should try and figure out if there are any missing or junk data in our dataframe. That way we can avoid problems later on. In this case, we're going to look for NaN (Not A Number) values in our dataframe. NAN values are blank cells or cells that contain strings instead of numbers. Use the `.isna()` method and see if you can spot if there's a problem somewhere.

```py
df.isna()
```

Did you find anything? Check the last couple of rows in the dataframe:

```py
df.tail()
```

Aha! We have a row that contains some information regarding the source of the data with blank values for all the other other columns. 

#### Delete the Last Row
We don't want this row in our dataframe. There's two ways you can go about removing this row. The first way is to manually remove the row at index 50. The second way is to simply use the `.dropna()` method from pandas. Let's create a new dataframe without the last row and examine the last 5 rows to make sure we removed the last row:

```py
clean_df = df.dropna()
clean_df.tail()
```

## Accessing Columns and Individual Cells in a Dataframe

### Find College Major with Highest Starting Salaries
To access a particular column from a data frame, we can use the square bracket notation, like so:

```py
clean_df['Starting Median Salary']
```

You should see all the values printed out below the cell for just this column:

```
0     46000.0
1     57700.0
2     42600.0
3     36800.0
4     41600.0
5     35800.0
6     38800.0
7     43000.0
8     63200.0
9     42600.0
10    53900.0
11    38100.0
12    61400.0
13    55900.0
14    53700.0
15    35000.0
16    35900.0
17    50100.0
18    34900.0
19    60900.0
20    38000.0
21    37900.0
22    47900.0
23    39100.0
24    41200.0
25    43500.0
26    35700.0
27    38800.0
28    39200.0
29    37800.0
30    57700.0
31    49100.0
32    36100.0
33    40900.0
34    35600.0
35    49200.0
36    40800.0
37    45400.0
38    57900.0
39    35900.0
40    54200.0
41    39900.0
42    39900.0
43    74300.0
44    50300.0
45    40800.0
46    35900.0
47    34100.0
48    36500.0
49    34000.0
Name: Starting Median Salary, dtype: float64
```
To find the highest starting salary we can simply chain the `.max()` method. 

```py
clean_df['Starting Median Salary'].max()
```

The highest starting salary is $74,300. But which college major earns this much on average? For this, we need to know the row number or **index** so that we can look up the name of the major. Lucky for us, the `.idxmax`() method will give us index for the row with the largest value. 

```py
clean_df['Starting Median Salary'].idxmax()
```

which is 43. To see the name of the major that corresponds to that particular row, we can use the `.loc` (location) property. 

```py
clean_df['Undergraduate Major'].loc[43]
```

Here we are selecting both a column ('Undergraduate Major') and a row at index 43, so we are retrieving the value of a particular cell. You might see people using the double square brackets notation to achieve exactly the same thing: 

```py
clean_df['Undergraduate Major'][43]
```

If you don't specify a particular column you can use the .loc property to retrieve an entire row: 

```py
clean_df.loc[43]
```

### Challenge
Now that we've found the major with the highest starting salary, can you write the code to find the following:

- What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).
- Which college major has the lowest starting salary and how much do graduates earn after university?
- Which college major has the lowest mid-career salary and how much can people expect to earn with this degree? 

I'll provide the solution and the code snippets in the next lesson =) 

## Solution: Highest and Lowest Earning Degrees

### The Highest Mid-Career Salary
```py
print(clean_df['Mid-Career Median Salary'].max())
print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
clean_df['Undergraduate Major'][8]
```

If you have multiple lines in the same cell, only the last one will get printed as an output automatically. If you'd like to see more than one thing printed out, then you still have to use a print statement on the lines above. 

### The Lowest Starting and Mid-Career Salary
```py
print(clean_df['Starting Median Salary'].min())
clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]
```

Here I've nested the code that we've seen in the previous lesson in the same line. We can also use the `.loc` property to access an entire row. Below I've accessed the row at the index of the smallest mid-career salary:

```py
clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]
```

Sadly, education is actually the degree with the lowest mid-career salary and Spanish is the major with the lowest starting salary. 


## Sorting Values & Adding Columns: Majors with the Most Potential vs Lowest Risk

### Lowest Risk Majors
A low-risk major is a degree where there is a small difference between the lowest and highest salaries. In other words, if the difference between the 10th percentile and the 90th percentile earnings of your major is small, then you can be more certain about your salary after you graduate.

How would we calculate the difference between the earnings of the 10th and 90th percentile? Well, Pandas allows us to do simple arithmetic with entire columns, so all we need to do is take the difference between the two columns:

```py
clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
```

Alternatively, you can also use the `.subtract()` method. 

```py
clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
```

The output of this computation will be another Pandas dataframe column. We can add this to our existing dataframe with the `.insert()` method:

```py
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()
```

The first argument is the position of where the column should be inserted. In our case, it's at position 1, so the second column. 

#### Sorting by the Lowest Spread
To see which degrees have the smallest spread, we can use the `.sort_values()` method. And since we are interested in only seeing the name of the degree and the major, we can pass a list of these two column names to look at the .head() of these two columns exclusively.

```py
low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()
```


Does `.sort_values()` sort in ascending or descending order? To find out, check out the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)

You can also bring up the quick documentation with shift + tab on your keyboard directly in the Python notebook. 

**The Answer:** Ascending

### Challenge
Using the .sort_values() method, can you find the degrees with the highest potential? Find the top 5 degrees with the highest values in the 90th percentile. 

Also, find the degrees with the greatest spread in salaries. Which majors have the largest difference between high and low earners after graduation.

I've got the solution for you in the next lesson. 

**Answers.** See `Careers wit hthe Highest Potential.ipynb`

## Solution: Degress with the Highest Potential
Here's the solution to the challenge from the previous lesson: 

### Majors with the Highest Potential
```py
highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()
```

### Majors with the Greatest Spread in Salaries
```py
highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()
```

Notice how 3 of the top 5 are present in both. This means that there are some very high earning Economics degree holders out there, but also some who are not earning as much. It's actually quite interesting to compare these two rankings versus the degrees where the median salary is very high. 

```py
highest_spread = clean_df.sort_values('Mid-Career Median Salary', ascending=False)
highest_spread[['Undergraduate Major', 'Mid-Career Median Salary']].head()
```

## Grouping and Pivoting Data with Pandas
Often times you will want to sum rows that belong to a particular category. For example, which category of degrees has the highest average salary? Is it STEM, Business or HASS (Humanities, Arts, and Social Science)? 

To answer this question we need to learn to use the `.groupby()` method. This allows us to manipulate data similar to a Microsoft Excel Pivot Table.

We have three categories in the 'Group' column: STEM, HASS and Business. Let's count how many majors we have in each category:

```py
clean_df.groupby('Group').count()
```

### Mini Challenge
Now can you use the `.mean()` method to find the average salary by group? 

```py
clean_df.groupby('Group').mean()
```

### Number formats in the Output
The above is a little hard to read, isn't it? We can tell Pandas to print the numbers in our notebook to look like 1,012.45 with the following line:

```py
pd.options.display.float_format = '{:,.2f}'.format 
```

### Extra Credit
The PayScale dataset used in this lesson was from 2008 and looked at the prior 10 years. Notice how Finance ranked very high on post-degree earnings at the time. However, we all know there was a massive financial crash in that year. Perhaps things have changed. Can you use what you've learnt about web scraping in the prior lessons (e.g., Day 45) and share some updated information from PayScale's website in the comments below? 

TODO: Return to this!

## Learning Points & Summary
- Use `.head()`, `.tail()`, `.shape` and `.columns` to explore your DataFrame and find out the number of rows and columns as well as the column names.
- Look for NaN (not a number) values with `.findna()` and consider using `.dropna()` to clean up yourDataFrame.
- You can access entire columns of a DataFrame using the square bracket notation: `df['column name']` or `d[['column name 1', 'column name 2', 'column name 3']]`
- You can access individual cells in a DataFrame by chaining square brackets `df['column name'][index]` or using `df['column name'].loc[index]`
- The largest and smallest values, as well as their positions, can be found with methods like `.max()`, `.mi()`, `.idxmax()` and `.idxmin()`
- You can sort the DataFrame with `.sort_values()` and add new columns with `.insert()`
- To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the `.groupby()` method


I've attached the completed notebook to this lesson as a .zip file. If you have any issues, unzip the file, upload it to google drive and open it as a Google Colab Notebook. 