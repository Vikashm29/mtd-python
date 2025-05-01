user_number = int(input('Enter the number of multiplication table:'))

for i in range(1 , 11):
    result = user_number * i
    print(f'{user_number} * {i} = {result}')