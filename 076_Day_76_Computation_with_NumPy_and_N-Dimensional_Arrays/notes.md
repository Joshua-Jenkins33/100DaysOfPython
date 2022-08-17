# Day 76: Advanced - Computation with NumPy and N-Dimensional Arrays

# What We'll Make
No Data Science course can be complete without learning NumPy (Numerical Python). NumPy is a Python library that’s used in almost every field of science and engineering. It’s practically **THE** standard for working with numerical data in Python. The case studies for how NumPy is being used speak for themselves 😮 

![Case Studies](https://img-b.udemycdn.com/redactor/raw/2020-10-12_10-22-08-b0c1d1c029ea910a79ae216ff161c1c1.png)

So far, we’ve been using Pandas, which is built on top of NumPy. Think of Pandas as a high-level data manipulation tool that includes functionality for working with time-series or for grouping, joining, merging and finding missing data (i.e., everything we’ve been doing so far). NumPy on the other hand shines with low-level tasks, like doing serious math and calculations.

**Today we'll learn:**
- How to leverage the power 💪 of NumPy's ndarrays
- How to access individual values and subsets inside an n-dimensional array.
- How broadcasting 📣 works with ndarrays.
- How to do linear algebra with NumPy.
- How to generate points that you can plot on a chart.
- How to manipulate images as ndarrays. 

![NumPy](https://img-b.udemycdn.com/redactor/raw/2020-10-12_10-09-26-7787e15311eec7748b7ef1aa01140549.png)

**Download and add the Notebook to Google Drive**

As usual, download the .zip file from this lesson and extract it. Add the .ipynb file into your Google Drive and open it as a Google Colaboratory notebook.

**Add the Data to the Notebook**

The .zip file also includes an image. This is the data for the project. Add this file to your notebook.


# NumPy's `ndarray` - Incredible Power at Your Fingertips!
Let’s import NumPy

![Import NumPy](https://img-b.udemycdn.com/redactor/raw/2020-10-12_09-41-31-067a30d8e9bda1db2f2e5752632a0da3.png)

We’ll follow convention and use the name `np`.

The crown jewel of NumPy is the `ndarray`. The **ndarray** is a *homogeneous n-dimensional array* object. What does that mean? 🤨

A Python List or a Pandas DataFrame can contain a mix of strings, numbers, or objects (i.e., a mix of different types). **Homogenous** means all the data have to have the same data type, for example all floating-point numbers.

And **n-dimensional** means that we can work with everything from a single column (1-dimensional) to the matrix (2-dimensional) to a bunch of matrices stacked on top of each other (n-dimensional).

![Different Dimensions](https://img-b.udemycdn.com/redactor/raw/2020-10-12_15-34-45-6fdebf22c1ab4c51fd82687144c0f215.gif)

## 1-Dimension
Let’s create a 1-dimensional array (i.e., a “vector”)
```py
    my_array = np.array([1.1, 9.2, 8.1, 4.7])
```
We can see `my_array` is 1 dimensional by looking at its shape
```py
    my_array.shape
```
We access an element in a ndarray similar to how we work with a Python List, namely by that element's index:
```py
    my_array[2]
```
Let’s check the dimensions of my_array with the `ndim` attribute:
```py
    my_array.ndim
```

![1-Dimension Array Image](https://img-b.udemycdn.com/redactor/raw/2020-10-12_09-45-49-516f9f87a63a881bad1f7d13a190b2a5.png)

## 2-Dimensions
Now, let’s create a 2-dimensional array (i.e., a “matrix”)
```py
    array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])
```
Note we have two pairs of square brackets. This array has 2 rows and 4 columns. NumPy refers to the dimensions as **axes**, so the first axis has length 2 and the second axis has length 4.
```py
    print(f'array_2d has {array_2d.ndim} dimensions')
    print(f'Its shape is {array_2d.shape}')
    print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
    print(array_2d)
```
Again, you can access a particular row or a particular value with the square bracket notation. To access a particular value, you have to provide an index for each dimension. We have two dimensions, so we need to provide an index for the row and for the column. Here’s how to access the 3rd value in the 2nd row:
```py
    array_2d[1,2]
```
To access an entire row and all the values therein, you can use the : operator just like you would do with a Python List. Here’s the entire first row:
```py
    array_2d[0, :]
```

![2-Dimensions Array Image](https://img-b.udemycdn.com/redactor/raw/2020-10-12_09-56-06-a843401b2d459f4afabfcb8979e0b5ae.png)

## N-Dimensions
An array of 3 dimensions (or higher) is often referred to as a ”tensor”. Yes, that’s also where Tensorflow, the popular machine learning tool, gets its name. A tensor simply refers to an n-dimensional array. Using what you've learned about 1- and 2-dimensional arrays, can you apply the same techniques to tackle a more complex array?

### Challenge
- How many dimensions does the array below have?
- What is its shape (i.e., how many elements are along each axis)?
- Try to access the value `18` in the last line of code.
- Try to retrieve a 1-dimensional vector with the values `[97, 0, 27, 18]`
- Try to retrieve a (3,2) matrix with the values `[[ 0, 4], [ 7, 5], [ 5, 97]]`

```py
mystery_array = np.array([[[0, 1, 2, 3],
                            [4, 5, 6, 7]],
                        
                          [[7, 86, 6, 98],
                          [5, 1, 0, 4]],
                          
                          [[5, 36, 32, 48],
                            [97, 0, 27, 18]]])
```

**My Code**
```py
print(f'mystery_array has {mystery_array.ndim} dimensions')
print(f'mystery_array has a shape of {mystery_array.shape}')
mystery_array[2,1,3]
mystery_array[2, 1, :]
mystery_array[:, :, 0]
```

**Solution: Working with Higher Dimensions**
This is really where we have to start to wrap our heads around how ndarrays work because it takes some getting used to the notation.

The `ndim` and `shape` attributes show us the number of dimensions and the length of the axes respectively.
```py
    print(f'We have {mystery_array.ndim} dimensions')
    print(f'The shape is {mystery_array.shape}')
```
The shape is (3, 2, 4), so we have 3 elements along axis #0, 2 elements along axis #1 and 4 elements along axis #3.

To access the value `18` we, therefore, have to provide three different indices - one for each axis. As such, we locate the number at index 2 for the first axis, index number 1 for the second axis, and index number 3 for the third axis.
```py
    mystery_array[2, 1, 3]
```
The values [97, 0, 27, 18] live on the 3rd axis and are on position 2 for the first axis and position 1 on the second axis. Hence we can retrieve them like so:

```py
    mystery_array[2, 1, :]
```
Finally, to retrieve all the first elements on the third axis, we can use the colon operator for the other two dimensions.
```py
    mystery_array[:, :, 0]
```
With the square brackets serving as your guide, the ndarray is quite difficult to visualise for 3 or more dimensions. So if any of this was unclear or confusing. Pause on this lesson for a minute and play around with the array above. Try selecting different subsets from the array. That way you can get comfortable thinking along the different dimensions of the ndarray.

![Challenge 1 Solution Picture](https://img-b.udemycdn.com/redactor/raw/2020-10-12_10-05-16-0b2602de044a3b75e9e084c6f329d39c.png)

# Generating and Manipulating ndarrays

# Broadcasting, Scalars, and Matrix Multiplication

# Manipulating Images as ndarrays

# Learning Points & Summary