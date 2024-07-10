from typing import ClassVar

type Hash = str


class Storage:
    data: ClassVar[dict[Hash, str]] = {}

    async def upsert(self, hash_value: Hash, payload: str) -> None:
        self.data[hash_value] = payload

    async def get(self, hash_value: Hash) -> str:
        return self.data[hash_value]
