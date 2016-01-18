from model.BaseModel import BaseModel
from workflow.workflow import Item
from xml.sax import saxutils


class ASCII(BaseModel):
    def __init__(self):
        self.name = u'ascii'
        self.desc = u'ASCII Converter'

    def convert(self, query):
        result = []

        try:
            result.append(Item(
                    title=u'Number to ASCII' + ': ' + query,
                    subtitle=str(chr(int(query))),
                    arg=self.name + u'-num2ascii:' + str(chr(int(query))),
                    valid=True
            ))
        except ValueError:
            pass

        try:
            if len(query) == 1:
                result.append(Item(
                        title=u'ASCII to Number' + ': ' + query,
                        subtitle=str(ord(query[0])),
                        arg=self.name + u'-ascii2number:' + str(ord(query[0])),
                        valid=True
                ))
        except ValueError:
            pass

        return result
