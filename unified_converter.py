# -*- coding: utf-8 -*-
from model.DateTime import DateTime
from model.MD5 import MD5
from workflow import Workflow


class UnifiedConverter:
    def __init__(self):
        self.wf = Workflow()
        self.models = [MD5(), DateTime()]
        self.modelDict = dict()
        for m in self.models:
            self.modelDict[m.name] = m

    def convert(self, query):
        result = []
        result += self.autocomplete(query)
        result += self.convert_by_type(query)
        # result += self.convert_all(query)

        # sort
        self.add_to_wf(result)
        self.wf.send_feedback()

    def convert_all(self, query):
        return

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

        result = []

        # 不是空的话有数量限制
        for m in self.models:
            result += m.autocomplete(query)

        return result

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
