# 1. Base image (explicit tag for reproducibility)
FROM python:3.9-slim  # see: use explicit, deterministic tags :contentReference[oaicite:0]{index=0}

# 2. Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# 3. Create and switch to a non-root user for security
RUN addgroup --system flaskgroup && adduser --system --group flaskuser
USER flaskuser

# 4. Set work directory
WORKDIR /app

# 5. Copy and install dependencies
COPY --chown=flaskuser:flaskgroup requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  # keeps image small :contentReference[oaicite:1]{index=1}

# 6. Copy application source
COPY --chown=flaskuser:flaskgroup . .

# 7. Expose the port your Flask app runs on
EXPOSE 8080

# 8. Launch the app with Gunicorn (4 workers for concurrency)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]
