number_of_line = int(input('Enter number of lines of the Square: '))

for i in range(1 , number_of_line+1):
    if i == 1 or i == number_of_line:
       print('* ' * number_of_line)
else:
    print('* ' + (' ' * ((number_of_line-2) * 2)) + '*')