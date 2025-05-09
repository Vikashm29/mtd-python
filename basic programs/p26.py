'''
A traffic system checking if signal is red and speed is greater than 60 then fine will be issued, if signal is red and speed is less than or equal to 60 then person gets a warning if signal is green all clear

Inputs:
1.Signal
2.Speed

Case1:
Signal = red
Speed = 65

>Signal = red : true
>Speed > 60 : true
pays fine

Case2:
Signal = red
speed = 55

>Signal =red : true
>Signal <= 60 : true
leaves with a warning

Case3:
Signal = green
all clear
'''
signal = input("Enter colour:").lower()
speed = int(input("Enter speed:"))

if signal == 'red':
    if speed > 60:
        print("You have a fine issued")
    else:
        print("You have a warning issued")
        
elif signal == 'green':
    print("All clear")
else:
    print("Invalid colour")