# AI Learning Universe

An intelligent learning platform combining LLMs, AI Agents, Computer Vision, Machine Learning, and Knowledge Graphs to create personalized learning experiences.

## Architecture

- **Frontend:** Next.js 14 + TypeScript + Tailwind + shadcn/ui
- **Backend:** FastAPI (Python 3.12)
- **Database:** Supabase PostgreSQL + pgvector
- **AI:** OpenRouter (GPT-4o, Claude 3.5, Gemini)
- **Deployment:** Vercel (frontend) + Render (backend)

## Features

- AI Tutor with RAG-based knowledge retrieval
- Personalized Learning Roadmap Generator
- Quiz Generation and Evaluation
- Progress Dashboard
- Knowledge Graph Based Learning Paths
- Computer Vision for Notes and Images
- Placement Readiness Prediction
- Adaptive Learning with Thompson Sampling

## Getting Started

### Prerequisites

- Node.js 20+
- Python 3.12+
- Docker Desktop

### Setup

```bash
# Frontend
cd frontend
npm install
npm run dev

# Backend
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Live Demo

[Coming Soon]

## Sprint Status

- Sprint 1: Foundation (In Progress)
