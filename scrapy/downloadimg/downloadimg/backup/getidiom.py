# -*- coding: utf-8 -*-
import scrapy
import random
import urllib


class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    startWord = u'夏'
    lastWord = u'夏'
    nextWord = u'夏'
    first = urllib.quote(startWord.encode('gb2312'))
    start_urls = ['http://chengyu.t086.com/chaxun.php?q1=' + first + '&q2=&q3=&q4=']
    lastUrl = start_urls
    totalCntTime = 10
    tryTime = 3

    def parse(self, response):
      IdoimList = response.css('.td1 a::text').extract()
      if len(IdoimList) == 0 and self.tryTime > 0:
        self.tryTime -= 1
        print 'no idoim found'
        return scrapy.Request(self.lastUrl, callback=self.parse, dont_filter=True)
      elif self.tryTime <= 0:
        print 'exit spider'
        return 

      if self.totalCntTime > 0:
        self.totalCntTime -= 1
        # Idoim = self.startWord.encode() + random.choice(IdoimList)
        Idoim = random.choice(IdoimList)
        Idoim = self.nextWord + Idoim
        self.lastWord = Idoim[0]
        self.nextWord = Idoim[-1]
        # print self.lastWord + '***' + self.nextWord
        self.lastUrl = 'http://chengyu.t086.com/chaxun.php?q1=' + urllib.quote(self.lastWord.encode('gb2312')) + '&q2=&q3=&q4='
        nextWord = urllib.quote(self.nextWord.encode('gb2312'))
        next_url = 'http://chengyu.t086.com/chaxun.php?q1=' + nextWord + '&q2=&q3=&q4='
        print self.lastUrl
        print next_url
        print self.totalCntTime
        print Idoim
        return scrapy.Request(next_url, callback=self.parse)
