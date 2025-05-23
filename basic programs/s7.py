matrix = [[1, 2], [3, 4], [5, 6]]

#combining row and column
flat = [num for row in matrix for num in row]

print(flat)