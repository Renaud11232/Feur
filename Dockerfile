FROM python:3.13-slim

RUN pip install --no-cache-dir "https://github.com/Renaud11232/Feur/archive/refs/heads/master.zip"

ENTRYPOINT ["feur"]