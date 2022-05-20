name = input()
student_class = 0
average_grade = 0
total_grade = 0
bad_grade = 0
while student_class < 12 and bad_grade < 2:
    grade = float(input())
    if grade >= 4:
        total_grade += grade
        student_class += 1
    else:
        bad_grade += 1

average_grade = total_grade / 12
if bad_grade < 2:
    print(f'{name} graduated. Average grade: {average_grade:.2f}')
else:
    print(f'{name} has been excluded at {student_class + 1} grade')