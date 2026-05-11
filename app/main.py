from fastapi import FastAPI

app = FastAPI(title="DataMind", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/query")
def query():
    # TODO: wire up planning agent
    return {"answer": "stub"}
