FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_SYSTEM_PYTHON=1 \
    APP_HOME=/app

WORKDIR ${APP_HOME}

# Copy uv binary from official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install system runtime dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    gettext \
    default-libmysqlclient-dev \
    libpq-dev \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies using uv
COPY pyproject.toml ./
RUN uv pip install -r pyproject.toml gunicorn

COPY ./docker/django/gunicorn_config.py gunicorn_config.py
COPY ./docker/django/start.sh start.sh
RUN sed -i 's/\r$//g' start.sh && chmod +x start.sh

COPY ./manage.py manage.py
COPY ./server/ server/

HEALTHCHECK --interval=30s --timeout=30s --retries=3 CMD curl -f http://localhost:8000/ || exit 1

EXPOSE 8000

ENTRYPOINT ["/bin/bash", "start.sh"]
