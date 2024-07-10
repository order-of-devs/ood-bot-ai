from src.url import Url


def normalize_url(url: Url) -> Url:
    return Url(
        base_url=url.base_url.replace("www.", ""),
        path=url.path,
        query=url.query.split("&")[0],
    )

