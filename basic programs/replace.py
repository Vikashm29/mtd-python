data = ["Apple", "Cherry", "Banana", "Orange", "Mango"]
index = -1

for item in data:
    index += 1
    if item == "Orange":
        data[index] = "Coconut"
    elif item == "Mango":
        data[index] = "Kivi"
    else:
        print("false")

print(data)