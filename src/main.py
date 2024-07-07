from bot import DiscordBot
from src.core.config import Settings


def main():
    settings = Settings()
    initialize = DiscordBot(settings)
    initialize()


if __name__ == '__main__':
    main()

