import numpy as np

def random_unit_vectors(num_vectors, dim):
    """
    Replace the code below with your own implementation.
    """
    ### Replace with your own code (begin) ###
    M = np.random.randn(num_vectors, dim)

    # b) compute Euclidean norm of each row
    row_norms = np.linalg.norm(M, axis=1, keepdims=True)

    # avoid division by 0 (extremely unlikely, but safe)
    row_norms[row_norms == 0] = 1.0

    # normalize each row
    M = M / row_norms

    # c) return the result
    return M
    ### Replace with your own code (end)   ###
    
V = random_unit_vectors(5, 3)
print(V)
print(np.linalg.norm(V, axis=1))
