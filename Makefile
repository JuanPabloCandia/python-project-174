install:
	uv sync

check:
	uv check

build:
	uv build

package-install:
	uv tool install dist/*.whl

publish:
	uv publish --dry-run

lint:
	uv run ruff check gendiff tests

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml tests
