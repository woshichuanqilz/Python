from bs4 import BeautifulSoup
import re

# doc = ['<html><head><title>Page title</title></head>',
       # '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       # '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       # '</html>']
# soup = BeautifulSoup(''.join(doc))

# print soup.prettify()

soup = BeautifulSoup(open("test.htm"))
for link in soup.find_all('h2'):
    print(link.text)
