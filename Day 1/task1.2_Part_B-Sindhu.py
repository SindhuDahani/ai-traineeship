import math
import random
import numpy as np


def dot_product(a, b):
    """ Example:
    [1,2,3] · [4,5,6]
    = 1*4 + 2*5 + 3*6
    = 32"""
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length.")

    total = 0.0

    for i in range(len(a)):
        total += a[i] * b[i]

    return total


def magnitude(v):
    """
    Length of a vector.

    sqrt(x1² + x2² + ... + xn²)
    """
    sum_of_squares = 0.0

    for value in v:
        sum_of_squares += value * value

    return math.sqrt(sum_of_squares)


def cosine_similarity(a, b):
    """
    Measures how similar two vectors point in direction.

    1   -> same direction
    0   -> unrelated / perpendicular
    -1  -> opposite direction

    This is the core operation later used in
    embeddings and RAG retrieval.
    """
    mag_a = magnitude(a)
    mag_b = magnitude(b)

    if mag_a == 0 or mag_b == 0:
        raise ValueError("Cosine similarity is undefined for zero vectors.")

    return dot_product(a, b) / (mag_a * mag_b)


def mean(v):
    if len(v) == 0:
        raise ValueError("Cannot calculate mean of an empty vector.")

    total = 0.0

    for value in v:
        total += value

    return total / len(v)


def variance(v):
    if len(v) == 0:
        raise ValueError("Cannot calculate variance of an empty vector.")

    avg = mean(v)

    squared_difference_sum = 0.0

    for value in v:
        difference = value - avg
        squared_difference_sum += difference * difference

    return squared_difference_sum / len(v)



# Verification against NumPy


TOLERANCE = 1e-9

for test_num in range(100):

    size = random.randint(2, 20)

    a = [random.uniform(-100, 100) for _ in range(size)]
    b = [random.uniform(-100, 100) for _ in range(size)]

    # Dot Product Test
    mine = dot_product(a, b)
    numpy_result = np.dot(a, b)

    assert abs(mine - numpy_result) < TOLERANCE

    # Magnitude Test
    mine = magnitude(a)
    numpy_result = np.linalg.norm(a)

    assert abs(mine - numpy_result) < TOLERANCE

    # Cosine Similarity Test
    mine = cosine_similarity(a, b)
    numpy_result = np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )

    assert abs(mine - numpy_result) < TOLERANCE

    # Mean Test
    mine = mean(a)
    numpy_result = np.mean(a)

    assert abs(mine - numpy_result) < TOLERANCE

    # Variance Test
    mine = variance(a)
    numpy_result = np.var(a)

    assert abs(mine - numpy_result) < TOLERANCE


print("✅ All 100 test cases passed within 1e-9 tolerance.")

print("Hello chanes")