from model.BaseModel import BaseModel
from workflow.workflow import Item
import urllib2


class Javascript(BaseModel):
    def __init__(self):
        self.name = u'javascript'
        self.desc = u'Javascript Converter'

    def convert(self, query):
        return [
            Item(
                    title=u'JavaScript encodeURI' + ': ' + query,
                    subtitle=urllib2.quote(query, "!#$&'()*+,-./:;=?@_~").encode("utf-8"),
                    key=self.name + u'-encodeURI',
                    arg=urllib2.quote(query, "!#$&'()*+,-./:;=?@_~").encode("utf-8"),
                    valid=True
            ),
            Item(
                    title=u'JavaScript encodeURIComponent' + ': ' + query,
                    subtitle=urllib2.quote(query, "!'()*-._~").encode("utf-8"),
                    key=self.name + u'-encodeURIComponent',
                    arg=urllib2.quote(query, "!'()*-._~").encode("utf-8"),
                    valid=True
            ),
            Item(
                    title=u'JavaScript decode' + ': ' + query,
                    subtitle=urllib2.unquote(query).encode("utf-8"),
                    key=self.name + u'-decode',
                    arg=urllib2.unquote(query).encode("utf-8"),
                    valid=True
            )
        ]
