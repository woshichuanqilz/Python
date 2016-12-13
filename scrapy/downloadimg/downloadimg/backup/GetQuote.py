# -*- coding: utf-8 -*-
import scrapy
import subprocess
from selenium import webdriver

class ProductSpider(scrapy.Spider):
    name = "quotespider"
    start_urls = ['http://news.iciba.com/views/dailysentence/daily.html#!/']

    def __init__(self):
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Program Files\phantomjs\bin\phantomjs.exe')

    def parse(self, response):
        self.driver.get(response.url)

        textWebElement = self.driver.find_element_by_css_selector(".sentence-en a");

        #clip board
        cmd='echo '+textWebElement.text.encode('utf-8').strip()+'|clip'
        subprocess.check_call(cmd, shell=True)
        print textWebElement.text
        self.driver.close()


