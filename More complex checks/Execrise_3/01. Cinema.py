type_of_the_movie = str(input())
rows = int(input())
columns = int(input())
total_place = rows * columns
price_per_ticket = 0
if type_of_the_movie == "Premiere":
    price_per_ticket = 12
elif type_of_the_movie == "Normal":
    price_per_ticket = 7.50
else:
    price_per_ticket = 5
total_income = total_place * price_per_ticket
print(f"{total_income:.2f} leva")