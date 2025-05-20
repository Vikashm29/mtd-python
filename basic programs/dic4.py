'''
Check If a Key Exists: Write a function to check if a given key exists in a dictionary.	
'''

fruits = {
    'a' : 'Apple',
    'b' : 'Banana',
    'c' : 'Coconut' 
}

if fruits.get('d'):
    print('The key exists')
else:
    print('The key does not exists')