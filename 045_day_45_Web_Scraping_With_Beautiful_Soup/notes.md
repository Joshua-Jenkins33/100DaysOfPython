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

```py
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
  print(tag.getText())
```

What if I didn't want to get the text but instead I wanted to get a hold of the actual `href` (link)?

```py
for tag in all_anchor_tags:
  print(tag.get("href")) # Gives me all of the links and nothing else; just got what I'm interested in
```

We can also get a hold of things by the attribute names. I can isolate it by the `id`

```py
heading = soup.find(name="h1", id="name")
print(heading)
```
 Now I've just isolated the lone h1 above.

```py
section_heading = soup.find(name="h3", class_="heading") # class is a keyword, special, and only to be used for creating classes; change the name to class_
print(section_heading) # use getText() to get the text from the h3 tag
print(section_heading.name) # get the name of the tag
print(section_heading.get("class"))
```

We want to have a way to drill down into a particular element. In our html code we have the following:
```html
<body>
	<h1 id="name">Angela Yu</h1>
	<p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
	<p>I am an iOS and Web Developer. I ❤️ coffee and motorcycles.</p>
	<hr>
```

No where else in our code do we have an `<a>` tag inside a `<p>` tag. We can use css selectors to narrow down on a particular element to specify it's style. That would look something like this:
```html
<style>
  p a {
    /* style here */
  }
```

When we're using BeautifulSoup, we can also use the css selector.
```py
company_url = soup.select_one(selector="p a") # this means we'll be able to get that anchor tag!
print(company_url)
```

We can also use `id`s or `class`es in our selectors. Those would look like the following:
```py
name = soup.select_one(selector="#name")
print(name)

# all elements that have a class of "heading"
headings = soup.select(".heading") # this returns a list
```

## Quiz 17: Beautiful Soup Exercises

## Scraping a Live Website

## Is Web Scraping Legal?  

## 100 Movies that You Must Watch