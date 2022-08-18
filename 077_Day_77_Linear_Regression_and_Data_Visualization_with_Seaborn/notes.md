# Day 77: Advanced - Linear Regression and Data Visualization with Seaborn

- [Day 77: Advanced - Linear Regression and Data Visualization with Seaborn](#day-77-advanced---linear-regression-and-data-visualization-with-seaborn)
- [What You Will Make](#what-you-will-make)
- [Explore and Clean the Data](#explore-and-clean-the-data)
  - [Challenge 1](#challenge-1)
  - [Challenge 2](#challenge-2)
  - [Challenge 3](#challenge-3)
- [Investigate the Films that had Zero Revenue](#investigate-the-films-that-had-zero-revenue)
- [Filter on Multiple Conditions: International Films](#filter-on-multiple-conditions-international-films)
- [Seaborn Data Visualization: Bubble Charts](#seaborn-data-visualization-bubble-charts)
- [Floor Division: A Trick to Convert Years to Decades](#floor-division-a-trick-to-convert-years-to-decades)
- [Plotting Linear Regressions with Seaborn](#plotting-linear-regressions-with-seaborn)
- [Use scikit-learn to Run Your Own Regression](#use-scikit-learn-to-run-your-own-regression)
- [Learning Points & Summary](#learning-points--summary)

# What You Will Make
In this lesson, we're going to be looking at movie budget and revenue data. This dataset is perfect for trying out some new tools like scikit-learn to run a linear regression and seaborn, a popular data visualisation library built on top of Matplotlib.  

![Movies](https://img-b.udemycdn.com/redactor/raw/2020-10-14_11-55-48-2c83542d09cb8d7e8c8dfc03616734f7.png)

The question we want to answer today is: Do higher film budgets lead to more revenue in the box office? In other words, should a movie studio spend more on a film to make more?  

**Today you'll learn:**
- How to use a popular data visualisation library called Seaborn
- How to run and interpret a linear regression with scikit-learn
- How to plot a regression a scatter plot to visualise relationships in the data
- How to add a third dimension to a scatter plot to create a bubble chart
- How to cleverly use floor division `//` to convert your data

![Seaborn Image](https://img-b.udemycdn.com/redactor/raw/2020-10-14_11-48-35-4f37a708b04a864a3fe1ab0b2138dd05.png)

**Download and add the Notebook to Google Drive**
As usual, download the .zip file from this lesson and extract it. Add the .ipynb file into your Google Drive and open it as a Google Colaboratory notebook.

**Add the Data to the Notebook**
The .zip file also includes a .csv file called cost_revenue_dirty. This is the data for the project. Add this file to your notebook.

![SciKit Learn Image](https://img-b.udemycdn.com/redactor/raw/2020-10-14_11-57-57-f2a45422e3025ee7021afa483d10ade8.png)

# Explore and Clean the Data
As with any dataset, the first steps are going to be data exploration and data cleaning. We need to get a better understanding of what we're dealing with. Since you've gone through this process a number of times before on previous days, can you tackle the following challenges on your own? 

## Challenge 1
Answer these questions about how the data is structured:
1. How many rows and columns does the dataset contain?
    - 5391 rows, 6 columns
2. Are there any NaN values present?
    - Negative
3. Are there any duplicate rows?
    - Negative
4. What are the data types of the columns?


| Column Name | Data Type |
| :--- | :--- |
| Rank | int64 |
| Release_Date | object |
| Movie_Title | object |
| USD_Production_Budget | object |
| USD_Worldwide_Gross | object | 
| USD_Domestic_Gross | object |

```py
data.shape
data.isna().any(axis=None)
data.duplicated().any(axis=None)
data.dtypes
```

**Instructor Solution**
With any new dataset, it's a good idea to do some standard checks and conversions. I typically always first look at `.shape`, `.head()`, `.tail()`, `.info()` and `.sample()`.  Here's what I'm spotting already:

![Soluion Image](https://img-b.udemycdn.com/redactor/raw/2020-10-14_14-46-28-63dd3d1025bbcd51f2effa33132c48f0.png)

There are thousands of entries in the DataFrame - one entry for each movie. We'll have some challenges formatting the data before we can do more analysis because we have non-numeric characters in our budget and revenue columns. 

We can check for NaN values with this line:
```py
    data.isna().values.any()
```
And check for duplicates with this line:
```py
    data.duplicated().values.any()
```
We can see the total number of duplicates by creating a subset and looking at the length of that subset:
```py
    duplicated_rows = data[data.duplicated()]
    len(duplicated_rows)
```

![Query Results](https://img-b.udemycdn.com/redactor/raw/2020-10-14_14-51-20-7ae3dea5e27c5d9ea9d7e26b9bdddc36.png)

The fact that there are no duplicates or NaN (not-a-number) values in the dataset will make our job easier. We can also see if there are null values in `.info()`, which also shows us that we need to do some type conversion.

![Info Results](https://img-b.udemycdn.com/redactor/raw/2020-10-14_14-54-47-6c35659efd0a6ebd03bde9de6851e72c.png)


## Challenge 2
Convert the `USD_Production_Budget`, `USD_Worldwide_Gross`, and `USD_Domestic_Gross` columns to a numeric format by removing `$` signs and `,`.

Note that *domestic* in this context refers to the United States.

```py
data[data.columns[3:]] = data[data.columns[3:]].replace('[\$,]','', regex=True).astype(float)
data[data.columns[3:]].dtypes
```

**Instructor Solution**
In order to convert the data in the budget and revenue columns and remove all the non-numeric characters, we can use a nested for loop. We create two Python lists: the characters to remove and the column names. Inside the nested loop we can combine `.replace()` and `.to_numeric()` to achieve our goal.
```py
    chars_to_remove = [',', '$']
    columns_to_clean = ['USD_Production_Budget', 
                        'USD_Worldwide_Gross',
                        'USD_Domestic_Gross']
     
    for col in columns_to_clean:
        for char in chars_to_remove:
            # Replace each character with an empty string
            data[col] = data[col].astype(str).str.replace(char, "")
        # Convert column to a numeric data type
        data[col] = pd.to_numeric(data[col])
```
![Results](https://img-b.udemycdn.com/redactor/raw/2020-10-14_15-01-32-a70628a70ce1a0f946a2a760132323ba.png)

## Challenge 3
Convert the Release_Date column to a Pandas Datetime type.
```py
data['Release_Date'] = pd.to_datetime(data['Release_Date'])
data.dtypes
```

**Instructor Solution**
To convert the Release_Date column to a DateTime object, all we need to do is call the `to_datetime()` function.
```py
    data.Release_Date = pd.to_datetime(data.Release_Date)
```
When we check `.info()` again we see that the columns now have the desired data type. This allows us to proceed with the next parts of our analysis. 

![Results](https://img-b.udemycdn.com/redactor/raw/2020-10-14_15-06-08-862b621b9dfc92e9110a1619e0da56ee.png)


# Investigate the Films that had Zero Revenue

# Filter on Multiple Conditions: International Films

# Seaborn Data Visualization: Bubble Charts

# Floor Division: A Trick to Convert Years to Decades

# Plotting Linear Regressions with Seaborn

# Use scikit-learn to Run Your Own Regression

# Learning Points & Summary