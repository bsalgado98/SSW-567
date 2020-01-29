def classify_triangle(a, b, c):
    sides = [a, b, c]
    classification = ""
    for side in sides:
        if sides.count(side) >= 3:
            classification += "equilateral "
            break
        elif sides.count(side) >= 2:
            classification += "isosceles "
            break
        else:
            classification += "scalene "
            break
    if (a**2 + b**2) == c**2:
        classification += "right"
    else:
        classification += "not right"
    return classification