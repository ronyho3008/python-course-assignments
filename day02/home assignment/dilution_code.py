def dilution_calculator(C1, C2, V2):
    """Calculate V1 (volume of stock) and Vbuffer (diluent) in ml.

    Inputs are expected in the same concentration units for C1/C2 and V2 in ml.
    """
    if C1 == 0:
        raise ValueError("Original concentration (C1) must be non-zero")
    V1 = (C2 * V2) / C1
    Vbuffer = V2 - V1
    return V1, Vbuffer

def get_unit_multiplier(unit):
    if unit == "ml":
        return 1
    elif unit == "ul" or unit == "µl":
        return 0.001  # converting µl to ml
    elif unit == "l" or unit == "litre" or unit == "liter":
        return 1000.0  # L to ml
    else:
        raise ValueError("Unit must be one of: ml, µl (or ul), l")

##

import sys


def main():
    ## Input
    try:
        C1 = float(input("original concentration: "))
        C2 = float(input("final concentration: "))
    except ValueError:
        print("Please enter numeric values for concentrations.")
        sys.exit(1)

    # prompt for units, normalize the user input
    unit = input("units like - ml, µl, L...: ").strip().lower()
    try:
        V2 = float(input(f"final volume ({unit})? "))
    except ValueError:
        print("Please enter a numeric value for volume.")
        sys.exit(1)

    # change volume to ml
    try:
        multiplier = get_unit_multiplier(unit)
    except ValueError as e:
        print(e)
        sys.exit(1)

    V2_ml = V2 * multiplier

    # calculate dilution
    try:
        V1, Vbuffer = dilution_calculator(C1, C2, V2_ml)
    except Exception as e:
        print(f"Calculation error: {e}")
        sys.exit(1)

    # convert back to original units
    V1_out = V1 / multiplier
    Vbuffer_out = Vbuffer / multiplier

    # output
    print(f"solution volume : {V1_out:.2f} {unit}")
    print(f"buffer volume : {Vbuffer_out:.2f} {unit}")


if __name__ == "__main__":
    main()
