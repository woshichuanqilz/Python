# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem


class WeatherSpider(scrapy.Spider):
    name = "myweatherst"
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        item = WeatherItem()
        item['city'] = response.css('h1 a::text').extract_first(),
        item['date'] = response.css('.question .vote-count-post::text').extract_first(),
        return item
