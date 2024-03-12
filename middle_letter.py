import math

def mid(s):
    print("word is: " + s)
    length = len(s)
    if length % 2 == 0:
        return ""
    middle_index = math.floor(length / 2)
    return s[middle_index]