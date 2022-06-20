# Day 53: Web Scraping Capstone—Data Entry Job Automation
Webscaping review! It'll use BeautifulSoup and Selenium.

Beautiful Soup to scrape form Zillow, Selenium to fill out the form (1 per listing on Zillow).

## Capstone PRoject Requirements

1. Go to [google forms](https://docs.google.com/forms/) and create your own form
2. Add 3 questions to the form, amke all questions "short-answer"
3. Click send and copy the link address of hte form. You will need to use this in your program
4. Go to [this web address on Zillow](https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D) and see how the website is structured, this is where you'll be scraping the data from

### Program Requirements
- Use BeautifulSoup/Requests to scrape all the listings from the Zillow web address
- Create a list of links for all the listings you scraped
- Create a list of prices for all the listings you scraped
- Create a list of addresses for all the listings you scraped
- Use Selenium to fill in the form you created. Each listing should have its price/address/link added to the form. You will need to fill in a new form for each new listing
- Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to the Google FOrm. You should end up with a spreadsheet with all the details from the properties.

## Hints and Solutions

### Hint 1
In order to access Zillow using requests, you'll need to provide your user agent and accepted languages via the header. We've discussed this in the Amazon Price Scraping project in [day 47](https://github.com/Joshua-Jenkins33/100DaysOfPython/tree/main/047_Day_47_Create_an_Automated_Amazon_Price_Tracker).

### Hint 2
Some of the links you get back from Zillow may be incomplete. In this case, all you need to do is just add the `https://www.zillow.com` in front

### Hint 3
[Get the last element in a list](https://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list).

### Hint 4
Listings with multiple properties have a different structure from listings with a single property only. Use Chrome's Inspect Element to double-check this on Zillow's website.

If all listings were using the same CSS class to hold the price information, then the 1st pass solution in the course resources would work. See if you can use a try-except structure (covered in [day 30](https://github.com/Joshua-Jenkins33/100DaysOfPython/tree/main/030_Day_30_Errors_Exceptions_JSON_Improving_the_Password)) to parse the tree with BeautifulSoup to handle both cases—scraping the headline price provided for multiple listings as well as the price/mo for single listings.