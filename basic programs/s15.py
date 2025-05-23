keys = ['name', 'age']
values = ['Shivu', 21]

#creating dictionary from keys and values
profile = {k: v for k, v in zip(keys, values)}

print(profile)