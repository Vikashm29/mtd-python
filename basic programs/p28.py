Employee_details = [
    {'employee': 'emp1' , 'experience': 2 }, 
    {'employee': 'emp2' , 'experience': 1 },
    {'employee': 'emp3' , 'experience': 5 },
    {'employee': 'emp4' , 'experience': 4 },
    {'employee': 'emp5' , 'experience': 3 },
    {'employee': 'emp6' , 'experience': 2 },
]


for i in Employee_details :
    if i ['experience'] > 2:
       print(f' employee , {i['employee']} got bouns')
