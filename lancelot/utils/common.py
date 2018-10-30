# -*- coding: utf-8 -*-

import json

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
