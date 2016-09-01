import scrapy
import os  
from selenium import webdriver
from scrapy.http import Request, FormRequest
import urlparse

class ProxyCrawler(scrapy.Spider):
    name = 'proxytest'
    start_urls = ['http://www.google.com.hk', 'http://www.porn.com/videos/korean']
    main_urls = ['http://www.google.com.hk', 'http://www.porn.com']
    URLINDEX = 1

    def __init__(self):
        service_args = [
            '--proxy=http://duotai:7EuGBhsQn.pac@hyatt.h.xduotai.com:11185',
            # '--proxy-type=socks5',
            '--proxy-type=http',
            ]
        # self.driver = webdriver.PhantomJS(executable_path=r'C:\Program Files\phantomjs\bin\phantomjs.exe', service_args=service_args)

        max_wait = 60
        # self.driver.set_page_load_timeout(max_wait)
        # self.driver.set_script_timeout(max_wait)

    def start_requests(self):
        return [Request(self.start_urls[self.URLINDEX], meta = {'proxy' : 'http://duotai:7EuGBhsQn.pac@hyatt.h.xduotai.com:11185'}, callback = self.parse)]

    def parse(self, response):
        # count = 0
        for href in response.css('.thumb::attr(href)').extract():
            full_url = urlparse.urljoin(self.main_urls[1], href)
            # if count > 0:
                # break
            # count += 1
            # full_url = 'www.baidu.com'
            # print full_url
            # yield scrapy.Request(full_url, meta = {'proxy' : 'http://duotai:7EuGBhsQn.pac@hyatt.h.xduotai.com:11185'}, callback=self.parse_subpage)

    def parse_subpage(self, response):
        href = response.url
        filename = href.split('/')[-1] + '.html'
        # full_url = 'www.porn.com' + href
        full_url = href
        # print full_url 
        downloadCMD = r'wget.exe -O E:\\scrapyVideo\\' + filename + ' ' + full_url
        # print downloadCMD
        os.system(downloadCMD)
        fullfilename = 'E:\\scrapyVideo\\' + filename
        
    def closed(self, spider):
        os.system('python e:\\scrapyVideo\\findUrl.py')
        print 'spider closed'
