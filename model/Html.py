from model.BaseModel import BaseModel
from workflow.workflow import Item
from xml.sax import saxutils


class Html(BaseModel):
    def __init__(self):
        self.name = u'html'
        self.desc = u'Html Converter'

    def convert(self, query):
        return [
            Item(
                    title=u'Html Encode',
                    subtitle=saxutils.escape(query),
                    arg=saxutils.escape(query),
                    valid=True
            ),
            Item(
                    title=u'Html Decode',
                    subtitle=saxutils.unescape(query),
                    arg=saxutils.unescape(query),
                    valid=True
            )
        ]
