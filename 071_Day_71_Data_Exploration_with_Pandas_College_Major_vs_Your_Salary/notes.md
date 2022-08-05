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

## Solution: Highest and Lowest Earning Degrees

## Sorting Values & Adding Columns: Majors with the Most Potential vs Lowest Risk