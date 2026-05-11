from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str
    context: str | None = None


class QueryResponse(BaseModel):
    answer: str
    sql: str | None = None
    sources: list[str] = []
