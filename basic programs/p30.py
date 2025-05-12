'''
range(1, 101): Generates numbers from 1 to 100.

number % 3 == 0: Checks if the number is divisible by 3.

number % 9 != 0: Ensures the number is not divisible by 9.

print(number): Displays the number if both conditions are met.
'''

for number in range(1, 101):
    if number % 3 == 0 and number % 9 != 0:
        print(number)
