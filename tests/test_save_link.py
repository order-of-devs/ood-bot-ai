from src.url.parser import parse_url, normalize_url
from src.url.save_link import save_link, Storage
import pytest

@pytest.mark.asyncio
async def tests_should_save_url():
    url = "https://www.youtube.com/watch?v=6v2L2UGZJAM"
    storage = Storage()
    normalized_url = normalize_url(parse_url(url))
    await save_link(
        storage,
        normalized_url,
        "message_id"
    )
    assert storage.data[normalized_url.hash()] == "message_id"
