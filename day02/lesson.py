def circle_area(radius, pi=3.14):
    # בדיקה שהרדיוס חיובי
    if radius <= 0:
        return "Radius must be a positive number"

    area = pi * (radius ** 2)
    return area
print(circle_area(5))  # Output: 78.5


def square_area(side_length):
    # בדיקה שהאורך חיובי
    if side_length <= 0:
        return "Side length must be a positive number"

    area = side_length ** 2
    return area

print(square_area(4))
