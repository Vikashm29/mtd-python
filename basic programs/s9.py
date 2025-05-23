original = {'a': 1, 'b': 2, 'c': 3}

#inverting the dictionary
inverted = {v: k for k, v in original.items()}

print(inverted)