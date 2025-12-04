FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
LABEL authors="mkgaj"

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project --no-dev

COPY . .

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]