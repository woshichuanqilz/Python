import scrapy

# scrapy crawl getanswer -a inputurllist=lizhe,xxzi --nolog
# ['lizhe', 'xxzi']
# Command line should be in the root dir and use a parameter

class StackOverflowSpider(scrapy.Spider):
    name = 'getanswer'

    def __init__(self, domain=None, inputurllist=''):
        self.queryKW = inputurllist.split(',')[0]

        # start_urls = ['http://stackoverflow.com/search?q=' + self.queryKW]
        start_urls = ['https://www.google.com.hk/?gws_rd=ssl#safe=strict&q=' + self.queryKW]
        print start_urls

    def parse(self, response):
        pass 

        # for href in response.css('.question-summary h3 a::attr(href)'):
            # full_url = response.urljoin(href.extract())
            # yield scrapy.Request(full_url, callback=self.parse_question)

    # def parse_question(self, response):
        # yield {
            # 'title': response.css('h1 a::text').extract_first(),
            # 'votes': response.css('.question .vote-count-post::text').extract_first(),
            # 'body': response.css('.question .post-text').extract_first(),
            # 'tags': response.css('.question .post-tag::text').extract(),
            # 'link': response.url,
        # }
