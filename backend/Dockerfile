FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
