days = int(input())
room_type = input()
rating = input()
price = 0
days -= 1
if room_type == "room for one person":
    price = 18.00
elif room_type == "apartment":
    price = 25.00
elif room_type == "president apartment":
    price = 35.00

if days < 10 and room_type == "apartment":
    price *= 0.70
elif 10 <= days <= 15 and room_type == "apartment":
    price *= 0.65
elif days > 15 and room_type == "apartment":
    price *= 0.50

if days < 10 and room_type == "president apartment":
    price *= 0.90
elif 10 <= days <= 15 and room_type == "president apartment":
    price *= 0.85
elif days > 15 and room_type == "president apartment":
    price *= 0.80

total_price = days * price

if rating == "positive":
    total_price *= 1.25
elif rating == "negative":
    total_price *= 0.90

print(f"{total_price:.2f}")
