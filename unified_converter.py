# -*- coding: utf-8 -*-
from workflow import Workflow
from datetime import datetime
import hashlib

class UnifiedConverter():
    def __init__(self):
        self.wf = Workflow()

    def convert(self, query):
        self.convert_by_type(query)
        self.wf.send_feedback()

    def add_autocomplete(self):
        return

    def xx(self):
        return

    def convert_by_type(self, query):
        query = str(query).strip()
        if query.find(' ') == -1:
            return

        group = query.split(' ', 1)
        type_value = group[0]
        input_value = group[1]

        if type_value.lower() == 'md5':
            self.md5(input_value)
        elif type_value.lower() == 'datetime':
            self.datetime(input_value)

    def datetime(self, query):
        try:
            dt = datetime.fromtimestamp(float(query))
            self.wf.add_item(
                    title=u'Timestamp to DateTime',
                    subtitle=str(dt),
                    arg=str(dt),
                    valid=True
            )
        except:
            self.wf.add_item(
                    title=u'Convert Failed'
            )

    def md5(self, query):
        m = hashlib.md5()
        m.update(query)
        self.wf.add_item(
                title=u'String to MD5',
                subtitle=m.hexdigest(),
                arg=m.hexdigest(),
                valid=True
        )
