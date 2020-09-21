def front_times(str, n):
    if len(str) <= 2:
        return (str * n)
    else:
        return (str[ :3] * n)
