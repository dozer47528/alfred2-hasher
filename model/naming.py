from model.base_model import BaseModel
from workflow.workflow import Item


class Naming(BaseModel):
    def __init__(self):
        self.name = u'naming'
        self.desc = u'Naming Converter'

    def split_words(self, query):
        result = []

        word = ""
        all_up_case = True

        for idx, c in enumerate(query):
            assert isinstance(c, basestring)

            if c in ["-", "_"] and word:
                result.append(word)
                word = ""
            elif c.islower() and idx + 1 < len(query) and str(query[idx + 1]).isupper():
                word += c.lower()
                result.append(word)
                word = ""
            elif all_up_case and c.isupper() and idx + 2 < len(query) and query[idx + 1].isupper() and query[idx + 2].islower():
                word += c.lower()
                result.append(word)
                word = ""
            else:
                if c.islower():
                    all_up_case = False
                word += c.lower()

        if word:
            result.append(word)

        return result

    def convert(self, query):
        query = str(query).strip()
        words = self.split_words(query)
        if not words:
            return

        result = [
            ["Camel", "".join(words[0:1] + [w[0].upper() + w[1:] for w in words[1:]])],
            ["Snake", "_".join(words)],
            ["Pascal", "".join([w[0].upper() + w[1:] for w in words])],
            ["Kebab", "-".join(words)]
        ]

        items = []

        for r in result:
            if r[1] == query:
                continue

            items.append(
                Item(
                    title='Naming ' + r[0] + ': ' + query,
                    subtitle=r[1],
                    arg=self.name + '-' + r[0].lower() + ':' + r[1],
                    valid=True,
                    icon=self.icon_path()
                )
            )

        return items
