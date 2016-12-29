from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open("test.html"), "lxml")
for link in soup.find_all('input'):
    print(link)
