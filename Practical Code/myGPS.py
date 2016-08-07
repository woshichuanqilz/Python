#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode
   
#----------------------------------
# 经纬度地址解析调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/15
#----------------------------------
   
def main():
   
    #配置您申请的APPKey
    appkey = "*********************"
   
    #1.经纬度地址解析
    request1(appkey,"GET")
   
   
   
#经纬度地址解析
def request1(appkey, m="GET"):
    url = "http://apis.juhe.cn/geo/"
    params = {
        "lng" : "", #经度 (如：119.9772857)
        "lat" : "", #纬度 (如：27.327578)
        "key" : appkey, #申请的APPKEY
        "type" : "", #传递的坐标类型,1:GPS 2:百度经纬度 3：谷歌经纬度
        "dtype" : "", #返回数据格式：json或xml,默认json
   
    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)
   
    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"
   
   
   
if __name__ == '__main__':
    main()
