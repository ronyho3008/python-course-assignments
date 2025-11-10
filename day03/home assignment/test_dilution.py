from dilution_logic import calculate_dilution

def test_simple_dilution():
    V1, buffer = calculate_dilution(10, 1, 2)
    assert round(V1, 2) == 0.2
    assert round(buffer, 2) == 1.8

def test_half_concentration():
    V1, buffer = calculate_dilution(4, 2, 10)
    assert round(V1, 2) == 5.0
    assert round(buffer, 2) == 5.0
