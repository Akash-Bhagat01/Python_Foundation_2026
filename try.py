try:
    x = 5
    assert x > 0, "x must be positive"
except AssertionError as e:
    print("Assertion Error:", e)
