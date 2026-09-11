FROM python:3.12-slim-bookworm

ADD . /app
WORKDIR /app
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["venv/bin/python", "-m", "uvicorn", "main:app", "--reload", "--reload-dir", "/app", "--host", "0.0.0.0", "--port", "8000"]