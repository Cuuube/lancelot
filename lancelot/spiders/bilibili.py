# -*- coding: utf-8 -*-
import scrapy

from lancelot.utils import jsonp2Dict

CALLBACK_NAME = 'GETDAZE'

class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    start_urls = [
        'https://api.bilibili.com/x/web-interface/dynamic/region?callback=' + CALLBACK_NAME + '&jsonp=jsonp&ps=5&rid=1'
    ]

    def start_requests(self):
        for url in self.start_urls:
            print url
            yield scrapy.Request(
                url,
                callback=self.get_data,
                headers={
                    'Referer': 'https://www.bilibili.com/'
                },
                # cookies={},
            )

    def parse(self, response):
        for link in response.css('ul li a::attr(href)').extract():
            # print link
            url = response.urljoin(link)
            # print('--------', url)

            yield scrapy.Request(
                url,
                callback=self.get_data,
                headers={
                    'Referer': 'https://www.bilibili.com/'
                },
                # cookies={},
            )

    def get_data(self, response):
        data = jsonp2Dict(response.body, CALLBACK_NAME)

        # data = {
        #     'name': response.css('h1::text').extract()[0],
        #     # 'author': response.css('div p::text').extract()[0],
        #     'author': response.css('div p::text')[0].re(':\s?([\w\s]*)')[0],
        #     # 'price': response.css('div p::text').extract()[1],
        #     'price': response.css('div p::text')[1].re(':\s?(\d*)')[0],
        #     # 'pages': response.css('div p::text').extract()[2],
        #     'pages': response.css('div p::text')[2].re(':\s?(\d*)')[0],
        #     'url': response.url,
        # }
        print '------------'
        print data
        print '------------'

        # print data
        yield data

'''
有用的东西：
1. api必须带上：Referer: https://www.bilibili.com/
2. 如下api是大区动态：
https://api.bilibili.com/x/web-interface/dynamic/region?callback=<callbackName>&jsonp=jsonp&ps=10&rid=<rid>
3. 如下是大区推荐
https://api.bilibili.com/x/web-interface/ranking/region?callback=<callbackName>&rid=<rid>&day=<3或者7代表几日最火>&original=0&jsonp=jsonp
4. 大区之间区别是rid，收集如下：
动画：1
国产动画相关：168
音乐：3
舞蹈：129
游戏：4
科技区：36
日常、搞笑、生活：160
鬼畜调教类：119
美妆：155
广告：165
明星、综艺：5
电影：23
电视剧：11
影视：181
社会、人文、军事、美食、旅行：177
'''