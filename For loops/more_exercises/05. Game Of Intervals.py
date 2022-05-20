moves = int(input())
points = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
for i in range(1, moves + 1):
    number = int(input())
    if 0 <= number <= 9:
        points += number * 0.20
        p1 += 1
    elif 10 <= number <= 19:
        points += number * 0.30
        p2 += 1
    elif 20 <= number <= 29:
        points += number * 0.40
        p3 += 1
    elif 30 <= number <= 39:
        points += 50
        p4 += 1
    elif 40 <= number <= 50:
        points += 100
        p5 += 1
    elif number < 0 or number > 50:
        points /= 2
        p6 += 1
end_result = p1 + p2 + p3 + p4 + p5 + p6
p1 = p1 / end_result * 100
p2 = p2 / end_result * 100
p3 = p3 / end_result * 100
p4 = p4 / end_result * 100
p5 = p5 / end_result * 100
p6 = p6 / end_result * 100
print(f"{points:.2f}")
print(f"From 0 to 9: {p1:.2f}%")
print(f"From 10 to 19: {p2:.2f}%")
print(f"From 20 to 29: {p3:.2f}%")
print(f"From 30 to 39: {p4:.2f}%")
print(f"From 40 to 50: {p5:.2f}%")
print(f"Invalid numbers: {p6:.2f}%")
