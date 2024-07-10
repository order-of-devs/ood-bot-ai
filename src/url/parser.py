from urllib.parse import urlparse
from typing import Optional
from urllib.request import urlopen

from src.url import Url


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

