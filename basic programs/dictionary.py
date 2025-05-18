data = {
    1: "One",
    2: "Two",
    3: "Three",
    "Hi": "Hello"
}

for key, value in data.items():
    print(value)

print(data.get("Hi")) 

print(data.values())

data.pop("Hi")
print(data)

