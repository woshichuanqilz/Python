import scrapy
import random
import re
import subprocess

class GetImage(scrapy.Spider):
    name = 'ImageSpider'
    start_urls = ['https://pixabay.com/zh/']


    def parse(self, response):
        imagelist = response.css('img::attr(src)').extract()
        imagelistnew = [ x for x in imagelist if 'blank.gif' not in x ]
        full_url = response.urljoin(random.choice(imagelistnew))

        name_arr = full_url.split('/')[-1].split('-')
        del name_arr[-1]
        # print name_arr
        name = " ".join(name_arr)
        # print name
        # copy2clip(txt) can't use here
        MarkdownURL='![' + name + '](' + full_url + ')'
        cmd='echo '+MarkdownURL.strip()+'|clip'
        subprocess.check_call(cmd, shell=True)

