import hw01

def test_classify_triangle():
    assert hw01.classify_triangle(3, 4, 5) == "scalene right"
    assert hw01.classify_triangle(10, 10, 10) == "equilateral not right"
    assert hw01.classify_triangle(10, 10, 9) == "isosceles not right"
    assert hw01.classify_triangle(0.256, 400, 0.256) == "isosceles not right"
    assert hw01.classify_triangle(0, -1, -2) == "scalene not right"
    assert hw01.classify_triangle(-21, -28, -35) == "scalene right"
    assert hw01.classify_triangle(3.99999999, 4.99999999, 5.99999999) == "scalene not right"
    assert hw01.classify_triangle(2.99999999, 3.99999999, 4.99999999) == "scalene not right"