from typing import Optional
from urllib.parse import urlparse
from urllib.request import urlopen

from src.url import Url

HTTP_OK = 200


def match_url_domain(base_url: str) -> Optional[str]:
    try:
        parsed_url = urlparse(base_url)
        return parsed_url.netloc  # noqa: TRY300
    except ValueError:
        return None


def parse_url(url: str) -> Optional[Url]:
    req_url = url
    if url.startswith("file://"):
        return None
    with urlopen(url) as response:  # noqa: S310
        if response.status != HTTP_OK:
            msg = f"Invalid URL: {url}"
            raise ValueError(msg)
        req_url = response.geturl()
    parsed_url = urlparse(req_url)
    return Url(
        base_url=parsed_url.netloc,
        path=parsed_url.path,
        query=parsed_url.query,
    )
