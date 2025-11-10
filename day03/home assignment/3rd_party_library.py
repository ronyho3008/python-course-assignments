import numpy as np

def calculate_dilution(C1, C2, V2_ml):
    V1_ml = np.divide(C2 * V2_ml, C1)
    buffer_ml = np.subtract(V2_ml, V1_ml)
    return V1_ml, buffer_ml
