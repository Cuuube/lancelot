# -*- coding: utf-8 -*-
import scrapy


class VqqSpider(scrapy.Spider):
    name = 'vqq'
    allowed_domains = ['qq.com']
    start_urls = ['http://qq.com/']

    def parse(self, response):
        pass
