# Listing 15.1: Scaled dot-product attention in NumPy
import numpy as np

def softmax(x, axis=-1):
    e = np.exp(x - x.max(axis=axis, keepdims=True))
    return e / e.sum(axis=axis, keepdims=True)

def attention(Q, K, V):
    """Scaled dot-product attention: softmax(QK^T / sqrt(d)) V"""
    d = Q.shape[-1]
    weights = softmax(Q @ K.T / np.sqrt(d))
    return weights @ V, weights
