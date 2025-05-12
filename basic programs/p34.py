'''
range(1, 11): Generates numbers from 1 to 10, representing each cycle.

cycle % 3 == 0: Checks if the cycle number is divisible by 3. If true, it prints "Red".

elif cycle % 5 == 0: If the cycle number is not divisible by 3 but is divisible by 5, it prints "Green".

else: For all other cycle numbers, it prints "Yellow".

'''

for cycle in range(1, 11):
    if cycle % 3 == 0:
        print(f"Cycle {cycle}: Red")
    elif cycle % 5 == 0:
        print(f"Cycle {cycle}: Green")
    else:
        print(f"Cycle {cycle}: Yellow")
