number_men = int(input())
number_women = int(input())
max_tables = int(input())
counter = 0
for x in range(1, number_men + 1):
    for y in range(1, number_women + 1):
        counter += 1
        if counter > max_tables:
            break
        print(f"({x} <-> {y})", end = " ")
