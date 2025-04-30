input_number = int(input('Enter the year:'))

if input_number % 4  == 0 or input_number % 100 == 0 or input_number % 400 == 0 :
    print (input_number, 'is a leap year')
else:
    print(f'{input_number} is not a leap year')