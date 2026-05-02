# Sample Course Corpus

## Transformer Architecture

Transformers process text by turning tokens into vectors, then using self-attention
to let each token gather information from other tokens. Queries, keys, and values
are learned projections of token vectors. Attention weights decide how strongly
one token should use information from another token.

## Embeddings And Similarity

An embedding is a numerical representation of text. Similar ideas should land
near each other in vector space, which lets applications use cosine similarity
to retrieve relevant passages. Classical methods such as bag of words and TF-IDF
count terms directly, while neural embedding models learn dense vectors.

## Retrieval Augmented Generation

Retrieval augmented generation combines search with generation. The system chunks
documents, embeds the chunks, retrieves passages for a user question, and asks a
language model to answer using that evidence. A strong RAG system checks whether
citations support the answer and handles missing evidence by saying it does not
know.

## Provider Capability Differences

OpenAI provides first-party embedding models as well as generation and evaluation
models. Anthropic provides Claude models for generation, reasoning, tool use,
query rewriting, critique, and evaluation, but it does not currently provide a
first-party embeddings API. Anthropic documentation points developers to external
embedding providers such as Voyage AI when vectors are needed.

## API Key Security

API keys are credentials and should be treated like passwords. Students should
store them in a local `.env` file, never print them in notebooks, never paste
them into shared documents, and never commit them to GitHub.
