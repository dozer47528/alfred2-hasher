import hashlib

from model.base_model import BaseModel
from workflow.workflow import Item


class SHA(BaseModel):
    def __init__(self):
        self.name = u'sha'
        self.desc = u'SHA Converter'

    def convert(self, query):
        sha1 = hashlib.sha1()
        sha1.update(query)
        sha1_result = sha1.hexdigest()

        sha224 = hashlib.sha224()
        sha224.update(query)
        sha224_result = sha224.hexdigest()

        sha256 = hashlib.sha256()
        sha256.update(query)
        sha256_result = sha256.hexdigest()

        sha384 = hashlib.sha384()
        sha384.update(query)
        sha384_result = sha384.hexdigest()

        sha512 = hashlib.sha512()
        sha512.update(query)
        sha512_result = sha512.hexdigest()

        return [Item(
            title="SHA1" + ': ' + query,
            subtitle=sha1_result,
            arg=self.name + u'-sha1:' + sha1_result,
            valid=True,
            icon=self.icon_path()
        ), Item(
            title="SHA256" + ': ' + query,
            subtitle=sha256_result,
            arg=self.name + u'-sha256:' + sha256_result,
            valid=True,
            icon=self.icon_path()
        ), Item(
            title="SHA512" + ': ' + query,
            subtitle=sha512_result,
            arg=self.name + u'-sha512:' + sha512_result,
            valid=True,
            icon=self.icon_path()
        ), Item(
            title="SHA224" + ': ' + query,
            subtitle=sha224_result,
            arg=self.name + u'-sha224:' + sha224_result,
            valid=True,
            icon=self.icon_path()
        ), Item(
            title="SHA384" + ': ' + query,
            subtitle=sha384_result,
            arg=self.name + u'-sha384:' + sha384_result,
            valid=True,
            icon=self.icon_path()
        )]
