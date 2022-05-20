number_of_groups = int(input())
number_of_people = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(number_of_groups):
    number_of_people = int(input())
    if number_of_people <= 5:
        p1 += number_of_people
    elif 6 <= number_of_people <= 12:
        p2 += number_of_people
    elif 13 <= number_of_people <= 25:
        p3 += number_of_people
    elif 26 <= number_of_people <= 40:
        p4 += number_of_people
    elif 41 <= number_of_people:
        p5 += number_of_people
n = p1 + p2 + p3 + p4 + p5
p1 = p1 / n * 100
p2 = p2 / n * 100
p3 = p3 / n * 100
p4 = p4 / n * 100
p5 = p5 / n * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
