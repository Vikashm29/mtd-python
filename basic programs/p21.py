age = int(input('Enter the age (0 to 100):'))

if age < 12:
    print('\n The viwer is child the ticket price is free ')
elif age >= 12 or age < 18:
    print('\n The viwer is teenager the ticket price is rs.100' )
elif age >= 18 or age <= 60:
    print('\n The viwer is adult the ticket price is rs.150')
else:
    print('\n The age out of range')