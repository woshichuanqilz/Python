import scrapy
import re


class GetJokeSpider(scrapy.Spider):
    name = 'JokeSpider'
    start_urls = ['http://jokes.cc.com']

    def parse(self, response):
        rawtext = response.css('.fulltext::text').extract()
        s = rawtext[0]
        s = re.sub("^\s*", "", s)
        s = re.sub("\s*$", "", s)
        print s # output is 'foo repalced'
