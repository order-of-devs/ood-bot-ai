from src.url.save_link import save_link, Storage, prepare_normalized_url
import pytest


@pytest.mark.asyncio
async def tests_should_save_url():
    url = "https://www.youtube.com/watch?v=6v2L2UGZJAM"
    storage = Storage()
    normalized_url = prepare_normalized_url(url)
    await save_link(
        storage,
        normalized_url,
        "message_id"
    )
    assert await storage.get(normalized_url.hash()) == "message_id"
