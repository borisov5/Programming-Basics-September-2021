price_of_party = float(input())
number_love_messages = int(input())
number_roses = int(input())
number_keyholders = int(input())
number_cartoons = int(input())
number_suprices = int(input())

sum = number_love_messages * 0.60 + number_roses * 7.20 + number_keyholders * 3.60 + number_cartoons * 18.20 + number_suprices * 22
number_articuls = number_love_messages + number_roses + number_keyholders + number_cartoons + number_suprices

if number_articuls >= 25:
    sum *= 0.65

earnings = sum * 0.9
diff = abs(earnings - price_of_party)
if earnings > price_of_party:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")