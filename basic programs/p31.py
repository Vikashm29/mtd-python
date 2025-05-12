'''
for i in range(1, 51):
This loop iterates over numbers from 1 to 50.

if i % 5 == 0:
The modulo operator (%) calculates the remainder when i is divided by 5. If the remainder is 0, it means i is divisible by 5.

print("Discount")
If the condition is true (i.e., i is divisible by 5), it prints "Discount".

else:
If the condition is false (i.e., i is not divisible by 5), it proceeds to the else block.

print(i)
In the else block, it prints the number i itsel
'''

for i in range(1, 51):
    if i % 5 == 0:
        print("Discount")
    else:
        print(i)
