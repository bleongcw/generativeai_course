"""Visualization helpers for embeddings and attention lessons."""

from __future__ import annotations

from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np


def softmax(values: Sequence[float]) -> np.ndarray:
    """Stable softmax for attention demonstrations."""

    arr = np.array(values, dtype=float)
    shifted = arr - np.max(arr)
    exp = np.exp(shifted)
    return exp / exp.sum()


def scaled_dot_product_attention(query, keys, values):
    """Compute one small attention step for classroom visualization."""

    query = np.array(query, dtype=float)
    keys = np.array(keys, dtype=float)
    values = np.array(values, dtype=float)
    scale = np.sqrt(keys.shape[-1])
    scores = keys @ query / scale
    weights = softmax(scores)
    output = weights @ values
    return scores, weights, output


def plot_similarity_matrix(labels: Sequence[str], matrix, title: str = "Similarity"):
    """Plot a labeled matrix without hiding the numerical concept."""

    fig, ax = plt.subplots(figsize=(8, 5))
    im = ax.imshow(matrix, cmap="viridis")
    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_yticklabels(labels)
    ax.set_title(title)
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    return fig, ax


def plot_attention(tokens: Sequence[str], weights, title: str = "Attention weights"):
    """Visualize how strongly one token attends to the others."""

    fig, ax = plt.subplots(figsize=(7, 2.5))
    ax.bar(tokens, weights)
    ax.set_ylim(0, 1)
    ax.set_ylabel("weight")
    ax.set_title(title)
    fig.tight_layout()
    return fig, ax
