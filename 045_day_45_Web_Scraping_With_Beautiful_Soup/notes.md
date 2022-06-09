# Day 45: Intermediate+ Web Scraping with Beautiful Soup
Some websites don't have APIs, or their APIs don't allow us to do all of the things that we want to do. So this is where we start thinking about using web scraping where we look through the underlying HTML code to get the information we want.

`BeautifulSoup` is a module that helps developers make sense of websites. Websites are like soup and rather convoluted and complex. If you want to make sense of a webpage and pull out the relevant parts of the data, then you'll need an HTML parser like BeautifulSoup. This enables you to find and pull out the HTML elements that you're interested in from this soup of jumbled HTML code.

Once we've mastered this skill, we will be able to take data from any website.

## Parsing HTML and Making Soup
Empty `main.py` file.  The data is going to come from `website.html`. 

[Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). 

### Challenge: Open the `website.html` document in python
Open the `website.html` file. Store all of its text in a variable called `contents`.

```py
with open("website.html") as html_file:
  contents = html_file.read()
```

Now we need to import Beautiful Soup!
`from bs4 import BeautifulSoup`

### Making Soup
Create an object from the soup class.
```py
from bs4 import BeautifulSoup

soup = BeautifulSoup(contents, "html.parser")
soup.title
print(soup.title) # gives the title tag
print(soup.title.name) # gives the name of the title tag
print(soup.title.string) # the actual string inside the title tag
```
This entire `soup` object now represents our entire html code.

`soup.prettify()` makes things indented and nice.

```py
print(soup.a) # gets the first anchor tag
```

We are drilling down into the HTML file, finding the tags we're interested in, and getting the name/text of the tag. Wht if we want **all** anchor tags or h2 tags as opposed to just "the first one"?

## Finding and Selecting Particular Elements with BeautifulSoup

## Quiz 17: Beautiful Soup Exercises

## Scraping a Live Website

## Is Web Scraping Legal?  

## 100 Movies that You Must Watch