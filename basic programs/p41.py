positive_number = int(input("Enter the number of  positive numbers: "))

unique_numbers = []
print(f'Enter the {positive_number}of unique positive numbers from 0 to {positive_number-1}')
for i in range(positive_number):
    temp_number = int(input())
    unique_numbers.append(temp_number)

print('user given numbers are \n ', unique_numbers)

for i in range(positive_number):
    unique_numbers[i] = i

print(f'the output list is: {unique_numbers}')




