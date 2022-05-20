city_name = input()
type_packet = input()
vip_discount = input()
days = int(input())

price_per_day = 0
discount = 0
total_price = 0
if days > 7:
    days -= 1
elif days < 1:
    print("Days must be positive number!")
if city_name == "Bansko" or city_name == "Borovets":
    if type_packet == "withEquipment":
        price_per_day = 100
        discount = 0.90
    elif type_packet == "noEquipment":
        price_per_day = 80
        discount = 0.95
    else:
        print("Invalid input!")
elif city_name == "Varna" or city_name == "Burgas":
    if type_packet == "withBreakfast":
        price_per_day = 130
        discount = 0.88
    elif type_packet == "noBreakfast":
        price_per_day = 100
        discount = 0.93
    else:
        print("Invalid input!")
else:
    print("Invalid input!")

if vip_discount == "yes":
    total_price = price_per_day * days * discount
else:
    total_price = price_per_day * days
if total_price > 0:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
