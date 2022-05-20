number_of_students = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
sum_grade = 0
for i in range(number_of_students):
    grade = float(input())
    if 2 <= grade < 3:
        p1 += 1
        sum_grade += grade
    elif 3 <= grade < 4:
        p2 += 1
        sum_grade += grade
    elif 4 <= grade < 5:
        p3 += 1
        sum_grade += grade
    elif 5 <= grade:
        p4 += 1
        sum_grade += grade
p = p1 + p2 + p3 + p4
p1 = p1 / p * 100
p2 = p2 / p * 100
p3 = p3 / p * 100
p4 = p4 / p * 100
average_grade = sum_grade / number_of_students
print(f"Top students: {p4:.2f}%")
print(f"Between 4.00 and 4.99: {p3:.2f}%")
print(f"Between 3.00 and 3.99: {p2:.2f}%")
print(f"Fail: {p1:.2f}%")
print(f"Average: {average_grade:.2f}")
