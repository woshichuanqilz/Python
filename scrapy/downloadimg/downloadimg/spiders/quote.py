import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls = [
            'http://sanguoshaenglish.blogspot.com/2010/07/liu-bei.html'
        ]
        for url in urls:
            request = scrapy.Request(url="http://sanguoshaenglish.blogspot.com/2010/07/liu-bei.html")
            request.meta['proxy'] = "http://xduotai.com/pRul7IqyV.pac@hilton.h.xduotai.com:16301"
            # set http_proxy=http://xduotai.com/pRul7IqyV.pac@hilton.h.xduotai.com:16301
            yield request
            # yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print response.body
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
            # f.write(response.body)
        # self.log('Saved file %s' % filename)
