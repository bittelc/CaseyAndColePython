def online_count(dict):
    total = 0
    for v in dict.values():
        if v == "online":
            total += 1
    return total
