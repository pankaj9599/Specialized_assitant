FROM ghcr.io/astral-sh/uv:python3.12-bookworm

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

COPY . .

ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "-m", "graph.graphbuilder"]