'''
conditions:
1) Iftemperature is >=40 it is very hot
2) Iftemperature is >=30 and <40 it will be hot
3) Iftemperature is >=20 and <30 it will be warm
4) Iftemperature is >=10 and <20 it is cool
5) Iftemperature is <10 then it is cold
6) Iftemperature is equal to 0 the it is freezing cold

Tracing:
1) temperature = 0
if temperature == 0: >True
Output: "Weather is Freezing Cold"

2) temperature = 5
if temperature == 0: >false
if temperature > 0 and temperature < 10: >True
Output: "Weather is Cold"

3) temperature = 15
temperature == 0: >false
temperature > 0 and < 10: >false
temperature >= 10 and < 20: >true

Output: "Weather is Cool"

4) temperature = 25
All above conditions > false
temperature >= 20 and < 30: > true
Output: "Weather is Warm"

5) temperature = 35
All above >false
temperature >= 30 and < 40: > true
Output: "Weather is Hot"

6) temperature = 45
All above> false
temperature >= 40: > true
Output: "Weather is Very Hot"

7) temperature = 9
temperature > 0 and < 10: > true
Output: "Weather is Cold
'''

temperature = float(input(f"Enter the temperature of the day: "))

for i in range(1, 8):
    if temperature == 0:
        print("Weather is Freezing Cold")
    elif temperature > 0 and temperature < 10:
        print("Weather is Cold")
    elif temperature >= 10 and temperature < 20:
        print("Weather is Cool")
    elif temperature >= 20 and temperature < 30:
        print("Weather is Warm")
    elif temperature >= 30 and temperature < 40:
        print("Weather is Hot")
    else:
        print("Weather is Very Hot")
    break
