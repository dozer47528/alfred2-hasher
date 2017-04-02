from model.base_model import BaseModel
from workflow.workflow import Item


class ASCII(BaseModel):
    def __init__(self):
        self.name = u'ascii'
        self.desc = u'ASCII Converter'

    def convert(self, query):
        result = []

        try:
            int_char = int(query)
            if 32 <= int_char <= 126:
                char = str(chr(int_char))
                if char:
                    result.append(Item(
                        title=u'Number to ASCII' + ': ' + query,
                        subtitle=char,
                        arg=self.name + u'-num2ascii:' + char,
                        valid=True,
                        icon=self.icon_path()
                    ))
        except ValueError:
            pass

        try:
            if len(query) == 1:
                result.append(Item(
                    title=u'ASCII to Number' + ': ' + query,
                    subtitle=str(ord(query[0])),
                    arg=self.name + u'-ascii2number:' + str(ord(query[0])),
                    valid=True,
                    icon=self.icon_path()
                ))
        except ValueError:
            pass

        return result
