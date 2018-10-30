# -*- coding: utf-8 -*-
import time
import scrapy

from lancelot.utils import jsonp2Dict
from lancelot.utils.common import MEDIA_BIZHAN, CALLBACK_NAME, BILI_CHANNAL_RIDS, BILI_VIDEO_LINK, BILI_SPACE_LINK

PER_PAGE = 100
class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    dynamic_url = 'https://api.bilibili.com/x/web-interface/dynamic/region?callback=' + CALLBACK_NAME + '&jsonp=jsonp&ps=' + str(PER_PAGE) + '&rid={}' # 首页推荐
    # ranking_url = 'https://api.bilibili.com/x/web-interface/ranking/region?callback=' + CALLBACK_NAME + '&rid={}&day=7&original=0&jsonp=jsonp' # TODO 排行榜
    # start_urls = []

    def start_requests(self):
        for rid in BILI_CHANNAL_RIDS:
            url = self.dynamic_url.format(rid)
            print url
            yield scrapy.Request(
                url,
                callback=self.dynamic_get_data,
                headers={
                    'Referer': 'https://www.bilibili.com/'
                },
                # cookies={},
            )

    def dynamic_get_data(self, response):
        data = jsonp2Dict(response.body, CALLBACK_NAME)
        # print '------------'
        # print data
        # print '------------'
        try:
            for archive in data['data']['archives']:
                stat_info = archive.get('stat', {})
                uploader_info = archive.get('owner', {})
                result = {
                    'media_name'         : archive.get('title'),
                    'media_snapshot'     : archive.get('pic'),
                    'media_description'  : archive.get('desc'),
                    'media_link'         : BILI_VIDEO_LINK.format(archive.get('aid')), # 用哔站规则组合
                    'played_count'       : stat_info.get('view'),
                    'likes'              : stat_info.get('like'),
                    'upload_time'        : archive.get('pubdate'),
                    'uploader'           : uploader_info.get('name'),
                    'uploader_avatar'    : uploader_info.get('face'),
                    'uploader_spaceLink' : BILI_SPACE_LINK.format(uploader_info.get('mid')), # 组合
                    'check_time'         : int(time.time()), # 抓取时间，取当前时间
                    'channel'            : archive.get('tname'),
                    'from_website'       : MEDIA_BIZHAN,
                    'original_id'        : str(archive.get('aid')),
                }
                yield result
        except Exception as e:
            print e
            pass

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