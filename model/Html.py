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
                    title=u'Html Encode' + ': ' + query,
                    subtitle=saxutils.escape(query),
                    key=self.name + u'-encode',
                    arg=saxutils.escape(query),
                    valid=True
            ),
            Item(
                    title=u'Html Decode' + ': ' + query,
                    subtitle=saxutils.unescape(query),
                    key=self.name + u'-decode',
                    arg=saxutils.unescape(query),
                    valid=True
            )
        ]
