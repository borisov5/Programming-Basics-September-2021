a = int(input())
b = int(input())
max_number_passwords = int(input())
password_counter = 0
first_symbol = 35
second_symbol = 64
for three in range(1, a + 1):
    if password_counter == max_number_passwords:
        break
    for four in range(1, b + 1):
        password_counter += 1
        print(f"{chr(first_symbol)}{chr(second_symbol)}{three}{four}{chr(second_symbol)}{chr(first_symbol)}", end="|")
        first_symbol += 1
        if first_symbol > 55:
            first_symbol = 35
        second_symbol += 1
        if second_symbol > 96:
            second_symbol = 64
        if password_counter == max_number_passwords:
            break
