from dataclasses import dataclass
import hashlib
from typing import Optional


@dataclass
class Url:
    base_url: str
    path: Optional[str]
    query: Optional[str]

    def hash(self):
        data = str(self.__repr__()).encode('utf-8')
        sha1 = hashlib.sha1()
        sha1.update(data)
        return sha1.hexdigest()

    def __repr__(self):
        return f"{self.base_url}{self.path}?{self.query}"

