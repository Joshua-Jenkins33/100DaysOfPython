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
NumPy has many `many` pages of documentation on all of its extensive functionality. But rather than go through the list one by one, the best way to actually learn NumPy is to apply it to a series of small problems. That way you can familiarise yourself with how to use NumPy for the common use cases that you'll encounter on your own data science journey too. 

## Challenge 1
Use `.arange()` to createa a vector `a` with values ranging from 10 to 29. You should get this:
```py
print(a)

[10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]
```

**My Code**
```py
a = np.arange(start=10, stop=30, step=1)
print(a)
```

**Instructor Solution**
```py
    a = np.arange(10,30)
    print(a)
```

## Challenge 2
Use Python slicing techniques on `a` to:
- Create an array containing only the last 3 values of `a`
- Create a subset with only the 4th, 5th, and 6th values
- Create a subset of `a` containing all the values except for the first 12 (i.e., `[22, 23, 24, 25, 26, 27, 28, 29]`)
- Create a subset that only contains the even numbers (i.e, every second number)

**My Code**
```py
print(f'Create an array containing only the last 3 values of a: {a[-3:]}')
print(f'Create a subset with only the 4th, 5th, and 6th values: {a[3:6]}')
print(f'Create a subset of a containing all the values except for the first 12: {a[12:]}')
print(f'Create a subset that only contains the even numbers (i.e. every second number): {a[0::2]}')
```

**Instructor Solution**
```py
# The last 3 values in the array:
    a[-3:]
# An interval between two values:
    a[3:6]
# All the values except the first 12:
    a[12:]
# Every second value (i.e., all the even values in our case)
    a[::2]
```

## Challenge 3
Reverse the order of the values in `a`, so that the first element comes last:

`[29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]`

If you need a hint, you can check out this part of the [NumPy beginner's guide](https://numpy.org/devdocs/user/absolute_beginners.html#how-to-reverse-an-array)

**My Code**
```py
print(a[::-1])
```

**Instructor Solution**
```py
    np.flip(a)
    # or
    a[::-1]
```

## Challenge 4
Print out all the indices of the non-zero elements in this array: [6,0,9,0,0,5,0]

**My Code**
```py
b = [6,0,9,0,0,5,0]
[print(b.index(item)) for item in b if item != 0]
```

**Instructor Solution**
If you did a quick Google search, chances are you discovered the built-in `.nonzero()` function to print out all the non-zero elements. You can use it like so:
```py
b = np.array([6,0,9,0,0,5,0])
nz_indices = np.nonzero(b)
nz_indices # note this is a tuple
```

## Challenge 5
Use NumPy to generate a 3x3x3 array with random numbers

Hint: Use the `.random()` [function](https://numpy.org/doc/stable/reference/random/index.html?highlight=random#module-numpy.random)

**My Code**
```py
super_three_array = np.random.randint(0, 100, size=(3, 3, 3))
print(super_three_array)
```

**Instructor Solution**
The .random() function is another way to quickly create a ndarray, just like `.arange()`. The .random() function lives under np.random so you'll either have to import random 
```py
    from numpy.random import random
    z = random((3,3,3))
    z

    #or use the full path to call it.

    z = np.random.random((3,3,3)) # without an import statement
    print(z.shape)
    z
```

## Challenge 6
Use [`.linspace()`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) to create a vector `x` of size 9 with values spaced out evenly between 0 to 100 (both included).

**My Code**
```py
x = np.linspace(start=0, stop=100, num=9)
print(x)
```

**Instructor Solution**
The `.linspace()` function is very similar to `.arange()` and great for generating evenly spaced numbers over an interval. To generate the vector use:
```py
    x = np.linspace(0, 100, num=9)
    print(x)
    x.shape
```

## Challenge 7
Use [`.linspace()`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) to create another vector `y` of size 9 with values between -3 to 3 (both included). Then plot `x` and `y` on a line chart using Matplotlib.

**My Code**
```py
y = np.linspace(start=-3, stop=3, num=9)
plt.plot(x,y)
```

**Instructor Solution**
A common use-case for `.linspace()` is to generate the points that you'd like to plot on a chart. 
```py
    y = np.linspace(start=-3, stop=3, num=9)
    plt.plot(x, y)
    plt.show()
```

## Challenge 8
Use NumPy to generate an array called `noise` with shape 128x128x3 that has random values. Then use Matplotlib's [`.imshow()`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html) to display the array as an image.

The random values will be interpreted as the RGB colours for each pixel.

**My Code**
```py
noise = np.random.randint(0, 255, size=(128, 128, 3))
plt.imshow(noise)
```

**Instructor Solution**
When you have a 3-dimensional array with values between 0 and 1, we can use Matplotlib to interpret these values as the red-green-blue (RGB) values for a pixel. 
```py
    noise = np.random.random((128,128,3))
    print(noise.shape)
    plt.imshow(noise)
```

That's pretty cool, right?! We've just generated a 128x128 pixel image of random noise because each dimension in our NumPy array can be interpreted to hold the colour information for a pixel.

# Broadcasting, Scalars, and Matrix Multiplication

# Manipulating Images as ndarrays

# Learning Points & Summary