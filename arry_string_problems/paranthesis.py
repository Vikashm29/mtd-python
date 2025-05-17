paranthesis = input('Enter a string of paranthesis:')

open_count = 0
close_count = 0
for char in paranthesis:
    if char == '(':
        open_count += 1
    else:
        close_count += 1
    if close_count > open_count:
        break
if close_count > open_count:
    print('Paranthesis are not properly arrenged')
elif close_count == open_count:
    print(f'Number of pairs of Paranthesis is {close_count}')
                                