from xml.sax import saxutils

from model.base_model import BaseModel
from workflow.workflow import Item


class Html(BaseModel):
    def __init__(self):
        self.name = u'html'
        self.desc = u'Html Converter'

    def convert(self, query):
        return [
            Item(
                title=u'Html Encode' + ': ' + query,
                subtitle=saxutils.escape(query),
                arg=self.name + u'-encode:' + saxutils.escape(query),
                valid=True,
                icon=self.icon_path()
            ),
            Item(
                title=u'Html Decode' + ': ' + query,
                subtitle=saxutils.unescape(query),
                arg=self.name + u'-decode:' + saxutils.unescape(query),
                valid=True,
                icon=self.icon_path()
            )
        ]
