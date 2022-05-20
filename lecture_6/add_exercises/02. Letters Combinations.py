first_char = input()
second_char = input()
third_char = input()
first_char = ord(first_char)
second_char = ord(second_char)
third_char = ord(third_char)
all_combinations = 0
for x in range(first_char, second_char + 1):
    for y in range(first_char, second_char + 1):
        for z in range(first_char, second_char + 1):
            if x != third_char and y != third_char and z != third_char:
                all_combinations += 1
                print(chr(x) + chr(y) + chr(z), end = " ")
print(all_combinations)