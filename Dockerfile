# Base image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy requirements and install
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app/ .

# Expose port
EXPOSE 80

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
