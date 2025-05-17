import math

number_of_employees = int(input('Enter the number of employees:'))
start_distance = int(input('Enter the starting distance:'))
end_distance = int(input('Enter the ending distance:'))

distances = []
for i in range (number_of_employees):
    print(f'Enter distance of employee with ID-{i}')
    distance = int(input())
    distances.append(distance)

print(f'The IDs of employees who stay in the range of distance {start_distance} to {end_distance} are')
for i in range(number_of_employees):
    distance = math.fabs(distances[i])
    if distance >= start_distance and distance <= end_distance:
        print(i, end=' ')