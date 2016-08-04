# encoding: utf-8
import requests
import re
import bs4
import sys
import codecs
import locale


# print str(sys.argv[1])
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 
index_url = 'http://dict.cn/' + sys.argv[1]

def get_video_page_urls():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    RawText = soup.select('.dict-basic-ul')[0]
    ResString = RawText.text
    ResArr = ResString.splitlines(True)
    return ResArr[1]

print(get_video_page_urls())
