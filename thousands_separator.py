def format_number(nmbr):
    arrayed = list(str(nmbr))
    counter = 0

    for i,v in reversed(list(enumerate(arrayed))):
        counter = counter + 1
        if counter == 3 and i != 0:
            arrayed.insert(i,",")
            counter = 0

    return ''.join(arrayed)
