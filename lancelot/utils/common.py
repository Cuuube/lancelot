# -*- coding: utf-8 -*-

import json

MEDIA_VQQ    = 'vqq'
MEDIA_IQIYI  = 'iqiyi'
MEDIA_BIZHAN = 'bilibili'

CALLBACK_NAME = 'GETDAZE'

BILI_CHANNAL_RIDS = [
    1,
    168,
    3,
    129,
    4,
    36,
    160,
    119,
    155,
    165,
    5,
    23,
    11,
    181,
    177,
]

BILI_VIDEO_LINK = 'https://www.bilibili.com/video/av{}'
BILI_SPACE_LINK = 'https://space.bilibili.com/{}'

def jsonp2Dict(jsonp_string, callback_name):
    result = ''
    if len(jsonp_string) > 0 and callback_name in jsonp_string:
        try:
            result = jsonp_string.replace(callback_name, '')
            result = result[1:len(result) - 1]
            result = json.loads(result)
            return result
        except:
            return dict()
    return dict()
