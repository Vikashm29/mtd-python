'''
range(1, 101): Generates numbers from 1 to 100, representing each participant.

participant % 10 == 0: Checks if the participant number is divisible by 10. If true, the participant is marked as "VIP".

else: For all other participants, the label "Regular" is assigned
'''

for participant in range(1, 101):
    if participant % 10 == 0:
        print("participant : VIP")
    else:
        print("participant : Regular")
