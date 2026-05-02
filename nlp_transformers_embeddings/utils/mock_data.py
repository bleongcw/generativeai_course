"""Small deterministic data sets used when live API keys are unavailable."""

from __future__ import annotations

from .schemas import Document


SAMPLE_DOCUMENTS = [
    Document(
        doc_id="doc-transformers",
        title="Transformer Architecture",
        source="course-note",
        text=(
            "Transformers process text by turning tokens into vectors, then using "
            "self-attention to let each token gather information from other tokens. "
            "Queries, keys, and values are learned projections of token vectors. "
            "Attention weights decide how strongly one token should use information "
            "from another token. Multi-head attention repeats this pattern in several "
            "representation spaces so the model can track syntax, meaning, and task "
            "signals at the same time."
        ),
    ),
    Document(
        doc_id="doc-embeddings",
        title="Embeddings And Similarity",
        source="course-note",
        text=(
            "An embedding is a numerical representation of text. Similar ideas should "
            "land near each other in vector space, which lets applications use cosine "
            "similarity to retrieve relevant passages. Classical methods such as bag "
            "of words and TF-IDF count terms directly, while neural embedding models "
            "learn dense vectors that capture broader semantic relationships."
        ),
    ),
    Document(
        doc_id="doc-rag",
        title="Retrieval Augmented Generation",
        source="course-note",
        text=(
            "Retrieval augmented generation, or RAG, combines search with generation. "
            "The system chunks documents, embeds the chunks, retrieves passages for a "
            "user question, and asks a language model to answer using that evidence. "
            "A strong RAG system checks whether citations support the answer and "
            "handles missing evidence by saying it does not know."
        ),
    ),
    Document(
        doc_id="doc-provider-differences",
        title="Provider Capability Differences",
        source="course-note",
        text=(
            "OpenAI provides first-party embedding models as well as generation and "
            "evaluation models. Anthropic provides Claude models for generation, "
            "reasoning, tool use, query rewriting, critique, and evaluation, but it "
            "does not currently provide a first-party embeddings API. Anthropic "
            "documentation points developers to external embedding providers such as "
            "Voyage AI when vectors are needed."
        ),
    ),
    Document(
        doc_id="doc-security",
        title="API Key Security",
        source="course-note",
        text=(
            "API keys are credentials and should be treated like passwords. Students "
            "should store them in a local .env file, never print them in notebooks, "
            "never paste them into shared documents, and never commit them to GitHub. "
            "Course notebooks should show only whether a key is loaded, not the key "
            "value itself."
        ),
    ),
]


MOCK_EMBEDDING_DIMENSIONS = 32
