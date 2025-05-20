number_of_projects = int(input("Enter the number of projects: "))

modules_per_project = []
for i in range (number_of_projects):
    print(f'Enter the numbrer of modules of projet-{i+1}')
    modules = int(input())
    modules_per_project.append(modules)
total_number_of_weeks = sum(modules_per_project)
print(total_number_of_weeks)