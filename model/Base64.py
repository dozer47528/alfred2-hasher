import base64

from model.BaseModel import BaseModel
from workflow.workflow import Item


class Base64(BaseModel):
    def __init__(self):
        self.name = u'base64'
        self.desc = u'Base64 Converter'

    def convert(self, query):
        result = []

        encode_result = base64.encodestring(query).replace('\n', '')
        result += [
            Item(
                    title=u'Base64 Encode',
                    subtitle=encode_result,
                    arg=encode_result,
                    valid=True
            )
        ]

        try:
            decode_result = base64.decodestring(query).replace('\n', '')
            if base64.encodestring(decode_result).replace('\n', '') == query:
                result += [
                    Item(
                            title=u'Base64 Decode',
                            subtitle=decode_result,
                            arg=decode_result,
                            valid=True
                    )
                ]
        except:
            pass

        return result
