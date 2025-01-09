# python -m pip install requests
    # => Get data from web (html, json, xml)

# python -m pip install beautifulsoup4
    # => parse html

# Both commands to be executed from terminal, ctrl+j.
    # For now, both requirements already satisfied. i.e. installed.

# Concept for scrapping,
    # browsing a website uses: GET & POST methods
    # understand inspect of website.
    # should understand concept of status code returned for website

# install git
# create repository in github

# go to git bash
# git configuration,
    # git config --global user.name "vishaljoshi-np"
    # got config --global user.email "vishaljoshi.np@gmail.com"

# git init
# git status => to check status of the files
# git diff => to check the changes
# git add .
# git commit -m "Message"
# copy paste git code from github

############################

# 1. change the code
# 2. git add .
# 3. git commit -m "message"
# 4. git push origin
###########################

# Importing libraries

import json
import requests # importing library requests
from bs4 import BeautifulSoup # importing a class BeautifulSoup from library BS4

# Setting url of the target website

URL = "http://books.toscrape.com/"

# Function to pass url for scrapping

def scrape_books (url):

    response = requests.get (url) # Return responsecode
    # print (response) # Returns response code in the form Response [StatusCode]
    # print (response.status_code) # This returns only the StatusCode, as an integer, which can be used to track the status | successful when code is 200.
    # These lines were written for test. commented intentionally,

    if response.status_code != 200:

        print ("Error") # if the StatusCode is not 200 (successful) no need to work further as the browsing of website was not successful
        return
    
    response.encoding = response.apparent_encoding
    # print (response.text) # Returns all text/content, intentionally commented.. was to test learn
    soup = BeautifulSoup (response.text, "html.parser") # html.parser for html data, json.parser for json returned by api
        # soup object is created.

    books = soup.find_all ("article", class_ = "product_pod") # inspect the webpage: required book data in in tag 'article', class 'product_pod'

    all_books = [] # empty list for dictinary | below

    for book in books:

        title = book.h3.a ["title"] # Retrieve book title: inspect website, book title is within tag h3 > a > title
        # print (title) # Prints book names, commented intentinally. for test.

        price_text = book.find ("p", class_ = "price_color").text # Retrive price from page. find is to retrieve where 'p' and 'price_color'
        # print (price_text) # returns price_text with pound 'currency' symbol
        currency = price_text [0] # Slicing to get character of pound symbol
        price = price_text [1:] # Slicing to get price without pound symbol

        # print (title, price, currency) # prints book title, price, and currency symbol | commented

        # Now to save the data in json, first convert to dictionary.

        formatted_book = {

            "titel": title,
            "currency": currency,
            "price": price,
        }

        all_books.append (formatted_book)

        # print (all_books) # Prints books title and price in the dictionary format wthin list. | for test.. commented

    return (all_books) # Returns the dictinary format data from the function 

        # To save in json, import json above.
    
books = scrape_books (URL)

with open ("books.json", "w") as f: # create a file and save json content
    json.dump (books, f, indent = 4)

    # Returns entire content in html
    # Some special characters of html cannot be properly parsed by html and so may return jpt data.
        # This can be resolved using encoding technique mentioned above, refer to 'requests documentation'
    ### The above code has returned the content 'html' from the page. <index page> in this case, now need to parse for required data. requires BeautifulSoup: above code.



# scrape_books (URL)

# To run from terminal, ctrl+j => python <filename.ext>