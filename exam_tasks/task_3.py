number_of_people = int(input())
season = input()
price = 0
if season == "spring":
    if number_of_people <= 5:
        price = 50
    elif number_of_people > 5:
        price = 48
elif season == "summer":
    if number_of_people <= 5:
        price = 48.50
    elif number_of_people > 5:
        price = 45
elif season == "autumn":
    if number_of_people <= 5:
        price = 60
    elif number_of_people > 5:
        price = 49.50
elif season == "winter":
    if number_of_people <= 5:
        price = 86
    elif number_of_people > 5:
        price = 85

sum = number_of_people * price

if season == "summer":
    sum *= 0.85
elif season == "winter":
    sum *= 1.08

print(f"{sum:.2f} leva.")