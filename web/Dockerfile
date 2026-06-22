FROM python:3.10-slim

RUN apt update && apt install -y nginx && rm -rf /var/lib/apt/lists/*

RUN pip install psycopg2-binary

COPY app.py /app/app.py
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/app/entrypoint.sh"]
