size = int(input("Enter the size of the X (odd number >= 3): "))

if size < 3 or size % 2 == 0:
    print("Size must be an odd number greater than or equal to 3.")
else:
    for i in range(size):
        line = [' '] * size
        line[i] = '*'                # Main diagonal
        line[size - 1 - i] = '*'     # Secondary diagonal
        print(''.join(line))
