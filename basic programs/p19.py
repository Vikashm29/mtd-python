number_of_line = int(input('Enter number of lines of hollow Rhombus:'))

for i in range(number_of_line):
    print(' ' * (number_of_line-i-1), end='')
    for j in range(number_of_line):
        if i == 0 or i == number_of_line-1 or j == 0 or j == number_of_line-1:
            print('* ', end=' ')
        else:
            print('  ', end=' ')
    print()
            