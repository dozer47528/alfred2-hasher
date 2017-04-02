from workflow.workflow import Item


class BaseModel:
    def autocomplete(self, query):
        item = Item(title=self.desc, autocomplete=self.name + ' ', icon=self.icon_path())

        if not query:
            item.sort = 0
        elif self.name == query:
            item.sort = len(query) * 10
        elif self.name.find(query) == 0:
            item.sort = len(query)
        else:
            return []
        return [item]

    def icon_path(self):
        return 'icons/%s.png' % self.name
