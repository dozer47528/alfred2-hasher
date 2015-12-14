from model.BaseModel import BaseModel
from workflow.workflow import Item
from datetime import datetime
import re


class DateTime(BaseModel):
    def __init__(self):
        self.name = u'datetime'
        self.desc = u'DateTime Converter'

    def convert(self, query):
        result = []

        if re.search('^\d+(\.\d?)?$', query):
            timestamp = float(query)
            local_datetime = datetime.fromtimestamp(timestamp)
            utc_datetime = datetime.utcfromtimestamp(timestamp)

            result += [
                Item(
                        title=u'TimeStamp to DataTime(Local)' + ': ' + query,
                        subtitle=str(local_datetime),
                        arg=str(local_datetime),
                        valid=True
                ),
                Item(
                        title=u'TimeStamp to DataTime(UTC)' + ': ' + query,
                        subtitle=str(utc_datetime),
                        arg=str(utc_datetime),
                        valid=True
                )
            ]
        return result
