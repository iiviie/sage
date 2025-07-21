# syntax=docker/dockerfile:1.4

FROM python:3.12-slim AS builder

# Install system dependencies and pipx for installing uv
RUN apt-get update && \
    apt-get install -y curl pipx && \
    pipx install uv && \
    pipx ensurepath

# Make sure uv is available in PATH
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy only dependency files first to leverage layer caching
COPY pyproject.toml uv.lock ./

# Create virtual environment and install dependencies
RUN uv venv /app/.venv && \
    . /app/.venv/bin/activate && \
    uv pip install -r uv.lock

# Now copy the source code and install the package
COPY src ./src
RUN . /app/.venv/bin/activate && uv pip install -e .

# --------------------------------------------------------

FROM python:3.12-slim AS stage-1

WORKDIR /app

# Copy only the necessary files from builder
COPY --from=builder /app/src ./src
COPY --from=builder /app/.venv /app/.venv

# Use the venv for all commands
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app/src:$PYTHONPATH"

# Default command with uvloop and reload enabled
CMD ["python", "-m", "uvicorn", "api_gateway.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--loop", "uvloop", "--reload-dir", "/app/src"]
