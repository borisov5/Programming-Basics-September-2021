capacity = int(input())
number_of_fans = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0

for i in range(1, number_of_fans + 1):
    sector = input()
    if sector == "A":
        p1 += 1
    elif sector == "B":
        p2 += 1
    elif sector == "V":
        p3 += 1
    elif sector == "G":
        p4 += 1
total_percent = p1 + p2 + p3 + p4
p1 = p1 / total_percent * 100
p2 = p2 / total_percent * 100
p3 = p3 / total_percent * 100
p4 = p4 / total_percent * 100
percent_all_fans = number_of_fans / capacity * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{percent_all_fans:.2f}%")
