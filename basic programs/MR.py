data = ["Apple", "Cherry", "Banana", "Orange", "Mango"]
change ={
    "Apple": "Apple 2",
    "Orange": "Oange 2"
}
print(data)

for find, change_value in change.items():
    index = -1
    for item in data:
        index = index + 1
        if item == find:
            data[index] = change_value

print(data)