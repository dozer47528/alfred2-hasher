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
                ),
                Item(
                    title=u'New UUID without dash',
                    subtitle=new_uuid.replace('-', ''),
                    arg=self.name + u'-uuid4-without-dash:' + new_uuid.replace('-', ''),
                    valid=True,
                    icon=self.icon_path()
                ),
                Item(
                    title=u'New UUID (Hex)',
                    subtitle='0x' + new_uuid.replace('-', ''),
                    arg=self.name + u'-uuid4-hex:0x' + new_uuid.replace('-', ''),
                    valid=True,
                    icon=self.icon_path()
                ),
            ]
        else:
            uuid_type = None
            if "-" in query and len(query) == 36:
                uuid_type = "dash"
            elif len(query) == 34 and query[0:2] == "0x":
                uuid_type = "hex"
            elif len(query) == 32:
                uuid_type = "normal"

            if uuid_type:
                normal_uuid = query.replace('-', '').replace('0x', '')

                if uuid_type != "normal":
                    result += [
                        Item(
                            title=u'UUID without dash',
                            subtitle=normal_uuid,
                            arg=self.name + u'-uuid-without-dash:' + normal_uuid,
                            valid=True,
                            icon=self.icon_path()
                        )
                    ]

                if uuid_type != "dash":
                    formatted_uuid = "%s-%s-%s-%s-%s" % (normal_uuid[0:8], normal_uuid[8:12], normal_uuid[12:16], normal_uuid[16:20], normal_uuid[20:])
                    result += [
                        Item(
                            title=u'Formatted UUID',
                            subtitle=formatted_uuid,
                            arg=self.name + u'-uuid:' + formatted_uuid,
                            valid=True,
                            icon=self.icon_path()
                        )
                    ]

                if uuid_type != "hex":
                    result += [
                        Item(
                            title=u'UUID (Hex)',
                            subtitle='0x' + normal_uuid,
                            arg=self.name + u'-uuid-hex:0x' + normal_uuid,
                            valid=True,
                            icon=self.icon_path()
                        )
                    ]

        return result
