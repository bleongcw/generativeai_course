"""Retrieval utilities kept intentionally small for teaching.

These functions are not trying to be a production vector database. They expose
the core mechanics students need to understand before they use managed search
systems: chunking, vector normalization, cosine similarity, and top-k ranking.
"""

from __future__ import annotations

import hashlib
import math
import re
from collections import Counter
from typing import Iterable, List, Sequence

import numpy as np

from .schemas import Document, RetrievedPassage, TextChunk


def tokenize_words(text: str) -> List[str]:
    """Return lowercase word tokens for simple classroom examples."""

    return re.findall(r"[a-zA-Z0-9']+", text.lower())


def approximate_token_count(text: str) -> int:
    """Estimate token count when tokenizer packages are not installed.

    English text often averages roughly four characters per token. This is only
    a teaching approximation; provider tokenizers should be used for billing.
    """

    return max(1, math.ceil(len(text) / 4))


def chunk_documents(
    documents: Sequence[Document],
    chunk_size_words: int = 80,
    overlap_words: int = 20,
) -> List[TextChunk]:
    """Split documents into overlapping word chunks for retrieval.

    Overlap preserves context that might otherwise be lost at chunk boundaries.
    The function records source metadata so answers can cite retrieved passages.
    """

    if chunk_size_words <= 0:
        raise ValueError("chunk_size_words must be positive")
    if overlap_words < 0 or overlap_words >= chunk_size_words:
        raise ValueError("overlap_words must be >= 0 and smaller than chunk_size_words")

    chunks: List[TextChunk] = []
    step = chunk_size_words - overlap_words

    for doc in documents:
        words = doc.text.split()
        for start in range(0, len(words), step):
            window = words[start : start + chunk_size_words]
            if not window:
                continue
            end = start + len(window)
            chunks.append(
                TextChunk(
                    chunk_id=f"{doc.doc_id}-chunk-{len(chunks)+1}",
                    doc_id=doc.doc_id,
                    title=doc.title,
                    text=" ".join(window),
                    source=doc.source,
                    start_word=start,
                    end_word=end,
                )
            )
            if end >= len(words):
                break

    return chunks


def cosine_similarity(left: Sequence[float], right: Sequence[float]) -> float:
    """Compute cosine similarity between two vectors."""

    a = np.array(left, dtype=float)
    b = np.array(right, dtype=float)
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)


def rank_chunks(
    query_embedding: Sequence[float],
    chunk_embeddings: Sequence[Sequence[float]],
    chunks: Sequence[TextChunk],
    top_k: int = 3,
) -> List[RetrievedPassage]:
    """Rank chunks by vector similarity and return the top matches."""

    if len(chunk_embeddings) != len(chunks):
        raise ValueError("chunk_embeddings and chunks must have the same length")

    scored = [
        (cosine_similarity(query_embedding, embedding), chunk)
        for embedding, chunk in zip(chunk_embeddings, chunks)
    ]
    scored.sort(key=lambda item: item[0], reverse=True)

    return [
        RetrievedPassage(chunk=chunk, score=score, rank=rank)
        for rank, (score, chunk) in enumerate(scored[:top_k], start=1)
    ]


def bag_of_words_vectors(texts: Sequence[str]) -> tuple[list[str], list[list[float]]]:
    """Create simple count vectors so students can see pre-neural retrieval."""

    vocabulary = sorted({token for text in texts for token in tokenize_words(text)})
    vectors = []
    for text in texts:
        counts = Counter(tokenize_words(text))
        vectors.append([float(counts.get(token, 0)) for token in vocabulary])
    return vocabulary, vectors


def deterministic_mock_embedding(text: str, dimensions: int = 32) -> List[float]:
    """Create a stable pseudo-embedding for offline classroom runs.

    The hash trick gives semantically weaker vectors than real embeddings, but it
    keeps the shape of the retrieval pipeline runnable without credentials.
    """

    vector = np.zeros(dimensions, dtype=float)
    for token in tokenize_words(text):
        digest = hashlib.sha256(token.encode("utf-8")).digest()
        index = int.from_bytes(digest[:4], "big") % dimensions
        sign = 1.0 if digest[4] % 2 == 0 else -1.0
        vector[index] += sign

    norm = np.linalg.norm(vector)
    if norm:
        vector = vector / norm
    return vector.tolist()


def deterministic_mock_embeddings(texts: Iterable[str], dimensions: int = 32) -> List[List[float]]:
    """Embed many texts with the deterministic mock embedding function."""

    return [deterministic_mock_embedding(text, dimensions=dimensions) for text in texts]
