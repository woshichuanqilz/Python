# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import MySQLdb
# from twisted.enterprise import adbapi    
# from scrapy.utils.project import get_project_settings   

# settings = get_project_settings() 

class DownloadimgPipeline(object):
    pass
    # db = MySQLdb.connect(host="192.168.1.122",user="lizhe",passwd="", db="test") 
    # cur = db.cursor()
    # def __init__(self):
        # # self.file = open('imginfo.txt', 'w+')
        # self.db = MySQLdb.connect(host="192.168.1.122",user="lizhe",passwd="", db="test") 
        # self.cur = self.db.cursor()


    # def process_item(self, item, spider):
        # # self.insert_data(item, self.insert_sql)    
        # res = self.select_data()    
        # return item 

    # def select_data(self):    
        # self.cur.execute("SELECT * FROM employee")
        # for row in self.cur.fetchall():
            # print str(row)
