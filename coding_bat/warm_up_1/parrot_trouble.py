def parrot_trouble(talking, hour):
    if talking and (hour in range(0,7) or hour in range(21,24)):
        return True
    else:
        return False