import scrapy

class StackOverflowSpider(scrapy.Spider):
    name = 'SampleSentence'
    start_urls = ['http://dict.youdao.com/example/blng/eng/%E9%A9%B4%E8%BD%A6/#keyfrom=dict.main.moreblng']

    def parse(self, response):
        # print keyword
        sentence = response.css('p:nth-child(2)').extract_first()
        print sentence
        return

    def parse_question(self, response):
        return
