avg_score = float(input('Enter average score of the student: '))
if avg_score <= 100 and avg_score >= 96:
    print('Result is Execellent')
elif avg_score >= 80:
    print('Result is First Class')
elif avg_score >= 50:
    print('Result is Second class')
elif avg_score >= 0:
    print('Result is Fail')
else:
    print('Input is invalid')