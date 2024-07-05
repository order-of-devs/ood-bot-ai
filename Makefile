.PHONY: tests

format:
	ruff check --fix --exit-non-zero-on-fix --show-fixes --preview --unsafe-fixes
	black src $(ARGS)

lint:
	ruff check
	black --check .
	mypy .

up:
	@docker compose up

down:
	@docker-compose down

logs:
	@docker compose logs -f

start:
	@docker compose down
	@docker system prune -a
	@docker compose build
	@docker compose up app -d

build:
	@docker compose build
