import scrapy
from downloadimg.items import DownloadimgItem
import MySQLdb

class DownloadingImg(scrapy.Spider):
    name = 'dlimg'
    # start_urls = ['https://pixabay.com/zh/']
    start_urls = ['https://www.pexels.com/']

    # DB info
    db = MySQLdb.connect(host="192.168.1.107",user="lizhe",passwd="", db="test") 
    cur = db.cursor()

    def parse(self, response):
        imagelist = response.css('img::attr(src)').extract()
        imagelistnew = [ x for x in imagelist if 'blank.gif' not in x ]

        print str(len(imagelistnew)) + 'record will be inserted'
        for full_url in imagelistnew:
            # full_url = response.urljoin(imageurl)
            print full_url
            name_arr = full_url.split('/')[-1].split('-')
            del name_arr[-1]
            name = " ".join(name_arr)
            res = self.insert_data(name, full_url)    

    def insert_data(self, name, full_url):    
        # print 'name ' + name + 'full_url ' + full_url
        statement = "INSERT INTO imgstore (imgname, imgurl) VALUES ('{}', '{}');".format(name, full_url)
        # print statement

        # self.cur.execute("SELECT * FROM employee")
        self.cur.execute(statement)
        self.db.commit()
        print 'insert success'
        # for row in self.cur.fetchall():
            # print str(row)
