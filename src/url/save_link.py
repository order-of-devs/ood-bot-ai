from src.url.parser import Url


class Storage:
    data = {}

    async def upsert(self, url: Url, message_id: str):
        self.data[url.hash()] = message_id


async def save_link(storage: Storage, normalized_url: Url, message_id: str):
    await storage.upsert(normalized_url, message_id)
