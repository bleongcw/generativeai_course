"""Shared data contracts for the NLP, embeddings, and RAG notebooks.

The notebooks use these models to make invisible LLM data flow visible:
documents become chunks, chunks become retrieved passages, and passages become
grounded answers with citations and evaluation scores.
"""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, field_validator


class Document(BaseModel):
    """A source document before it is split into chunks."""

    doc_id: str
    title: str
    text: str
    source: str = "course"


class TextChunk(BaseModel):
    """A retrieval-sized text segment derived from a document."""

    chunk_id: str
    doc_id: str
    title: str
    text: str
    source: str = "course"
    start_word: int = 0
    end_word: int = 0

    @field_validator("text")
    @classmethod
    def text_must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("chunk text cannot be empty")
        return value


class RetrievedPassage(BaseModel):
    """A chunk returned by semantic search with a similarity score."""

    chunk: TextChunk
    score: float = Field(ge=-1.0, le=1.0)
    rank: int = Field(ge=1)


class GroundedAnswer(BaseModel):
    """A model answer that should be supported by retrieved passages."""

    provider: str
    question: str
    answer: str
    citations: List[str] = Field(default_factory=list)
    confidence: Optional[float] = Field(default=None, ge=0.0, le=1.0)


class EvaluationScore(BaseModel):
    """A compact rubric score for RAG outputs."""

    evaluator: str
    faithfulness: float = Field(ge=0.0, le=1.0)
    relevance: float = Field(ge=0.0, le=1.0)
    citation_quality: float = Field(ge=0.0, le=1.0)
    notes: str
