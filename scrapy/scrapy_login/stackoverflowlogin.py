#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest

class GitHubLogin(scrapy.Spider) :
    name = "sk"
    start_urls = [
        "https://stackoverflow.com/users/login?ssrc=head"
    ]

    def start_requests(self):
        return [Request("https://stackoverflow.com/users/login?ssrc=head", meta = {'cookiejar' : 1}, callback = self.post_login)]

    def post_login(self, response):
        fkey = response.css('#login-form > input[type="hidden"]:nth-child(1)::attr(value)').extract_first() 
        print fkey

        return [FormRequest.from_response(response,   #"http://www.zhihu.com/login",
                            meta = {'cookiejar' : response.meta['cookiejar']},
                            formdata = {
                            'fkey': fkey,
                            'ssrc': 'head',
                            'login': '513278236@qq.com',
                            'password': 'woshichuanqilz72',
                            },
                            callback = self.after_login,
                            dont_filter = True
                            )]
 
    def after_login(self, response):
        # print response.body
        return
