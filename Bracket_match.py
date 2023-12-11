def sample(items, n):
    result = []
    for i, item in enumerate(items):
        if i < n:
            result.append(item)
        else:
            j = randint(0, i) # random integer, inclusive
            if j < n:
                # (Fill in the missing line here)
                return result
