# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from lancelot.models import Media

class LancelotPipeline(object):
    def process_item(self, item, spider):
        # TODO 存到数据库
        # print item
        Media.insert(**item)
        return item
