# 🤖 Market Research Crew API

A multi-agent AI system built with **CrewAI** and **FastAPI** that performs comprehensive market research on any topic. The system uses a team of specialized AI agents working together to research, analyze, write, and edit professional market research reports.

---

## 🎯 What This Does

This project creates an **AI Agent Crew** that:
1. **Senior Research Agent** - Searches the web and gathers information on your topic
2. **Market Analyst Agent** - Analyzes the research data and identifies trends
3. **Content Writer Agent** - Writes a comprehensive report from the analysis
4. **Senior Editor Agent** - Reviews and polishes the final report

All agents work sequentially in a pipeline to produce high-quality market research reports.

---

## 📁 Project Structure

```
crew/
├── config.py              # Environment settings (API keys)
├── docker-compose.yml     # Docker compose configuration
├── Dockerfile             # Docker build instructions
├── pyproject.toml         # Python dependencies
├── uv.lock                # Locked dependencies
├── .env                   # Environment variables (create this)
├── README.md              # This file
└── app/
    ├── main.py            # FastAPI application & endpoints
    ├── agents.py          # AI Agent definitions
    ├── tasks.py           # Task definitions for agents
    ├── crew_runner.py     # Crew orchestration logic
    ├── prompts.py         # Agent prompts (role, goal, backstory)
    ├── schemas.py         # Pydantic request/response models
    └── tools.py           # Agent tools (web search, etc.)
```

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose installed
- API Keys:
  - **Groq API Key** (for LLM) - Get from [groq.com](https://groq.com)
  - **Serper API Key** (for web search) - Get from [serper.dev](https://serper.dev)

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd crew
```

### 2. Create Environment File
Create a `.env` file in the root directory:

```env
LLM_API_KEY=your_groq_api_key_here
LLM_API_BASE=https://api.groq.com/openai/v1
MODEL_NAME=llama-3.1-70b-versatile
SERPER_API_KEY=your_serper_api_key_here
```

### 3. Run with Docker
```bash
docker-compose up --build
```

### 4. Access the API
- **API Base URL:** `http://localhost:8000`
- **Health Check:** `http://localhost:8000/health`
- **API Docs:** `http://localhost:8000/docs`

---

## 📡 API Endpoints

### Health Check
```http
GET /health
```
**Response:**
```json
{
  "status": "healthy"
}
```

### Generate Research Report
```http
POST /research
Content-Type: application/json

{
  "topic": "AI Agents in 2025"
}
```

**Response:**
```json
{
  "status": "success",
  "result": "... comprehensive market research report ..."
}
```

## ⚙️ Configuration

| Environment Variable | Description | Example |
|---------------------|-------------|---------|
| `LLM_API_KEY` | Your Groq API key | `gsk_xxxx...` |
| `LLM_API_BASE` | LLM API base URL | `https://api.groq.com/openai/v1` |
| `MODEL_NAME` | Model to use | `llama-3.1-70b-versatile` |
| `SERPER_API_KEY` | Serper.dev API key for web search | `xxxx...` |

---

## 🛠️ Local Development (Without Docker)

### Using UV (Recommended)
```bash
# Install dependencies
uv sync

# Run the server
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Using pip
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -e .

# Run the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🐳 Docker Commands

```bash
# Build and run
docker-compose up --build

# Run in background
docker-compose up -d

# Stop containers
docker-compose down

# View logs
docker-compose logs -f
```

---

## 🧠 How the Agent Crew Works

```
┌─────────────────┐
│  User Request   │
│  (Topic Input)  │
└────────┬────────┘
         ▼
┌─────────────────┐
│ Senior Research │ ──► Searches web, gathers data
│     Agent       │
└────────┬────────┘
         ▼
┌─────────────────┐
│ Market Analyst  │ ──► Analyzes trends & insights
│     Agent       │
└────────┬────────┘
         ▼
┌─────────────────┐
│ Content Writer  │ ──► Writes comprehensive report
│     Agent       │
└────────┬────────┘
         ▼
┌─────────────────┐
│ Senior Editor   │ ──► Reviews & polishes content
│     Agent       │
└────────┬────────┘
         ▼
┌─────────────────┐
│  Final Report   │
│    (Output)     │
└─────────────────┘
```

---

## 📦 Tech Stack

- **[CrewAI](https://github.com/joaomdmoura/crewAI)** - Multi-agent orchestration framework
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern Python web framework
- **[Groq](https://groq.com/)** - Fast LLM inference
- **[Serper](https://serper.dev/)** - Google Search API
- **[Pydantic](https://docs.pydantic.dev/)** - Data validation
- **[UV](https://github.com/astral-sh/uv)** - Fast Python package manager
- **[Docker](https://www.docker.com/)** - Containerization

---

## 📄 License

MIT License

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

