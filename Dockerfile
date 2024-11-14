FROM python:3.10-slim as client

WORKDIR /app

RUN pip install pymodbus==2.5.0

COPY modbus_client.py .

CMD ["python", "modbus_client.py"]
