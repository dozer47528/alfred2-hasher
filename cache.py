# -*- coding: utf-8 -*-

import sys

from workflow import Workflow


class Hasher:
    def __init__(self, wf):
        self.wf = wf
        self.max_age = 60 * 60 * 24 * 365

    def cache(self, query):
        if not query:
            sys.stdout.write("")
            sys.stdout.flush()
            return

        result = query.split(":", 1)
        key = result[0]
        value = result[1]

        count = self.wf.cached_data(key, max_age=self.max_age)
        if not count:
            count = 0
        count += 1

        self.wf.cache_data(key, count)

        sys.stdout.write(value)
        sys.stdout.flush()


def main(wf):
    query = None

    if len(wf.args):
        query = wf.args[0]

    hasher = Hasher(wf)
    hasher.cache(query)


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
