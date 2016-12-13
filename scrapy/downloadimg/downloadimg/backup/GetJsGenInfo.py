import scrapy
from selenium import webdriver

class ProductSpider(scrapy.Spider):
    name = "product_spider"
    start_urls = ['http://news.iciba.com/views/dailysentence/daily.html#!/']

    def __init__(self):
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Program Files\phantomjs\bin\phantomjs.exe')

    def parse(self, response):
        self.driver.get(response.url)

        next = self.driver.find_element_by_css_selector(".sentence-en a");
        # next = self.driver.find_element_by_xpath('shtml/body/div[2]/div[4]/div[3]/div[4]/div/div[4]/div[1]/a')
        print next.text
        # while True:
            # next = self.driver.find_element_by_xpath('//td[@class="pagn-next"]/a')

            # try:
                # next.click()

                # # get the data and write it to scrapy items
            # except:
                # break

        self.driver.close()
