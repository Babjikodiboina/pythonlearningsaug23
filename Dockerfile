# Use a base Python image
FROM python:3.10-slim as client

# Set the working directory
WORKDIR /app

# Install pymodbus, specify a stable version
RUN pip install pymodbus==2.5.0

# Copy the Modbus client script into the container
COPY modbus_client.py .

# Set the entrypoint to run client script
CMD ["python", "modbus_client.py"]
