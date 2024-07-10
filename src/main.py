from bot import DiscordBot

from src.bot import AskAICommand, SummarizeCommand
from src.core.config import Settings


def main() -> None:
    settings = Settings()
    initialize = DiscordBot(settings,
                            AskAICommand(),
                            SummarizeCommand())
    initialize.register_commands()
    initialize()


if __name__ == "__main__":
    main()

