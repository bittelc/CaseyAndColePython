# https://pythonprinciples.com/challenges/Capital-indexes/

def capital_indexes(word):
    j = []
    for c,v in enumerate(word):
        if v.isupper():
            j.append(c)
    print("elements of uppercase characters: " + str(j))
    return j
