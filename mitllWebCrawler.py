# https://careers.ll.mit.edu/search/?q=CO-OP&startrow=25
# crawl opportunities and checks if any of them don't need US Citizenship (if any have the phrase "U.S. citizenship is required")
# Tutorial Notes
#   https://pypi.org/project/beautifulsoup4/
#   converts incoming docs into Unicode and outgoing into UTF-8. Uses python parsers like lxml (can parse XML and HTML) and html5lib for diff parsing or speed techniques
#   does the tree traversal stuff for you. You can tell it "Find all the links", or "Find all the links of class externalLink", or "Find all the links whose urls match "foo.com", or "Find the table heading that's got bold text, then give me that text."
#   Inspiration- https://www.crummy.com/software/BeautifulSoup/ 


import requests
from bs4 import BeautifulSoup

