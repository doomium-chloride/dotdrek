import numpy as np

def build_chance(rate, builds):
    other_rate = np.power(1 - rate, builds)
    return 1 - other_rate