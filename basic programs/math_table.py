number_of_line = int(input('Enter number of lines of the Triangle: '))

for i in range(1, number_of_line+1 ):
    print(' ' * ( number_of_line - i), end='')
    print('@' * (2*i-1))

     