FROM python:3.11-alpine AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install project dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY listener.py ./listener.py
COPY modules ./modules
COPY Files ./Files

RUN adduser -D bot && chown -R bot:bot /app
USER bot

CMD ["python", "listener.py"]
