def string_splosion(str):
    new_str = ''
    for i in range(0,len(str)):
        if i == 0:
            new_str = new_str + str[i]
        else:
            new_str = new_str + str[0:i+1]
    return new_str