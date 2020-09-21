def string_bits(str):
    new_str = ''
    for i in range(0, len(str)):
        if i % 2 == 0:
            new_str = new_str + str[i]
    return new_str

