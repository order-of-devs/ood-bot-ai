from src.storage import Storage
from src.url.normalizer import normalize_url
from src.url.parser import Url, parse_url


def prepare_normalized_url(url: str) -> Url:
    return normalize_url(parse_url(url))


async def save_link(storage: Storage, normalized_url: Url, message_id: str) -> str:
    await storage.upsert(normalized_url.hash(), message_id)
