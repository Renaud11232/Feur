FROM python:3.12-slim

RUN pip install --no-cache-dir "https://github.com/Renaud11232/Feur/archive/refs/heads/master.zip"

ENTRYPOINT ["feur"]