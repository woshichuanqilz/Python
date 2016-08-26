import scrapy


class SubstitleSpider(scrapy.Spider):
    name = 'subtitle'
    start_urls = ['https://subscene.com/subtitles/title?q=braveheart&l=']

    def parse(self, response):
        for href in response.css('#left a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)


    def parse_question(self, response):
        hreflist = response.css('tr:nth-child(82) .positive-icon+ span').xpath('../@href').extract()
    
        # the hreflist may out of range here
        print len(hreflist)
        if len(hreflist) > 0:
            full_url = response.urljoin(hreflist[0])
            print full_url


		
		
		
