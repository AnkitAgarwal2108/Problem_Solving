def diff21(n):
    if n <= 21:
        diff = 21-n
    else:
        diff = (21-n) * 2
    return abs(diff)