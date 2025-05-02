number_of_line = int(input('Enter number of lines of X: '))
 
for i in range(1,number_of_line+1):
    for j in range(1,number_of_line+1):
        if(i == j or j == number_of_line - i + 1 ):
           print('*', end='')
        else:
           print(' ',end=' ')
    print()
