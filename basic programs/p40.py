import math

number_of_customers = int(input("Enter the number of cumstomers: "))

bill_amounts = []
count_of_discounted_bills = 0
for i in range (number_of_customers):
    bill_amount = int(input(f'Enter the bill amount of the coustomre-{i+1}: '))
    bill_amounts.append(bill_amount)
    sqrt_root = int(math.sqrt(bill_amount))
    if bill_amount == sqrt_root * sqrt_root:
       count_of_discounted_bills += 1
print(f"Number of customers eligible for promotional discount is : {count_of_discounted_bills} ")      