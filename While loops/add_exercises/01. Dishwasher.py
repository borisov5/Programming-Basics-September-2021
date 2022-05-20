number_of_bottles = int(input())
total_detergent = number_of_bottles * 750
enought_detergent = True
number_clean_plates = 0
number_clean_pots = 0
command = input()
counter = 0
while command != "End":
    charging = int(command)
    counter += 1
    if counter % 3 == 0:
        dishes = 15
        number_clean_pots += charging
    else:
        dishes = 5
        number_clean_plates += charging
    total_detergent -= (charging * dishes)
    if total_detergent < 0:
        enought_detergent = False
        break
    command = input()
difference = abs(total_detergent)
if enought_detergent:
    print("Detergent was enough!")
    print(f"{number_clean_plates} dishes and {number_clean_pots} pots were washed.")
    print(f"Leftover detergent {difference} ml.")
else:
    print(f"Not enough detergent, {difference} ml. more necessary!")
