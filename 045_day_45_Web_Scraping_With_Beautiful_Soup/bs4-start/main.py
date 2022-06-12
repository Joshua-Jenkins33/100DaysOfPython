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