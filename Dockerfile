FROM python:3.11-slim-buster

ADD . /app
WORKDIR /app
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

EXPOSE 8000
CMD ["venv/bin/uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]