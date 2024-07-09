from urllib.parse import urlparse
from typing import Optional
from dataclasses import dataclass
from urllib.request import urlopen
import hashlib


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


def match_url_domain(base_url: str) -> Optional[str]:
    try:
        parsed_url = urlparse(base_url)

        return parsed_url.netloc
    except ValueError:
        return None


def parse_url(url: str) -> Url:
    req_url = url
    with urlopen(url) as response:
        if response.status != 200:
            raise ValueError(f"Invalid URL: {url}")
        req_url = response.geturl()
    parsed_url = urlparse(req_url)
    return Url(
        base_url=parsed_url.netloc,
        path=parsed_url.path,
        query=parsed_url.query,
    )


def normalize_url(url: Url) -> Url:
    return Url(
        base_url=url.base_url.replace("www.", ""),
        path=url.path,
        query=url.query.split("&")[0],
    )
