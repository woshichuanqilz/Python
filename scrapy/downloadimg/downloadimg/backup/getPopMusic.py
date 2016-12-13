# -*- coding: utf-8 -*-
import scrapy
import subprocess
from selenium import webdriver

class ProductSpider(scrapy.Spider):
    name = "getPopMusic"
    start_urls = ['http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0']

    def __init__(self):
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Program Files\phantomjs\bin\phantomjs.exe')

    def parse(self, response):
        self.driver.get(response.url)
        textWebElement = self.driver.find_element_by_css_selector("#m-pl-container");

        print textWebElement.text
        self.driver.close()


