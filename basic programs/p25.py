'''
a weather alert system that gives warnings based on current temperature.
>If temp is greater than 40°c then it's a heat wave.
>If temp is lower than 0°c then it's a cold wave.
>For any other temp input then it's normal temp.
--------
1) 35.9°c
35.9 > 40 = false
35.9<0 = false
normal temperature

2)52.5
52.5 > 40 = true
heat wave.
'''
temperatue = float(input("Enter the temperature:"))

if temperatue > 40:
    print("Heat wave")
elif temperatue < 0:
    print("Cold wave")
else:
    print("Normal weather")