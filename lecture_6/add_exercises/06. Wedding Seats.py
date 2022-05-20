last_sector = input()
number_rows_first_sector = int(input())
number_places = int(input())
places = number_places
counter = 0
count_places = 0
for x in range(65, ord(last_sector) + 1):
    counter += 1
    if counter != 1:
        number_rows_first_sector += 1
    for y in range(1, number_rows_first_sector + 1):
        places = number_places
        if y % 2 == 0:
            places += 2
        for z in range(97, places + 97):
            count_places += 1
            print(f"{chr(x)}{y}{chr(z)}")
print(count_places)