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

### Question 1:

This is an unordered list (`<ul>`) extracted from the BeautifulSoup Home Page. What's the code to get all the anchor tags (`<a>`) if we have already made soup from the HTML?
```html
    <ul class="simple">
        <li><p><a class="reference external" href="https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/">这篇文档当然还有中文版.</a></p></li>
        <li><p>このページは日本語で利用できます(<a class="reference external" href="http://kondou.com/BS4/">外部リンク</a>)</p></li>
        <li><p><a class="reference external" href="https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/">이 문서는 한국어 번역도 가능합니다.</a></p></li>
        <li><p><a class="reference external" href="https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr">Este documento também está disponível em Português do Brasil.</a></p></li>
        <li><p><a class="reference external" href="https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/">Эта документация доступна на русском языке.</a></p></li>
    </ul>
```

`soup.find_all("a")`

### Question 2: 
Below is a simplified version of the Beautiful Soup Hall of Fame. The HTML code comes from the Beautiful Soup home page.

If soup was made from the HTML below, how would you extract only the anchor tags from inside the unordered list? (So excluding the first anchor tag `<a name="HallOfFame"><h2>Hall of Fame</h2></a>`?

```html
    <a name="HallOfFame"><h2>Hall of Fame</h2></a>
    <p>Over the years, Beautiful Soup has been used in hundreds of different projects.</p>
    <ul>
    <li>Alexander Harrowell uses Beautiful Soup to <a href="http://www.harrowell.org.uk/viktormap.html">track the business activities</a> of an arms merchant.</li>
    <li>The developers of Python itself used Beautiful Soup to <ahref="http://svn.python.org/view/tracker/importer/">migrate the Pythonbug tracker from Sourceforge to Roundup</a>.</li>
    </ul>
```
`soup.select("li a")`

### Question 3:
If we make `soup` with the HTML code below, how would you get hold of the value of `maxlength`?
```html
    <form method="get" action="/search/">
     <input type="text" name="q" maxlength="255" value=""></input>
    </form> 
```
There's no shame in looking at the [documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)!

```py
form_tag = soup.find("input")
max_length = form_tag.get("maxlength")
```

## Scraping a Live Website
It's much more fun to scrape from something life on the internet! We're going to pull from [y.combinator hacker news website](news.ycombinator.com).

```py
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

print(response.text) # this is equivalent to what we did when we read our `website.html` file!

# We're not interested in this entire output, however. We want pieces of each article posting. Shows by default 30 articles. It doesn't order them by # of upvotes and that's what we are going to track. Without having to manually search through it.

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title) # this is what you see in the tab bar.
```

### Challenge: Get the Title of the Article
```py
title_text = soup.find_all("a", class="storylink").getText()
```

### The Rest
```py
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [upvote.getText() for upvote in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

article_upvotes = [int(point.split(" ")[0]) for point in article_upvotes]

print("\n")

largest_number = max(article_upvotes)
most_upvotes_index = article_upvotes.index(largest_number)

print(article_upvotes.index(largest_number))
print(article_texts[most_upvotes_index])
print(article_links[most_upvotes_index])
```

## Is Web Scraping Legal?  
What is the Law on Webscraping? The Law seems to favor webscraping as long as you think about a few things. It's not a blanket statement; only data that is publicly available and not copyrighted, it's fair game for web crawlers.

1. **You can't commercialize copyrighted content.**
2. **You can't scrape data behind authentication.**

Just because it's legal doesn't mean you can actually do it. `reCAPTCHA`s can prevent this. 

**ETHICS**
1. Public API First (Apply for the application to their data!)
2. Respect the Web Owner (Don't DDOS) (`.com/robots.txt` are endpoints they don't want bots using these endpoints; crawl delay is number of seconds)
3. Limit your rate (don't scrape more than once per minute)


## 100 Movies that You Must Watch