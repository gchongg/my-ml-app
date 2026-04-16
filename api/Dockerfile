FROM python:3.11 AS builder
WORKDIR /app
COPY requirements.txt .
RUN python -m venv /venv && /venv/bin/pip install -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /venv /venv
COPY . .
RUN useradd -m appuser
USER appuser
ENV PATH="/venv/bin:$PATH"
CMD ["python", "app.py"]