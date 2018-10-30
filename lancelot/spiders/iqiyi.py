# -*- coding: utf-8 -*-
import scrapy


class IqiyiSpider(scrapy.Spider):
    name = 'iqiyi'
    allowed_domains = ['iqiyi.com']
    start_urls = ['http://iqiyi.com/']

    def parse(self, response):
        pass
