import re
import time
from datetime import datetime

from dateutil.parser import parse
from model.base_model import BaseModel
from workflow.workflow import Item


class DateTime(BaseModel):
    def __init__(self):
        self.name = u'datetime'
        self.desc = u'DateTime Converter'

    def to_timestamp(self, dt, epoch=datetime(1970, 1, 1)):
        td = dt - epoch
        return (td.microseconds + (td.seconds + td.days * 86400) * 10 ** 6) / 10 ** 6

    def convert(self, query):
        result = []

        if not query:
            now = int(time.time())
            local_datetime = datetime.fromtimestamp(now)
            utc_datetime = datetime.utcfromtimestamp(now)

            result += [
                Item(
                    title=u'Timestamp',
                    subtitle=str(now),
                    arg=self.name + u'-now-timestamp:' + str(now),
                    valid=True,
                    icon=self.icon_path()
                ),
                Item(
                    title=u'Local Datetime',
                    subtitle=str(local_datetime),
                    arg=self.name + u'-now-datetime-local:' + str(local_datetime),
                    valid=True,
                    icon=self.icon_path()
                ),
                Item(
                    title=u'UTC Datetime',
                    subtitle=str(utc_datetime),
                    arg=self.name + u'-now-datetime--utc:' + str(utc_datetime),
                    valid=True,
                    icon=self.icon_path()
                )
            ]
        else:
            if re.search(r'^\d+(\.\d?)?$', query):
                timestamp = float(query)
                try:
                    local_datetime = datetime.fromtimestamp(timestamp)
                    utc_datetime = datetime.utcfromtimestamp(timestamp)
                except ValueError:
                    timestamp = timestamp / 1000
                    local_datetime = datetime.fromtimestamp(timestamp)
                    utc_datetime = datetime.utcfromtimestamp(timestamp)

                result += [
                    Item(
                        title=u'TimeStamp to DateTime(Local)' + ': ' + query,
                        subtitle=str(local_datetime),
                        arg=self.name + u'-timestamp-to-datetime-local:' + str(local_datetime),
                        valid=True,
                        icon=self.icon_path()
                    ),
                    Item(
                        title=u'TimeStamp to DateTime(UTC)' + ': ' + query,
                        subtitle=str(utc_datetime),
                        arg=self.name + u'-timestamp-to-datetime-utc:' + str(utc_datetime),
                        valid=True,
                        icon=self.icon_path()
                    )
                ]
            else:
                try:
                    parsed_datetime = parse(query)
                    convert_result = str(self.to_timestamp(parsed_datetime))
                    result += [
                        Item(
                            title=u'TimeStamp to DateTime to TimeStamp' + ': ' + query,
                            subtitle=convert_result,
                            arg=self.name + u'-datetime-to-timestamp:' + convert_result,
                            valid=True,
                            icon=self.icon_path()
                        )
                    ]
                except:
                    pass

        return result
