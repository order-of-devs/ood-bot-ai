import pytest

from src.url.save_link import Storage, prepare_normalized_url, save_link


@pytest.mark.asyncio
async def tests_should_save_url() -> None:
    url = "https://www.youtube.com/watch?v=6v2L2UGZJAM"
    storage = Storage()
    normalized_url = prepare_normalized_url(url)
    await save_link(
        storage,
        normalized_url,
        "message_id"
    )
    assert await storage.get(normalized_url.hash()) == "message_id"
