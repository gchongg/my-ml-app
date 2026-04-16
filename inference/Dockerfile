FROM python:3.11 AS builder
WORKDIR /inference
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

FROM python:3.11-slim
WORKDIR /inference
COPY --from=builder /install /usr/local
COPY . .
RUN useradd -m appuser
USER appuser
CMD ["python", "model.py"]