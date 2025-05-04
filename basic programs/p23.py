'''
-->if seats are availble the system confirms the booking and notified.
-->if seats are filled the system add the booking in the waiting list.
-->the system holds the all the waiting list passengers details for seat availablilty.Ensuring that htey can prioritized if seat is vacant.
-->the system confirms the waiting passengers about their seat confirmation.

==<
if seat is available = booking confirmed
if seat is unavilable = waiting list
and show the status of the waiting list 
'''
book_ticket = input('if seats are available or unavailable then it is (confirmed or waiting list):')

if book_ticket == 'confirmed' and book_ticket == 'waiting list': 
    print('The seats are avilable')
else:
    print('The seats are not available')

show_status = input('Enter the book_ticket status:')
if show_status == 'confirmed' or show_status == 'waiting list': 
    print('confirmed')
else:
    print('not confirmed')