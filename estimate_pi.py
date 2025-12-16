import numpy as np

def estimate_pi(num_samples):
    """
    Replace the code below with your own implementation.
    """
    ### Replace with your own code (begin) ###
    points = np.random.rand(num_samples, 2)
    
    print(points)
    
    x = points[:, 0]
    y = points[:, 1]

    inside = (x*x + y*y) <= 1

    fraction = inside.mean()

    pi_estimate = 4 * fraction

    return pi_estimate     
    ### Replace with your own code (end)   ###

estimate_pi(5)