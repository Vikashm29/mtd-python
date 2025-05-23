""" Scenario 2: Inventory Management for a Store 

# You run a store. Your inventory is stored in a dictionary where:
 #- keys = item names
#- values = quantity in stock
 # Tasks:
 #- Add a new item to the inventory
 #- Update stock after a purchase
 #- Display items with stock less than 5 """


fruits = {
    'Apple' : 5,
    'Banana' : 9,
    'Coconut' : 11
}

fruits['Strawberry'] = 6
print(fruits)