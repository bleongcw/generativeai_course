"""OpenAI helper functions with secure defaults and mock-mode fallback."""

from __future__ import annotations

import json
import os
from typing import Iterable, List, Optional

from dotenv import load_dotenv

from .retrieval import deterministic_mock_embeddings


DEFAULT_OPENAI_GENERATION_MODEL = "gpt-5.2"
DEFAULT_OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"


def load_environment() -> None:
    """Load `.env` without printing credential values."""

    load_dotenv(override=False)


def key_loaded(name: str) -> bool:
    """Return whether an API key exists without exposing the secret."""

    return bool(os.getenv(name))


def live_api_enabled() -> bool:
    """Require both LIVE_API=true and a key before making paid network calls."""

    return os.getenv("LIVE_API", "false").lower() == "true"


def openai_ready() -> bool:
    """OpenAI calls are allowed only when explicitly enabled and keyed."""

    return live_api_enabled() and key_loaded("OPENAI_API_KEY")


def get_openai_client():
    """Create the OpenAI client lazily so notebooks can run without the package."""

    from openai import OpenAI

    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def embed_texts(
    texts: Iterable[str],
    model: str = DEFAULT_OPENAI_EMBEDDING_MODEL,
    mock_dimensions: int = 32,
) -> List[List[float]]:
    """Embed text with OpenAI, or use deterministic vectors in mock mode."""

    text_list = list(texts)
    if not openai_ready():
        return deterministic_mock_embeddings(text_list, dimensions=mock_dimensions)

    client = get_openai_client()
    response = client.embeddings.create(model=model, input=text_list)
    return [item.embedding for item in response.data]


def generate_text(
    prompt: str,
    model: str = DEFAULT_OPENAI_GENERATION_MODEL,
    instructions: Optional[str] = None,
    mock_response: Optional[str] = None,
) -> str:
    """Generate text with the Responses API, or return a clear mock response."""

    if not openai_ready():
        return mock_response or (
            "[MOCK OpenAI response] LIVE_API is false or OPENAI_API_KEY is missing. "
            "This placeholder keeps the lesson runnable while preserving the API call shape."
        )

    client = get_openai_client()
    response = client.responses.create(
        model=model,
        instructions=instructions,
        input=prompt,
    )
    return response.output_text


def generate_json(
    prompt: str,
    schema_name: str,
    schema: dict,
    model: str = DEFAULT_OPENAI_GENERATION_MODEL,
    mock_payload: Optional[dict] = None,
) -> dict:
    """Request structured JSON from OpenAI, or return deterministic mock JSON."""

    if not openai_ready():
        return mock_payload or {"provider": "openai-mock", "notes": "mock JSON payload"}

    client = get_openai_client()
    response = client.responses.create(
        model=model,
        input=prompt,
        text={
            "format": {
                "type": "json_schema",
                "name": schema_name,
                "schema": schema,
                "strict": True,
            }
        },
    )
    return json.loads(response.output_text)
