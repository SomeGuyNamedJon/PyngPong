import numpy as np

def smoothMap(n, a, b):
    k = (n/a) * b
    return k

def normalizeVector(vector):
    (vx, vy) = vector
    u = np.sqrt(vx**2 + vy**2)
    
    if u == 0:
        return (0, 0)
    else:
        return (vx/u, vy/u)