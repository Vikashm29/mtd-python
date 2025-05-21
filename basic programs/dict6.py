'''You’re designing a system to track student grades.
 # Create a dictionary with student names as keys and their scores as values.
 # Then write code to:
 #- Add a new student
 #- Update a student's grade
 #- Find the student with the highest grade
 '''

students_marx = {'Vikas' : 79, 'Shivu' : 75, 'Ravi' : 80}

students_marx['Darshan'] = 72
print(students_marx)

students_marx.update({'Vikas' : 82}) 
print(students_marx)

highest_scorer = max(students_marx, key = students_marx.get)
print(f"Top student: {highest_scorer} with {students_marx[highest_scorer]} marx")