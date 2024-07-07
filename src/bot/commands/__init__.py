from typing import Protocol


class Command(Protocol):
    async def execute(self, command: str):
        pass
