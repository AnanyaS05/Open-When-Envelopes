# Use a Python 3.9 slim image
FROM python:3.9-slim

# Set env vars for Python behavior
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system packages needed by mysqlclient
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      python3-dev \
      default-libmysqlclient-dev \
      pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port your app runs on
EXPOSE 8080

# Use Gunicorn for serving the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]
