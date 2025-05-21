'''
    Method	        Description

1.  clear()->	    Removes all the elements from the dictionary

2.  copy()->	    Returns a copy of the dictionary

3.  fromkeys()->	Returns a dictionary with the specified keys and value

4.  get()->	        Returns the value of the specified key

5.  items()->	    Returns a list containing a tuple for each key value pair

6.  keys()->	    Returns a list containing the dictionary's keys

7.  pop()->	        Removes the element with the specified key

8.  popitem()->	    Removes the last inserted key-value pair

9.  setdefault()->	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

10. update()->	    Updates the dictionary with the specified key-value pairs

11. values()->	    Returns a list of all the values in the dictionary
'''

# get() method.
d = {'Name': 'Vikas', 'Age': '19', 'Country': 'India'}
print(d.get('Name'))
print(d.get('Gender'))

# items() method.
d = {'Name': 'Vikas', 'Age': '19', 'Country': 'India'}
print(tuple(d.items())[0][1])
print(tuple(d.items())[0][0])

# keys() method.
d = {'Name': 'Vikas', 'Age': '19', 'Country': 'India'}
print(list(d.keys()))

# update() method.
d1 = {'Name': 'Vikas', 'Age': '19', 'Country': 'India'}
d2 = {'Name': 'shivu', 'Age': '22'}

d1.update(d2)
print(d1)

# values() method.
d = {'Name': 'Vikas', 'Age': '19', 'Country': 'India'}
print(list(d.values()))

# pop() method.
d = {'Name': 'Vikas', 'Age': '19', 'Country': 'India'}
d.pop('Age')
print(d)

# popitem() method.
d = {1: 'Vikas', 2: 'Shivu', 3: 'Darshan'}
res = d.popitem()
print(res)
print(d)

# copy() method.
d = {1:'Vikas', 2:'Shivu'}
d3 = d.copy()

1# setdefault() method.
d = {1: 'Vikas', 2: 'Shivu', 3: 'Darshan'}
d.setdefault('', 'Ravi')
print(d)