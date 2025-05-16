for i in range(1, 21):
    number = int(input(f"Enter number {i}: "))
    print("Number:", number)

    if number % 2 == 0:
        print("The number is Even")
        if 1 <= number <= 10:
            print("The number lies between the range 1 to 10")
        elif 11 <= number <= 20:
            print("The number lies between the range 11 to 20")
        else:
            print("The number is out of range")
    else:
        print("The number is odd")
        if number < 10:
            print("The number is less than ten")
        else:
            print("The number is greater than 10")