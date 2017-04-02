import hashlib

from model.base_model import BaseModel
from workflow.workflow import Item


class MD5(BaseModel):
    def __init__(self):
        self.name = u'md5'
        self.desc = u'MD5 Converter'

    def convert(self, query):
        m = hashlib.md5()
        m.update(query)
        v = m.hexdigest()
        return [Item(
            title=self.name + ': ' + query,
            subtitle=v,
            arg=self.name + u'-md5:' + v,
            valid=True,
            icon=self.icon_path()
        )]
