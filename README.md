# Discord Bot for Order of Devs

This Discord bot is designed for the Order of Devs community, featuring functionality to summarize 24-hour discussions and provide a knowledge base.

## Features

- Summarize 24-hour discussions
- AI-powered question answering
- Knowledge base integration (coming soon)

## Prerequisites

- Python 3.12 or higher
- (Optional) Mise
- Poetry for dependency management

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
```
3. Install poetry:
```bash
pip install poetry
```
4. Install dependencies:
```bash
poetry install
```
5. Create a `.env` file in the project root and add your Discord bot token:
`DISCORD_TOKEN=your_discord_bot_token_here`

## Running the Bot

To run the bot locally:
`poetry run python src/main.py`

To run the bot using Docker:

1. Build the Docker image:
`docker build -t discord-bot .`
2. Run the container:
`docker run -d --env-file .env discord-bot`

### Code Style and Linting

To run all checks:
```bash
make lint
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes and commit them
4. Push to your fork and submit a pull request

Please ensure your code passes all tests and follows the established code style before submitting a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
