FROM python:3.12-slim

WORKDIR .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requerments.txt .

RUN pip install --no-cache-dir -r requerments.txt

COPY . .

CMD ["python", "main.py"]
