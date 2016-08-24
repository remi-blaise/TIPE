#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

from json import JSONEncoder as BaseEncoder


class JSONEncoder(BaseEncoder):
    def default(self, obj):
        if hasattr(obj,'reprJSON'):
            return obj.reprJSON()
        else:
            return BaseEncoder.default(self, obj)
