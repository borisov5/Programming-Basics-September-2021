k = int(input())
l = int(input())
m = int(input())
n = int(input())
counter = 0
for first_digit in range(k, 9):
    for second_digit in range(9, l - 1, -1):
        for third_digit in range(m, 9):
            for fourth_digit in range(9, n - 1, -1):
                if first_digit % 2 == 0 and third_digit % 2 == 0:
                    if second_digit % 2 == 1 and fourth_digit % 2 == 1:
                        counter += 1
                        if first_digit == third_digit and second_digit == fourth_digit:
                            if counter <= 6:
                                counter -= 1
                                print("Cannot change the same player.")
                        elif (counter <= 6) and (first_digit != third_digit or second_digit != fourth_digit):
                            print(f"{first_digit}{second_digit} - {third_digit}{fourth_digit}")
                        elif counter > 6:
                            break


