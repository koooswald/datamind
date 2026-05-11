from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/query")
def query():
    # TODO: implement
    return {"answer": "stub"}


@router.get("/metrics")
def metrics():
    # TODO: implement
    return []
