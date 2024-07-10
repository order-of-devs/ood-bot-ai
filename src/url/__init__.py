import hashlib
from dataclasses import dataclass
from typing import Optional


@dataclass
class Url:
    base_url: str
    path: Optional[str]
    query: Optional[str]

    def hash(self) -> str:
        data = str(self.__repr__()).encode("utf-8")
        sha1 = hashlib.sha1()  # noqa: S324
        sha1.update(data)
        return sha1.hexdigest()

    def __repr__(self) -> str:
        return f"{self.base_url}{self.path}?{self.query}"

