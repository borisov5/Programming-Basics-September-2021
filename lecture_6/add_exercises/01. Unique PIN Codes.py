first_digit = int(input())
second_digit = int(input())
third_digit = int(input())

for x in range(2, first_digit + 1, 2):
    for y in range(2, second_digit + 1):
        for z in range(2, third_digit + 1, 2):
            if y == 2 or y == 3 or y == 5 or y == 7:
                print(f"{x} {y} {z}")