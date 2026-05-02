"""Anthropic helper functions with secure defaults and mock-mode fallback."""

from __future__ import annotations

import os
from typing import Optional

from dotenv import load_dotenv


DEFAULT_CLAUDE_MODEL = "claude-sonnet-4-5-20250929"


def load_environment() -> None:
    """Load `.env` without printing credential values."""

    load_dotenv(override=False)


def key_loaded(name: str) -> bool:
    """Return whether an API key exists without exposing the secret."""

    return bool(os.getenv(name))


def live_api_enabled() -> bool:
    """Require LIVE_API=true before live Anthropic calls."""

    return os.getenv("LIVE_API", "false").lower() == "true"


def anthropic_ready() -> bool:
    """Claude calls are allowed only when explicitly enabled and keyed."""

    return live_api_enabled() and key_loaded("ANTHROPIC_API_KEY")


def get_anthropic_client():
    """Create the Anthropic client lazily so notebooks can run without live keys."""

    from anthropic import Anthropic

    return Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def claude_message(
    prompt: str,
    system: Optional[str] = None,
    model: str = DEFAULT_CLAUDE_MODEL,
    max_tokens: int = 1200,
    mock_response: Optional[str] = None,
) -> str:
    """Generate a Claude response, or return a clear mock response."""

    if not anthropic_ready():
        return mock_response or (
            "[MOCK Claude response] LIVE_API is false or ANTHROPIC_API_KEY is missing. "
            "This placeholder keeps provider-comparison lessons runnable."
        )

    client = get_anthropic_client()
    kwargs = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system:
        kwargs["system"] = system

    response = client.messages.create(**kwargs)
    return "".join(
        block.text for block in response.content if getattr(block, "type", None) == "text"
    )


def rewrite_query(question: str, context_hint: str = "") -> str:
    """Use Claude-style prompting to rewrite a query for retrieval."""

    prompt = f"""Rewrite the user question as a precise retrieval query.

Question: {question}
Context hint: {context_hint or "none"}

Return only the rewritten query."""
    return claude_message(
        prompt,
        system="You rewrite vague user questions into concise search queries.",
        mock_response=f"{question} {context_hint}".strip(),
    )


def critique_grounding(question: str, answer: str, evidence: str) -> str:
    """Ask Claude to critique whether an answer is supported by evidence."""

    prompt = f"""Evaluate whether the answer is grounded in the evidence.

Question:
{question}

Answer:
{answer}

Evidence:
{evidence}

Return three short bullets: supported claims, unsupported claims, and improvement."""
    return claude_message(
        prompt,
        system="You are a careful RAG evaluator. Reward answers only when evidence supports them.",
        mock_response=(
            "- Supported claims: mock mode cannot verify live model output.\n"
            "- Unsupported claims: check citations manually.\n"
            "- Improvement: quote or cite the retrieved passage more directly."
        ),
    )
