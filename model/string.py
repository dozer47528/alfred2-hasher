from model.base_model import BaseModel
from workflow.workflow import Item


class String(BaseModel):
    def __init__(self):
        self.name = u'string'
        self.desc = u'String Converter'

    def convert(self, query):
        result = []

        if query:
            if query != query.lower():
                result += [
                    Item(
                        title=u'String lowercase',
                        subtitle=query.lower(),
                        arg=self.name + u'-lowercase:' + query.lower(),
                        valid=True,
                        icon=self.icon_path()
                    )
                ]
            if query != query.upper():
                result += [
                    Item(
                        title=u'String uppercase',
                        subtitle=query.upper(),
                        arg=self.name + u'-uppercase:' + query.upper(),
                        valid=True,
                        icon=self.icon_path()
                    )
                ]
        return result
