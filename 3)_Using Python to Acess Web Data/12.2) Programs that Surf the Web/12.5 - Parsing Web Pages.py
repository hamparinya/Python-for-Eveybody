# Why Scrape?
# - Pull data - particularly social data - who links to who?
# - Get your own data back out of some system that has no "expot capability"
# - Monitor a site for new information
# - Spider the web to make a database for a search engine

# Scraping Web Pages
# There id some controversy about web page scraping and some sites are a bit snippy about it
# Repubishing copyrighted information is not allowed
# Violating terms of service is not allowed

# BeautifulSoup Installation
# To run this, you can install BeautifulSoup
# http://pypi.python.org/pypi/beautifulsoup4
# or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
