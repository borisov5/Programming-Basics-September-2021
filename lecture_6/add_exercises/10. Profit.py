number_one_lev_coins = int(input())
number_two_leva_coins = int(input())
number_five_leva_coins = int(input())
sum = int(input())

for x in range(number_one_lev_coins + 1):
    for y in range(number_two_leva_coins + 1):
        for z in range(number_five_leva_coins + 1):
            if (x + (y * 2) + (z * 5)) == sum:
                print(f"{x} * 1 lv. + {y} * 2 lv. + {z} * 5 lv. = {sum} lv.")