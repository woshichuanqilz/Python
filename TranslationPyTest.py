# encoding: utf-8
import requests
import re
import bs4
import sys
import codecs
import locale


# print str(sys.argv[1])
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 
# index_url = 'http://dict.cn/' + sys.argv[1]
index_url = 'http://dict.cn/operation'

def get_video_page_urls():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    # RawText = soup.select('.dict-basic-ul')[0]
    # RawText = soup.select('.dict-basic-ul')
    # address = soup.find('section', class_="dict-basic-ul")
    # for lis in soup.select('.dict-basic-ul').find_all('li'):
    address = soup.find('ul', class_="dict-basic-ul")
    list = address.find_all('li')
    index = 0
    ArrLength = len(list)
    # print 'len = ' + str(len1)
    for lis in list:
        index += 1
        if index < ArrLength : print(lis.get_text())
    return

get_video_page_urls()

