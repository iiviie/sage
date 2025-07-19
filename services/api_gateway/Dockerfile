FROM python:3.12-slim as builder

WORKDIR /app

# Install build dependencies and uv in a single layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    pip install uv && \
    rm -rf /var/lib/apt/lists/*

# Create venv
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Copy requirements first for better caching
COPY requirements.txt .
RUN uv pip install --no-cache -r requirements.txt

# Final stage
FROM python:3.12-slim

WORKDIR /app

# Install uv in final stage for incremental installs
RUN pip install --no-cache-dir uv

# Copy the entire venv from builder
COPY --from=builder /app/venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Copy application code LAST to avoid cache invalidation
COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--loop", "uvloop"] 