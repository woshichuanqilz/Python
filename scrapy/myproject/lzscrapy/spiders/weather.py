# -*- coding: utf-8 -*-
import scrapy
import re



class GetWeather(scrapy.Spider):
    name = 'weatherSpider'
    start_urls = ['http://www.weather.com.cn/weather/101091001.shtml']

    def parse(self, response):
        weather = response.css('.on .wea::text').extract()[0]
        wind = response.css('.on .win i::text').extract()[0]

        HTemperature = response.css('.on .tem span::text').extract()[0]
        LTemperature = response.css('.on .tem i::text').extract()[0]
        
        print 'Weather   Today Is        :   ' + weather
        print 'Wind      Today Is        :   ' + wind
        print 'Highest   Temperature Is  :   ' + HTemperature
        print 'Lowest    Temperature Is  :   ' + LTemperature

        print '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print 'You will not take a umbrella, even if it rain outside.\nSo,  why you ask me to check the weather info?'
        # s = re.sub("^\s*", "", s)
        # s = re.sub("\s*$", "", s)
        # print s # output is 'foo repalced'

