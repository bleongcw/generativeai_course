from nlp_transformers_embeddings.utils.mock_data import SAMPLE_DOCUMENTS
from nlp_transformers_embeddings.utils.retrieval import (
    chunk_documents,
    cosine_similarity,
    deterministic_mock_embedding,
    rank_chunks,
)
from nlp_transformers_embeddings.utils.schemas import TextChunk


def test_chunk_documents_creates_metadata():
    chunks = chunk_documents(SAMPLE_DOCUMENTS[:1], chunk_size_words=12, overlap_words=3)
    assert chunks
    assert chunks[0].doc_id == "doc-transformers"
    assert chunks[0].start_word == 0
    assert chunks[0].end_word <= 12


def test_cosine_similarity_identity():
    assert cosine_similarity([1, 0, 0], [1, 0, 0]) == 1.0


def test_rank_chunks_returns_top_match_shape():
    chunks = [
        TextChunk(chunk_id="a", doc_id="d", title="A", text="transformer attention"),
        TextChunk(chunk_id="b", doc_id="d", title="B", text="api key security"),
    ]
    embeddings = [deterministic_mock_embedding(chunk.text) for chunk in chunks]
    query = deterministic_mock_embedding("attention in transformer models")
    ranked = rank_chunks(query, embeddings, chunks, top_k=1)
    assert ranked[0].rank == 1
    assert -1.0 <= ranked[0].score <= 1.0


def test_schema_rejects_empty_chunk_text():
    try:
        TextChunk(chunk_id="bad", doc_id="d", title="Bad", text=" ")
    except ValueError as exc:
        assert "chunk text cannot be empty" in str(exc)
    else:
        raise AssertionError("empty chunk text should fail validation")
