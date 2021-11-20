def score(x, y):
    distance = (x * x + y * y)**0.5
    if distance > 10:
        return 0
    elif distance > 5:
        return 1
    elif distance > 1:
        return 5
    else:
        return 10

