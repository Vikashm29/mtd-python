#program to check if a number is a positive or negative or zero

print('Enter the input number')
input_number = int(input())
 
if input_number > 0:
    print(input_number,'is positive')
    elif input_number < 0:
        print(f'{input_number} is negstive')
else:
    print('The input number is zero')