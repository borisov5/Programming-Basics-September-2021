season = input()
type_of_group = input()
number_of_students = int(input())
number_of_nights = int(input())

nights_price = 0
sport = ''

if season == "Winter":
    if type_of_group == "boys" or type_of_group == "girls":
        nights_price = 9.60
    elif type_of_group == "mixed":
        nights_price = 10
elif season == "Spring":
    if type_of_group == "boys" or type_of_group == "girls":
        nights_price = 7.20
    elif type_of_group == "mixed":
        nights_price = 9.50
elif season == "Summer":
    if type_of_group == "boys" or type_of_group == "girls":
        nights_price = 15
    elif type_of_group == "mixed":
        nights_price = 20

if number_of_students >= 50:
    nights_price *= 0.50
elif 20 <= number_of_students < 50:
    nights_price *= 0.85
elif 10 <= number_of_students < 20:
    nights_price *= 0.95

if season == "Winter":
    if type_of_group == "girls":
        sport = "Gymnastics"
    elif type_of_group == "boys":
        sport = "Judo"
    elif type_of_group == "mixed":
        sport = "Ski"
elif season == "Spring":
    if type_of_group == "girls":
        sport = "Athletics"
    elif type_of_group == "boys":
        sport = "Tennis"
    elif type_of_group == "mixed":
        sport = "Cycling"
elif season == "Summer":
    if type_of_group == "girls":
        sport = "Volleyball"
    elif type_of_group == "boys":
        sport = "Football"
    elif type_of_group == "mixed":
        sport = "Swimming"

price = number_of_nights * nights_price * number_of_students
print(f"{sport} {price:.2f} lv.")