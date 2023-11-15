
student_heights = [180, 124, 165, 173, 189, 169, 146]

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

print(f'Total height = {total_height}')

number_of_students = 0
for student in student_heights:
    number_of_students += 1

print(f'number of students = {number_of_students}')

average_height = round(total_height / number_of_students)
print(f'average height = {average_height}')