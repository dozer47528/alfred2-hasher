from workflow.workflow import Item
from model.BaseModel import BaseModel
import hashlib


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
                arg=v,
                valid=True
        )]
