# my-ml-app

Containerized ML system with three services: an API gateway, an inference service, and a PostgreSQL database.

## Quickstart

Create a `.env` file:
```
POSTGRES_PASSWORD=your_password_here
```

Run everything:
```bash
docker compose up --build
```

Test it:
```bash
curl http://localhost:8080/predict
```

## Services

- **api** — Flask gateway on port 8080
- **inference** — model predictions on port 8081
- **db** — PostgreSQL on port 5432

## CI/CD

Pushes to `main` automatically build and push the API image to Docker Hub via GitHub Actions.