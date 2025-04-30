avg_score = float(input('Enter average score of the student: '))
if avg_score >= 0 and avg_score <= 49:
    print('Result is Fail')
elif avg_score <= 79:
    print('Result is Second Class')
elif avg_score <= 95:
    print('Result is First Class')
elif avg_score <= 100:
    print('Result is Excellent')
else:
    print('Input is invalid')