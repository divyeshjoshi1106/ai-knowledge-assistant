# AI Knowledge Assistant

An AI-powered document management and question-answering system built with FastAPI.

The goal of this project is to build a production-style AI application that allows users to upload documents and retrieve information using RAG (Retrieval-Augmented Generation).

## Current Features

- FastAPI backend
- REST API for document management
- Pydantic request validation
- Basic CRUD operations for documents
- PostgreSQL database running with Docker Compose

## Tech Stack

### Backend
- Python
- FastAPI
- Pydantic

### Database
- PostgreSQL
- Docker
- Docker Compose

## Project Structure

```
app/
├── api/
│   └── documents.py
├── main.py
├── models/
├── schemas/
├── services/
└── database/

tests/

docker-compose.yml
```

## Planned Features

- PostgreSQL integration with SQLAlchemy
- Database migrations using Alembic
- User authentication with JWT
- PDF document upload
- Document processing pipeline
- Vector database integration
- RAG-based question answering
- LLM integration
- Docker deployment
- CI/CD pipeline with GitHub Actions
- Monitoring with Prometheus and Grafana
- Kubernetes deployment

## Running Locally

### Start PostgreSQL

```bash
docker compose up -d
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start FastAPI

```bash
uvicorn app.main:app --reload
```

API documentation:

```
http://localhost:8000/docs
```

## Project Status

Currently in early development.

The project will gradually evolve into a complete AI application combining:

- Backend engineering
- Artificial Intelligence
- Database systems
- DevOps practices
- Cloud deployment