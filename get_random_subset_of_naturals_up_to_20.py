import numpy as np


def get_random_subset_of_naturals_up_to_20():
    """
    Replace the code below with your own implementation.
    """
    ### Replace with your own code (begin) ###
    mask = np.random.randint(0, 2**20)
    chosen = []
    for i in range(20):               
        if ((mask >> i) & 1) == 1:
            chosen.append(i + 1)
    return np.array(chosen, dtype=int)
    ### Replace with your own code (end)   ###

print(get_random_subset_of_naturals_up_to_20())
print(get_random_subset_of_naturals_up_to_20())
print(get_random_subset_of_naturals_up_to_20())
