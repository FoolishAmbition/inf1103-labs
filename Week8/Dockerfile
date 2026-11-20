FROM python:3.11-slim

WORKDIR /usr/src/app

COPY main.py products.py orders.py storage.py inventory.json products.csv ./
COPY tests/ tests/

CMD ["python", "main.py"]
