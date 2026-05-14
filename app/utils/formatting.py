# General formatting functions

from dataclasses import dataclass


@dataclass
class QueryResult:
    sql: str
    rows: list[dict]
    row_count: int
    

def format_query_result(result: QueryResult) -> str:
    """Format a query result into a human-readable summary."""
    if result.row_count == 0:
        return "No results found."
    return f"Found {result.row_count} rows. \nSQL: {result.sql}"


def validate_question(question: str) -> bool:
    """Return True if the question is a non-empty string."""
    return isinstance(question, str) and len(question.strip()) > 0


def load_config(raw: dict[str, str], required_keys: list[str]) -> dict[str, str]:
    """Extract and validate required keys from a config dict."""
    missing = [k for k in required_keys if k not in raw]
    if missing:
        raise ValueError(f"Missing config keys: {missing}")
    return {k: raw[k] for k in required_keys}