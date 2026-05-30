# Multi-stage build: keeps image small and fast
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (required for ML libraries)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Install Python packages with retries and no cache
RUN pip install --no-cache-dir \
    --retries 5 \
    --timeout 1000 \
    -r requirements.txt

# Copy app files (excluding large files via .dockerignore)
COPY . .

EXPOSE 5000

# Run Flask in non-debug mode for production
CMD ["python", "app.py"]
