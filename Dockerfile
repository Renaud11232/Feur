FROM python:3.13 AS builder

ADD dist/*.whl /tmp/

RUN python -m venv /app \
    && /app/bin/pip install --no-cache-dir /tmp/*.whl


FROM python:3.13-slim

COPY --from=builder /app /app

ENTRYPOINT ["/app/bin/feur"]