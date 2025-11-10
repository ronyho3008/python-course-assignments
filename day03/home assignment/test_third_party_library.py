from third_party_library import calculate_dilution

def test_dilution_normal():
    V1, buffer = calculate_dilution(10, 2, 5)  # C1=10, C2=2, V2=5 mL
    assert round(V1, 6) == 1.0   # הציפייה: V1 = 1 mL
    assert round(buffer, 6) == 4.0  # הציפייה: buffer = 4 mL

def test_dilution_equal_concentrations():
    V1, buffer = calculate_dilution(5, 5, 10)
    assert V1 == 10
    assert buffer == 0

def test_dilution_zero_final():
    V1, buffer = calculate_dilution(5, 0, 10)
    assert V1 == 0
    assert buffer == 10
