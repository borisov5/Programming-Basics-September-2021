starting_value_first_pair = int(input())
starting_value_second_pair = int(input())
difference_first_pair = int(input())
difference_second_pair = int(input())

for x in range(starting_value_first_pair, starting_value_first_pair + difference_first_pair + 1):
    for a in range(2, x):
        if (x % a) == 0:
            break
    else:
        for y in range(starting_value_second_pair, starting_value_second_pair + difference_second_pair + 1):
            for b in range(2, y):
                if (y % b) == 0:
                    break
            else:
                print(f"{x}{y}")