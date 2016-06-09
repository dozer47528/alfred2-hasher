from model.base_model import BaseModel
from workflow.workflow import Item
from xml.sax import saxutils


class Number(BaseModel):
    def __init__(self):
        self.name = u'num'
        self.desc = u'Number Converter'

    def convert(self, query):
        result = []

        decSource = None
        try:
            decSource = int(query)
        except ValueError:
            pass

        try:
            result.append(Item(
                    title=u'Bin to Dec' + ': ' + query,
                    subtitle=str(int(query, 2)),
                    arg=self.name + u'-bin2dec:' + str(int(query, 2)),
                    valid=True
            ))
        except ValueError:
            pass

        try:
            result.append(Item(
                    title=u'Oct to Dec' + ': ' + query,
                    subtitle=str(int(query, 8)),
                    arg=self.name + u'-oct2dec:' + str(int(query, 8)),
                    valid=True
            ))
        except ValueError:
            pass

        try:
            result.append(Item(
                    title=u'Hex to Dec' + ': ' + query,
                    subtitle=str(int(query, 16)),
                    arg=self.name + u'-hex2dec:' + str(int(query, 16)),
                    valid=True
            ))
        except ValueError:
            pass

        if decSource:
            result.append(Item(
                    title=u'Dec to Hex' + ': ' + query,
                    subtitle=hex(decSource),
                    arg=self.name + u'-dec2hex:' + hex(decSource),
                    valid=True
            ))
            result.append(Item(
                    title=u'Dec to Bin' + ': ' + query,
                    subtitle=bin(decSource),
                    arg=self.name + u'-dec2bin:' + bin(decSource),
                    valid=True
            ))
            result.append(Item(
                    title=u'Dec to Oct' + ': ' + query,
                    subtitle=oct(decSource),
                    arg=self.name + u'-dec2oct:' + oct(decSource),
                    valid=True
            ))

        return result
