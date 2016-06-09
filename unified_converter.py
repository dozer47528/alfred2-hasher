# -*- coding: utf-8 -*-
from model.base_64 import Base64
from model.date_time import DateTime
from model.html import Html
from model.md5 import MD5
from model.sha import SHA
from model.number import Number
from model.ascii import ASCII
from model.javascript import Javascript
from workflow import Workflow


class UnifiedConverter:
    def __init__(self):
        self.wf = Workflow()
        self.models = [
            MD5(),
            DateTime(),
            Base64(),
            Html(),
            Javascript(),
            SHA(),
            Number(),
            ASCII()
        ]
        self.modelDict = dict()
        self.max_age = 60 * 60 * 24 * 365
        for m in self.models:
            self.modelDict[m.name] = m

    def cache(self, query):
        if not query:
            return ""
        result = query.split(":", 1)
        key = result[0]
        value = result[1]

        count = self.wf.cached_data(key, max_age=self.max_age)
        if not count:
            count = 0
        count += 1

        self.wf.cache_data(key, count)

        return value

    def convert(self, query):
        result = []
        result += self.autocomplete(query)
        result += self.sort_items(self.convert_by_type(query))
        result += self.sort_items(self.convert_all(query))

        self.add_to_wf(result)
        self.wf.send_feedback()

    def convert_all(self, query):
        result = []

        if not query:
            return result

        for m in self.models:
            result += m.convert(query)

        return result

    def convert_by_type(self, query):
        query = str(query).strip()
        if query.find(' ') == -1:
            return []

        group = query.split(' ', 1)
        type_value = group[0]
        input_value = group[1]

        if type_value in self.modelDict:
            return self.modelDict[type_value].convert(input_value)

    def autocomplete(self, query):
        result = []

        if query.find(' ') >= 0:
            return result

        # 不是空的话有数量限制
        for m in self.models:
            result += m.autocomplete(query)

        return result

    def sort_items(self, items):
        def sort_by_usage(item):
            key = item.arg.split(":", 1)[0]
            count = self.wf.cached_data(key, max_age=self.max_age)
            if not count:
                return 0
            return count

        return sorted(items, reverse=True, key=sort_by_usage)

    def add_to_wf(self, items):
        for item in items:
            self.wf.add_item(
                    title=item.title,
                    subtitle=item.subtitle,
                    modifier_subtitles=item.modifier_subtitles,
                    arg=item.arg,
                    autocomplete=item.autocomplete,
                    valid=item.valid,
                    uid=item.uid,
                    icon=item.icon,
                    icontype=item.icontype,
                    type=item.type,
                    largetext=item.largetext,
                    copytext=item.copytext
            )
