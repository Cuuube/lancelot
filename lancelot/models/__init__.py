# -*- coding: utf8 -*-
from mongoengine import connect
from .media import Media

connect('lancelot', host='mongodb://localhost:27017/watchwhat')


