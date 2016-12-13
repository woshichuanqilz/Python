# -*- coding: utf-8 -*-
import scrapy
import subprocess
from selenium import webdriver
from scrapy.http import Request, FormRequest

class StackOverflowSpider(scrapy.Spider):
    name = 'getporn'
    start_urls = ['http://www.porn.com/videos/korean']

    def __init__(self):
        service_args = [
            '--proxy=duotai:7EuGBhsQn.pac@hyatt.h.xduotai.com:11185',
            # '--proxy-type=socks5',
            '--proxy-type=http',
            ]
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Program Files\phantomjs\bin\phantomjs.exe', service_args=service_args)

        max_wait = 60
        self.driver.set_page_load_timeout(max_wait)
        self.driver.set_script_timeout(max_wait)
        # self.driver = webdriver.Chrome()

    def start_requests(self):
        print 'start Request'
        return [Request("http://www.porn.com/videos/korean", meta = {'proxy' : '7EuGBhsQn.pac@hyatt.h.xduotai.com:11185'}, callback = self.parse)]



    def parse(self, response):
        print 'inside'
        response.css('.thumb::attr(href)').extract()
        for href in response.css('.thumb::attr(href)').extract() :
            filename = href.split('/')[-1] + '.mp4'
            full_url = 'www.porn.com' + href
            print full_url 

            # os.system('C:\GnuWin32\GetGnuWin32\bin\wget.exe')
            # full_url = response.urljoin(href.extract())
            # yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        self.driver.get(response.url)
        textWebElement = self.driver.find_element_by_css_selector("video");
        print textWebElement.text
        # downloadCMD = r'C:\\GnuWin32\\GetGnuWin32\\bin\\wget.exe -O E:\\pornVideo\\' + filename + ' ' + full_url

