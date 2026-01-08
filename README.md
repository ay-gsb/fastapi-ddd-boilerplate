### Domain Drive Design: FastApi Postgres SqlAlchemy Boilerplate

#### Development Environment
```bash
# Checkout repo and cd to it.
cp env.example to .env  # make changes .env if needed
uv sync
uv run analytics-api
```

Ruff for formatting
```bash
uv run ruff check # or with --fix
uv run ruff format
```
