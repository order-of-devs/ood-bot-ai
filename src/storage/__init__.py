type Hash = str


class Storage:
    data = {}

    async def upsert(self, hash_value: Hash, payload: str):
        self.data[hash_value] = payload

    async def get(self, hash_value: Hash) -> str:
        return self.data[hash_value]
