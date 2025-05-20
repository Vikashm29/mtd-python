'''
1)  append(): Adds an element to the end of the list.
2)  copy(): Returns a shallow copy of the list.
3)  clear(): Removes all elements from the list.
4)  count(): Returns the number of times a specified element appears in the list.
5)  extend(): Adds elements from another list to the end of the current list.
6)  index(): Returns the index of the first occurrence of a specified element.
7)  insert(): Inserts an element at a specified position.
8)  pop(): Removes and returns the element at the specified position (or the last element if no index is specified).
9)  remove(): Removes the first occurrence of a specified element.
10) reverse(): Reverses the order of the elements in the list.
11) sort(): Sorts the list in ascending order (by default).

'''
# WORKOUT

a = [1,2,3,4,5]
print(a)

a.append(6)
print(a)

b = a.copy()
print(b)

# a.clear()
# print(a)

print(a.count(2))

