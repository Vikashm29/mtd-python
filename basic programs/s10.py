prices = {"apple": 2, "banana": 1, "cherry": 3}

#filtering by values
cheap = {k: v for k, v in prices.items() if v <= 2}

print(cheap)