# datamind
A multi-agent data intelligence system that takes natural language business questions and produces answers by orchestrating specialised agents

## Portfolio Project: DataMind Agent System

A **multi-agent data intelligence system** that takes natural language business questions and produces answers by orchestrating specialised agents — directly mirroring the JD's core responsibilities.

### What it does
1. User asks: *"Show me revenue by region for Q1 vs Q2"*
2. **Planning Agent** breaks the question into sub-tasks
3. **SQL Agent** generates + executes queries against a business dataset
4. **RAG Layer** grounds responses in a metric definition store (what "revenue" means, how it's calculated)
5. **Analysis Agent** interprets results and generates a natural language summary
6. **Data Quality Agent** flags anomalies or missing data
7. **FastAPI backend** exposes everything as REST endpoints
8. **Docker + GitHub Actions** for containerisation and CI/CD

### Why this project wins interviews
- Directly mirrors every bullet in the JD's "What You Will Be Doing" section
- Demonstrates multi-agent orchestration, RAG, SQL, API design, and DevOps in one repo
- Shows you can think about production concerns: data quality, hallucination detection, access control

### GitHub Repo Structure
```
datamind/
├── README.md                  # Architecture diagram + demo GIF
├── docker-compose.yml
├── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml             # Lint, test, build on push
├── app/
│   ├── main.py                # FastAPI entrypoint
│   ├── api/
│   │   ├── routes.py          # /query, /health, /metrics endpoints
│   │   └── schemas.py         # Pydantic request/response models
│   ├── agents/
│   │   ├── planner.py         # Planning agent
│   │   ├── sql_agent.py       # Text-to-SQL agent
│   │   ├── analyst.py         # Analysis agent
│   │   └── monitor.py         # Data quality agent
│   ├── rag/
│   │   ├── ingestion.py       # Document processing + chunking
│   │   ├── embeddings.py      # Embedding pipeline
│   │   └── retriever.py       # Retrieval logic
│   ├── data/
│   │   ├── sample_db.sqlite   # Business dataset (orders, revenue, customers)
│   │   └── metric_definitions/ # Business glossary docs for RAG
│   └── utils/
│       ├── llm_client.py      # Anthropic/OpenAI client wrapper
│       └── eval.py            # Output quality checks
├── tests/
│   ├── test_agents.py
│   ├── test_rag.py
│   └── test_api.py
└── notebooks/
    └── exploration.ipynb      # Exploratory work, shows your thinking
```

---