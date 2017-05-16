import uuid

from model.base_model import BaseModel
from workflow.workflow import Item


class TheUUID(BaseModel):
    def __init__(self):
        self.name = u'uuid'
        self.desc = u'UUID Converter'

    def convert(self, query):
        result = []

        if not query:
            new_uuid = str(uuid.uuid4())
            result += [
                Item(
                    title=u'New UUID',
                    subtitle=new_uuid,
                    arg=self.name + u'-uuid4:' + new_uuid,
                    valid=True,
                    icon=self.icon_path()
                )
            ]
        else:
            if "-" in query:
                no_dash_uuid = query.replace('-', '')
                result += [
                    Item(
                        title=u'UUID without dash',
                        subtitle=no_dash_uuid,
                        arg=self.name + u'-uuid-without-dash:' + no_dash_uuid,
                        valid=True,
                        icon=self.icon_path()
                    )
                ]

            if "-" not in query and len(query) == 32:
                formatted_uuid = "%s-%s-%s-%s-%s" % (query[0:8], query[8:12], query[12:16], query[16:20], query[20:])
                result += [
                    Item(
                        title=u'Formatted UUID',
                        subtitle=formatted_uuid,
                        arg=self.name + u'-formatted-uuid:' + formatted_uuid,
                        valid=True,
                        icon=self.icon_path()
                    )
                ]

        return result
