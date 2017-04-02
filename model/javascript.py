import urllib2

from model.base_model import BaseModel
from workflow.workflow import Item


class Javascript(BaseModel):
    def __init__(self):
        self.name = u'javascript'
        self.desc = u'Javascript Converter'

    def convert(self, query):
        return [
            Item(
                title=u'JavaScript encodeURI' + ': ' + query,
                subtitle=urllib2.quote(query, "!#$&'()*+,-./:;=?@_~").encode("utf-8"),
                arg=self.name + u'-encodeURI:' + urllib2.quote(query, "!#$&'()*+,-./:;=?@_~").encode("utf-8"),
                valid=True,
                icon=self.icon_path()
            ),
            Item(
                title=u'JavaScript encodeURIComponent' + ': ' + query,
                subtitle=urllib2.quote(query, "!'()*-._~").encode("utf-8"),
                arg=self.name + u'-encodeURIComponent:' + urllib2.quote(query, "!'()*-._~").encode("utf-8"),
                valid=True,
                icon=self.icon_path()
            ),
            Item(
                title=u'JavaScript decode' + ': ' + query,
                subtitle=urllib2.unquote(query).encode("utf-8"),
                arg=self.name + u'-decode:' + urllib2.unquote(query).encode("utf-8"),
                valid=True,
                icon=self.icon_path()
            )
        ]
