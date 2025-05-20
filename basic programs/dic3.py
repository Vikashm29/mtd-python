'''
Modify a Dictionary: Add a new key-value pair, update an existing key, and delete a key.
'''

fruits = {
    'a' : 'Apple',
    'b' : 'Banana',
    'c' : 'Coconut' 
}

print(fruits)

fruits['d'] = 'Dragon Fruit'
print(fruits)

fruits.update({'a' : 'Avocado'})
print(fruits)

fruits.pop('c')
print(fruits)