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
	make build
	make package-install
	uv run pytest

test-coverage:
	make build
	make package-install
	uv run pytest --cov=gendiff --cov-report xml tests
