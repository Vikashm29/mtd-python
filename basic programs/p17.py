number_of_line = int(input('Enter number of line in x in a hollow square:'))
if number_of_line < 3 or number_of_line % 2 == 0:
     print("Please enter an odd number greater than or equal to 3.")

for i in range(number_of_line):
        for j in range(number_of_line):
            if i == 0 or i == number_of_line - 1 or j == 0 or j == number_of_line - 1:
                print('*', end='')
            elif i == j or i + j == number_of_line - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

'print_hollow_square_with_x',(number_of_line)
