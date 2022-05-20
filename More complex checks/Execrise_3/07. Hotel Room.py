month = input()
number_days = int(input())
price_apartment = ''
price_studio = ''
if month == "May" or month == "October":
    price_apartment = 65
    price_studio = 50
elif month == "June" or month == "September":
    price_apartment = 68.70
    price_studio = 75.20
elif month == "July" or month == "August":
    price_apartment = 77
    price_studio = 76
if 7 < number_days <= 14 and (month == "May" or month == "October"):
    price_studio *= 0.95
elif number_days > 14 and (month == "May" or month == "October"):
    price_studio *= 0.70
elif number_days > 14 and (month == "June" or month == "September"):
    price_studio *= 0.80
if number_days > 14:
    price_apartment *= 0.90
price_for_apartament = price_apartment * number_days
price_for_studio = price_studio * number_days
print(f"Apartment: {price_for_apartament:.2f} lv.")
print(f"Studio: {price_for_studio:.2f} lv.")