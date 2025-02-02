FROM python:3.11-slim

WORKDIR .
COPY . .

EXPOSE 5090
CMD ["python", "server.py"]
