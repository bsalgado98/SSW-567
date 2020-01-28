def classify_triangle(a, b, c):
    sides = [a, b, c]
    classification = ""
    for side in sides:
        if sides.count(side) >= 3:
            classification += "equilateral "
        elif sides.count(side) >= 2:
            classification += "isosceles "
        else:
            classification += "scalene "
    if (a**2 + b**2) == c**2:
        classification += "right"
    else:
        classification += "not right"
    return classification
print(classify_triangle(3, 4, 5))