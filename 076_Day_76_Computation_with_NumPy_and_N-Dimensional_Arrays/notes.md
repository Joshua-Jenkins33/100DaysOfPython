# Day 76: Advanced - Computation with NumPy and N-Dimensional Arrays

- [Day 76: Advanced - Computation with NumPy and N-Dimensional Arrays](#day-76-advanced---computation-with-numpy-and-n-dimensional-arrays)
- [What We'll Make](#what-well-make)
- [NumPy's `ndarray` - Incredible Power at Your Fingertips!](#numpys-ndarray---incredible-power-at-your-fingertips)
  - [1-Dimension](#1-dimension)
  - [2-Dimensions](#2-dimensions)
  - [N-Dimensions](#n-dimensions)
    - [Challenge](#challenge)
- [Generating and Manipulating ndarrays](#generating-and-manipulating-ndarrays)
  - [Challenge 1](#challenge-1)
  - [Challenge 2](#challenge-2)
  - [Challenge 3](#challenge-3)
  - [Challenge 4](#challenge-4)
  - [Challenge 5](#challenge-5)
  - [Challenge 6](#challenge-6)
  - [Challenge 7](#challenge-7)
  - [Challenge 8](#challenge-8)
- [Broadcasting, Scalars, and Matrix Multiplication](#broadcasting-scalars-and-matrix-multiplication)
  - [Linear Alegbra with Vectors](#linear-alegbra-with-vectors)
  - [Broadcasting](#broadcasting)
  - [Matrix Multiplication](#matrix-multiplication)
- [Manipulating Images as ndarrays](#manipulating-images-as-ndarrays)
  - [Import Statements](#import-statements)
  - [Challenge](#challenge-1)
  - [Challenge](#challenge-2)
  - [Challenge](#challenge-3)
  - [Use Your Own Images](#use-your-own-images)
- [Learning Points & Summary](#learning-points--summary)

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

## Linear Alegbra with Vectors
NumPy is designed to do math (and do it well!). This means that NumPy will treat vectors, matrices and tensors in a way that a mathematician would expect. For example, if you had two vectors:
```py
    v1 = np.array([4, 5, 2, 7])
    v2 = np.array([2, 1, 3, 3])
```
And you add them together
```py
    v1 + v2
```
The result will be a ndarray where all the elements have been added together. 

`array([ 6, 6, 5, 10])`

In contrast, if we had two Python Lists
```py
    list1 = [4, 5, 2, 7]
    list2 = [2, 1, 3, 3]
```
adding them together would just concatenate the lists.
```py
    list1 + list2
    # output: [4, 5, 2, 7, 2, 1, 3, 3]
```
Multiplying the two vectors together also results in an element by element operation:
```py
    v1 * v2
```
Gives us `array([ 8, 5, 6, 21])` since 4x2=8, 5x1=5 and so on. And for a Python List, this operation would not work at all.
```py
    list1 * list2 # error!
```

## Broadcasting
Now, oftentimes you'll want to do some sort of operation between an array and a single number. In mathematics, this single number is often called a **scalar**. For example, you might want to multiply every value in your NumPy array by 2:

![Scalar Image](https://img-b.udemycdn.com/redactor/raw/2020-10-12_16-01-36-b9c2fefd91ad6764599526cd883cc721.gif)

In order to achieve this result, NumPy will make the shape of the smaller array - our scalar - compatible with the larger array. This is what the documentation refers to when it mentions the term "broadcasting".

The same rules about 'expanding' the smaller ndarray hold true for 2 or more dimensions. We can see this with a 2-Dimensional Array:
```py
    array_2d = np.array([[1, 2, 3, 4], 
                         [5, 6, 7, 8]])
```
The scalar operates on an element by element basis.

![Broadcast 2-Dim Array Image](https://img-b.udemycdn.com/redactor/raw/2020-10-12_16-13-09-11f207876f5bb5d4a1e542da2558d4e9.png)

The documentation on broadcasting also shows us a few more examples:

![Broadcast 2-Dim Array Image 2](https://img-b.udemycdn.com/redactor/raw/2020-10-12_16-07-56-fbba1b975a8b7e2ad2cc5323ebe4d771.png)

## Matrix Multiplication
But what if we're not multiplying our ndarray by a single number? What if we multiply it by another vector or a 2-dimensional array? In this case, we follow [the rules of linear algebra](https://en.wikipedia.org/wiki/Matrix_multiplication#Illustration). 

![Wikipedia's Example of Linear Algebra](https://img-b.udemycdn.com/redactor/raw/2020-10-12_17-01-09-7243f82f4dd88bec877e3206fb9d9add.png)

```py
    a1 = np.array([[1, 3],
                   [0, 1],
                   [6, 2],
                   [9, 7]])
     
    b1 = np.array([[4, 1, 3],
                   [5, 8, 5]])
```

**Challenge:** Let's multiply `a1` with `b1`. Looking at the Wikipedia example above, work out the values for c12 and c33 on paper. Then use the `.matmul()` function or the @ operator to check your work.

Worked out on Paper: 
- c12 = 25 (1\*1+3\*8)
- c33 = 28 (6\*3+2\*5)

```py
np.matmul(a1, b1)
```

**Solution: Matrix multiplication with NumPy**
The solution code is pretty straightforward

```py
c = np.matmul(a1,b1)
print(f'Matrix c has {c.shape[0]} rows and {c.shape[1]} columns.')
c

a1 @ b1
```

But how did the calculations arrive at 25 for c12 and 28 for c33? Substituting the number into the formula we get:

c12 = 1\*1 + 3\*8 = 1 + 24 = 25

c33 = 6\*3 + 2\*5 = 18 + 10 = 28

# Manipulating Images as ndarrays
Images are nothing other than a collection of pixels. And each pixel is nothing other than value for a colour. And any colour can be represented as a combination of red, green, and blue (RGB). 

![RGB](https://img-b.udemycdn.com/redactor/raw/2020-10-12_17-25-44-d5854190572f3330c9e306fbf2933923.gif)

## Import Statements
![Import Statements](https://img-b.udemycdn.com/redactor/raw/2020-10-12_17-19-35-d1bcbb657bc7436583140c99856b1347.png)

You should have these two import statements at the top. Scipy and PIL will help us work with images.

The Scipy library contains an image of a racoon under 'miscellaneous' (misc). We an fetch it like so:
```py
    img = misc.face()
```
and display it using Matplotlib's `.imshow()`

```py
plt.imshow(img)
```

## Challenge
What is the data type of `img`? Also, what is the shape of `img` and how many dimensions does it have? What is the resolution of the image?

- `img` is an `ndarray` data type
- `img` dimensions = `(768, 1024, 3)`
- `img` resolution = 1024x768

**Solution: An image as a ndarray**
Let us question the nature of our reality and take a look under the surface. Here's what our "image" actually looks like:  
![Matrix](https://img-b.udemycdn.com/redactor/raw/2020-10-13_09-28-44-6f41078c913d2304ad5e606add8704e2.png)

We can now clearly see that we're dealing with a ndarray. And it's a 3 dimensional array at that.

![Solution](https://img-b.udemycdn.com/redactor/raw/2020-10-12_17-42-09-192012f781f92f80a849dc1ea3212494.png)

There are three matrices stacked on top of each other - one for the red values, one for the green values and one for the blue values. Each matrix has a 768 rows and 1024 columns, which makes sense since 768x1024 is the resolution of the image. 

## Challenge
Now can you try and convert the image to black and white? All you need need to do is use a [formula](https://en.wikipedia.org/wiki/Grayscale#Colorimetric_(perceptual_luminance-preserving)_conversion_to_grayscale). 

![Formula Image](https://img-b.udemycdn.com/redactor/raw/2020-10-12_17-56-16-aff5999394e88abae2995c6d700a8cb1.png)

Y_linear is what we're after - our black and white image. However, this formula only works if our red, green and blue values are between 0 and 1 - namely in sRGB format. Currently the values in our `img` range from 0 to 255. So:
- Divide all the values by 255 to convert them to sRGB. 
- Multiply the sRGB array by the `grey_vals` array (provided) to convert the image to grayscale.
- Finally use Matplotlib's [`.imshow()`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html) with the colormap parameter set to gray `cmap=gray` to display the result.

**My Code**
```py
grey_vals = np.array([0.2126, 0.7152, 0.0722])
sRGB = img / 255
grey_img = sRGB @ grey_vals #np.matmul(sRGB, grey_vals)
plt.imshow(grey_img, cmap='gray')
```

**Solution: Converting an image to grayscale**
The first step is a division by a scalar
```py
    sRGB_array = img / 255
```
Here NumPy will use broadcasting to divide all the values in our ndarray by 255.

Next, we use matrix multiplication to multiply our two ndarrays together.
```py
    grey_vals = np.array([0.2126, 0.7152, 0.0722])
```
These are the values given by the formula above
```py
    img_gray = sRGB_array @ grey_vals
```
We can either multiply them together with the @ operator or the `.matmul()` function.
```py
    img_gray = sRGB_array @ grey_vals

    img_gray = np.matmul(sRGB_array, grey_vals)
```
Finally, to show the image we use Matplotlib
```py
    plt.imshow(img_gray, cmap='gray')
```
The `cmap` parameter is important here. If we leave it out the function will not know that is dealing with a black and white image. 

## Challenge
Can you manipulate the images by doing some operations on the underlying ndarrays? See if you can change the values in the ndarray so that:
1. You flip the grayscale image upside down
2. Rotate the colour image
3. Invert (i.e., solarize) the colour image. To do this you need to convert all the pixels to their "opposite" value, so black (0) becomes white (255).

**My Code**
```py
upside_down_grey_img = grey_img[::-1]
plt.imshow(upside_down_grey_img, cmap='gray')

plt.imshow(np.rot90(img))

plt.imshow(np.invert(img))
```

**Solution: Manipulating the ndarray to change the image**
For the first challenge, all you need to do is reverse the order of the rows and the columns in the NumPy array with the `.flip()` function:

![Flipped Array Image](https://img-b.udemycdn.com/redactor/raw/2020-10-13_09-55-11-fefab18ee7919d2c38c006905c90db86.png)

You can display the upside down image in a single line of code:
```py
    plt.imshow(np.flip(img_gray), cmap='gray')
```
To rotate the image, all you need to do is rotate the array with `.rot90()`

![Rotated Array Image](https://img-b.udemycdn.com/redactor/raw/2020-10-13_10-00-59-8f4764f22d74c4902ad3e1a9929330d1.png)

This will rotate our image too:
`plt.imshow(np.,rot90(img))`

Inverting the colour image is a bit more tricky. It involved making use of NumPy's ability to broadcast when doing operations with a scalar. In this case, our scalar is 255 - the maximum value for a pixel in RGB (see gif at the very top). If we subtract the values of our `img` from 255, then we get the opposite value for each pixel: 

```py
    solar_img = 255 - img
    plt.imshow(solar_img)
```

## Use Your Own Images
I've provided a .jpg file in the starting .zip file, so you can try your code out with an image that isn't a racoon 🦝. The key is that your image should have 3 channels (red-green-blue). If you use a .png file with 4 channels there are additional pre-processing steps involved to replicate what we're doing here.

How do you open an image and put it into a NumPy array?
![PIL to Open Image](https://img-b.udemycdn.com/redactor/raw/2020-10-13_10-29-27-3a3e2d19291e4b76effc62168f2023cd.png)

First, make sure you've added the image to your project. All you need to do is use the PIL library to open the image and then create the ndarray using the image. You should see that your ndarray has 3 dimensions. The shape will be the resolution of your image. 

![Macarons Image Dimension and Shape](https://img-b.udemycdn.com/redactor/raw/2020-10-13_10-31-07-65d5d16e9295629db82713dc42220031.png)

Now feel free to manipulate your own images as you see fit. If you discover something particularly cool, be sure to share in the comments below! 👇 I'd love to see your hard work 😎

![Macarons](https://img-b.udemycdn.com/redactor/raw/2020-10-13_10-34-04-6e3c1ebc7c0899aefd0d78ad8e899634.png)

![Shiny Macarons](https://img-b.udemycdn.com/redactor/raw/2020-10-13_10-34-04-6e3c1ebc7c0899aefd0d78ad8e899634.png)

# Learning Points & Summary
In this lesson we looked at how to:
- Create arrays manually with `np.array()`
- Generate arrays using  `.arange()`, `.random()`, and `.linspace()`
- Analyse the shape and dimensions of a ndarray
- Slice and subset a ndarray based on its indices
- Do linear algebra like operations with scalars and matrix multiplication
- Use NumPys broadcasting to make ndarray shapes compatible
- Manipulate images in the form of ndarrays

You can download the completed code for today in this lesson. 

Oh, and congratulations on completing one of the most mathematical lessons in the course!  Good stuff!