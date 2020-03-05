from model.base_model import BaseModel
from workflow.workflow import Item


class Number(BaseModel):
    def __init__(self):
        self.name = u'number'
        self.desc = u'Number Converter'

    def convert(self, query):
        result = []

        dec_source = None
        try:
            dec_source = int(query)
        except ValueError:
            pass

        try:
            result.append(Item(
                title=u'Bin to Dec' + ': ' + query,
                subtitle=str(int(query, 2)),
                arg=self.name + u'-bin2dec:' + str(int(query, 2)),
                valid=True,
                icon=self.icon_path()
            ))
        except ValueError:
            pass

        try:
            result.append(Item(
                title=u'Oct to Dec' + ': ' + query,
                subtitle=str(int(query, 8)),
                arg=self.name + u'-oct2dec:' + str(int(query, 8)),
                valid=True,
                icon=self.icon_path()
            ))
        except ValueError:
            pass

        try:
            result.append(Item(
                title=u'Hex to Dec' + ': ' + query,
                subtitle=str(int(query, 16)),
                arg=self.name + u'-hex2dec:' + str(int(query, 16)),
                valid=True,
                icon=self.icon_path()
            ))
        except ValueError:
            pass

        if dec_source:
            result.append(Item(
                title=u'Dec to Hex' + ': ' + query,
                subtitle=hex(dec_source),
                arg=self.name + u'-dec2hex:' + hex(dec_source),
                valid=True,
                icon=self.icon_path()
            ))
            result.append(Item(
                title=u'Dec to Bin' + ': ' + query,
                subtitle=bin(dec_source),
                arg=self.name + u'-dec2bin:' + bin(dec_source),
                valid=True,
                icon=self.icon_path()
            ))
            result.append(Item(
                title=u'Dec to Oct' + ': ' + query,
                subtitle=oct(dec_source),
                arg=self.name + u'-dec2oct:' + oct(dec_source),
                valid=True,
                icon=self.icon_path()
            ))

        return result
