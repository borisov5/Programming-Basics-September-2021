hundreds = int(input())
dozens = int(input())
units = int(input())

for x in range(1, hundreds + 1):
    if x % 2 == 0:
        for y in range(1, dozens + 1):
            if y == 2 or y == 3 or y == 5 or y == 7:
                for z in range(1, units + 1):
                    if z % 2 == 0:
                        print(f"{x} {y} {z}")