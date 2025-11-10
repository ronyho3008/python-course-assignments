def calculate_dilution(C1, C2, V2_ml):
    """Return V1 and buffer volumes in mL"""
    V1_ml = (C2 * V2_ml) / C1
    buffer_ml = V2_ml - V1_ml
    return V1_ml, buffer_ml
