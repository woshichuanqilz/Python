from bs4 import BeautifulSoup
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup, "lxml")

print soup.get_text()
# u'\nI linked to example.com\n'
# soup.i.get_text()
# u'example.com'
